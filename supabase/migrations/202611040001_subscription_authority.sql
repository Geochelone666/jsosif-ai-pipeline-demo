-- Candidate backend foundation. Apply only to an approved Supabase project.
-- auth.users, auth.uid(), authenticated and service_role are supplied by Supabase.
begin;
create schema subscription_private;
revoke all on schema subscription_private from public;
grant usage on schema subscription_private to authenticated, service_role;

create table subscription_private.settings (
  singleton boolean primary key default true check (singleton),
  revision bigint not null default 1,
  config jsonb not null default '{"groups":{},"max_report_age_days":4,"allow_degraded":false}'
);
insert into subscription_private.settings default values;
create table subscription_private.securities (ticker text primary key);
create table subscription_private.members (
  user_id uuid primary key references auth.users(id),
  -- Preserve existing member IDs on migration: these identify weekly reservations.
  member_id text not null unique,
  version bigint not null default 1,
  preferences jsonb not null,
  updated_at timestamptz not null default now()
);
create table subscription_private.requests (
  user_id uuid not null references auth.users(id),
  request_id uuid not null,
  fingerprint text not null,
  result jsonb not null,
  primary key(user_id, request_id)
);
alter table subscription_private.members enable row level security;
alter table subscription_private.settings enable row level security;
alter table subscription_private.securities enable row level security;
alter table subscription_private.requests enable row level security;
create policy own_subscription on subscription_private.members
  for select to authenticated using (user_id = auth.uid());
-- Do not inherit potentially permissive project-wide default table grants.
revoke all on all tables in schema subscription_private from public, anon, authenticated;
grant select on subscription_private.members to authenticated;
grant all on all tables in schema subscription_private to service_role;

create function public.get_my_subscription() returns jsonb
language sql stable security invoker set search_path = '' as $$
  select jsonb_build_object('version',version,'updated_at',updated_at,'preferences',preferences)
  from subscription_private.members where user_id = auth.uid()
$$;

create function public.save_my_subscription(p_preferences jsonb, p_expected_version bigint,
                                           p_request_id uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare
  actor uuid := auth.uid();
  old subscription_private.members;
  prior subscription_private.requests;
  configuration jsonb;
  fingerprint text := encode(sha256(convert_to(p_preferences::text || ':' || p_expected_version::text, 'UTF8')), 'hex');
  result jsonb;
  item text;
begin
  if actor is null or not exists (select 1 from auth.users where id=actor and email_confirmed_at is not null) then
    raise exception 'Verified authentication required' using errcode='42501';
  end if;
  if p_request_id is null or p_expected_version is null or p_expected_version < 0 then
    raise exception 'Version and request ID required' using errcode='22023';
  end if;
  -- Serialize snapshot revisions and first-time creation as well as updates.
  select config into configuration from subscription_private.settings where singleton for update;
  select * into prior from subscription_private.requests where user_id=actor and request_id=p_request_id;
  if found then
    if prior.fingerprint is distinct from fingerprint then
      raise exception 'Request ID reused with different input' using errcode='22023';
    end if;
    return prior.result;
  end if;
  select * into old from subscription_private.members where user_id=actor for update;
  if coalesce(old.version,0) <> p_expected_version then
    raise exception 'Subscription version conflict' using errcode='40001';
  end if;
  if jsonb_typeof(p_preferences) is distinct from 'object' or
     not (p_preferences ?& array['name','enabled','timezone','send_weekday','send_time','groups','tickers']) or
     p_preferences - array['name','enabled','timezone','send_weekday','send_time','groups','tickers','delivery_start_date','content_preferences'] <> '{}'::jsonb then
    raise exception 'Invalid preference fields' using errcode='22023';
  end if;
  if jsonb_typeof(p_preferences->'name') is distinct from 'string' or
     length(btrim(p_preferences->>'name')) not between 1 and 200 or
     (p_preferences->>'name') ~ '[[:cntrl:]]' or
     jsonb_typeof(p_preferences->'enabled') is distinct from 'boolean' or
     jsonb_typeof(p_preferences->'send_weekday') is distinct from 'number' or
     (p_preferences->>'send_weekday') !~ '^[0-6]$' or
     jsonb_typeof(p_preferences->'send_time') is distinct from 'string' or
     (p_preferences->>'send_time') !~ '^([01][0-9]|2[0-3]):[0-5][0-9]$' or
     jsonb_typeof(p_preferences->'timezone') is distinct from 'string' or
     not exists(select 1 from pg_catalog.pg_timezone_names where name=p_preferences->>'timezone') then
    raise exception 'Invalid member or schedule' using errcode='22023';
  end if;
  if jsonb_typeof(p_preferences->'groups') is distinct from 'array' or
     jsonb_typeof(p_preferences->'tickers') is distinct from 'array' then
    raise exception 'Expected holding lists' using errcode='22023';
  end if;
  if jsonb_array_length(p_preferences->'groups') + jsonb_array_length(p_preferences->'tickers') = 0 or
     jsonb_array_length(p_preferences->'groups') > 20 or jsonb_array_length(p_preferences->'tickers') > 100 then
    raise exception 'Invalid holding count' using errcode='22023';
  end if;
  if exists(select 1 from jsonb_array_elements(p_preferences->'groups') where jsonb_typeof(value) <> 'string') or
     exists(select 1 from jsonb_array_elements(p_preferences->'tickers') where jsonb_typeof(value) <> 'string') then
    raise exception 'Holdings must be strings' using errcode='22023';
  end if;
  for item in select jsonb_array_elements_text(p_preferences->'groups') loop
    if not (configuration->'groups' ? item) then raise exception 'Unknown group' using errcode='22023'; end if;
  end loop;
  for item in select jsonb_array_elements_text(p_preferences->'tickers') loop
    if not exists(select 1 from subscription_private.securities where ticker=item) then
      raise exception 'Security is not active' using errcode='22023';
    end if;
  end loop;
  if p_preferences ? 'delivery_start_date' then
    if jsonb_typeof(p_preferences->'delivery_start_date') is distinct from 'string' or
       (p_preferences->>'delivery_start_date') !~ '^\d{4}-\d{2}-\d{2}$' then
      raise exception 'Invalid start date' using errcode='22023';
    end if;
    perform (p_preferences->>'delivery_start_date')::date;
  end if;
  if p_preferences ? 'content_preferences' then
    if jsonb_typeof(p_preferences->'content_preferences') is distinct from 'object' or
       (p_preferences->'content_preferences') - array['sector_brief','macro_overview','news_catalysts'] <> '{}'::jsonb or
       exists(select 1 from jsonb_each(p_preferences->'content_preferences') where jsonb_typeof(value) <> 'boolean') then
      raise exception 'Invalid content preferences' using errcode='22023';
    end if;
  end if;
  insert into subscription_private.members(user_id,member_id,version,preferences)
    values(actor,actor::text,1,p_preferences)
    on conflict(user_id) do update set version=subscription_private.members.version+1,
      preferences=excluded.preferences,updated_at=now();
  update subscription_private.settings set revision=revision+1 where singleton;
  select jsonb_build_object('version',version,'updated_at',updated_at) into result
    from subscription_private.members where user_id=actor;
  insert into subscription_private.requests values(actor,p_request_id,fingerprint,result);
  return result;
end $$;

-- One statement / MVCC snapshot. Service credentials must remain server-side.
create function public.subscription_snapshot() returns jsonb
language sql stable security definer set search_path = '' as $$
  select jsonb_build_object('schema_version',1,'revision',s.revision::text,'generated_at',now(),
    'config',s.config || jsonb_build_object('members',coalesce((
      select jsonb_agg(m.preferences || jsonb_build_object('id',m.member_id,'email',u.email)
                       order by m.member_id)
      from subscription_private.members m join auth.users u on u.id=m.user_id
      where u.email_confirmed_at is not null and u.email is not null), '[]'::jsonb)))
  from subscription_private.settings s where singleton
$$;
revoke all on function public.get_my_subscription() from public, anon;
revoke all on function public.save_my_subscription(jsonb,bigint,uuid) from public, anon;
revoke all on function public.subscription_snapshot() from public, anon, authenticated;
grant execute on function public.get_my_subscription() to authenticated;
grant execute on function public.save_my_subscription(jsonb,bigint,uuid) to authenticated;
grant execute on function public.subscription_snapshot() to service_role;
commit;

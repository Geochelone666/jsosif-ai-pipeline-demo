-- Named, verified administrators; candidate only. Apply after prior migrations.
begin;
-- Keep member and administrator validation identical. Only RPC owners call this helper.
create function subscription_private.validate_preferences(p_preferences jsonb, configuration jsonb)
returns void language plpgsql set search_path='' as $$
declare item text;
begin
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
end $$;
revoke all on function subscription_private.validate_preferences(jsonb,jsonb)
 from public,anon,authenticated,service_role;

create or replace function public.save_my_subscription(p_preferences jsonb, p_expected_version bigint,
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
  if actor is null or not subscription_private.is_approved_member() then
    raise exception 'Verified identity and team approval required' using errcode='42501';
  end if;
  if p_request_id is null or p_expected_version is null or p_expected_version < 0 then
    raise exception 'Version and request ID required' using errcode='22023';
  end if;
  -- Serialize snapshot revisions and first-time creation as well as updates.
  select config into configuration from subscription_private.settings where singleton for update;
  -- Recheck after waiting for an administrator's serialized approval change.
  if not subscription_private.is_approved_member() then
    raise exception 'Verified identity and team approval required' using errcode='42501';
  end if;
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
  perform subscription_private.validate_preferences(p_preferences,configuration);
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

create table subscription_private.administrators (
 user_id uuid primary key references auth.users(id),
 granted_at timestamptz not null default now()
);
create table subscription_private.administration_changes (
 actor_id uuid not null references auth.users(id),
 request_id uuid not null,
 target_id uuid not null references auth.users(id),
 fingerprint text not null,
 reason text not null,
 before_state jsonb not null,
 after_state jsonb not null,
 result jsonb not null,
 created_at timestamptz not null default now(),
 primary key(actor_id,request_id)
);
alter table subscription_private.administrators enable row level security;
alter table subscription_private.administration_changes enable row level security;
revoke all on subscription_private.administrators,subscription_private.administration_changes
 from public,anon,authenticated,service_role;
grant select on subscription_private.administrators,subscription_private.administration_changes to service_role;

create function subscription_private.require_administrator() returns uuid
language plpgsql security definer set search_path='' as $$
declare actor uuid:=auth.uid();
begin
 -- Hold verified role membership for this transaction. Revoking an administrator
 -- waits for in-flight actions; subsequent calls, including retries, are denied.
 perform 1 from subscription_private.administrators a join auth.users u on u.id=a.user_id
  where a.user_id=actor and u.email_confirmed_at is not null and u.email is not null
  for share of a,u;
 if not found then raise exception 'Verified administrator required' using errcode='42501'; end if;
 return actor;
end $$;
revoke all on function subscription_private.require_administrator() from public,anon,authenticated,service_role;

create function public.get_admin_subscription(p_user_id uuid) returns jsonb
language plpgsql security definer set search_path='' as $$
declare actor uuid; result jsonb;
begin
 actor:=subscription_private.require_administrator();
 select jsonb_build_object('operator_id',actor,'user_id',u.id,'email',u.email,
  'email_verified',u.email_confirmed_at is not null,'member_id',m.member_id,
  'version',coalesce(m.version,0),'preferences',m.preferences,'updated_at',m.updated_at,
  'approved',a.user_id is not null,'settings_revision',s.revision,
  'groups',s.config->'groups',
  'tickers',(select coalesce(jsonb_agg(ticker order by ticker),'[]'::jsonb) from subscription_private.securities))
 into result from auth.users u cross join subscription_private.settings s
 left join subscription_private.members m on m.user_id=u.id
 left join subscription_private.approved_members a on a.user_id=u.id
 where u.id=p_user_id and s.singleton;
 if result is null then raise exception 'Unknown account' using errcode='22023'; end if;
 return result;
end $$;

create function public.correct_admin_subscription(
 p_user_id uuid,p_preferences jsonb,p_approved boolean,p_expected_version bigint,
 p_expected_approved boolean,p_request_id uuid,p_reason text,p_expected_actor uuid
) returns jsonb language plpgsql security definer set search_path='' as $$
declare
 actor uuid; configuration jsonb; old subscription_private.members;
 prior subscription_private.administration_changes; approved boolean; verified boolean;
 before_state jsonb; after_state jsonb; result jsonb; digest text; new_version bigint;
begin
 actor:=subscription_private.require_administrator();
 if p_expected_actor is distinct from actor then
  raise exception 'Review belongs to a different administrator' using errcode='42501';
 end if;
 if p_user_id is null or p_approved is null or p_expected_approved is null or p_request_id is null or
    p_expected_version is null or p_expected_version<0 or p_reason is null or
    length(btrim(p_reason)) not between 1 and 1000 or p_reason ~ '[[:cntrl:]]' then
  raise exception 'Target, expected state, request ID and reason required' using errcode='22023';
 end if;
 digest:=encode(sha256(convert_to(jsonb_build_object('target',p_user_id,'preferences',p_preferences,
  'approved',p_approved,'expected_version',p_expected_version,'expected_approved',p_expected_approved,
  'reason',p_reason)::text,'UTF8')),'hex');
 -- Same lock order as member saves, making versions and sender revision atomic.
 select config into configuration from subscription_private.settings where singleton for update;
 select * into prior from subscription_private.administration_changes where actor_id=actor and request_id=p_request_id;
 if found then
  if prior.fingerprint<>digest then raise exception 'Request ID reused with different input' using errcode='22023'; end if;
  return prior.result;
 end if;
 select email_confirmed_at is not null and email is not null into verified from auth.users where id=p_user_id for share;
 if not found then raise exception 'Unknown account' using errcode='22023'; end if;
 select * into old from subscription_private.members where user_id=p_user_id for update;
 approved:=exists(select 1 from subscription_private.approved_members where user_id=p_user_id);
 if coalesce(old.version,0)<>p_expected_version or approved<>p_expected_approved then
  raise exception 'Member state changed; inspect and review again' using errcode='40001';
 end if;
 if not verified and (p_approved or p_preferences is not null) then
  raise exception 'Verified target required for approval or preference edits' using errcode='22023';
 end if;
 if p_preferences is not null then
  if old.user_id is null then raise exception 'Use member signup or reviewed legacy migration before editing preferences' using errcode='22023'; end if;
  perform subscription_private.validate_preferences(p_preferences,configuration);
 end if;
 if approved=p_approved and (p_preferences is null or p_preferences=old.preferences) then
  raise exception 'No member change requested' using errcode='22023';
 end if;
 before_state:=jsonb_build_object('member_id',old.member_id,'version',coalesce(old.version,0),
  'approved',approved,'preferences',old.preferences);
 if p_approved then
  insert into subscription_private.approved_members(user_id) values(p_user_id) on conflict(user_id) do nothing;
 else
  delete from subscription_private.approved_members where user_id=p_user_id;
 end if;
 new_version:=coalesce(old.version,0);
 if old.user_id is not null then
  update subscription_private.members set preferences=coalesce(p_preferences,preferences),
   version=version+1,updated_at=now() where user_id=p_user_id returning version into new_version;
 end if;
 update subscription_private.settings set revision=revision+1 where singleton;
 after_state:=jsonb_build_object('member_id',old.member_id,'version',new_version,
  'approved',p_approved,'preferences',coalesce(p_preferences,old.preferences));
 result:=jsonb_build_object('user_id',p_user_id,'member_id',old.member_id,'version',new_version,
  'approved',p_approved,'request_id',p_request_id,'operator_id',actor);
 insert into subscription_private.administration_changes
  (actor_id,request_id,target_id,fingerprint,reason,before_state,after_state,result)
  values(actor,p_request_id,p_user_id,digest,p_reason,before_state,after_state,result);
 return result;
end $$;

create function public.get_admin_subscription_history(p_user_id uuid) returns jsonb
language plpgsql security definer set search_path='' as $$
begin
 perform subscription_private.require_administrator();
 return (select coalesce(jsonb_agg(row order by row.created_at desc,row.request_id),'[]'::jsonb) from
  (select actor_id,request_id,target_id,reason,before_state,after_state,created_at
   from subscription_private.administration_changes where target_id=p_user_id
   order by created_at desc,request_id limit 50) row);
end $$;

revoke all on function public.get_admin_subscription(uuid) from public,anon,authenticated,service_role;
revoke all on function public.correct_admin_subscription(uuid,jsonb,boolean,bigint,boolean,uuid,text,uuid)
 from public,anon,authenticated,service_role;
revoke all on function public.get_admin_subscription_history(uuid) from public,anon,authenticated,service_role;
grant execute on function public.get_admin_subscription(uuid) to authenticated;
grant execute on function public.correct_admin_subscription(uuid,jsonb,boolean,bigint,boolean,uuid,text,uuid) to authenticated;
grant execute on function public.get_admin_subscription_history(uuid) to authenticated;
commit;

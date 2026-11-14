-- Review queue only: this migration never activates securities or subscriptions.
begin;
create table subscription_private.security_requests (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id),
  ticker text not null check (ticker ~ '^[A-Z0-9][A-Z0-9.-]{0,19}$'),
  exchange_mic text not null check (exchange_mic ~ '^[A-Z0-9]{4}$'),
  reason text not null check (length(reason) between 1 and 1000),
  status text not null default 'pending' check (status in ('pending','reviewing','available','rejected')),
  review_note text,
  version bigint not null default 1,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique(user_id,ticker,exchange_mic)
);
create table subscription_private.security_request_reviews (
  request_id uuid not null references subscription_private.security_requests(id),
  version bigint not null,
  status text not null,
  note text not null,
  reviewed_at timestamptz not null default now(),
  primary key(request_id,version)
);
alter table subscription_private.security_requests enable row level security;
alter table subscription_private.security_request_reviews enable row level security;
-- Explicitly replace inherited defaults, including broad service-role grants.
revoke all on subscription_private.security_requests, subscription_private.security_request_reviews from public,anon,authenticated,service_role;
grant select on subscription_private.security_requests to authenticated;
grant select on subscription_private.security_requests, subscription_private.security_request_reviews to service_role;
create policy own_security_requests on subscription_private.security_requests
  for select to authenticated using (user_id=auth.uid() and subscription_private.is_approved_member());

create function public.get_my_security_requests() returns jsonb
language plpgsql stable security invoker set search_path='' as $$
begin
 if not subscription_private.is_approved_member() then
  raise exception 'Team approval required' using errcode='42501';
 end if;
 return (select coalesce(jsonb_agg(jsonb_build_object('id',id,'ticker',ticker,'exchange_mic',exchange_mic,
   'reason',reason,'status',status,'review_note',review_note,'version',version,
   'created_at',created_at,'updated_at',updated_at) order by created_at desc,id),'[]'::jsonb)
   from subscription_private.security_requests where user_id=auth.uid());
end $$;

create function public.request_security(p_ticker text,p_exchange_mic text,p_reason text) returns jsonb
language plpgsql security definer set search_path='' as $$
declare
 actor uuid:=auth.uid();
 symbol text:=upper(btrim(p_ticker));
 mic text:=upper(btrim(p_exchange_mic));
 explanation text:=btrim(p_reason);
 existing subscription_private.security_requests;
begin
 if actor is null or not subscription_private.is_approved_member() then
  raise exception 'Team approval required' using errcode='42501';
 end if;
 if symbol is null or symbol !~ '^[A-Z0-9][A-Z0-9.-]{0,19}$' or
    mic is null or mic !~ '^[A-Z0-9]{4}$' or explanation is null or
    length(explanation) not between 1 and 1000 or explanation ~ '[[:cntrl:]]' then
  raise exception 'Ticker, exchange MIC and reason required' using errcode='22023';
 end if;
 -- Per-member lock serializes duplicate submissions and the outstanding limit.
 perform 1 from subscription_private.approved_members where user_id=actor for update;
 if not found then raise exception 'Team approval required' using errcode='42501'; end if;
 select * into existing from subscription_private.security_requests
   where user_id=actor and ticker=symbol and exchange_mic=mic;
 if not found then
  if (select count(*) from subscription_private.security_requests
      where user_id=actor and status in ('pending','reviewing')) >= 20 then
   raise exception 'At most 20 outstanding requests' using errcode='22023';
  end if;
  insert into subscription_private.security_requests(user_id,ticker,exchange_mic,reason)
    values(actor,symbol,mic,explanation) returning * into existing;
 end if;
 -- Repeated submissions retain the original reason, identity and review state.
 return jsonb_build_object('id',existing.id,'status',existing.status,'version',existing.version);
end $$;

-- Backend-only review. Notes are member-visible; never include private research.
-- Availability requires separate identity/source/cost acceptance and active catalogue entry.
create function public.review_security_request(p_id uuid,p_expected_version bigint,p_status text,p_note text) returns jsonb
language plpgsql security definer set search_path='' as $$
declare existing subscription_private.security_requests;
begin
 if p_expected_version is null or p_expected_version < 1 or p_status is null or
    p_status not in ('reviewing','available','rejected') or p_note is null or
    length(btrim(p_note)) not between 1 and 1000 or p_note ~ '[[:cntrl:]]' then
  raise exception 'Valid review fields required' using errcode='22023';
 end if;
 select * into existing from subscription_private.security_requests where id=p_id for update;
 if not found then raise exception 'Unknown request' using errcode='22023'; end if;
 -- Retry after an ambiguous response must not append another audit record.
 if existing.version=p_expected_version+1 and existing.status=p_status and existing.review_note=btrim(p_note) then
  return jsonb_build_object('id',existing.id,'status',existing.status,'version',existing.version);
 end if;
 if existing.version<>p_expected_version then raise exception 'Request version conflict' using errcode='40001'; end if;
 if existing.status not in ('pending','reviewing') then raise exception 'Request already resolved' using errcode='22023'; end if;
 if p_status='available' and not exists(select 1 from subscription_private.securities where ticker=existing.ticker) then
  raise exception 'Security must pass onboarding and be active first' using errcode='22023';
 end if;
 update subscription_private.security_requests set status=p_status,review_note=btrim(p_note),
   version=version+1,updated_at=now() where id=p_id returning * into existing;
 insert into subscription_private.security_request_reviews(request_id,version,status,note)
   values(existing.id,existing.version,existing.status,existing.review_note);
 return jsonb_build_object('id',existing.id,'status',existing.status,'version',existing.version);
end $$;
revoke all on function public.get_my_security_requests() from public,anon;
revoke all on function public.request_security(text,text,text) from public,anon;
revoke all on function public.review_security_request(uuid,bigint,text,text) from public,anon,authenticated;
grant execute on function public.get_my_security_requests() to authenticated;
grant execute on function public.request_security(text,text,text) to authenticated;
grant execute on function public.review_security_request(uuid,bigint,text,text) to service_role;
commit;

\set ON_ERROR_STOP on
-- Disposable database only: emulate Supabase's auth identity/roles, never real users.
do $$ begin
 if not exists(select 1 from pg_roles where rolname='anon') then create role anon; end if;
 if not exists(select 1 from pg_roles where rolname='authenticated') then create role authenticated; end if;
 if not exists(select 1 from pg_roles where rolname='service_role') then create role service_role bypassrls; end if;
end $$;
create schema storage;
create table storage.buckets(id text primary key, public boolean);
create schema auth;
create table auth.users(id uuid primary key, email text, email_confirmed_at timestamptz);
create function auth.uid() returns uuid language sql stable as $$
 select nullif(current_setting('request.jwt.claim.sub',true),'')::uuid
$$;
grant usage on schema auth to authenticated;
grant execute on function auth.uid() to authenticated;
\ir ../../supabase/migrations/202611040001_subscription_authority.sql
\ir ../../supabase/migrations/202611050001_subscription_options.sql
\ir ../../supabase/seed_securities.sql
insert into auth.users values
 ('00000000-0000-0000-0000-000000000001','one@example.com',now()),
 ('00000000-0000-0000-0000-000000000002','two@example.com',now()),
 ('00000000-0000-0000-0000-000000000003','unverified@example.com',null);
insert into subscription_private.approved_members(user_id) values ('00000000-0000-0000-0000-000000000001');
set role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
do $$
declare
 p jsonb := '{"name":"Example","enabled":true,"timezone":"America/Toronto","send_weekday":1,"send_time":"09:00","groups":[],"tickers":["CSCO"]}';
 first jsonb;
 r uuid := '10000000-0000-0000-0000-000000000001';
begin
 if jsonb_array_length(public.subscription_options()->'tickers') <> 50 then raise exception 'invalid active catalogue'; end if;
 first := public.save_my_subscription(p,0,r);
 if first->>'version' <> '1' then raise exception 'bad initial version'; end if;
 if public.save_my_subscription(p,0,r) <> first then raise exception 'retry was not idempotent'; end if;
 begin
   perform public.save_my_subscription(p || '{"enabled":false}',0,r);
   raise exception 'request conflict was accepted';
 exception when invalid_parameter_value then null; end;
 begin
   perform public.save_my_subscription(p,0,gen_random_uuid());
   raise exception 'stale update accepted';
 exception when serialization_failure then null; end;
 begin
   perform public.save_my_subscription(p || '{"email":"other@example.com"}',1,gen_random_uuid());
   raise exception 'email injection accepted';
 exception when invalid_parameter_value then null; end;
 begin
   perform public.save_my_subscription(p || '{"tickers":["UNSUPPORTED"]}',1,gen_random_uuid());
   raise exception 'unsupported security activated';
 exception when invalid_parameter_value then null; end;
 begin
   perform public.save_my_subscription(p || '{"groups":[null]}',1,gen_random_uuid());
   raise exception 'null group accepted';
 exception when invalid_parameter_value then null; end;
 begin
   perform public.save_my_subscription(p || '{"content_preferences":{"sector_brief":"yes"}}',1,gen_random_uuid());
   raise exception 'invalid content preference accepted';
 exception when invalid_parameter_value then null; end;
 begin
   perform public.subscription_snapshot();
   raise exception 'member exported all subscriptions';
 exception when insufficient_privilege then null; end;
 begin
   update subscription_private.members set preferences=p;
   raise exception 'member bypassed versioned API';
 exception when insufficient_privilege then null; end;
 perform public.save_my_subscription(p || '{"enabled":false,"content_preferences":{"sector_brief":true}}',1,gen_random_uuid());
 if (public.get_my_subscription()->'preferences'->>'enabled')::boolean then
   raise exception 'pause failed'; end if;
end $$;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000002',false);
do $$ begin
 if public.get_my_subscription() is not null or exists(select 1 from subscription_private.members) then
  raise exception 'cross-member read'; end if;
 begin
  perform public.subscription_options();
  raise exception 'unapproved catalogue access';
 exception when insufficient_privilege then null; end;
 begin
  perform public.save_my_subscription('{"name":"Unapproved","enabled":true,"timezone":"America/Toronto","send_weekday":1,"send_time":"09:00","groups":[],"tickers":["CSCO"]}',0,gen_random_uuid());
  raise exception 'unapproved verified account enrolled';
 exception when insufficient_privilege then null; end;
 begin
  insert into subscription_private.approved_members(user_id) values(auth.uid());
  raise exception 'member self-approval accepted';
 exception when insufficient_privilege then null; end;
end $$;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000003',false);
do $$ begin
 begin
  perform public.save_my_subscription('{}',0,gen_random_uuid());
  raise exception 'unverified write accepted';
 exception when insufficient_privilege then null; end;
end $$;
reset role;
-- A migrated member retains their pre-existing delivery identity through edits.
update subscription_private.members set member_id='legacy-member-001';
set role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
select public.save_my_subscription(public.get_my_subscription()->'preferences',2,gen_random_uuid());
reset role;
set role service_role;
do $$ declare s jsonb; begin
 s := public.subscription_snapshot();
 if s->>'revision' <> '4' or jsonb_array_length(s->'config'->'members') <> 1 or
    s->'config'->'members'->0->>'id' <> 'legacy-member-001' or
    s->'config'->'members'->0->>'email' <> 'one@example.com' or
    (s->'config'->'members'->0->>'enabled')::boolean then
   raise exception 'snapshot disagrees with saved preferences'; end if;
end $$;
reset role;
set role anon;
do $$ begin
 begin
   perform public.get_my_subscription();
   raise exception 'anonymous access accepted';
 exception when insufficient_privilege then null; end;
end $$;
reset role;
select 'Subscription isolation, idempotency, stale-write, pause and snapshot checks passed' as result;

-- Revocation blocks read-back, writes/replayed requests and sender snapshots.
delete from subscription_private.approved_members;
set role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
do $$ begin
 if public.get_my_subscription() is not null then raise exception 'revoked read'; end if;
 begin
  perform public.save_my_subscription('{}',0,'10000000-0000-0000-0000-000000000001');
  raise exception 'revoked request accepted';
 exception when insufficient_privilege then null; end;
end $$;
reset role;
set role service_role;
do $$ begin
 if jsonb_array_length(public.subscription_snapshot()->'config'->'members') <> 0 then
  raise exception 'revoked member exported'; end if;
end $$;
reset role;
insert into subscription_private.approved_members(user_id) values ('00000000-0000-0000-0000-000000000001');

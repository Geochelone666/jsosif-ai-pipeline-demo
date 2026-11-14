-- Included after subscription_authority.sql, disposable database only.
do $$ begin
 if has_table_privilege('service_role','subscription_private.security_requests','INSERT,UPDATE,DELETE,TRUNCATE') or
    has_table_privilege('service_role','subscription_private.security_request_reviews','INSERT,UPDATE,DELETE,TRUNCATE') or
    has_table_privilege('authenticated','subscription_private.security_request_reviews','SELECT') then
  raise exception 'Queue inherited excessive privileges';
 end if;
end $$;
set role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',false);
do $$ declare first jsonb; other jsonb; i integer; begin
 first:=public.request_security(' xyz ','xnas','Example company');
 if public.request_security('XYZ','XNAS','Changed reason')<>first then raise exception 'duplicate request'; end if;
 if public.get_my_security_requests()->0->>'reason'<>'Example company' then raise exception 'duplicate overwrote reason'; end if;
 other:=public.request_security('XYZ','XNYS','Different listing');
 if other->>'id'=first->>'id' then raise exception 'exchange identity conflated'; end if;
 begin
  perform public.request_security('BAD/INPUT','XNAS','Example');
  raise exception 'invalid symbol accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.request_security('XYZ','NASDAQ','Example');
  raise exception 'invalid MIC accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.request_security('XYZ','XNAS',null);
  raise exception 'null reason accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.request_security('XYZ','XNAS',repeat('x',1001));
  raise exception 'oversized reason accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.request_security('XYZ','XNAS',E'line\nbreak');
  raise exception 'control character accepted';
 exception when invalid_parameter_value then null; end;
 begin
  update subscription_private.security_requests set status='available';
  raise exception 'member reviewed requests';
 exception when insufficient_privilege then null; end;
 begin
  perform public.review_security_request((first->>'id')::uuid,1,'available','Self approval');
  raise exception 'member called review RPC';
 exception when insufficient_privilege then null; end;
 for i in 1..18 loop perform public.request_security('TEST'||i,'XNAS','Limit test'); end loop;
 begin
  perform public.request_security('OVERLIMIT','XNAS','Too many');
  raise exception 'outstanding limit exceeded';
 exception when invalid_parameter_value then null; end;
 if public.request_security('XYZ','XNAS','Retry at limit')<>first then raise exception 'retry at limit failed'; end if;
end $$;
reset role;
insert into subscription_private.approved_members(user_id) values('00000000-0000-0000-0000-000000000002');
set role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000002',false);
do $$ begin
 if public.get_my_security_requests()<>'[]'::jsonb or exists(select 1 from subscription_private.security_requests) then
  raise exception 'cross-account request read'; end if;
 perform public.request_security('XYZ','XNAS','Independent member request');
end $$;
reset role;
set role service_role;
do $$ declare rid uuid; reviewed jsonb; before_snapshot jsonb; begin
 before_snapshot:=public.subscription_snapshot();
 select id into rid from subscription_private.security_requests where ticker='XYZ' and exchange_mic='XNAS'
  and user_id='00000000-0000-0000-0000-000000000001';
 begin
  perform public.review_security_request(rid,1,'available','Not active');
  raise exception 'unvalidated security declared available';
 exception when invalid_parameter_value then null; end;
 reviewed:=public.review_security_request(rid,1,'reviewing','Checking listing identity and sources');
 if public.review_security_request(rid,1,'reviewing','Checking listing identity and sources')<>reviewed then
  raise exception 'review retry not idempotent'; end if;
 begin
  perform public.review_security_request(rid,1,'rejected','Stale reviewer');
  raise exception 'stale review accepted';
 exception when serialization_failure then null; end;
 perform public.review_security_request(rid,2,'rejected','Insufficient source coverage');
 begin
  perform public.review_security_request(rid,3,'reviewing','Reopen');
  raise exception 'terminal request changed';
 exception when invalid_parameter_value then null; end;
 if (select count(*) from subscription_private.security_request_reviews where request_id=rid)<>2 then
  raise exception 'invalid audit history'; end if;
 if public.subscription_snapshot()<>before_snapshot then raise exception 'queue changed sender snapshot'; end if;
 if exists(select 1 from subscription_private.securities where ticker='XYZ') then raise exception 'queue activated security'; end if;
end $$;
reset role;
-- Active catalogue requests can be marked available, without auto-subscription.
set role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000002',false);
select public.request_security('CSCO','XNAS','Existing supported listing');
reset role;
set role service_role;
do $$ declare rid uuid; begin
 select id into rid from subscription_private.security_requests where ticker='CSCO';
 perform public.review_security_request(rid,1,'available','Listing checked; choose CSCO in your preferences');
end $$;
reset role;
-- Approval revocation and unverified accounts cannot list or submit requests.
delete from subscription_private.approved_members where user_id='00000000-0000-0000-0000-000000000002';
-- Approval alone cannot authorize an unverified email identity.
insert into subscription_private.approved_members(user_id) values('00000000-0000-0000-0000-000000000003');
set role authenticated;
do $$ begin
 if exists(select 1 from subscription_private.security_requests) then raise exception 'revoked request read'; end if;
 begin
  perform public.get_my_security_requests(); raise exception 'revoked RPC read';
 exception when insufficient_privilege then null; end;
 begin
  perform public.request_security('REVOKED','XNAS','No access'); raise exception 'revoked submission';
 exception when insufficient_privilege then null; end;
end $$;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000003',false);
do $$ begin
 begin
  perform public.request_security('UNVERIFIED','XNAS','No access'); raise exception 'unverified submission';
 exception when insufficient_privilege then null; end;
end $$;
reset role;
set role anon;
do $$ begin
 begin
  perform public.get_my_security_requests(); raise exception 'anonymous request access';
 exception when insufficient_privilege then null; end;
 begin
  perform public.request_security('ANON','XNAS','No access'); raise exception 'anonymous submission';
 exception when insufficient_privilege then null; end;
end $$;
reset role;
select 'Security queue isolation, limits, review audit, retry, version and non-activation checks passed' as result;

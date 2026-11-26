-- All additional test data rolls back, preserving the concurrent test baseline.
begin;
insert into auth.users values
 ('00000000-0000-0000-0000-000000000004','admin@example.com',now()),
 ('00000000-0000-0000-0000-000000000005','unverified-admin@example.com',null),
 ('00000000-0000-0000-0000-000000000006','new-member@example.com',now());
insert into subscription_private.administrators(user_id) values
 ('00000000-0000-0000-0000-000000000004'),('00000000-0000-0000-0000-000000000005');
do $$ begin
 if has_function_privilege('service_role','public.get_admin_subscription(uuid)','EXECUTE') or
    has_table_privilege('service_role','subscription_private.administration_changes','INSERT,UPDATE,DELETE,TRUNCATE') or
    has_table_privilege('authenticated','subscription_private.administrators','INSERT,UPDATE,DELETE,SELECT') then
  raise exception 'Inherited administrative privilege';
 end if;
end $$;
set local role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',true);
do $$ begin
 begin
  perform public.get_admin_subscription(auth.uid()); raise exception 'ordinary member inspected admin data';
 exception when insufficient_privilege then null; end;
 begin
  perform public.get_admin_subscription_history(auth.uid()); raise exception 'ordinary member read audit';
 exception when insufficient_privilege then null; end;
 begin
  insert into subscription_private.administrators(user_id) values(auth.uid()); raise exception 'self administrator enrollment';
 exception when insufficient_privilege then null; end;
 begin
  perform public.correct_admin_subscription(auth.uid(),null,false,3,true,gen_random_uuid(),'Unauthorized',auth.uid());
  raise exception 'ordinary member corrected account';
 exception when insufficient_privilege then null; end;
end $$;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000005',true);
do $$ begin
 begin
  perform public.get_admin_subscription(auth.uid()); raise exception 'unverified admin access';
 exception when insufficient_privilege then null; end;
end $$;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000004',true);
do $$ declare before jsonb; p jsonb; result jsonb; history jsonb; uid uuid:='00000000-0000-0000-0000-000000000001'; begin
 before:=public.get_admin_subscription(uid);p:=before->'preferences'||'{"send_time":"10:00"}';
 if before->>'member_id'<>'legacy-member-001' or before->>'operator_id'<>auth.uid()::text then raise exception 'invalid admin view'; end if;
 result:=public.correct_admin_subscription(uid,p,true,3,true,'20000000-0000-0000-0000-000000000001','Schedule correction',auth.uid());
 if result->>'version'<>'4' or result->>'member_id'<>'legacy-member-001' then raise exception 'identity or version changed incorrectly'; end if;
 if public.correct_admin_subscription(uid,p,true,3,true,'20000000-0000-0000-0000-000000000001','Schedule correction',auth.uid())<>result then
  raise exception 'admin retry not idempotent'; end if;
 history:=public.get_admin_subscription_history(uid);
 if jsonb_array_length(history)<>1 or history->0->>'actor_id'<>auth.uid()::text or
    history->0->'before_state'<>jsonb_build_object('member_id','legacy-member-001','version',3,'approved',true,'preferences',before->'preferences') or
    history->0->'after_state'->'preferences'<>p then raise exception 'missing named audit evidence'; end if;
 begin
  perform public.correct_admin_subscription(uid,p,true,3,true,'20000000-0000-0000-0000-000000000001','Changed reason',auth.uid());
  raise exception 'changed retry input accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.correct_admin_subscription(uid,p,true,3,true,gen_random_uuid(),'Stale version',auth.uid());
  raise exception 'stale correction accepted';
 exception when serialization_failure then null; end;
 begin
  perform public.correct_admin_subscription(uid,p,true,4,false,gen_random_uuid(),'Stale approval',auth.uid());
  raise exception 'stale approval accepted';
 exception when serialization_failure then null; end;
 begin
  perform public.correct_admin_subscription(uid,p||'{"email":"injected@example.com"}',true,4,true,gen_random_uuid(),'Email injection',auth.uid());
  raise exception 'Auth email injection accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.correct_admin_subscription(uid,p||'{"tickers":["UNSUPPORTED"]}',true,4,true,gen_random_uuid(),'Unsupported security',auth.uid());
  raise exception 'administrator bypassed catalogue';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.correct_admin_subscription(uid,p,true,4,true,gen_random_uuid(),'Wrong actor',uid);
  raise exception 'different operator applied plan';
 exception when insufficient_privilege then null; end;
 begin
  update subscription_private.administration_changes set reason='rewrite'; raise exception 'admin rewrote audit';
 exception when insufficient_privilege then null; end;
 perform public.correct_admin_subscription(uid,null,false,4,true,'20000000-0000-0000-0000-000000000002','Revoke access',auth.uid());
 if (public.get_admin_subscription(uid)->>'approved')::boolean then raise exception 'revocation failed'; end if;
end $$;
reset role;
do $$ begin
 if jsonb_array_length(public.subscription_snapshot()->'config'->'members')<>0 then raise exception 'revoked account exported'; end if;
 if (select preferences->>'enabled' from subscription_private.members where member_id='legacy-member-001')<>'false' then
  raise exception 'correction changed opt-out'; end if;
end $$;
set local role authenticated;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000001',true);
do $$ begin
 if public.get_my_subscription() is not null then raise exception 'revoked member read settings'; end if;
 begin
  perform public.save_my_subscription('{}',5,gen_random_uuid()); raise exception 'revoked member saved';
 exception when insufficient_privilege then null; end;
end $$;
select set_config('request.jwt.claim.sub','00000000-0000-0000-0000-000000000004',true);
do $$ declare uid uuid:='00000000-0000-0000-0000-000000000001'; begin
 perform public.correct_admin_subscription(uid,null,true,5,false,gen_random_uuid(),'Restore approved membership',auth.uid());
 if public.get_admin_subscription(uid)->'preferences'->>'enabled'<>'false' then raise exception 'reapproval opted member in'; end if;
 perform public.correct_admin_subscription('00000000-0000-0000-0000-000000000006',null,true,0,false,gen_random_uuid(),'Approve verified signup',auth.uid());
 if public.get_admin_subscription('00000000-0000-0000-0000-000000000006')->'preferences'<>'null'::jsonb then
  raise exception 'approval created subscription'; end if;
 begin
  perform public.correct_admin_subscription('00000000-0000-0000-0000-000000000003',null,true,0,true,gen_random_uuid(),'Approve unverified target',auth.uid());
  raise exception 'unverified account approved';
 exception when invalid_parameter_value then null; end;
 perform public.correct_admin_subscription('00000000-0000-0000-0000-000000000003',null,false,0,true,gen_random_uuid(),'Revoke unverified target',auth.uid());
end $$;
reset role;
delete from subscription_private.administrators where user_id='00000000-0000-0000-0000-000000000004';
set local role authenticated;
do $$ begin
 begin
  perform public.get_admin_subscription('00000000-0000-0000-0000-000000000001'); raise exception 'revoked admin read';
 exception when insufficient_privilege then null; end;
 begin
  perform public.correct_admin_subscription('00000000-0000-0000-0000-000000000001',null,false,4,true,
    '20000000-0000-0000-0000-000000000002','Revoke access',auth.uid()); raise exception 'revoked admin retried';
 exception when insufficient_privilege then null; end;
end $$;
reset role;
set local role anon;
do $$ begin
 begin
  perform public.get_admin_subscription(null); raise exception 'anonymous admin access';
 exception when insufficient_privilege then null; end;
end $$;
reset role;
rollback;
select 'Administrator authorization, immutable identity, shared validation, versioned correction, approvals and named audit passed' as result;

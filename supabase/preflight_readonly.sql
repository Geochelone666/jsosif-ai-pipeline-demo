-- Run in the team's Supabase SQL Editor BEFORE approving any migration.
-- Read-only metadata and aggregate counts only: no credentials or member records.
begin transaction read only;
select current_database() as database_name, current_user as inspected_as,
       current_setting('server_version') as postgres_version;
select nspname as schema_name from pg_catalog.pg_namespace
 where nspname not like 'pg_%' and nspname <> 'information_schema' order by 1;
select n.nspname as schema_name,c.relname as object_name,c.relkind,
       c.relrowsecurity as rls_enabled,c.relforcerowsecurity as rls_forced
 from pg_catalog.pg_class c join pg_catalog.pg_namespace n on n.oid=c.relnamespace
 where n.nspname not like 'pg_%' and n.nspname <> 'information_schema'
 and c.relkind in ('r','p','v','m','f') order by 1,2;
select schemaname,tablename,policyname,permissive,roles,cmd
 from pg_catalog.pg_policies order by 1,2,3;
select n.nspname as schema_name,p.proname as function_name,
       pg_catalog.pg_get_function_identity_arguments(p.oid) as arguments,
       p.prosecdef as security_definer
 from pg_catalog.pg_proc p join pg_catalog.pg_namespace n on n.oid=p.pronamespace
 where n.nspname not like 'pg_%' and n.nspname <> 'information_schema'
 order by 1,2,3;
select event_object_schema,event_object_table,trigger_name,event_manipulation
 from information_schema.triggers order by 1,2,3;
select table_schema,table_name,grantee,privilege_type
 from information_schema.table_privileges
 where grantee in ('PUBLIC','anon','authenticated','service_role') order by 1,2,3,4;
select extname,extversion from pg_catalog.pg_extension order by 1;
select count(*) as auth_users,
       count(*) filter(where email_confirmed_at is not null) as confirmed_email_users
 from auth.users;
select count(*) as storage_buckets,count(*) filter(where public) as public_buckets
 from storage.buckets;
select to_regclass('supabase_migrations.schema_migrations') is not null as migration_registry_exists,
       to_regnamespace('subscription_private') is not null as subscription_schema_exists;
commit;
-- Counts are an observation, not evidence of a verified backup or an empty project.
-- Review conflicts and existing policies before applying any write migration.

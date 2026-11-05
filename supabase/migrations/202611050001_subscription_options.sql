-- Apply after subscription_authority; public catalogue, no other members' data.
begin;
create function public.subscription_options() returns jsonb
language plpgsql stable security definer set search_path = '' as $$
begin
 if not subscription_private.is_approved_member() then
  raise exception 'Team approval required' using errcode='42501';
 end if;
 return (select jsonb_build_object('groups',s.config->'groups',
          'tickers',(select coalesce(jsonb_agg(ticker order by ticker),'[]'::jsonb)
                     from subscription_private.securities))
         from subscription_private.settings s where singleton);
end $$;
revoke all on function public.subscription_options() from public,anon;
grant execute on function public.subscription_options() to authenticated;
commit;

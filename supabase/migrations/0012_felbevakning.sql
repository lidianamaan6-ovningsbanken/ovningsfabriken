-- Felbevakning: fel som uppstår hos tränarna sparas här, så att du ser dem i Supabase
-- (Table Editor → client_errors). Bara felmeddelande, var i koden, appversion och vy – inga pass eller personuppgifter.
create table if not exists public.client_errors (
  id bigint generated always as identity primary key,
  at timestamptz not null default now(),
  user_id uuid default auth.uid(),
  message text not null,
  source text,
  app_version text,
  view text,
  device text
);
alter table public.client_errors enable row level security;
revoke all on public.client_errors from anon, authenticated;

create or replace function public.report_error(msg text, src text default null, ver text default null, vw text default null, dev text default null) returns void
language plpgsql security definer set search_path = public as $$
begin
  -- högst 30 fel per tränare och dygn, så att en trasig enhet inte fyller tabellen
  if auth.uid() is not null and (select count(*) from client_errors where user_id = auth.uid() and at > now() - interval '1 day') >= 30 then return; end if;
  insert into client_errors (message, source, app_version, view, device)
  values (left(coalesce(msg, ''), 500), left(src, 300), left(ver, 40), left(vw, 40), left(dev, 120));
end $$;
revoke all on function public.report_error(text, text, text, text, text) from public;
grant execute on function public.report_error(text, text, text, text, text) to anon, authenticated;

-- Rensa fel äldre än 90 dagar (kör gärna då och då): delete from public.client_errors where at < now() - interval '90 days';

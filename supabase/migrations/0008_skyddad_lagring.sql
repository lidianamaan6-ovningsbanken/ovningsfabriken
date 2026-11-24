-- Skyddad lagring för appens kod, övningsfilmer och förhandsbilder.
-- Bara inloggade tränare med aktiv klubblicens (eller admin) kan hämta filer,
-- och då bara via tillfälliga länkar (signed URLs). Bara admin kan lägga in filer.

insert into storage.buckets (id, name, public, file_size_limit)
values ('skyddat', 'skyddat', false, 52428800)
on conflict (id) do update set public = false, file_size_limit = excluded.file_size_limit;

create or replace function public.has_access() returns boolean language sql stable security definer set search_path = public as $$
  select is_admin() or exists (
    select 1 from club_members m join licenses l on l.club_id = m.club_id
    where m.user_id = auth.uid() and l.valid_until >= current_date)
$$;
revoke execute on function public.has_access from anon, public;
grant execute on function public.has_access to authenticated;

drop policy if exists "skyddat: licens läser" on storage.objects;
drop policy if exists "skyddat: admin lägger in" on storage.objects;
drop policy if exists "skyddat: admin ändrar" on storage.objects;
drop policy if exists "skyddat: admin tar bort" on storage.objects;
create policy "skyddat: licens läser" on storage.objects for select to authenticated
  using (bucket_id = 'skyddat' and public.has_access());
create policy "skyddat: admin lägger in" on storage.objects for insert to authenticated
  with check (bucket_id = 'skyddat' and public.is_admin());
create policy "skyddat: admin ändrar" on storage.objects for update to authenticated
  using (bucket_id = 'skyddat' and public.is_admin()) with check (bucket_id = 'skyddat' and public.is_admin());
create policy "skyddat: admin tar bort" on storage.objects for delete to authenticated
  using (bucket_id = 'skyddat' and public.is_admin());

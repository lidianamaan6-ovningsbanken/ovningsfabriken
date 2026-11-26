-- Tränare kan själv lämna sin klubb (”Lämna laget” i appen).
-- Den sista ansvariga kan inte lämna – då står klubben utan ansvarig.
create or replace function public.leave_club(cid uuid) returns void
language plpgsql security definer set search_path = public as $$
declare r text; owners int;
begin
  if auth.uid() is null then raise exception 'Du måste vara inloggad'; end if;
  select role into r from club_members where club_id = cid and user_id = auth.uid();
  if r is null then return; end if;
  if r = 'owner' then
    select count(*) into owners from club_members where club_id = cid and role = 'owner';
    if owners <= 1 then raise exception 'Du är klubbens enda ansvariga. Gör någon annan till ansvarig först, eller kontakta Övningsfabriken.'; end if;
  end if;
  delete from club_members where club_id = cid and user_id = auth.uid();
end $$;
revoke all on function public.leave_club(uuid) from public, anon;
grant execute on function public.leave_club(uuid) to authenticated;

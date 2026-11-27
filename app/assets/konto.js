/* Övningsfabriken – konto och molnsynk (inloggningsrutan) */
(function () {
  'use strict';
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const M = () => window.OF_MOLN;
  const ago = t => { if (!t) return 'aldrig'; const s = Math.round((Date.now() - t) / 1000); return s < 10 ? 'nyss' : s < 60 ? s + ' s sedan' : s < 3600 ? Math.round(s / 60) + ' min sedan' : new Date(t).toLocaleString('sv-SE'); };
  const STATUS = { av: 'Inte inloggad', ansluter: 'Ansluter …', sparar: 'Sparar …', synkad: 'Sparat i molnet', fel: 'Kunde inte synka' };

  function statusLine(st) {
    if (!st.user) return 'Sparas bara på den här enheten';
    if (st.status === 'fel') return 'Kunde inte synka. Försöker igen.';
    if (st.pending || st.pushing) return 'Sparar …';
    return 'Sparat i molnet';
  }
  function navHTML() {
    const st = M()?.state || {};
    if (!st.user) return '<span class="of-acc-ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4M10 17l5-5-5-5M15 12H3"/></svg></span>'
      + '<span><strong>Logga in</strong><small>Spara dina pass i molnet</small></span>';
    const ok = st.status !== 'fel';
    return '<span class="of-acc-ic is-in" aria-hidden="true">' + esc((st.user.email || '?').slice(0, 1).toUpperCase()) + '<i class="of-acc-dot is-' + (ok ? 'ok' : 'fel') + '"></i></span>'
      + '<span><strong>' + esc(st.user.email) + '</strong><small data-moln-line>' + esc(statusLine(st)) + '</small></span>';
  }
  function refresh() {
    document.querySelectorAll('[data-moln-nav]').forEach(el => { el.innerHTML = navHTML(); });
    const d = document.getElementById('of-konto'); if (d?.open && !d.querySelector('input:focus')) d.innerHTML = dialogHTML();
  }

  function dialogHTML(msg) {
    const st = M()?.state || {};
    const head = '<div class="of-konto-head"><div><span class="of-eyebrow">Konto</span><h2>' + (st.user ? 'Ditt konto' : 'Spara i molnet') + '</h2></div>'
      + '<button type="button" class="of-konto-x" data-konto="close" aria-label="Stäng">×</button></div>';
    if (!M()) return head + '<p>Molnet är inte tillgängligt just nu.</p>';
    if (!st.user) return head
      + '<p class="of-konto-lead">Logga in med e-post så sparas dina pass, matcher och favoriter i molnet. Då finns de på alla dina enheter.</p>'
      + '<form class="of-konto-form" data-konto="form"><label for="of-konto-mail">E-postadress</label>'
      + '<input id="of-konto-mail" name="email" type="email" autocomplete="email" inputmode="email" required placeholder="namn@klubb.se">'
      + '<button class="btn primary" type="submit">Skicka inloggningslänk</button></form>'
      + (msg ? '<p class="of-konto-msg" role="status">' + msg + '</p>' : '')
      + '<p class="of-konto-note">Du behöver inget lösenord. Vi mejlar en länk som loggar in dig. Allt du redan gjort på den här enheten följer med upp.</p>';
    return head
      + '<dl class="of-konto-list"><div><dt>Inloggad som</dt><dd>' + esc(st.user.email) + '</dd></div>'
      + '<div><dt>Status</dt><dd><span class="of-acc-dot is-' + (st.status === 'fel' ? 'fel' : 'ok') + '"></span> ' + esc(statusLine(st)) + '</dd></div>'
      + '<div><dt>Senast synkad</dt><dd>' + esc(ago(st.lastSync)) + '</dd></div></dl>'
      + (st.lastError && st.status === 'fel' ? '<p class="of-konto-msg">' + esc(st.lastError) + '</p>' : '')
      + '<div class="of-konto-actions"><button type="button" class="btn" data-konto="sync">Synka nu</button>'
      + '<button type="button" class="of-text-action" data-konto="out">Logga ut</button></div>'
      + '<p class="of-konto-note"><button type="button" class="of-text-action" data-konto="data">Så sparas dina data →</button></p>'
      + '<div id="of-klubb" class="of-klubb">' + (clubCache || '<p class="of-konto-note">Hämtar klubb …</p>') + '</div>'
      + '<details class="of-konto-pass"><summary>Byt lösenord</summary><form data-konto="pass" class="of-konto-form"><label for="of-nytt-pass">Nytt lösenord</label>'
      + '<input id="of-nytt-pass" name="password" type="password" minlength="8" autocomplete="new-password" required><button class="btn" type="submit">Spara lösenord</button></form></details>';
  }

  /* ---------- Klubben: kollegor och inbjudningar ---------- */
  let clubCache = '';
  const inviteURL = t => location.origin + location.pathname.replace(/[^/]*$/, '') + 'app.html?inbjudan=' + t;
  async function loadClub() {
    const box = document.getElementById('of-klubb'); if (!box || !M()?.state.user) return;
    let a; try { a = await M().rpc('my_access'); window.OF_ACCESS = a; } catch (e) { box.innerHTML = '<p class="of-konto-msg">' + esc(e.message) + '</p>'; return; }
    const clubs = a?.clubs || [];
    if (!clubs.length) { clubCache = '<h3>Klubb</h3><p class="of-konto-note">' + (a?.admin ? 'Du är admin men inte med i någon klubb.' : 'Kontot är inte kopplat till någon klubb.') + '</p>'; box.innerHTML = clubCache; return; }
    let h = '';
    for (const c of clubs) {
      h += '<section class="of-klubb-c"><div class="of-klubb-top"><div><span class="of-eyebrow">' + (c.role === 'owner' ? 'Klubbadministration · du är ansvarig' : 'Tränare i klubben') + '</span><h3>' + esc(c.name) + '</h3></div>'
        + '<span class="of-klubb-seats"><b>' + c.used + '</b> / ' + c.seats + ' platser</span></div>'
        + '<p class="of-konto-note">' + (c.active ? 'Licensen gäller till ' + esc(c.valid_until) : 'Licensen gick ut ' + esc(c.valid_until)) + '</p>'
        + '<p class="of-konto-note of-roller">' + (c.role === 'owner'
          ? '<b>Ansvarig</b> bjuder in och tar bort tränare och ser vilka som är med. <b>Tränare</b> använder appen. Ingen av er ser någon annans pass, matcher eller anteckningar.'
          : 'Klubbens ansvariga bjuder in och tar bort tränare. Dina pass, matcher och anteckningar ser bara du.') + '</p>';
      const { data: members } = await M().sb.from('club_members').select('user_id,email,role,joined_at').eq('club_id', c.id).order('joined_at');
      const me = M().state.user.id;
      h += '<ul class="of-klubb-list">' + (Array.isArray(members) ? members : []).map(m => '<li><span class="of-acc-ic is-in sm">' + esc((m.email || '?').slice(0, 1).toUpperCase()) + '</span><span class="grow">' + esc(m.email || 'Okänd') + (m.user_id === me ? ' <small>(du)</small>' : '') + '<small>' + (m.role === 'owner' ? 'Ansvarig' : 'Tränare') + '</small></span>'
        + (c.role === 'owner' && m.role !== 'owner' ? '<button type="button" class="of-text-action" data-konto="remove" data-club="' + c.id + '" data-user="' + m.user_id + '" data-name="' + esc(m.email) + '">Ta bort</button>' : '') + '</li>').join('') + '</ul>';
      if (c.role === 'owner') {
        const { data: inv } = await M().sb.from('club_invites').select('token,label,role,expires_at,created_at').eq('club_id', c.id).is('used_by', null).eq('revoked', false).gt('expires_at', new Date().toISOString()).order('created_at');
        h += (inv?.length ? '<h4>Väntar på att gå med</h4><ul class="of-klubb-list">' + inv.map(i => '<li><span class="grow">' + esc(i.label || 'Inbjudan') + '<small>Gäller till ' + esc(i.expires_at.slice(0, 10)) + '</small></span>'
          + '<button type="button" class="of-text-action" data-konto="copy" data-url="' + esc(inviteURL(i.token)) + '">Kopiera länk</button>'
          + '<button type="button" class="of-text-action" data-konto="revoke" data-token="' + esc(i.token) + '">Ta bort</button></li>').join('') + '</ul>' : '')
          + (c.active && c.used < c.seats ? '<form class="of-konto-form of-klubb-inv" data-konto="invite" data-club="' + c.id + '"><label for="of-inv-' + c.id + '">Bjud in en kollega</label>'
            + '<div class="of-klubb-row"><input id="of-inv-' + c.id + '" name="label" placeholder="Namn, t.ex. Anna (valfritt)" maxlength="80"><button class="btn primary" type="submit">Skapa länk</button></div></form>'
            : '<p class="of-konto-note">' + (c.active ? 'Alla platser är använda. Ta bort någon eller kontakta Övningsfabriken för fler platser.' : '') + '</p>');
      }
      h += '</section>';
    }
    const { data: devs } = await M().sb.from('user_devices').select('device_id,label,last_seen').order('last_seen', { ascending: false });
    const mine = M().deviceId();
    h += '<section class="of-klubb-c"><h4>Dina enheter</h4><ul class="of-klubb-list">' + (Array.isArray(devs) ? devs : []).map(d => '<li><span class="grow">' + esc(d.label || 'Okänd enhet') + (d.device_id === mine ? ' <small>(den här)</small>' : '')
      + '<small>Senast använd ' + esc(String(d.last_seen).slice(0, 10)) + '</small></span>'
      + (d.device_id !== mine ? '<button type="button" class="of-text-action" data-konto="forget" data-dev="' + esc(d.device_id) + '">Logga ut</button>' : '') + '</li>').join('') + '</ul>'
      + '<p class="of-konto-note">Kontot är personligt och kan användas på ett begränsat antal enheter.</p></section>';
    clubCache = h; box.innerHTML = h;
  }
  async function copy(url) {
    try { if (navigator.share && /Mobi/i.test(navigator.userAgent)) { await navigator.share({ title: 'Inbjudan till Övningsfabriken', url }); return; } } catch (e) { }
    try { await navigator.clipboard.writeText(url); (window.toast || alert)('Länken är kopierad. Skicka den till din kollega.'); }
    catch (e) { prompt('Kopiera länken och skicka den till din kollega:', url); }
  }

  function open() {
    let d = document.getElementById('of-konto');
    if (!d) {
      d = document.createElement('dialog'); d.id = 'of-konto'; d.className = 'of-konto'; d.setAttribute('aria-label', 'Konto');
      document.body.appendChild(d);
      d.addEventListener('click', async e => {
        if (e.target === d) { d.close(); return; }
        const a = e.target.closest('[data-konto]')?.dataset.konto;
        if (a === 'close') d.close();
        if (a === 'data') { d.close(); window.OF_DATA_INFO?.(); }
        if (a === 'sync') { await M().pull(false, true); await M().push(); d.innerHTML = dialogHTML(); }
        if (a === 'out') { await M().signOut(); clubCache = ''; d.close(); }
        if (a === 'forget') { try { await M().rpc('forget_device', { dev: e.target.closest('[data-dev]').dataset.dev }); } catch (err) { alert(err.message); } loadClub(); }
        if (a === 'copy') copy(e.target.closest('[data-url]').dataset.url);
        if (a === 'revoke') { const t = e.target.closest('[data-token]').dataset.token; if (confirm('Ta bort inbjudan? Länken slutar fungera.')) { try { await M().rpc('revoke_invite', { invite_token: t }); } catch (err) { alert(err.message); } loadClub(); } }
        if (a === 'remove') { const b = e.target.closest('[data-user]'); if (confirm('Ta bort ' + b.dataset.name + ' från klubben? Platsen blir ledig.')) { try { await M().rpc('remove_member', { cid: b.dataset.club, member: b.dataset.user }); } catch (err) { alert(err.message); } loadClub(); } }
      });
      d.addEventListener('submit', async e => {
        e.preventDefault();
        const kind = e.target.dataset.konto;
        if (kind === 'invite') {
          const btn = e.target.querySelector('button'); btn.disabled = true;
          try { const t = await M().rpc('create_invite', { cid: e.target.dataset.club, invite_label: e.target.elements.label.value }); await loadClub(); copy(inviteURL(t)); }
          catch (err) { alert(err.message); btn.disabled = false; }
          return;
        }
        if (kind === 'pass') {
          try { await M().setPassword(e.target.elements.password.value); (window.toast || alert)('Lösenordet är sparat'); e.target.reset(); e.target.closest('details').open = false; }
          catch (err) { alert(err.message); }
          return;
        }
        const email = e.target.elements.email.value.trim(); const btn = e.target.querySelector('button');
        btn.disabled = true; btn.textContent = 'Skickar …';
        try {
          await M().signIn(email);
          d.innerHTML = dialogHTML('Klart! Öppna mejlet till <b>' + esc(email) + '</b> och tryck på länken. Kolla skräpposten om det dröjer.');
        } catch (err) {
          const m = /rate|seconds|limit/i.test(err.message || '') ? 'För många inloggningsmejl just nu. Vänta en stund och försök igen.' : 'Det gick inte att skicka mejlet: ' + esc(err.message || err);
          d.innerHTML = dialogHTML(m); d.querySelector('input').value = email;
        }
      });
    }
    d.innerHTML = dialogHTML();
    d.showModal();
    loadClub();
    d.querySelector('input, [data-konto="sync"]')?.focus();
  }

  window.OF_KONTO = { open, navHTML };
  const boot = () => { if (M()) { M().on(refresh); M().ready.then(refresh); } else setTimeout(boot, 100); };
  boot();
})();

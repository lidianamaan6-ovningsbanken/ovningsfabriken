/* Övningsfabriken – inloggningsgrind
 * Appen visas bara för inloggade tränare med aktiv klubblicens (eller admin).
 * Nya tränare kommer in via en inbjudningslänk: app.html?inbjudan=<kod>
 * Obs: grinden döljer appen i webbläsaren. Övningarna ligger ännu i appens JS-fil
 * och flyttas bakom databasens säkerhetsregler i nästa steg.
 */
(function () {
  'use strict';
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const M = () => window.OF_MOLN;
  const CACHE = 'of-tillgang';
  const DAYS7 = 7 * 864e5;
  const q = new URLSearchParams(location.search);
  // Inbjudan sparas på enheten så att den följer med även om man loggar in via en länk på mejlen
  let invite = q.get('inbjudan') || (() => { try { const v = JSON.parse(localStorage.getItem('of-inbjudan') || 'null'); return v && Date.now() - v.at < 864e5 ? v.t : null; } catch (e) { return null; } })();
  if (q.get('inbjudan')) { try { localStorage.setItem('of-inbjudan', JSON.stringify({ t: invite, at: Date.now() })); } catch (e) { } }
  const devOn = () => { try { return localStorage.getItem('of-utvecklare') === '1' || location.hostname === 'localhost' || q.get('utvecklare') === '1'; } catch (e) { return false; } };

  const st = { phase: 'start', access: null, msg: '', mode: invite ? 'signup' : 'login', busy: false, inviteClub: '', teamMode: 'first', picked: [] };
  const g = n => { try { return (0, eval)(n); } catch (e) { return undefined; } };

  /* ---------- Klubbens profil: märke och färg (sparas på enheten för startbilden) ---------- */
  const JFA_CREST = 'assets/club-crests/jfa-stor.png';
  const crestFor = c => c?.crest || (c?.catalog === 'Järfälla FA' ? JFA_CREST : (c?.catalog && window.OF_SIGN_IN?.crests?.[c.catalog])) || '';
  let brandInfo = (() => { try { return JSON.parse(localStorage.getItem('of-klubb') || 'null'); } catch (e) { return null; } })();
  function setBrand(c, save) {
    if (!c) return;
    brandInfo = { name: c.name, crest: crestFor(c), color: c.color || '#16392b' };
    if (save) { try { localStorage.setItem('of-klubb', JSON.stringify(brandInfo)); } catch (e) { } }
    applyTheme();
  }
  function applyTheme() {
    if (!brandInfo) return;
    document.documentElement.style.setProperty('--klubb', brandInfo.color);
    document.querySelector('meta[name=theme-color]')?.setAttribute('content', brandInfo.color);
  }
  applyTheme();
  function hideSplash() {
    const sp = document.getElementById('of-splash'); if (!sp || sp.dataset.ut) return; sp.dataset.ut = '1';
    const wait = Math.max(0, 900 - (Date.now() - (window.OF_SPLASH_AT || 0)));
    setTimeout(() => { sp.style.opacity = '0'; setTimeout(() => sp.remove(), 450); }, wait);
  }
  const primary = () => (st.access?.clubs || []).find(c => c.active) || (st.access?.clubs || [])[0] || null;
  const clubTeams = c => (window.OF_SIGN_IN?.teams || []).filter(t => c?.catalog && t.club === c.catalog);
  const skipKey = (uid, cid) => 'of-lag-hoppat.' + uid + '.' + cid;
  const readCache = () => { try { return JSON.parse(localStorage.getItem(CACHE) || 'null'); } catch (e) { return null; } };
  const writeCache = (v) => { try { v ? localStorage.setItem(CACHE, JSON.stringify(v)) : localStorage.removeItem(CACHE); } catch (e) { } };

  /* Snabbstart: senast kända tillgång på enheten släpper in direkt, sedan kontrolleras den på nytt */
  const cached = readCache();
  let open = !!(cached && cached.ok && Date.now() - cached.at < DAYS7 && !invite);
  if (open && cached.access) { st.access = cached.access; window.OF_ACCESS = cached.access; }

  function allowed(view) { return open || (view === 'dev' && devOn()); }

  /* ---------- Rendering ---------- */
  let root = null;
  function ensureRoot() {
    if (root) return root;
    root = document.createElement('div'); root.id = 'of-grind'; root.className = 'of-grind';
    document.body.appendChild(root);
    root.addEventListener('submit', onSubmit);
    root.addEventListener('click', onClick);
    return root;
  }
  const ofLogo = '<img class="of-grind-logo" src="assets/ovningsfabriken-logo-light.svg" alt="Övningsfabriken" width="280" height="92">';
  const brandHTML = () => brandInfo?.crest
    ? '<div class="of-grind-club"><img src="' + esc(brandInfo.crest) + '" alt=""><div><b>' + esc(brandInfo.name) + '</b><small>Övningsfabriken</small></div></div>'
    : ofLogo;
  function view() {
    const user = M()?.state.user;
    const msg = st.msg ? '<p class="of-grind-msg" role="alert">' + st.msg + '</p>' : '';
    const dev = devOn() ? '<button type="button" class="of-grind-dev" data-g="dev">Utvecklarfliken →</button>' : '';
    let body = '';
    if (st.phase === 'start' || st.phase === 'checking') {
      body = '<div class="of-grind-wait"><span class="of-grind-spin" aria-hidden="true"></span><p>Kontrollerar inloggningen …</p></div>';
    } else if (!user) {
      const signup = st.mode === 'signup';
      body = (invite ? '<span class="of-eyebrow">Inbjudan' + (st.inviteClub ? ' · ' + esc(st.inviteClub) : '') + '</span><h1>' + (signup ? 'Skapa ditt konto' : 'Logga in för att gå med') + '</h1><p class="of-grind-lead">Du har blivit inbjuden till ' + (st.inviteClub ? '<b>' + esc(st.inviteClub) + '</b> på ' : '') + 'Övningsfabriken. ' + (signup ? 'Välj e-post och lösenord så kopplas du till klubben.' : 'Logga in så kopplas kontot till klubben.') + '</p>'
        : '<span class="of-eyebrow">' + (brandInfo?.name ? esc(brandInfo.name) : 'Välkommen') + '</span><h1>Logga in</h1><p class="of-grind-lead">' + (brandInfo?.name ? 'Välkommen tillbaka till klubbens träningsplanering.' : 'Övningsfabriken är till för tränare med klubblicens.') + '</p>')
        + '<form class="of-grind-form" data-g="auth"><label for="g-mail">E-post</label><input id="g-mail" name="email" type="email" autocomplete="email" inputmode="email" required>'
        + '<label for="g-pass">Lösenord</label><input id="g-pass" name="password" type="password" autocomplete="' + (signup ? 'new-password' : 'current-password') + '" minlength="8" required>'
        + (signup ? '<small class="of-grind-hint">Minst 8 tecken.</small>' : '')
        + '<button class="of-grind-btn" type="submit"' + (st.busy ? ' disabled' : '') + '>' + (st.busy ? 'Vänta …' : signup ? 'Skapa konto och gå med' : 'Logga in') + '</button></form>' + msg
        + (invite ? '<p class="of-grind-alt">' + (signup ? 'Har du redan ett konto? <button type="button" data-g="mode" data-v="login">Logga in</button>' : 'Inget konto än? <button type="button" data-g="mode" data-v="signup">Skapa konto</button>') + '</p>'
          : '<p class="of-grind-alt">Ny tränare? Be klubbens ansvariga om en inbjudningslänk.</p>')
        + '<details class="of-grind-more"' + (st.mode === 'login' && invite ? ' open' : '') + '><summary>Glömt lösenordet?</summary><p>Kontakta klubbens ansvariga eller Övningsfabriken, så hjälper vi dig. Du kan också få en inloggningslänk på mejlen:</p>'
        + '<form data-g="link" class="of-grind-inline"><input name="email" type="email" required placeholder="din@epost.se" aria-label="E-post för inloggningslänk"><button type="submit">Skicka länk</button></form></details>';
    } else if (st.phase === 'team') {
      const c = st.teamClub; const teams = clubTeams(c); const groups = {};
      teams.forEach(t => { (groups[t.g || 'Lag'] = groups[t.g || 'Lag'] || []).push(t); });
      const name = M()?.state.user?.user_metadata?.name || '';
      body = '<span class="of-eyebrow">' + esc(c?.name || 'Klubben') + '</span><h1>' + (st.teamMode === 'change' ? 'Dina lag' : 'Vilket lag tränar du?') + '</h1>'
        + '<p class="of-grind-lead">' + (st.teamMode === 'change' ? 'Välj de lag du tränar. Det första blir ditt aktiva lag.' : 'Välj ditt lag så anpassas pass, övningar och läroplan efter åldern. Du kan välja flera.') + '</p>'
        + '<form class="of-grind-form" data-g="team"><label for="g-name">Ditt förnamn</label><input id="g-name" name="name" autocomplete="given-name" maxlength="40" value="' + esc(name) + '" placeholder="Så hälsar appen på dig">'
        + (st.teamMode === 'change' && st.picked.length > 1 ? '<label for="g-active">Aktivt lag i appen</label><select id="g-active" name="active" class="of-grind-select">' + teams.filter(t => st.picked.includes(t.id)).map(t => '<option value="' + esc(t.id) + '"' + (t.id === st.picked[0] ? ' selected' : '') + '>' + esc(t.name) + '</option>').join('') + '</select><small class="of-grind-hint">Lagen du kryssar i nedan sparas. Det aktiva laget måste vara ikryssat.</small>' : '')
        + Object.entries(groups).map(([grp, list]) => '<fieldset class="of-grind-teams"><legend>' + esc(grp) + '</legend>' + list.map(t =>
          '<label class="of-grind-team"><input type="checkbox" name="team" value="' + esc(t.id) + '"' + (st.picked.includes(t.id) ? ' checked' : '') + '><span>' + esc(t.name) + '</span></label>').join('') + '</fieldset>').join('')
        + '<button class="of-grind-btn" type="submit"' + (st.busy ? ' disabled' : '') + '>' + (st.busy ? 'Sparar …' : st.teamMode === 'change' ? 'Spara' : 'Spara och fortsätt') + '</button></form>' + msg
        + '<div class="of-grind-row">' + (st.teamMode === 'change' ? '<button type="button" class="of-grind-link" data-g="teamcancel">Avbryt</button>' : '<button type="button" class="of-grind-link" data-g="teamskip">Jag tränar inget lag just nu</button>') + '</div>';
    } else if (st.phase === 'devices') {
      const fmt = t => { try { return new Date(t).toLocaleDateString('sv-SE', { day: 'numeric', month: 'short' }); } catch (e) { return ''; } };
      body = '<span class="of-eyebrow">Enhetsgräns</span><h1>Kontot används redan</h1>'
        + '<p class="of-grind-lead">Ditt konto är aktivt på ' + st.devices.length + ' enheter, och licensen tillåter ' + st.limit + ' per tränare. Logga ut en av dem för att använda den här.</p>'
        + '<ul class="of-grind-devices">' + st.devices.map(d => '<li><span><b>' + esc(d.label || 'Okänd enhet') + '</b><small>Senast använd ' + esc(fmt(d.last_seen)) + '</small></span>'
          + '<button type="button" class="of-grind-btn is-ghost" data-g="replace" data-id="' + esc(d.id) + '"' + (st.busy ? ' disabled' : '') + '>Logga ut den</button></li>').join('') + '</ul>'
        + msg + '<p class="of-grind-alt">Kontot är personligt. Kollegor behöver en egen inbjudan från klubbens ansvariga.</p>'
        + '<div class="of-grind-row"><button type="button" class="of-grind-link" data-g="out">Logga ut här i stället</button></div>';
    } else {
      const clubs = st.access?.clubs || [];
      const expired = clubs.filter(c => !c.active);
      body = '<span class="of-eyebrow">Ingen aktiv licens</span><h1>Nästan där</h1>'
        + '<p class="of-grind-lead">Du är inloggad som <b>' + esc(user.email) + '</b>, men kontot är inte kopplat till någon klubb med aktiv licens.</p>'
        + (expired.length ? '<p class="of-grind-msg">' + expired.map(c => esc(c.name) + 's licens gick ut ' + esc(c.valid_until)).join('<br>') + '. Kontakta klubbens ansvariga.</p>' : '')
        + msg
        + '<ul class="of-grind-steps"><li>Har du fått en <b>inbjudningslänk</b>? Öppna den igen, så kopplas du till klubben.</li><li>Ansvarig för klubben? Kontakta Övningsfabriken för en licens.</li></ul>'
        + '<div class="of-grind-row"><button type="button" class="of-grind-btn is-ghost" data-g="retry">Försök igen</button><button type="button" class="of-grind-link" data-g="out">Logga ut</button></div>';
    }
    const club = brandInfo?.crest ? ' has-club' : '';
    return '<div class="of-grind-card' + club + '" role="dialog" aria-modal="true" aria-labelledby="g-title"><div class="of-grind-side" aria-hidden="true"><div>' + brandHTML() + '<p>Planera träningen.<br>Utveckla spelarna.</p></div></div>'
      + '<div class="of-grind-main"><div class="of-grind-mobile-logo">' + brandHTML() + '</div>' + body.replace('<h1>', '<h1 id="g-title">') + dev + '</div></div>';
  }
  function show() {
    hideSplash();
    const r = ensureRoot(); r.hidden = false; document.documentElement.classList.add('of-grind-on');
    const focus = document.activeElement?.id; const vals = {};
    r.querySelectorAll('input').forEach(i => { vals[i.id || i.name] = i.value; });
    r.innerHTML = view();
    r.querySelectorAll('input').forEach(i => { if (vals[i.id || i.name]) i.value = vals[i.id || i.name]; });
    (focus && document.getElementById(focus) || r.querySelector('input'))?.focus({ preventScroll: true });
  }
  function hide() { if (root) { root.hidden = true; root.innerHTML = ''; } document.documentElement.classList.remove('of-grind-on'); }

  const appLoaded = () => { try { return typeof (0, eval)('render') === 'function'; } catch (e) { return false; } };
  function refreshApp() {
    const ST = (() => { try { return (0, eval)('ST'); } catch (e) { return null; } })();
    if (open) { hide(); if (!appLoaded()) window.OF_SKYDD?.loadApp(); else { applyAccount(); hideSplash(); } }
    else if (ST && ST.view === 'dev' && devOn()) hide(); else show();
    try { if (appLoaded()) (0, eval)('render')(); } catch (e) { }
  }
  function devStandalone() {
    hide();
    const app = document.getElementById('app');
    if (app && window.OF_DEV) {
      app.className = 'wrap of-workspace';
      app.innerHTML = '<p class="of-muted-note" style="margin:0 0 8px">Utvecklarläge utan inloggning. <button type="button" class="of-text-action" data-g-login>Logga in</button></p>' + OF_DEV.html();
      if (!app.dataset.gLogin) { app.dataset.gLogin = '1'; app.addEventListener('click', e => { if (e.target.closest('[data-g-login]')) { st.phase = M()?.state.user ? st.phase : 'login'; show(); } }); }
      OF_DEV.mount();
    }
  }

  /* ---------- Logik ---------- */
  const friendly = (e) => {
    const m = e?.message || String(e);
    if (/Invalid login credentials/i.test(m)) return 'Fel e-post eller lösenord.';
    if (/already registered|already exists/i.test(m)) { st.mode = 'login'; return 'Det finns redan ett konto med den e-posten. Logga in med ditt lösenord, eller tryck Glömt lösenordet? nedan så får du en inloggningslänk på mejlen.'; }
    if (/Password should be at least/i.test(m)) return 'Lösenordet måste vara minst 8 tecken.';
    if (/Email not confirmed/i.test(m)) return 'E-postadressen är inte bekräftad än.';
    if (/rate|seconds/i.test(m)) return 'För många försök. Vänta en stund och försök igen.';
    return esc(m);
  };

  async function check() {
    lastCheck = Date.now();
    const user = M()?.state.user;
    if (!user) { open = false; writeCache(null); st.phase = 'login'; refreshApp(); return; }
    if (!readCache() || !open) { st.phase = 'checking'; if (!open) show(); }
    try {
      if (invite) {
        try {
          const r = await M().rpc('accept_invite', { invite_token: invite });
          st.msg = ''; st.inviteClub = r?.club || '';
          (window.toast || (() => { }))(r?.already ? 'Du är redan med i ' + r.club : 'Välkommen till ' + r.club + '!');
        } catch (e) { st.msg = 'Inbjudan kunde inte användas: ' + friendly(e); }
        invite = null; try { localStorage.removeItem('of-inbjudan'); } catch (e) { }
        const u = new URL(location.href); u.searchParams.delete('inbjudan');
        if (!u.searchParams.get('team') && u.searchParams.get('utan-lag') !== '1' && /app\.html$/.test(u.pathname)) u.searchParams.set('utan-lag', '1');
        history.replaceState(null, '', u.toString());
      }
      const reg = await M().rpc('register_device', { dev: M().deviceId(), dev_label: M().deviceLabel() });
      if (reg && reg.ok === false) {
        open = false; writeCache(null); st.phase = 'devices'; st.devices = reg.devices || []; st.limit = reg.limit; refreshApp(); return;
      }
      const a = await M().rpc('my_access');
      st.access = a;
      const ok = !!(a?.admin || (a?.clubs || []).some(c => c.active));
      open = ok; writeCache(ok ? { ok, at: Date.now(), uid: user.id, access: a } : null);
      window.OF_ACCESS = a;
      st.phase = ok ? 'open' : 'nolicense';
      const pc = primary();
      if (pc) setBrand(pc, true);
      let skipped = false; try { skipped = localStorage.getItem(skipKey(user.id, pc?.id)) === '1'; } catch (e) { }
      if (ok && pc && !(pc.teams || []).length && clubTeams(pc).length && !skipped) {
        open = false; st.phase = 'team'; st.teamMode = 'first'; st.teamClub = pc; st.picked = [];
      }
    } catch (e) {
      const c = readCache();
      if (c?.ok && c.uid === user.id && Date.now() - c.at < DAYS7) { open = true; st.phase = 'open'; window.OF_ACCESS = c.access; st.access = c.access; }
      else { open = false; st.phase = 'nolicense'; st.msg = 'Kunde inte kontrollera licensen: ' + friendly(e); }
    }
    refreshApp();
  }

  async function onSubmit(e) {
    const f = e.target; const kind = f.dataset.g; if (!kind) return;
    e.preventDefault();
    if (kind === 'auth') {
      const email = f.elements.email.value.trim(), password = f.elements.password.value;
      st.busy = true; st.msg = ''; show();
      try {
        if (st.mode === 'signup') {
          const d = await M().signUp(email, password);
          if (!d.session) { st.msg = 'Kontot är skapat men behöver bekräftas. Kontakta Övningsfabriken.'; }
        } else await M().signInPassword(email, password);
      } catch (err) { st.msg = friendly(err); }
      st.busy = false; if (!M().state.user) show();
    }
    if (kind === 'team') {
      const ids = [...f.querySelectorAll('input[name=team]:checked')].map(i => i.value);
      const name = f.elements.name.value.trim();
      if (!ids.length) { st.msg = 'Välj minst ett lag, eller tryck "Jag tränar inget lag just nu".'; show(); return; }
      st.busy = true; st.msg = ''; show();
      try {
        const c = st.teamClub;
        // aktivt lag först: behåll nuvarande om det fortfarande är valt
        const act = f.elements.active?.value;
        const cur = act && ids.includes(act) ? act : (st.teamMode === 'change' && st.picked[0] && ids.includes(st.picked[0]) ? st.picked[0] : null);
        const ordered = cur ? [cur, ...ids.filter(i => i !== cur)] : ids;
        await M().rpc('set_my_teams', { cid: c.id, team_ids: ordered });
        if (name !== (M().state.user?.user_metadata?.name || '')) await M().sb.auth.updateUser({ data: { name } });
        c.teams = ordered; (st.access?.clubs || []).forEach(x => { if (x.id === c.id) x.teams = ordered; });
        writeCache({ ok: true, at: Date.now(), uid: M().state.user.id, access: st.access }); window.OF_ACCESS = st.access;
        st.busy = false; open = true; st.phase = 'open'; forceTeam = ordered[0];
        refreshApp();
      } catch (err) { st.busy = false; st.msg = friendly(err); show(); }
      return;
    }
    if (kind === 'link') {
      const btn = f.querySelector('button'); btn.disabled = true;
      try { await M().signIn(f.elements.email.value.trim()); st.msg = 'Klart! Öppna mejlet och tryck på länken' + (invite ? ' – inbjudan följer med automatiskt.' : '.') + ' Kolla skräpposten om det dröjer.'; }
      catch (err) { st.msg = friendly(err); }
      show();
    }
  }
  async function onClick(e) {
    const b = e.target.closest('[data-g]'); if (!b || b.tagName === 'FORM') return;
    const a = b.dataset.g;
    if (a === 'mode') { st.mode = b.dataset.v; st.msg = ''; show(); }
    if (a === 'out') { open = false; writeCache(null); await M().signOut(); st.msg = ''; show(); }
    if (a === 'retry') { st.msg = ''; check(); }
    if (a === 'teamskip') { try { localStorage.setItem(skipKey(M().state.user.id, st.teamClub?.id), '1'); } catch (err) { } open = true; st.phase = 'open'; refreshApp(); }
    if (a === 'teamcancel') { open = true; st.phase = 'open'; hide(); }
    if (a === 'replace') {
      st.busy = true; st.msg = ''; show();
      try { const r = await M().rpc('replace_device', { dev: M().deviceId(), dev_label: M().deviceLabel(), remove_dev: b.dataset.id }); if (r?.ok === false) { st.devices = r.devices || []; } else { st.busy = false; return check(); } }
      catch (err) { st.msg = friendly(err); }
      st.busy = false; show();
    }
    if (a === 'dev') {
      if (appLoaded()) { try { (0, eval)('ST').view = 'dev'; } catch (err) { } hide(); try { (0, eval)('render')(); } catch (err) { } }
      else devStandalone();
    }
  }

  let lastUid;
  function boot() {
    if (!M()) { setTimeout(boot, 50); return; }
    if (open) window.OF_SKYDD?.loadApp();
    if (!M().sb) { open = false; st.phase = 'nolicense'; st.msg = 'Kunde inte ansluta till Övningsfabriken. Kontrollera nätet och ladda om sidan.'; show(); return; }
    if (invite && M().sb) M().rpc('invite_info', { invite_token: invite }).then(r => { if (r?.ok) { st.inviteClub = r.name; setBrand(r, false); if (!open) show(); } }).catch(() => { });
    else if (q.get('klubb') && M().sb) M().rpc('club_brand', { club_slug: q.get('klubb') }).then(r => { if (r?.name) { setBrand(r, true); if (!open) show(); } }).catch(() => { });
    M().ready.then(() => { lastUid = M().state.user?.id; check(); });
    M().on(s => { const uid = s.user?.id; if (uid !== lastUid) { lastUid = uid; open = false; check(); } });
  }
  if (!open) document.documentElement.classList.add('of-grind-on');
  /* Kontrollera igen när appen öppnas på nytt (högst var tionde minut), så att en utloggad enhet låses */
  let lastCheck = 0;
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible' && M()?.state.user && Date.now() - lastCheck > 6e5) { lastCheck = Date.now(); check(); }
  });
  /* Ställ in tränarens lag och namn i appen när den har laddats */
  let forceTeam = null;
  function applyAccount() {
    const ST = g('ST'); if (!ST || !appLoaded()) return;
    const c = primary() || (window.OF_ACCESS?.clubs || [])[0]; const user = M()?.state.user;
    window.OF_PROFILE = { name: user?.user_metadata?.name || '', club: c || null, crest: crestFor(c) };
    const teams = c?.teams || [];
    const want = forceTeam || (teams.length && !teams.includes(ST.team) ? teams[0] : null); forceTeam = null;
    if (want) {
      const t = (g('CLUB_TEAMS') || []).find(x => x.id === want);
      if (t) { g('applyTeam')(t); ST.workspaceTeamChoice = true; ST.bankJ = { t: t.id, sf: '' }; try { g('persist')(); } catch (e) { } }
    }
    try { g('render')(); } catch (e) { }
  }
  function pickTeam() {
    const c = primary(); if (!c || !clubTeams(c).length) return false;
    st.teamClub = c; st.teamMode = 'change'; st.picked = (c.teams || []).slice(); st.msg = ''; st.phase = 'team'; open = true;
    show(); return true;
  }
  function appReady() { applyAccount(); hideSplash(); }
  setTimeout(hideSplash, 4000);
  window.OF_GRIND = { allowed, show, check, isOpen: () => open, pickTeam, appReady, applyAccount };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();

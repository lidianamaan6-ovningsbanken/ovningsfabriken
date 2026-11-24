/* Övningsfabriken – Utvecklarfliken
 * Syns bara när den slagits på med ?utvecklare=1 (sparas på enheten) eller på localhost.
 * Kräver ingen inloggning. Den använder bara den publika nyckeln, så den kan inte läsa
 * någon annans data – databasens säkerhetsregler (RLS) gäller som vanligt.
 */
(function () {
  'use strict';
  const ERR = [];
  window.addEventListener('error', e => ERR.unshift(new Date().toLocaleTimeString('sv-SE') + ' ' + (e.message || 'Fel') + (e.filename ? ' (' + e.filename.split('/').pop() + ':' + e.lineno + ')' : '')));
  window.addEventListener('unhandledrejection', e => ERR.unshift(new Date().toLocaleTimeString('sv-SE') + ' Promise: ' + (e.reason?.message || e.reason)));
  const g = (n) => { try { return (0, eval)(n); } catch (e) { return undefined; } };
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const M = () => window.OF_MOLN;
  const nf = new Intl.NumberFormat('sv-SE');
  const KIND = { sess: 'Pass', match: 'Matcher', mxteam: 'Matchlag', mxform: 'Uppställningar', saved: 'Favoriter', settings: 'Inställningar' };
  let ping = null, cloud = null, cloudErr = '', searchQ = '', adminClubs = null, adminErr = '', newLink = '';
  const inviteURL = t => location.origin + location.pathname.replace(/[^/]*$/, '') + 'app.html?inbjudan=' + t;
  const inYear = () => { const d = new Date(); d.setFullYear(d.getFullYear() + 1); return d.toISOString().slice(0, 10); };

  const card = (title, eyebrow, body, wide) => '<section class="of-home-panel of-dev-card' + (wide ? ' is-wide' : '') + '"><div class="of-panel-head"><div><span class="of-eyebrow">' + eyebrow + '</span><h2>' + title + '</h2></div></div>' + body + '</section>';
  const rows = (pairs) => '<dl class="of-dev-dl">' + pairs.map(([k, v]) => '<div><dt>' + esc(k) + '</dt><dd>' + v + '</dd></div>').join('') + '</dl>';
  const ver = (re) => esc((document.querySelector(re)?.getAttribute('src') || document.querySelector(re)?.getAttribute('href') || '').split('?v=')[1] || '–');
  const lsSize = () => { let n = 0; try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); n += k.length + (localStorage.getItem(k) || '').length; } } catch (e) { } return n * 2; };

  function html() {
    const BANK = g('BANK') || [], FILMS = g('OF_EXERCISE_FILM_IDS') || new Set(), POST = g('OF_FILM_POSTERS') || {};
    const st = M()?.state || {};
    const cols = M()?.collections() || {};
    const theme = document.documentElement.dataset.theme || 'system';
    const top = (g('workspaceTop') || ((t) => '<h1>' + t + '</h1>'))('Utvecklare', 'Bara för dig · syns inte för tränare');

    const version = rows([
      ['Appens JS', '<code>' + ver('script[src*="assets/app-"]') + '</code>'],
      ['CSS', '<code>' + ver('link[href*="workspace.css"]') + '</code>'],
      ['Övningar i banken', nf.format(BANK.length)],
      ['Med film', nf.format(FILMS.size) + ' (' + Math.round(FILMS.size / Math.max(1, BANK.length) * 100) + ' %)'],
      ['Med förhandsbild', nf.format(Object.keys(POST).length)],
      ['Skärm', innerWidth + ' × ' + innerHeight + ' · ' + devicePixelRatio + 'x'],
      ['Nätverk', navigator.onLine ? 'Online' : 'Offline'],
      ['Installerad app', matchMedia('(display-mode: standalone)').matches ? 'Ja' : 'Nej'],
    ]);

    const countRows = Object.keys(KIND).map(k => '<tr><td>' + KIND[k] + '</td><td>' + nf.format(Object.keys(cols[k] || {}).length) + '</td><td>' + (cloud ? nf.format(cloud[k] || 0) : '–') + '</td></tr>').join('');
    const moln = rows([
      ['Databasen', ping ? (ping.ok ? '<span class="of-acc-dot is-ok"></span> Svarar på ' + ping.ms + ' ms' : '<span class="of-acc-dot is-fel"></span> ' + esc(ping.error)) : 'Kontrollerar …'],
      ['Inloggad', st.user ? esc(st.user.email) : 'Nej (appen fungerar ändå, allt sparas lokalt)'],
      ['Synkstatus', esc(st.status || '–') + (st.pending ? ' · ' + st.pending + ' väntar' : '')],
      ['Senast synkad', st.lastSync ? new Date(st.lastSync).toLocaleTimeString('sv-SE') : '–'],
    ]) + '<table class="of-dev-table"><thead><tr><th>Data</th><th>På enheten</th><th>I molnet</th></tr></thead><tbody>' + countRows + '</tbody></table>'
      + (cloudErr ? '<p class="of-konto-msg">' + esc(cloudErr) + '</p>' : '')
      + '<div class="of-dev-actions">' + (st.user
        ? '<button class="btn" data-dev="sync">Synka nu</button><button class="btn" data-dev="resync">Full omsynk</button><button class="of-text-action" data-a="ofAccount">Konto</button>'
        : '<button class="btn primary" data-a="ofAccount">Logga in</button>') + '</div>';

    const lokal = rows([
      ['Pass', nf.format(Object.keys(cols.sess || {}).length)],
      ['Matcher', nf.format(Object.keys(cols.match || {}).length)],
      ['Favoriter', nf.format(Object.keys(cols.saved || {}).length)],
      ['Lagringsutrymme', nf.format(Math.round(lsSize() / 1024)) + ' kB'],
    ]) + '<div class="of-dev-actions"><button class="btn" data-dev="export">Exportera som JSON</button>'
      + '<button class="btn" data-dev="testdata">Skapa testvecka</button><button class="btn" data-dev="cleartest">Ta bort testdata</button>'
      + '<button class="of-text-action of-dev-danger" data-dev="wipe">Rensa all lokal data</button></div>';

    const tema = '<div class="of-dev-seg" role="group" aria-label="Tema">' + [['system', 'System'], ['light', 'Ljust'], ['dark', 'Mörkt']].map(([k, l]) =>
      '<button type="button" data-dev="theme" data-v="' + k + '" aria-pressed="' + (theme === k) + '">' + l + '</button>').join('') + '</div>'
      + '<p class="of-muted-note">Gäller bara den här fliken tills sidan laddas om.</p>';

    const search = '<label class="of-dev-search"><span class="sr-only">Söktest</span><input id="of-dev-q" type="search" placeholder="Testa sökningen, t.ex. 3 mot 3" value="' + esc(searchQ) + '"></label><ol class="of-dev-results" id="of-dev-res"></ol>';

    const byStage = {}; BANK.forEach(b => { const k = b.stage || b.phase || 'Övrigt'; const o = byStage[k] = byStage[k] || { n: 0, f: 0 }; o.n++; if (FILMS.has(b.id)) o.f++; });
    const tack = '<table class="of-dev-table"><thead><tr><th>Spelmoment</th><th>Filmer</th><th>Täckning</th></tr></thead><tbody>'
      + Object.entries(byStage).sort((a, b) => b[1].n - a[1].n).map(([k, o]) => '<tr><td>' + esc(k) + '</td><td>' + o.f + ' / ' + o.n + '</td><td><span class="of-dev-bar"><i style="width:' + Math.round(o.f / o.n * 100) + '%"></i></span></td></tr>').join('') + '</tbody></table>';

    const errs = ERR.length ? '<ul class="of-dev-log">' + ERR.slice(0, 30).map(e => '<li>' + esc(e) + '</li>').join('') + '</ul>' : '<p class="of-muted-note">Inga fel sedan sidan laddades.</p>';
    const mlog = (st.log || []).length ? '<ul class="of-dev-log">' + st.log.slice(0, 30).map(e => '<li>' + esc(e) + '</li>').join('') + '</ul>' : '<p class="of-muted-note">Inget har hänt än.</p>';

    const isAdmin = !!window.OF_ACCESS?.admin;
    const lic = !st.user ? '<p class="of-muted-note">Logga in med ditt admin-konto för att skapa och hantera klubblicenser.</p>'
      : !isAdmin ? '<p class="of-muted-note">Ditt konto är inte admin. Kör raden i README (supabase/README.md) för att bli admin.</p>'
      : '<form class="of-dev-lic" data-devform="club"><label>Klubbens namn<input name="name" required minlength="2" placeholder="t.ex. Järfälla FF"></label>'
        + '<div class="of-dev-two"><label>Platser<input name="seats" type="number" min="1" max="500" value="6" required></label><label>Gäller till<input name="valid" type="date" value="' + inYear() + '" required></label></div>'
        + '<button class="btn primary" type="submit">Skapa klubb och ägarlänk</button></form>'
        + (newLink ? '<div class="of-dev-link"><span class="of-eyebrow">Skicka till klubbens ansvariga</span><code>' + esc(newLink) + '</code><button class="btn" data-dev="copy" data-url="' + esc(newLink) + '">Kopiera länk</button></div>' : '')
        + (adminErr ? '<p class="of-konto-msg">' + esc(adminErr) + '</p>' : '')
        + (adminClubs ? (adminClubs.length ? '<table class="of-dev-table"><thead><tr><th>Klubb</th><th>Platser</th><th>Till</th></tr></thead><tbody>' + adminClubs.map(c =>
          '<tr><td><b>' + esc(c.name) + '</b><br><small class="of-muted-note">' + (c.owners.length ? esc(c.owners.join(', ')) : 'Ingen ansvarig än') + '</small><br>'
          + '<button class="of-text-action" data-dev="ownerlink" data-id="' + c.id + '">Ny ägarlänk</button> · <button class="of-text-action" data-dev="extend" data-id="' + c.id + '" data-seats="' + c.seats + '" data-valid="' + c.valid_until + '">+1 år</button> · <button class="of-text-action" data-dev="seats" data-id="' + c.id + '" data-seats="' + c.seats + '" data-valid="' + c.valid_until + '">Ändra platser</button></td>'
          + '<td>' + c.members + ' / ' + c.seats + '</td><td' + (c.valid_until < new Date().toISOString().slice(0, 10) ? ' class="of-dev-danger"' : '') + '>' + esc(c.valid_until) + '</td></tr>').join('') + '</tbody></table>'
          : '<p class="of-muted-note">Inga klubbar än.</p>') : '<p class="of-muted-note">Hämtar klubbar …</p>');

    return top + '<div class="of-home2 of-dev">' + '<div class="of-dev-grid">'
      + card('Licenser', 'Admin', lic, true)
      + card('Molnet', 'Supabase', moln) + card('Versioner', 'Bygget', version)
      + card('Lokal data', 'Den här enheten', lokal) + card('Tema', 'Utseende', tema)
      + card('Söktest', 'Övningsbanken', search) + card('Filmtäckning', 'Övningsbanken', tack)
      + card('Felogg', 'Sedan sidan laddades', errs) + card('Synklogg', 'Molnet', mlog)
      + '</div></div>';
  }

  function runSearch() {
    const box = document.getElementById('of-dev-res'); if (!box) return;
    const q = searchQ.trim(); if (!q) { box.innerHTML = ''; return; }
    const FILMS = g('OF_EXERCISE_FILM_IDS') || new Set();
    const res = (g('searchBank') || (() => []))(q, g('BANK'), 12);
    box.innerHTML = res.length ? res.map(b => '<li><button type="button" data-a="open" data-id="bank-' + esc(b.id) + '"><code>' + esc(b.id) + '</code> ' + esc(b.name) + (FILMS.has(b.id) ? ' <span class="of-dev-tag">film</span>' : '') + '</button></li>').join('') : '<li class="of-muted-note">Inga träffar</li>';
  }

  async function refreshRemote() {
    if (!M()) return;
    try { ping = await M().ping(); } catch (e) { ping = { ok: false, error: e.message }; }
    try { cloud = await M().cloudCounts(); cloudErr = ''; } catch (e) { cloudErr = e.message; }
    if (M().state.user) {
      try { window.OF_ACCESS = await M().rpc('my_access'); } catch (e) { }
      if (window.OF_ACCESS?.admin) { try { adminClubs = await M().rpc('admin_clubs'); adminErr = ''; } catch (e) { adminErr = e.message; } }
    }
    rerender();
  }
  function rerender() {
    if (g('ST')?.view !== 'dev') return;
    const y = scrollY; const focus = document.activeElement?.id;
    g('render')?.();
    scrollTo(0, y); if (focus) document.getElementById(focus)?.focus();
  }

  let bound = false, unsub = null, timer = null;
  function mount() {
    runSearch();
    if (!unsub && M()) unsub = M().on(() => { clearTimeout(timer); timer = setTimeout(() => { if (!document.activeElement || document.activeElement.id !== 'of-dev-q') rerender(); }, 400); });
    if (!ping) refreshRemote();
    if (bound) return; bound = true;
    document.addEventListener('input', e => { if (e.target.id === 'of-dev-q') { searchQ = e.target.value; runSearch(); } });
    document.addEventListener('submit', async e => {
      const f = e.target; if (f.dataset.devform !== 'club') return; e.preventDefault();
      try {
        const r = await M().rpc('admin_create_club', { club_name: f.elements.name.value, seat_count: Number(f.elements.seats.value), valid: f.elements.valid.value });
        newLink = inviteURL(r.token); adminClubs = await M().rpc('admin_clubs'); adminErr = '';
      } catch (err) { adminErr = err.message; }
      rerender();
    });
    document.addEventListener('click', async e => {
      const b = e.target.closest('[data-dev]'); if (!b) return;
      const a = b.dataset.dev; const T = g('toast') || alert;
      if (a === 'copy') { try { await navigator.clipboard.writeText(b.dataset.url); T('Länken är kopierad'); } catch (err) { prompt('Kopiera länken:', b.dataset.url); } }
      if (a === 'ownerlink') { try { newLink = inviteURL(await M().rpc('admin_owner_link', { cid: b.dataset.id })); } catch (err) { adminErr = err.message; } rerender(); }
      if (a === 'extend' || a === 'seats') {
        let seats = Number(b.dataset.seats), valid = b.dataset.valid;
        if (a === 'extend') { const d = new Date(Math.max(Date.now(), new Date(valid).getTime())); d.setFullYear(d.getFullYear() + 1); valid = d.toISOString().slice(0, 10); }
        else { const v = prompt('Antal platser:', seats); if (!v) return; seats = Number(v); }
        try { await M().rpc('admin_set_license', { cid: b.dataset.id, seat_count: seats, valid }); adminClubs = await M().rpc('admin_clubs'); } catch (err) { adminErr = err.message; }
        rerender();
      }
      if (a === 'sync') { await M().pull(false); await M().push(); refreshRemote(); T('Synkat'); }
      if (a === 'resync') { await M().resetSync(); refreshRemote(); T('Full omsynk klar'); }
      if (a === 'theme') { const v = b.dataset.v; if (v === 'system') delete document.documentElement.dataset.theme; else document.documentElement.dataset.theme = v; rerender(); }
      if (a === 'export') {
        const data = JSON.stringify({ exporterad: new Date().toISOString(), ...M()?.collections() }, null, 2);
        const url = URL.createObjectURL(new Blob([data], { type: 'application/json' }));
        const l = document.createElement('a'); l.href = url; l.download = 'ovningsfabriken-data.json'; l.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
      }
      if (a === 'testdata') {
        const W = g('workspaceWeek')(g('todayStr')()); const BANK = g('BANK');
        const pick = n => g('bankToEx')(BANK[(n * 97) % BANK.length]);
        [[0, 'Passningar och mottagning', '17:30', true], [1, 'Speluppbyggnad från målvakten', '17:30'], [3, 'Avslut och kontring', '18:00'], [4, 'Försvarsspel i zon', '17:30']].forEach(([d, name, time, done], i) => {
          const s = g('newSess')('[Test] ' + name); s.date = W[d]; s.time = time; s.test = true;
          s.blocks = [g('mkBlock')(pick(i * 3 + 1), 'warm', 15), g('mkBlock')(pick(i * 3 + 2), 'main', 25), g('mkBlock')(pick(i * 3 + 3), 'game', 20)];
          if (done) s.completedAt = Date.now(); g('saveSess')(s);
        });
        T('Testvecka skapad'); rerender();
      }
      if (a === 'cleartest') {
        const S = g('SESS'); let n = 0; Object.keys(S).forEach(k => { if (S[k]?.test) { delete S[k]; n++; } }); g('persistSess')(); T(n + ' testpass borttagna'); rerender();
      }
      if (a === 'wipe') {
        if (!confirm('Rensa alla pass, matcher och favoriter på den här enheten? Det som finns i molnet ligger kvar.')) return;
        Object.keys(localStorage).filter(k => !k.startsWith('of-moln-auth') && k !== 'of-utvecklare').forEach(k => localStorage.removeItem(k));
        location.reload();
      }
    });
  }

  window.OF_DEV = { html, mount };
})();

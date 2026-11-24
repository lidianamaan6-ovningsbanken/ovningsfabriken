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
      + '<p class="of-konto-note">Loggar du ut finns dina pass kvar på den här enheten.</p>';
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
        if (a === 'sync') { await M().pull(false); await M().push(); d.innerHTML = dialogHTML(); }
        if (a === 'out') { await M().signOut(); d.innerHTML = dialogHTML(); }
      });
      d.addEventListener('submit', async e => {
        e.preventDefault();
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
    d.querySelector('input, [data-konto="sync"]')?.focus();
  }

  window.OF_KONTO = { open, navHTML };
  const boot = () => { if (M()) { M().on(refresh); M().ready.then(refresh); } else setTimeout(boot, 100); };
  boot();
})();

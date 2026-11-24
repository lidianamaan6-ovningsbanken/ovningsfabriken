/* Övningsfabriken – molnsynk (Supabase)
 * Sparar tränarens pass, matcher, favoriter och några inställningar i databasen,
 * så att de följer med mellan enheter. Appen fungerar som förut utan inloggning.
 * Varje sak sparas som en egen rad (coach_items). Den senast ändrade versionen vinner.
 */
(function () {
  'use strict';
  const URL_ = 'https://fwgvfmkdmrpmgririxpt.supabase.co';
  const KEY = 'sb_publishable_Gi3qXYCia2WPxGIXcT8spQ_0ck6NMiT'; // publik nyckel, data skyddas av RLS
  const SETTINGS_KEYS = ['team', 'n', 'gk', 'age', 'level', 'passDur', 'workspaceTeamChoice', 'bankJ'];

  const state = { user: null, status: 'av', lastSync: 0, lastError: '', pushing: false, pulling: false, pending: 0, log: [] };
  const listeners = new Set();
  const emit = () => listeners.forEach(fn => { try { fn(state); } catch (e) { } });
  const log = (msg) => { state.log.unshift(new Date().toLocaleTimeString('sv-SE') + ' ' + msg); state.log.length = Math.min(state.log.length, 60); };

  if (!window.supabase?.createClient) { window.OF_MOLN = { state, ready: Promise.resolve(), on: () => { } }; return; }
  const sb = window.supabase.createClient(URL_, KEY, {
    auth: { flowType: 'implicit', persistSession: true, detectSessionInUrl: true, autoRefreshToken: true, storageKey: 'of-moln-auth' },
  });

  /* ---------- Lokala samlingar ---------- */
  const g = (name) => { try { return (0, eval)(name); } catch (e) { return undefined; } }; // appens globala let-variabler
  function collections() {
    const ST = g('ST') || {}, MX = g('MX') || {}, SESS = g('SESS') || {}, SAVED = g('SAVED') || {};
    const settings = {}; SETTINGS_KEYS.forEach(k => { if (ST[k] !== undefined) settings[k] = ST[k]; });
    return {
      sess: SESS, match: MX.matches || {}, mxteam: MX.teams || {}, mxform: MX.forms || {}, saved: SAVED,
      settings: { st: Object.assign({ updatedAt: Number(localStorage.getItem(skey('settingsAt')) || 0) }, settings) },
    };
  }
  const skey = (k) => 'of-moln.' + (state.user?.id || 'ute') + '.' + k;
  const readJSON = (k, d) => { try { return JSON.parse(localStorage.getItem(skey(k)) || 'null') ?? d; } catch (e) { return d; } };
  const writeJSON = (k, v) => { try { localStorage.setItem(skey(k), JSON.stringify(v)); } catch (e) { } };
  const stamp = (o) => Number(o?.updatedAt || o?.savedAt || o?.createdAt || 0);
  const sig = (o) => JSON.stringify(o);

  /* synced[kind][id] = signatur av senast synkade version */
  let synced = {};
  function diff() {
    const cols = collections(); const out = [];
    for (const [kind, items] of Object.entries(cols)) {
      const was = synced[kind] || {};
      for (const [id, item] of Object.entries(items)) {
        if (!item || typeof item !== 'object') continue;
        const s = sig(item); if (was[id] !== s) out.push({ kind, item_id: id, data: item, deleted: false, s });
      }
      for (const id of Object.keys(was)) if (!(id in items) && was[id] !== '__deleted') out.push({ kind, item_id: id, data: {}, deleted: true, s: '__deleted' });
    }
    return out;
  }

  /* ---------- Skicka ---------- */
  let pushTimer = null;
  function schedulePush(delay = 800) {
    if (!state.user) return;
    clearTimeout(pushTimer); pushTimer = setTimeout(push, delay);
    state.pending = diff().length; emit();
  }
  async function push() {
    if (!state.user || state.pushing) return;
    const changes = diff(); state.pending = changes.length;
    if (!changes.length) { emit(); return; }
    state.pushing = true; state.status = 'sparar'; emit();
    try {
      for (let i = 0; i < changes.length; i += 200) {
        const part = changes.slice(i, i + 200);
        const { error } = await sb.from('coach_items').upsert(part.map(c => ({ kind: c.kind, item_id: c.item_id, data: c.data, deleted: c.deleted })), { onConflict: 'user_id,kind,item_id' });
        if (error) throw error;
        part.forEach(c => { (synced[c.kind] = synced[c.kind] || {})[c.item_id] = c.s; });
      }
      writeJSON('synced', synced);
      log('Sparade ' + changes.length + ' ändring' + (changes.length === 1 ? '' : 'ar'));
      state.status = 'synkad'; state.lastSync = Date.now(); state.lastError = '';
    } catch (e) {
      state.status = 'fel'; state.lastError = e.message || String(e); log('Fel vid sparande: ' + state.lastError);
      clearTimeout(pushTimer); pushTimer = setTimeout(push, 8000);
    } finally {
      state.pushing = false; state.pending = diff().length; emit();
    }
  }

  /* ---------- Hämta ---------- */
  async function pull(full) {
    if (!state.user || state.pulling) return;
    state.pulling = true; emit();
    try {
      const since = full ? null : readJSON('pulledAt', null);
      let rows = [], from = 0;
      for (;;) {
        let q = sb.from('coach_items').select('kind,item_id,data,deleted,updated_at').order('updated_at').range(from, from + 999);
        if (since) q = q.gt('updated_at', since);
        const { data, error } = await q; if (error) throw error;
        rows = rows.concat(data); if (data.length < 1000) break; from += 1000;
      }
      let changed = 0;
      const ST = g('ST'), MX = g('MX'), SESS = g('SESS'), SAVED = g('SAVED');
      const target = { sess: SESS, match: MX?.matches, mxteam: MX?.teams, mxform: MX?.forms, saved: SAVED };
      for (const r of rows) {
        (synced[r.kind] = synced[r.kind] || {});
        if (r.kind === 'settings') {
          const localAt = Number(localStorage.getItem(skey('settingsAt')) || 0);
          if (!r.deleted && stamp(r.data) > localAt && ST) {
            SETTINGS_KEYS.forEach(k => { if (r.data[k] !== undefined) ST[k] = r.data[k]; });
            localStorage.setItem(skey('settingsAt'), String(stamp(r.data))); localStorage.setItem(skey('settingsSig'), settingsSig()); changed++;
          }
          (synced.settings = synced.settings || {}).st = sig(collections().settings.st);
          continue;
        }
        const col = target[r.kind]; if (!col) continue;
        const local = col[r.item_id];
        if (r.deleted) {
          if (local && synced[r.kind][r.item_id] === sig(local)) { delete col[r.item_id]; changed++; }
          if (!local || synced[r.kind][r.item_id] === sig(local)) synced[r.kind][r.item_id] = '__deleted';
          continue;
        }
        if (!local || stamp(r.data) > stamp(local) || (stamp(r.data) === stamp(local) && sig(local) !== sig(r.data) && synced[r.kind][r.item_id] === sig(local))) {
          col[r.item_id] = r.data; changed++;
        }
        if (sig(col[r.item_id]) === sig(r.data)) synced[r.kind][r.item_id] = sig(r.data);
      }
      if (rows.length) writeJSON('pulledAt', rows[rows.length - 1].updated_at);
      writeJSON('synced', synced);
      if (changed) {
        quiet = true;
        try { g('persist')?.(); localStorage.setItem(g('LS_S'), JSON.stringify(g('SESS'))); localStorage.setItem(g('LS_M'), JSON.stringify(g('MX'))); } catch (e) { }
        quiet = false;
        log('Hämtade ' + changed + ' ändring' + (changed === 1 ? '' : 'ar') + ' från molnet');
        try { g('render')?.(); } catch (e) { }
      }
      state.lastSync = Date.now(); if (state.status !== 'fel') state.status = 'synkad';
    } catch (e) {
      state.status = 'fel'; state.lastError = e.message || String(e); log('Fel vid hämtning: ' + state.lastError);
    } finally {
      state.pulling = false; emit();
      schedulePush(300); // det som bara finns lokalt skickas upp
    }
  }

  /* ---------- Krokar från appen ---------- */
  let quiet = false;
  function settingsSig() { const ST = g('ST') || {}; const o = {}; SETTINGS_KEYS.forEach(k => { if (ST[k] !== undefined) o[k] = ST[k]; }); return sig(o); }
  function changedLocally() {
    if (quiet) return;
    const now = settingsSig();
    if (now !== localStorage.getItem(skey('settingsSig'))) {
      try { localStorage.setItem(skey('settingsSig'), now); localStorage.setItem(skey('settingsAt'), String(Date.now())); } catch (e) { }
    }
    schedulePush();
  }

  /* ---------- Inloggning ---------- */
  async function signIn(email) {
    const redirect = location.origin + location.pathname;
    const { error } = await sb.auth.signInWithOtp({ email, options: { emailRedirectTo: redirect, shouldCreateUser: true } });
    if (error) throw error;
    log('Inloggningslänk skickad');
  }
  async function signOut() {
    await push().catch(() => { });
    await sb.auth.signOut();
  }
  function setUser(user) {
    const before = state.user?.id; state.user = user || null;
    if (state.user?.id === before) return;
    synced = state.user ? readJSON('synced', {}) : {};
    if (state.user && localStorage.getItem(skey('settingsSig')) === null) { try { localStorage.setItem(skey('settingsSig'), settingsSig()); } catch (e) { } }
    state.status = state.user ? 'ansluter' : 'av';
    log(state.user ? 'Inloggad som ' + state.user.email : 'Utloggad');
    emit();
    if (state.user) pull(!readJSON('pulledAt', null));
  }

  const ready = sb.auth.getSession().then(({ data }) => setUser(data.session?.user)).catch(e => { state.lastError = e.message; emit(); });
  sb.auth.onAuthStateChange((_evt, session) => setUser(session?.user));
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') pull(false); else push(); });
  window.addEventListener('online', () => { pull(false); });
  setInterval(() => { if (document.visibilityState === 'visible') pull(false); }, 60000);

  async function ping() {
    const t = performance.now();
    const { count, error } = await sb.from('categories').select('*', { count: 'exact', head: true });
    return { ok: !error, ms: Math.round(performance.now() - t), error: error?.message, count };
  }
  async function cloudCounts() {
    if (!state.user) return null;
    const { data, error } = await sb.from('coach_items').select('kind,deleted');
    if (error) throw error;
    const out = {}; data.forEach(r => { if (!r.deleted) out[r.kind] = (out[r.kind] || 0) + 1; }); return out;
  }

  window.OF_MOLN = {
    state, ready, signIn, signOut, push, pull, ping, cloudCounts, changedLocally, collections,
    on: (fn) => { listeners.add(fn); return () => listeners.delete(fn); },
    resetSync: () => { synced = {}; writeJSON('synced', {}); writeJSON('pulledAt', null); return pull(true); },
  };
})();

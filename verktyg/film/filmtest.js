const { chromium } = require('playwright');
(async () => {
  const base = process.argv[2]; const proxy = process.env.HTTPS_PROXY||process.env.https_proxy;
  const b = await chromium.launch(base.startsWith('https')&&proxy?{proxy:{server:proxy},args:['--ignore-certificate-errors']}:{}); const errs=[];
  const p = await b.newPage({viewport:{width:1440,height:900}}); p.on('pageerror',e=>errs.push(e.message)); p.on('response',r=>{if(r.status()>=400)errs.push(r.status()+' '+r.url())});
  await p.goto(base+'app.html?utan-lag=1'); await p.waitForTimeout(1500);
  await p.click('button[data-a=view][data-v=bank]',{force:true}); await p.waitForTimeout(800);
  const res=[];
  for (const [id,q] of process.argv.slice(3).map(x=>x.split('='))) {
    await p.fill('input[placeholder*="Till exempel"]',q); await p.waitForTimeout(900);
    try { await p.click(`button.of-exercise-preview[data-id="bank-${id}"]`,{force:true,timeout:5000}); } catch(e) { res.push(id+': hittades ej i sök'); continue; } await p.waitForTimeout(1000);
    const ok = await p.evaluate(async()=>{const v=document.querySelector('video.of-exercise-film');if(!v)return 'ingen video';v.muted=true;await v.play();await new Promise(r=>setTimeout(r,600));return v.currentTime>0?'spelar':'står'});
    res.push(id+': '+ok);
    await p.goBack().catch(()=>{}); await p.waitForTimeout(500);
    if (!await p.$('input[placeholder*="Till exempel"]')) { await p.click('button[data-a=view][data-v=bank]',{force:true}); await p.waitForTimeout(600); }
  }
  console.log(res.join(' | ')); console.log('fel:',errs.slice(0,5)); await b.close();
})();

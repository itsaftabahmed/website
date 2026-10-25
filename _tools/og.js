// Usage: node og.js [slug ...]  (no args = every blog post). Writes images/og/<slug>.png (1200x630).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const W = '/home/user/website/';
const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const slugs = process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync(W + 'blog').filter(d => fs.existsSync(W + 'blog/' + d + '/index.html'));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  fs.mkdirSync(W + 'images/og', { recursive: true });
  for (const s of slugs) {
    const h = fs.readFileSync(W + 'blog/' + s + '/index.html', 'utf8');
    const title = (h.match(/<h1>([\s\S]*?)<\/h1>/) || [])[1].replace(/<[^>]+>/g, '').replace(/&amp;/g, '&');
    const kicker = ((h.match(/<div class="kicker">([\s\S]*?)<\/div>/) || [])[1] || '').replace(/&amp;/g, '&');
    const size = title.length > 70 ? 58 : title.length > 50 ? 66 : 76;
    await p.setContent(`<html><body style="margin:0;width:1200px;height:630px;background:#0A0A0A;font-family:'DejaVu Sans',Arial,sans-serif;color:#fff;position:relative;overflow:hidden">
      <div style="position:absolute;right:-180px;top:-180px;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(224,17,25,.45),transparent 65%)"></div>
      <div style="position:absolute;left:0;top:0;bottom:0;width:14px;background:#E01119"></div>
      <div style="position:absolute;left:80px;right:90px;top:70px;font-size:24px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#FF4A50">${esc(kicker)}</div>
      <div style="position:absolute;left:80px;right:90px;top:130px;bottom:150px;display:flex;align-items:center"><div style="font-size:${size}px;font-weight:800;line-height:1.08;letter-spacing:-1.5px">${esc(title)}</div></div>
      <div style="position:absolute;left:80px;bottom:62px;font-size:30px;font-weight:800;letter-spacing:3px">AFTAB <span style="color:#E01119">AHMED</span></div>
      <div style="position:absolute;right:90px;bottom:66px;font-size:24px;color:#9E9E9E">iamaftabahmed.com</div>
    </body></html>`);
    await p.screenshot({ path: W + 'images/og/' + s + '.png' });
    console.log('og', s);
  }
  await b.close();
})();

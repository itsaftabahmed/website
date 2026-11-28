# Builds pricing/index.html (the separate Pricing page). Shell and head come from gen_tool_aicost.py,
# header and footer from chrome.py. Edit PLANS / COMPARE / FAQ here, then run: python3 _tools/gen_pricing.py
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome
import gen_tool_aicost as A
U, ROOT = A.U, A.ROOT
url = f'{U}pricing/'
TITLE = 'Pricing: Website, CRM & Lead Generation Plans | Aftab Ahmed'
DESC = 'Monthly plans for service businesses: a website and CRM from $297/month, Facebook and Google lead generation, and a full growth system. Ad spend separate.'
e = lambda t: html.escape(t, quote=False)

# name, headline, price, note, outcome, intro line, key items, button style
PLANS = [
 dict(name='Get Found', video='', head='A website that works and brings you customers', price=297, hot=False,
      note='Website build included, no setup fee.',
      outcome='Customers find you online, every lead gets a reply in seconds, and past customers come back to book again.',
      plus=None,
      items=['<b>Custom website</b>, built for you and ready for Google and AI answers like ChatGPT',
             '<b>Google Business Profile</b> set up so you show on Google Maps',
             '<b>CRM with instant lead alerts</b> and missed call text back',
             '<b>Automatic follow-up</b> texts and emails, booking and reminders',
             '<b>Review requests</b> after every job',
             '<b>Database reactivation:</b> win business back from old leads']),
 dict(name='Get Leads', video='', head='New leads every month, answered in seconds', price=497, hot=True,
      note='Ad spend is separate, paid by you directly to Meta.',
      outcome='A steady flow of new inquiries from Facebook and Instagram, answered in seconds and booked without you chasing anyone.',
      plus='Everything in Get Found, plus:',
      items=['<b>Facebook and Instagram lead generation</b>, built and managed for you',
             '<b>Offer and lead form</b> written to attract the right customers',
             '<b>AI chat assistant</b> that answers and books on your website 24/7',
             'New leads go <b>straight into your CRM</b> with an instant reply',
             '<b>Bi-weekly reports:</b> leads, booked jobs and cost per lead']),
 dict(name='Full Growth System', short='Full Growth', video='', head='New customers every month, on autopilot', price=997, hot=False,
      note='Ad spend is separate, paid by you directly to Google and Meta.',
      outcome='New customers every month from Google and Facebook, every call answered and every lead followed up for you.',
      plus='Everything in Get Leads, plus:',
      items=['<b>Google Ads</b> as well as Facebook and Instagram',
             '<b>AI phone receptionist</b> that answers and books calls 24/7',
             '<b>Ongoing SEO:</b> articles, Google Business Profile posts and site checks',
             '<b>Custom automations</b> for your busywork',
             '<b>Monthly strategy call</b> and <b>weekly reports</b>']),
]
# feature, Get Found, Get Leads, Full Growth (True = included, text = included with detail)
COMPARE = [
 ('Your website', None),
 ('Custom website, built for you', True, True, True),
 ('SEO and AI-search ready (Google, ChatGPT, Gemini)', True, True, True),
 ('Google Business Profile setup', True, True, True),
 ('Hosting, updates and monthly maintenance', True, True, True),
 ('Ongoing SEO: 2 articles a month, weekly Google Business Profile posts', False, False, True),
 ('Your CRM and follow-up', None),
 ('Instant new-lead alerts', True, True, True),
 ('Missed call text back', True, True, True),
 ('Automatic follow-up texts and emails', True, True, True),
 ('Online booking and appointment reminders', True, True, True),
 ('Review requests', True, True, True),
 ('Database reactivation for old leads', True, True, True),
 ('AI chat assistant on your website', False, True, True),
 ('AI phone receptionist', False, False, True),
 ('Custom automations for busywork', False, False, 'Up to 2'),
 ('Getting new leads', None),
 ('Facebook and Instagram ads, managed', False, True, True),
 ('Google Ads, managed', False, False, True),
 ('Reports and support', None),
 ('Reports', 'Monthly', 'Every 2 weeks', 'Weekly'),
 ('Strategy call with Aftab', False, False, 'Monthly'),
]
STEPS = [('Week 1 to 2', 'Your website and CRM go live. Lead alerts, follow-up, reminders and review requests start working with your existing customers right away.'),
         ('Month 1', 'For Get Leads and Full Growth: your offer, ads and lead forms launch, and every new lead gets an instant reply.'),
         ('Month 2 onward', 'We improve what is working, cut what is not, and report the numbers that matter: leads, booked jobs and cost per lead.'),
         ('Month 6 to 12', 'SEO builds up. Most businesses see steady results from Google search in 6 to 12 months, because ranking takes time.')]
FAQ = [
 ('Is ad spend included in the price?', 'No. Ad spend is never included in any plan. You pay Google or Meta directly for your ads, so you always own your ad accounts and see exactly what is spent. The monthly plan price covers the work, the tools and the management.'),
 ('Are there any hidden charges?', 'No. The plan price includes your website, hosting, the CRM and normal texting and email use. The only separate cost is your ad spend, paid directly to Google or Meta. Anything extra, such as more locations, is quoted and agreed before it starts.'),
 ('Is there a contract or minimum term?', 'Every plan starts with a 3-month minimum, because the website and system are built at no setup fee. After the first 3 months, plans run month to month and you can cancel any time with 30 days notice.'),
 ('Who owns the website and accounts?', 'You do. Your website, domain, ad accounts and customer data stay in your name, even if you leave.'),
 ('How long does SEO take to bring customers?', 'SEO usually takes 6 to 12 months to bring steady results from Google, depending on your market and competition. That is why every plan also includes tools that work in week one, such as instant lead alerts, follow-up and review requests.'),
 ('I already have a website. Can I still use a plan?', 'Yes. On a free call we look at your current site. If it works well, we connect it to your CRM and follow-up; if it is holding you back, the new website is included in your plan.'),
]
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>'
INTRO_VIDEO = 'CI87I9J2kJg'   # homepage "Hi, I'm Aftab" video, shown until a plan has its own video
def vbtn(p):
    # Plan walkthrough video (VSL). Set PLANS[...]['video'] to the plan's YouTube video id when it is recorded;
    # until then the button plays the intro video with matching wording.
    if p.get('video'):
        vid, t, sub = p['video'], 'Watch Aftab explain this plan', '2-minute video: what is included and who it is for'
    else:
        vid, t, sub = INTRO_VIDEO, 'Watch Aftab explain the plans', 'Short video: who I help and how it works'
    return f'<button type="button" class="pc__vid" data-vid="{vid}" data-title="{p["name"]}: video"><span class="pc__play">{PLAY}</span><span><b>{t}</b><small>{sub}</small></span></button>'
cards = ''
for p in PLANS:
    plus = f'<p class="pc__plus">{p["plus"]}</p>' if p['plus'] else '<p class="pc__plus">What you get:</p>'
    cards += f'''  <div class="pc{' pc--hot' if p['hot'] else ''}">
    {'<div class="pc__tag">Most popular</div>' if p['hot'] else ''}<div class="pc__name">{p['name']}</div>
    <h2 class="pc__head">{p['head']}</h2>
    <div class="pc__price">${p['price']}<small>/ month</small></div>
    <div class="pc__note">{p['note']}</div>
    <div class="pc__out"><b>The outcome</b>{p['outcome']}</div>
    {vbtn(p)}
    {plus}
    <ul>{''.join(f'<li><span>{i}</span></li>' for i in p['items'])}</ul>
    <a class="btn{'' if p['hot'] else ' pc__ghost'}" href="../#book" data-plan="{p['name']}">Start with {p.get('short', p['name'])} →</a>
  </div>
'''
TICK = '<span class="cmp__y" aria-label="Included">✓</span>'
NO = '<span class="cmp__n" aria-label="Not included">–</span>'
cell = lambda v: TICK if v is True else NO if v is False else f'<span class="cmp__t">{e(v)}</span>'
rows = ''
for r in COMPARE:
    if r[1] is None: rows += f'<tr class="cmp__g"><th colspan="4">{e(r[0])}</th></tr>'
    else: rows += f'<tr><td>{e(r[0])}</td>' + ''.join(f'<td>{cell(v)}</td>' for v in r[1:]) + '</tr>'
steps = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in STEPS)
faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in FAQ)
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebPage", "name": "Pricing", "url": url, "description": DESC},
  {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}, {"@type": "ListItem", "position": 2, "name": "Pricing", "item": url}]},
  {"@type": "Service", "name": "Website, CRM and lead generation for service businesses", "provider": A.person, "areaServed": "US",
   "offers": [{"@type": "Offer", "name": p['name'], "description": p['outcome'], "priceCurrency": "USD",
               "priceSpecification": {"@type": "UnitPriceSpecification", "price": p['price'], "priceCurrency": "USD", "unitText": "month"}} for p in PLANS]},
  {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
CSS = '''.pz{padding:10px 0 30px}
.pz__grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;align-items:stretch;margin-top:10px}
.pc{position:relative;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:30px 28px}
.pc--hot{border-color:rgba(224,17,25,.7);background:linear-gradient(180deg,rgba(224,17,25,.10),rgba(224,17,25,0) 40%),var(--surface);box-shadow:0 30px 80px -30px rgba(224,17,25,.55)}
.pc__tag{position:absolute;top:-13px;left:28px;background:#E01119;color:#fff;font-weight:800;font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;padding:6px 12px;border-radius:99px}
.pc__name{font-weight:800;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--red-text)}
.pc__head{font-family:'Plus Jakarta Sans',sans-serif;font-stretch:100%;color:#fff;font-size:20px;font-weight:700;margin:10px 0 18px;line-height:1.3;min-height:2.6em}
.pc__price{font-family:var(--display);font-stretch:115%;font-weight:900;font-size:54px;letter-spacing:-.03em;color:#fff;line-height:1}
.pc__price small{font-family:'Plus Jakarta Sans',sans-serif;font-stretch:100%;font-weight:600;font-size:16px;color:var(--muted);letter-spacing:0;margin-left:6px}
.pc__note{color:var(--muted);font-size:13.5px;line-height:1.6;margin:10px 0 18px;min-height:44px}
.pc__out{padding:14px 16px;border-radius:16px;background:#141414;border:1px solid #262626;color:var(--soft);font-size:14.5px;line-height:1.55;margin-bottom:20px;min-height:140px;box-sizing:border-box}
.pc--hot .pc__out{border-color:rgba(224,17,25,.35);background:rgba(224,17,25,.06)}
.pc__out b{display:block;color:#fff;font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px}
.pc__vid{display:flex;align-items:center;gap:12px;width:100%;margin:-6px 0 20px;padding:10px 12px;border-radius:16px;background:#111;border:1px solid #2c2c2c;color:#fff;text-align:left;cursor:pointer;font:inherit;transition:border-color .3s,background .3s}
.pc__vid:hover{border-color:var(--red);background:#161010}
.pc__play{flex:none;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:#E01119;box-shadow:0 0 0 6px rgba(224,17,25,.15)}.pc__play svg{width:18px;height:18px;margin-left:2px;color:#fff}
.pc__vid b{display:block;font-size:14.5px}.pc__vid small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.vm{position:fixed;inset:0;z-index:200;display:none;align-items:center;justify-content:center;padding:20px;background:rgba(0,0,0,.82)}.vm.on{display:flex}
.vm__box{position:relative;width:min(960px,100%);aspect-ratio:16/9;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 90px -20px rgba(224,17,25,.5)}
.vm__box iframe{width:100%;height:100%;border:0}
.vm__x{position:absolute;top:-46px;right:0;width:38px;height:38px;border-radius:50%;border:1px solid #444;background:#111;color:#fff;font-size:20px;cursor:pointer}
.pc__plus{color:#fff;font-weight:700;font-size:15px;margin:0 0 12px}
.pc ul{list-style:none;padding:0;margin:0 0 24px;display:grid;gap:11px;flex:1;align-content:start}
.pc li{display:flex;gap:10px;color:var(--soft);font-size:15px;line-height:1.45}
.pc li::before{content:"";flex:none;width:18px;height:18px;margin-top:2px;border-radius:50%;background:rgba(224,17,25,.14) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23ff4a50' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 12.5l4 4 8-9'/%3E%3C/svg%3E") center/12px no-repeat;border:1px solid rgba(224,17,25,.4)}
.pc li b{color:#fff;font-weight:700}
.pc .btn{justify-content:center;text-align:center;width:100%;box-sizing:border-box}
.pc__ghost{background:none!important;border:1px solid #3a3a3a!important;box-shadow:none!important}
.pz__all{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:28px 0 0}
.pz__all span{display:inline-flex;align-items:center;gap:8px;padding:9px 14px;border-radius:999px;background:var(--surface);border:1px solid var(--line);font-size:14px;color:var(--soft)}
.pz__all span::before{content:"✓";color:#4ade80;font-weight:800}
.pz__sec{margin:90px auto 0;max-width:1000px}
.pz__sec>.kicker{display:flex;justify-content:center}
.pz__sec>h2{font-family:var(--display);font-stretch:115%;font-weight:900;font-size:clamp(28px,3.4vw,40px);letter-spacing:-.03em;margin:10px 0 24px;text-align:center}
.cmpw{overflow-x:auto;border:1px solid var(--line);border-radius:22px;background:var(--surface)}
.cmp{width:100%;min-width:620px;border-collapse:collapse;font-size:15px}
.cmp th,.cmp td{padding:13px 18px;border-bottom:1px solid var(--line);text-align:center;color:var(--soft)}
.cmp td:first-child,.cmp th:first-child{text-align:left}
.cmp thead th{color:#fff;font-size:14px;font-weight:800;position:sticky;top:0;background:#121212}
.cmp thead th small{display:block;color:var(--muted);font-weight:600;font-size:13px;margin-top:2px}
.cmp .cmp__g th{background:#101010;color:var(--red-text);font-size:12px;letter-spacing:.14em;text-transform:uppercase;text-align:left}
.cmp tr:last-child td{border-bottom:0}
.cmp__y{color:#4ade80;font-weight:800}.cmp__n{color:#555}.cmp__t{color:#fff;font-weight:600;font-size:14px}
.cmp td:nth-child(3),.cmp thead th:nth-child(3){background:rgba(224,17,25,.05)}
.cmp-tabs{display:none}
@media (max-width:760px){
  .cmp-tabs{display:flex;gap:4px;margin:0 0 16px;padding:5px;border:1px solid var(--line);border-radius:999px;background:#121212}
  .cmp-tabs button{flex:1;border:0;border-radius:999px;background:none;color:#cfcfcf;font-family:inherit;font-size:13px;font-weight:700;padding:9px 2px;line-height:1.25;cursor:pointer}
  .cmp-tabs button small{display:block;font-weight:600;font-size:11px;color:var(--muted)}
  .cmp-tabs button.on{background:var(--red);color:#fff;box-shadow:0 8px 20px -8px rgba(224,17,25,.9)}
  .cmp-tabs button.on small{color:#ffd9db}
  .cmpw{overflow:visible}
  .cmp{min-width:0}
  .cmp th,.cmp td{padding:12px 14px}
  .cmp[data-p] tr>:nth-child(n+2){display:none}
  .cmp[data-p="1"] tr>:nth-child(2),.cmp[data-p="2"] tr>:nth-child(3),.cmp[data-p="3"] tr>:nth-child(4){display:table-cell;width:96px}
}
.tl{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.tl li{background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:20px}
.tl b{display:block;color:var(--red-text);font-size:13px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:8px}.tl span{color:var(--soft);font-size:14.5px;line-height:1.55}
.pfaq details{border-bottom:1px solid var(--line);padding:18px 4px}.pfaq summary{cursor:pointer;color:#fff;font-weight:700;font-size:17px;list-style:none}
.pfaq summary::after{content:"+";float:right;color:var(--red-text);font-size:22px;line-height:1}.pfaq details[open] summary::after{content:"–"}
.pfaq p{color:var(--soft);margin:12px 0 0;line-height:1.65}
@media (max-width:980px){.pz__grid{grid-template-columns:1fr;max-width:560px;margin-left:auto;margin-right:auto}.pc--hot{order:-1}.pc__head,.pc__note,.pc__out{min-height:0}.tl{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.tl{grid-template-columns:1fr}.pz__sec{margin-top:70px}}
'''
VSCRIPT = '''<script>
(function(){
  var vm=document.getElementById('vm'),pl=document.getElementById('vmPlayer'),last=null;
  function close(){vm.classList.remove('on');pl.innerHTML='';if(last)last.focus()}
  document.querySelectorAll('.pc__vid').forEach(function(b){b.addEventListener('click',function(){
    last=b;pl.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+encodeURIComponent(b.dataset.vid)+'?autoplay=1&rel=0" title="'+b.dataset.title+'" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
    vm.classList.add('on');vm.querySelector('.vm__x').focus();(window.dataLayer=window.dataLayer||[]).push({event:'plan_video_play',plan:b.dataset.title});
  })});
  vm.addEventListener('click',function(e){if(e.target===vm||e.target.classList.contains('vm__x'))close()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&vm.classList.contains('on'))close()});
  var cmp=document.querySelector('.cmp');   // phones: the comparison shows one plan at a time
  document.querySelectorAll('.cmp-tabs button').forEach(function(b,i,all){b.addEventListener('click',function(){cmp.dataset.p=b.dataset.p;all.forEach(function(x){x.classList.toggle('on',x===b);x.setAttribute('aria-pressed',x===b)})})});
  document.querySelectorAll('.pc .btn[data-plan]').forEach(function(a){a.addEventListener('click',function(){(window.dataLayer=window.dataLayer||[]).push({event:'plan_cta',plan:a.dataset.plan})})});
})();
</script>'''
page = A.head(TITLE, DESC, url, 'Pricing: simple plans that bring you business', f'{U}images/og/pricing.png', ld, CSS, '../') + f'''
<section class="hero"><div class="wrap" style="text-align:center">
  <nav class="crumbs" aria-label="Breadcrumb" style="justify-content:center"><a href="../">Home</a><span>/</span>Pricing</nav>
  <div class="kicker" style="justify-content:center">Pricing</div>
  <h1>Simple plans that bring you business</h1>
  <p class="lead" style="margin-left:auto;margin-right:auto">More calls, a fuller calendar and less time chasing leads. One monthly price, no hidden charges, and you own your website, domain and ad accounts.</p>
</div></section>

<main class="wrap pz">
<div class="pz__grid">
{cards}</div>
<div class="pz__all" aria-label="Included in every plan"><span>No setup fee</span><span>No hidden charges</span><span>Ad spend separate, paid by you</span><span>You own everything</span><span>Month to month after 3 months</span></div>

<section class="pz__sec" aria-labelledby="cmpH">
  <div class="kicker" style="justify-content:center">Compare plans</div>
  <h2 id="cmpH">Everything in each plan</h2>
  <div class="cmp-tabs" role="group" aria-label="Show one plan"><button type="button" data-p="1" aria-pressed="false">Get Found<small>$297/mo</small></button><button type="button" data-p="2" aria-pressed="true" class="on">Get Leads<small>$497/mo</small></button><button type="button" data-p="3" aria-pressed="false">Full Growth<small>$997/mo</small></button></div>
  <div class="cmpw"><table class="cmp" data-p="2">
    <thead><tr><th>Feature</th><th>Get Found<small>$297/mo</small></th><th>Get Leads<small>$497/mo</small></th><th>Full Growth<small>$997/mo</small></th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
</section>

<section class="pz__sec" aria-labelledby="tlH">
  <div class="kicker" style="justify-content:center">What to expect</div>
  <h2 id="tlH">From sign-up to new customers</h2>
  <ol class="tl">{steps}</ol>
</section>

<section class="pz__sec pfaq" aria-labelledby="pfH" style="max-width:820px">
  <div class="kicker" style="justify-content:center">Questions</div>
  <h2 id="pfH">Pricing questions</h2>
  {faq}
</section>

</main>

{chrome.footer('../')}
<div class="vm" id="vm" role="dialog" aria-modal="true" aria-label="Plan video"><div class="vm__box"><button type="button" class="vm__x" aria-label="Close video">×</button><div id="vmPlayer"></div></div></div>
{VSCRIPT}
</body>
</html>
'''
os.makedirs(f'{ROOT}/pricing', exist_ok=True)
open(f'{ROOT}/pricing/index.html', 'w').write(page)
print('built pricing', len(TITLE), len(DESC))

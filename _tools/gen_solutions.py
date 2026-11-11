# Generates problem-based solution pages (/solutions/<slug>/) in the service-page design.
# Edit SOL below, then run: python3 _tools/gen_solutions.py
import json, os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = 'https://iamaftabahmed.com/'
e = lambda t: html.escape(t, quote=False)
src = open(f'{ROOT}/services/ai-automation/index.html').read()
TRACK = src[src.index('<head>') + 6:src.index('<title>')]
BODY_TRACK = src[src.index('<body>') + 6:re.search(r'<div class="ann">|<header', src).start()]
ICON = re.search(r'<link rel="icon"[^>]*>', src).group(0)

def phone(top, rows):
    return ('<div class="sv-phone" aria-hidden="true"><div class="sv-phone__top">' + top + '</div>'
            + ''.join(f'<div class="sv-{k}">{t}</div>' for k, t in rows) + '<div class="sv-ex">Example conversation</div></div>')

SOL = [
 dict(slug='missed-calls', name='Missed Calls', menu='Stop missed calls',
  title='Stop Missing Calls: AI Receptionist & Missed Call Text Back',
  desc='Stop losing customers to missed calls. An AI receptionist and missed call text back answer every caller in seconds and book them, day or night.',
  kicker='Solution · Missed calls',
  h1='Every missed call is a customer calling someone else',
  lead='When you can’t pick up, callers try the next business on the list. I set up an AI receptionist and an instant text back so every caller gets an answer in seconds and a booked time, even after hours.',
  visual=phone('Cool Air Heating · 7:42 pm', [('miss', 'Missed call from (512) 555-0187'), ('me', 'Hi, this is Cool Air Heating. Sorry we missed you! Is your AC or heat acting up?'), ('you', 'AC is blowing warm air'), ('me', 'I can get a tech out tomorrow at 9 am or 1 pm. Which works?'), ('you', '9 works'), ('ok', '✓ Booked · Tomorrow 9:00 am · tech assigned')]),
  intro=['Most missed calls are not lost because the business is bad. They happen because the team is on a job, with a patient, or closed for the night, and the caller won’t leave a voicemail.',
         'The fix is simple: answer every call, or reply to it within seconds, and give the caller an easy way to book. That is what this setup does.'],
  before=['Calls go to voicemail when the team is busy', 'After-hours callers book with a competitor', 'Callbacks happen hours later, if at all'],
  after=['Every call answered or texted back in seconds', 'Appointments booked straight into your calendar', 'Urgent calls passed to a person right away'],
  included=[('AI receptionist', 'Answers calls 24/7 with your approved answers, in a natural voice, using your business name.'),
            ('Missed call text back', 'Any call you can’t answer gets a friendly text within seconds, so the caller stays with you.'),
            ('Calendar booking', 'Offers real open times and books the appointment while the caller is still on the line.'),
            ('Smart handoff', 'Emergencies, complaints and sensitive calls go straight to you or your team.'),
            ('Call summaries in your CRM', 'Every call is logged with notes, so nothing gets lost between staff.'),
            ('Monthly report', 'Calls answered, appointments booked and calls handed off, in plain numbers.')],
  fit=['Home service businesses whose teams are out on jobs', 'Dental, medical and wellness practices with a busy front desk', 'Law firms, agencies and offices that close at 5 pm', 'Any business running ads that bring in phone calls'],
  steps=[('Book a call.', 'We look at your call volume, missed calls and how bookings work today.'),
         ('Get a clear plan.', 'Script, booking rules and handoffs agreed before anything is built.'),
         ('Go live.', 'Tested on real questions, connected to your number and calendar, then switched on with reporting.')],
  quote=('“Our biggest problem wasn’t getting leads — it was following up with them fast enough. Aftab connected our ads, CRM, SMS and automated follow-up so every enquiry was contacted immediately. We stopped losing good leads simply because the team was busy.”', 'Sarah Mitchell', 'Managing Director, Healthcare Practice'),
  case=('hvac', 'HVAC · Austin, Texas', 'Turning more inquiries into booked service calls', ['Inquiry from ad', 'Acknowledgment sent', 'Office callback', 'Service call booked']),
  faq=[('Will callers know they are talking to an AI?', 'They should, and the assistant says so if asked. Most callers care more about a fast, helpful answer and an easy way to book than about who picks up.'),
       ('Can I keep my existing phone number?', 'Usually, yes. Calls can be forwarded to the AI after hours, when lines are busy or after a set number of rings, so customers keep calling the number they know.'),
       ('What happens with urgent or complicated calls?', 'You decide the rules. Emergencies, complaints or anything outside the script can be transferred to you, sent as an instant alert, or booked as a priority callback.'),
       ('How much does it cost?', 'It depends on call volume and what needs connecting, such as your calendar and CRM. Most setups combine a one-time build with a monthly running cost. On a free call I’ll give you a clear quote.')],
  related=[('demo/', 'Try the AI receptionist live demo'), ('tools/missed-call-calculator/', 'Missed call cost calculator'),
           ('blog/missed-call-text-back/', 'Missed call text back: never lose a caller again'), ('blog/ai-receptionist-vs-answering-service/', 'AI receptionist vs answering service'),
           ('services/ai-automation/', 'AI automation and AI receptionists')]),
]

def page(x):
    url = f'{U}solutions/{x["slug"]}/'; up = '../../'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": x['title'].split(':')[0], "serviceType": x['name'], "url": url, "description": x['desc'],
         "provider": {"@type": "Person", "@id": f"{U}#person", "name": "Aftab Ahmed", "url": f"{U}about/"}, "areaServed": {"@type": "Country", "name": "United States"}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U},
         {"@type": "ListItem", "position": 2, "name": "Solutions", "item": url}, {"@type": "ListItem", "position": 3, "name": x['name'], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in x['faq']]}]}
    li = lambda xs: ''.join(f'<li>{e(t)}</li>' for t in xs)
    q, who, role = x['quote']; cid, ck, ct, flow = x['case']
    fl = '<i aria-hidden="true">→</i>'.join(f'<span>{e(s)}</span>' for s in flow)
    return f'''<!doctype html>
<html lang="en">
<head>{TRACK}<title>{e(x['title'])}</title>
<meta name="description" content="{html.escape(x['desc'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Aftab Ahmed">
<meta name="theme-color" content="#0A0A0A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aftab Ahmed">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(x['title'])}">
<meta property="og:description" content="{html.escape(x['desc'])}">
<meta property="og:image" content="{U}images/aftab-cutout.webp">
<meta name="twitter:card" content="summary_large_image">
{ICON}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}blog/blog.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False)}
</script>
</head>
<body>{BODY_TRACK}{chrome.nav(up)}

<section class="hero hero--svc"><div class="wrap"><div class="sv-copy">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{up}">Home</a><span>/</span>Solutions<span>/</span>{e(x['name'])}</nav>
  <div class="kicker">{e(x['kicker'])}</div>
  <h1>{e(x['h1'])}</h1>
  <p class="lead">{e(x['lead'])}</p>
  <a class="btn" href="{up}#book">Book a free 30-minute call →</a> <a class="btn" href="{up}demo/" style="background:none;border:1px solid #3a3a3a;box-shadow:none;margin-left:6px">Try the live demo</a>
</div>
{x['visual']}</div></section>

<article class="svc">
{''.join(f'  <p>{e(p)}</p>' + chr(10) for p in x['intro'])}  <div class="sv-ba"><div class="sv-card"><b>Today</b><ul>{li(x['before'])}</ul></div><div class="sv-arrow" aria-hidden="true">→</div><div class="sv-card sv-card--good"><b>After we set it up</b><ul>{li(x['after'])}</ul></div></div>

  <h2 id="included">What's included</h2>
  <div class="svc-grid">{''.join(f'<div><b>{e(t)}</b><p>{e(d)}</p></div>' for t, d in x['included'])}</div>

  <div class="midcta"><div><b>See what missed calls cost you</b><p>Enter your call numbers and get a monthly estimate in 30 seconds.</p></div><a class="btn" href="{up}tools/missed-call-calculator/">Open the calculator →</a></div>

  <h2 id="fit">Who this is for</h2>
  <ul class="check">{li(x['fit'])}</ul>

  <h2 id="process">How it works</h2>
  <ol class="steps">{''.join(f'<li><strong>{e(a)}</strong> {e(b)}</li>' for a, b in x['steps'])}</ol>

  <h2 id="proof">What clients say</h2>
  <div class="sv-proof"><figure class="sv-card"><blockquote>{e(q)}</blockquote><figcaption><b>{e(who)}</b><small>{e(role)}</small></figcaption></figure><div class="sv-card"><div class="kicker">Case study · {e(ck)}</div><h3>{e(ct)}</h3><div class="pflow">{fl}</div><p><a href="{up}case-studies/#{cid}">Read the case study →</a></p></div></div>

  <h2 id="faq">FAQ</h2>
{''.join(f'  <h3>{e(q)}</h3>' + chr(10) + f'  <p>{e(a)}</p>' + chr(10) for q, a in x['faq'])}
  <div class="related"><b>Related</b><ul>{''.join(f'<li><a href="{up}{h}">{e(t)}</a></li>' for h, t in x['related'])}</ul></div>

  <div class="cta">
    <h2>Ready to stop losing callers?</h2>
    <p>Book a free 30-minute call. I’ll look at your calls and show you exactly how this would work for your business.</p>
    <a class="btn" href="{up}#book">Book a free call →</a>
  </div>
</article>

<div class="sv-bar"><a class="btn" href="{up}#book">Book a free call →</a></div>
{chrome.footer(up)}
</body>
</html>
'''

if __name__ == '__main__':
    for x in SOL:
        os.makedirs(f'{ROOT}/solutions/{x["slug"]}', exist_ok=True)
        open(f'{ROOT}/solutions/{x["slug"]}/index.html', 'w').write(page(x))
        print('ok', x['slug'], len(x['title']), len(x['desc']))

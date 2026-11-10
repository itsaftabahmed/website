# Adds the visual service-page design (hero visual, before/after, proof block, mobile booking bar)
# to the pages in /services/. Safe to re-run. Edit D below, then: python3 _tools/svc_design.py
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def phone(top, rows):
    out = f'<div class="sv-phone" aria-hidden="true"><div class="sv-phone__top">{top}</div>'
    for kind, text in rows:
        out += f'<div class="sv-{kind}">{text}</div>'
    return out + '<div class="sv-ex">Example conversation</div></div>'

D = {
 'ai-automation': dict(
  visual=phone('Bright Smile Dental · 9:14 pm', [('miss', 'Missed call from (512) 555-0142'), ('me', 'Hi, this is Bright Smile Dental. Sorry we missed you! Are you looking to book a visit?'), ('you', 'Yes, I have a toothache. Anything tomorrow?'), ('me', 'I have 9:30 am or 2:00 pm tomorrow with Dr. Lee. Which works?'), ('you', '9:30 please'), ('ok', '✓ Booked · Tue 9:30 am · added to calendar')]),
  before=['Calls and messages wait until someone is free', 'After-hours inquiries get a reply the next day', 'Your team answers the same questions all day'],
  after=['Every inquiry answered in seconds, day or night', 'Appointments booked straight into your calendar', 'Your team only handles what needs a person'],
  quote=('“Our biggest problem wasn’t getting leads — it was following up with them fast enough. Aftab connected our ads, CRM, SMS and automated follow-up so every enquiry was contacted immediately. We stopped losing good leads simply because the team was busy.”', 'Sarah Mitchell', 'Managing Director, Healthcare Practice'),
  case=('dental', 'Dental · Raleigh, North Carolina', 'Making new-patient inquiries easier to manage', ['Question answered', 'Appointment request', 'Front desk review', 'Appointment confirmed'])),
 'lead-generation': dict(
  visual='<div class="sv-panel" aria-hidden="true"><div class="sv-panel__h">New leads today</div>'
         '<div class="sv-lead"><b>Maria G.</b><span>AC repair quote · Google Ads</span><i class="g">Call booked</i></div>'
         '<div class="sv-lead"><b>James P.</b><span>Kitchen remodel · Facebook</span><i class="y">Text sent · 1 min</i></div>'
         '<div class="sv-lead"><b>Dana W.</b><span>Website form</span><i class="y">Follow-up day 2</i></div>'
         '<div class="sv-lead"><b>Chris L.</b><span>Missed call</span><i class="g">Replied</i></div><div class="sv-ex">Example pipeline</div></div>',
  before=['Leads scattered across inboxes, forms and voicemail', 'Follow-up depends on who remembers', 'No clear view of which leads became customers'],
  after=['Every lead lands in one place within seconds', 'Automatic text, email and call tasks until they book', 'A simple pipeline that shows what turned into revenue'],
  quote=('“Our marketing felt disconnected. Ads were running, leads were coming in, but there was no proper journey after that. Aftab built the whole system from ad to landing page to CRM and follow-up. It made the process much easier to manage and convert.”', 'Michael Thompson', 'Director, Consulting Firm'),
  case=('hvac', 'HVAC · Austin, Texas', 'Turning more inquiries into booked service calls', ['Inquiry from ad', 'Acknowledgment sent', 'Office callback', 'Service call booked'])),
 'google-ads': dict(
  visual='<div class="sv-panel" aria-hidden="true"><div class="sv-search">🔍 emergency ac repair near me</div>'
         '<div class="sv-ad"><small>Sponsored · coolairheating.example</small><b>Same-Day AC Repair · Licensed Local Techs</b><p>No heat or no cooling? Book a visit online or call now. Upfront pricing.</p><span class="sv-call">📞 Call now</span></div>'
         '<div class="sv-ok">✓ New call · 2 min 14 sec · booked for today</div><div class="sv-ex">Example ad</div></div>',
  before=['Clicks from people who were never going to buy', 'Ads pointing at a general homepage', 'No idea which keywords bring real calls'],
  after=['Budget focused on searches with buying intent', 'Landing pages built for one service and one action', 'Calls and bookings tracked back to the keyword'],
  quote=('“We were spending money on ads but the leads weren’t turning into actual conversations. Aftab rebuilt the campaign, improved the messaging and fixed our follow-up. We started getting better-quality enquiries and finally had a system that moved leads toward booking.”', 'Daniel Morris', 'Founder, Property Services Company'),
  case=('roofing', 'Roofing · Denver, Colorado', 'Following up on estimate requests', ['Estimate request', 'Details and photos', 'Callback', 'Inspection scheduled'])),
 'facebook-ads': dict(
  visual='<div class="sv-panel sv-panel--fb" aria-hidden="true"><div class="sv-fbh"><span class="sv-av">GS</span><div><b>Glow Studio Med Spa</b><small>Sponsored</small></div></div>'
         '<p>New to Glow Studio? Book a free skin consultation this month. Limited evening slots.</p><div class="sv-img">Your offer, shown to local people</div>'
         '<div class="sv-fbf"><span>Free consultation</span><span class="sv-call">Book now</span></div><div class="sv-ok">✓ New lead · text sent in 40 seconds</div><div class="sv-ex">Example ad</div></div>',
  before=['Boosted posts with no clear offer', 'Leads that never answer the phone', 'Results that swing from week to week'],
  after=['A specific offer people want to claim', 'Instant follow-up while they still remember you', 'Steady testing of creative, audience and landing page'],
  quote=('“We had tried Meta Ads before and assumed they just didn’t work for our business. Aftab changed the offer, creative and landing page instead of simply changing the targeting. The campaigns became much more consistent and started bringing in enquiries we actually wanted.”', 'James Carter', 'Owner, Home Services Business'),
  case=('med-spa', 'Med spa · Scottsdale, Arizona', 'Helping inquiries become consultations', ['Consultation request', 'Acknowledgment', 'Staff follow-up', 'Consultation confirmed'])),
}

for slug, d in D.items():
    p = f'{ROOT}/services/{slug}/index.html'; s = open(p).read()
    # strip a previous run
    s = re.sub(r'\n?  <!--sv-->.*?<!--/sv-->\n?', '\n', s, flags=re.S)
    s = re.sub(r'<section class="hero hero--svc"><div class="wrap"><div class="sv-copy">(.*?)</div>\s*<div class="sv-phone.*?<!--/svv--></div></section>', r'<section class="hero"><div class="wrap">\1</div></section>', s, flags=re.S)
    s = re.sub(r'<section class="hero hero--svc"><div class="wrap"><div class="sv-copy">(.*?)</div>\s*<div class="sv-panel.*?<!--/svv--></div></section>', r'<section class="hero"><div class="wrap">\1</div></section>', s, flags=re.S)
    s = s.replace('<article class="svc">', '<article>')
    # hero with visual
    m = re.search(r'<section class="hero"><div class="wrap">(.*?)</div></section>', s, re.S)
    s = s[:m.start()] + f'<section class="hero hero--svc"><div class="wrap"><div class="sv-copy">{m.group(1)}</div>\n{d["visual"]}<!--/svv--></div></section>' + s[m.end():]
    s = s.replace('<article>', '<article class="svc">', 1)
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    ba = (f'  <!--sv--><div class="sv-ba"><div class="sv-card"><b>Today</b><ul>{li(d["before"])}</ul></div><div class="sv-arrow" aria-hidden="true">→</div>'
          f'<div class="sv-card sv-card--good"><b>After we set it up</b><ul>{li(d["after"])}</ul></div></div><!--/sv-->\n')
    s = s.replace('  <h2 id="included">', ba + '  <h2 id="included">', 1)
    q, who, role = d['quote']; cid, ck, ct, flow = d['case']
    fl = '<i aria-hidden="true">→</i>'.join(f'<span>{x}</span>' for x in flow)
    proof = (f'  <!--sv--><h2 id="proof">What clients say</h2>\n  <div class="sv-proof"><figure class="sv-card"><blockquote>{q}</blockquote><figcaption><b>{who}</b><small>{role}</small></figcaption></figure>'
             f'<div class="sv-card"><div class="kicker">Case study · {ck}</div><h3>{ct}</h3><div class="pflow">{fl}</div><p><a href="../../case-studies/#{cid}">Read the case study →</a></p></div></div><!--/sv-->\n\n')
    s = s.replace('  <h2 id="faq">', proof + '  <h2 id="faq">', 1)
    s = s.replace('<footer class="ft">', '<!--sv--><div class="sv-bar"><a class="btn" href="../../#book">Book a free call →</a></div><!--/sv-->\n<footer class="ft">', 1)
    open(p, 'w').write(s); print('ok', slug)

# Shared menu and footer for every inner page (not the homepage, which has its own).
# Edit the lists below, then run: python3 _tools/chrome.py   (rewrites the header/footer of all inner pages)
# gen_industries.py and mkpost.py import nav() and footer() from here.
import glob, os, re
from social_icons import SOCIAL3D
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SERVICES = [('services/ai-automation/', 'AI Automation &amp; AI Chatbots', 'Answer, qualify and book leads 24/7'),
            ('services/lead-generation/', 'Lead Generation Systems', 'Landing pages, CRM and follow-up'),
            ('services/google-ads/', 'Google Ads Management', 'High-intent local searches'),
            ('services/facebook-ads/', 'Facebook &amp; Instagram Ads', 'Offers that fill your calendar')]
SOLUTIONS = [('solutions/missed-calls/', 'Stop missed calls', 'AI receptionist and instant text back'),
             ('solutions/lead-follow-up/', 'Fix slow follow-up', 'Reply to every lead in seconds'),
             ('solutions/no-shows/', 'Reduce no-shows', 'Reminders and easy rescheduling'),
             ('solutions/ads-not-converting/', 'Fix ads that don’t convert', 'Offer, page, tracking and follow-up'),
             ('solutions/busywork/', 'Automate busywork', 'Onboarding, admin, reviews and reports')]
INDUSTRIES = [('industries/dental/', 'Dental &amp; medical'), ('industries/real-estate/', 'Real estate'),
              ('industries/home-services/', 'Home services'), ('industries/law/', 'Law firms'),
              ('industries/med-spa/', 'Med spas'), ('industries/accounting/', 'Accounting &amp; CPA'),
              ('industries/chiropractic/', 'Chiropractic &amp; PT'), ('industries/insurance/', 'Insurance agencies')]
LINKS = [('case-studies/', 'Case studies'), ('blog/', 'Blog'), ('tools/missed-call-calculator/', 'Free tools'), ('about/', 'About')]
SOCIAL = [('https://www.linkedin.com/in/iamaftabahmed/', 'in', 'LinkedIn'), ('https://www.youtube.com/@ItsAftab_Ahmed', 'YT', 'YouTube'),
          ('https://www.instagram.com/itsaftab.ahmed/', 'IG', 'Instagram'), ('https://www.tiktok.com/@itsaftab_ahmed', 'TT', 'TikTok')]

def latest_post():
    """Newest blog post (title, path) from the blog index, so the announcement stays current."""
    b = open(f'{ROOT}/blog/index.html').read()
    m = re.search(r'<a class="card" href="([^"]+)">\s*<div class="kicker">[^<]*</div>\s*<h2>([^<]+)</h2>', b)
    return (m.group(2), 'blog/' + m.group(1)) if m else ('Latest guides', 'blog/')

def short(t, n=34):
    t = re.split(r'[:?(]', t)[0].strip()
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'

def news():
    """Messages for the announcement capsule and the homepage bot: (path, short text, long text, emoji)."""
    title, path = latest_post()
    crumb = re.search(r'<nav class="crumbs".*?</a><span>/</span>([^<]+)</nav>', open(f'{ROOT}/{path}index.html').read(), re.S)
    label = crumb.group(1).strip() if crumb else short(title, 26)   # the post's short breadcrumb title
    guide = 'New guide: ' + label.lower().capitalize()
    return [('tools/missed-call-calculator/', 'Free missed call calculator', 'Free tool: what missed calls cost you', 'calc'),
            (path, guide, guide, 'guide'),
            ('#book', 'Taking new clients this month', 'Taking new clients: book a free call', 'cal')]

def ann(up):
    msgs = ''.join(f'<span class="ann__m{" on" if i == 0 else ""}" data-href="{up}{h}">{t} <b>→</b></span>' for i, (h, t, l, e) in enumerate(news()))
    on = ' class="on"'
    dots = ''.join('<i' + (on if i == 0 else '') + '></i>' for i in range(len(news())))
    return (f'<div class="ann"><a class="ann__in" href="{up}{news()[0][0]}" aria-live="polite"><span class="ann__new">NEW</span>'
            f'<span class="ann__msgs">{msgs}</span><span class="ann__dots" aria-hidden="true">{dots}</span></a></div>')

def nav(up):
    svc = ('<span class="nav__grp">Problems we solve</span>' + ''.join(f'<a href="{up}{h}">{t}<small>{d}</small></a>' for h, t, d in SOLUTIONS)
           + '<span class="nav__grp">Services</span>' + ''.join(f'<a href="{up}{h}" class="nav__sm">{t}</a>' for h, t, d in SERVICES))
    ind = ''.join(f'<a href="{up}{h}">{t}</a>' for h, t in INDUSTRIES) + f'<a href="{up}industries/">All industries →</a>'
    links = ''.join(f'<a class="nav__l" href="{up}{h}">{t}</a>' for h, t in LINKS)
    return (ann(up) + f'<header class="top"><div class="wrap"><a class="logo" href="{up}">AFTAB <span>AHMED</span></a>'
            f'<button type="button" class="nav__burger" aria-label="Menu" aria-expanded="false" aria-controls="siteNav"><i></i><i></i><i></i></button>'
            f'<nav class="nav" id="siteNav" aria-label="Main">'
            f'<div class="nav__dd"><button type="button" class="nav__l" aria-expanded="false">Solutions</button><div class="nav__menu nav__menu--sol">{svc}</div></div>'
            f'<div class="nav__dd"><button type="button" class="nav__l" aria-expanded="false">Industries</button><div class="nav__menu nav__menu--2">{ind}</div></div>'
            f'{links}<a class="btn" href="{up}#book">Book a call</a></nav></div></header>')

def footer(up):
    col = lambda title, items: f'<div><b>{title}</b>' + ''.join(f'<a href="{h}"{x}>{t}</a>' for h, t, x in items) + '</div>'
    soc = ''.join(f'<a href="{h}" rel="noopener" aria-label="{n}">{SOCIAL3D[n.lower()]}</a>' for h, s, n in SOCIAL)
    return (f'<footer class="ft"><div class="wrap">'
            f'<div class="ft__cta"><div><span class="ft__k">Let\'s talk</span><b>Ready for a business that <br>keeps working when you\'re not?</b></div><a class="btn" href="{up}#book">Book a free 30-minute call →</a></div>'
            f'<div class="ft__g">'
            f'<div><a class="logo" href="{up}">AFTAB <span>AHMED</span></a><p>AI automation, ads and lead follow-up for US service businesses.</p><div class="ft__soc">{soc}</div></div>'
            + col('Solutions', [(up + h, t, '') for h, t, d in SOLUTIONS])
            + col('Services', [(up + h, t, '') for h, t, d in SERVICES])
            + col('Industries', [(up + h, t, '') for h, t in INDUSTRIES[:4]] + [(up + 'industries/', 'All industries →', '')])
            + col('Resources', [(up + 'blog/', 'Blog', ''), (up + 'case-studies/', 'Case studies', ''), (up + 'tools/missed-call-calculator/', 'Missed call calculator', ''), (up + 'about/', 'About', '')])
            + col('Contact', [('mailto:hello@iamaftabahmed.com', 'hello@iamaftabahmed.com', ''), (up + '#book', 'Book a free call', ''), (up + 'privacy/', 'Privacy', '')])
            + f'</div><div class="ft__big" aria-hidden="true">AFTAB AHMED</div><div class="ft__b"><span>© 2026 Aftab Ahmed · AI, Automation &amp; Marketing</span><span>Serving businesses across the United States</span></div></div></footer>\n'
            f'<script src="{up}blog/site.js" defer></script><script src="{up}blog/ann.js" defer></script><script src="{up}blog/book.js" defer></script>')

def apply():
    n = 0
    for p in sorted(glob.glob(f'{ROOT}/**/index.html', recursive=True)):
        rel = os.path.relpath(p, ROOT)
        if rel == 'index.html' or rel.startswith(('_', '.', 'node_modules')): continue
        up = '../' * rel.count('/')
        s = open(p).read()
        t = re.sub(r'(<div class="ann">.*?</a></div>)?<header class="top">.*?</header>', lambda m: nav(up), s, 1, flags=re.S)
        t = re.sub(r'<footer[^>]*>.*?</footer>(\s*<script src="[^"]*site\.js" defer></script>(<script src="[^"]*ann\.js" defer></script>)?(<script src="[^"]*book\.js" defer></script>)?)?', lambda m: footer(up), t, 1, flags=re.S)
        if t != s: open(p, 'w').write(t); n += 1
    p = f'{ROOT}/404.html'; s = open(p).read()   # 404 is served from any path, so it uses absolute links
    t = re.sub(r'(<div class="ann">.*?</a></div>)?<header class="top">.*?</header>', lambda m: nav('/'), s, 1, flags=re.S)
    t = re.sub(r'<footer[^>]*>.*?</footer>(\s*<script src="[^"]*site\.js" defer></script>(<script src="[^"]*ann\.js" defer></script>)?(<script src="[^"]*book\.js" defer></script>)?)?', lambda m: footer('/'), t, 1, flags=re.S)
    if t != s: open(p, 'w').write(t); n += 1
    # homepage: announcement capsule + bot news (between markers)
    p = f'{ROOT}/index.html'; s = open(p).read()
    t = re.sub(r'<!--ann-->.*?<!--/ann-->', lambda m: '<!--ann-->' + ann('') + '<!--/ann-->', s, 1, flags=re.S)
    import json
    t = re.sub(r'/\*news\*/.*?/\*/news\*/', lambda m: '/*news*/' + json.dumps([{'href': h, 'text': l, 'icon': e} for h, x, l, e in news()], ensure_ascii=False) + '/*/news*/', t, 1, flags=re.S)
    if t != s: open(p, 'w').write(t); n += 1
    print('updated', n, 'pages')

if __name__ == '__main__':
    apply()

# Shared menu and footer for every inner page (not the homepage, which has its own).
# Edit the lists below, then run: python3 _tools/chrome.py   (rewrites the header/footer of all inner pages)
# gen_industries.py and mkpost.py import nav() and footer() from here.
import glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SERVICES = [('services/ai-automation/', 'AI Automation &amp; AI Chatbots', 'Answer, qualify and book leads 24/7'),
            ('services/lead-generation/', 'Lead Generation Systems', 'Landing pages, CRM and follow-up'),
            ('services/google-ads/', 'Google Ads Management', 'High-intent local searches'),
            ('services/facebook-ads/', 'Facebook &amp; Instagram Ads', 'Offers that fill your calendar')]
INDUSTRIES = [('industries/dental/', 'Dental &amp; medical'), ('industries/real-estate/', 'Real estate'),
              ('industries/home-services/', 'Home services'), ('industries/law/', 'Law firms'),
              ('industries/med-spa/', 'Med spas'), ('industries/accounting/', 'Accounting &amp; CPA'),
              ('industries/chiropractic/', 'Chiropractic &amp; PT'), ('industries/insurance/', 'Insurance agencies')]
LINKS = [('case-studies/', 'Case studies'), ('blog/', 'Blog'), ('tools/missed-call-calculator/', 'Free tools'), ('about/', 'About')]
SOCIAL = [('https://www.linkedin.com/in/iamaftabahmed/', 'in', 'LinkedIn'), ('https://www.youtube.com/@ItsAftab_Ahmed', 'YT', 'YouTube'),
          ('https://www.instagram.com/itsaftab.ahmed/', 'IG', 'Instagram'), ('https://www.tiktok.com/@itsaftab_ahmed', 'TT', 'TikTok')]

def nav(up):
    svc = ''.join(f'<a href="{up}{h}">{t}<small>{d}</small></a>' for h, t, d in SERVICES)
    ind = ''.join(f'<a href="{up}{h}">{t}</a>' for h, t in INDUSTRIES) + f'<a href="{up}industries/">All industries →</a>'
    links = ''.join(f'<a class="nav__l" href="{up}{h}">{t}</a>' for h, t in LINKS)
    return (f'<header class="top"><div class="wrap"><a class="logo" href="{up}">AFTAB <span>AHMED</span></a>'
            f'<button type="button" class="nav__burger" aria-label="Menu" aria-expanded="false" aria-controls="siteNav"><i></i><i></i><i></i></button>'
            f'<nav class="nav" id="siteNav" aria-label="Main">'
            f'<div class="nav__dd"><button type="button" class="nav__l" aria-expanded="false">Services</button><div class="nav__menu">{svc}</div></div>'
            f'<div class="nav__dd"><button type="button" class="nav__l" aria-expanded="false">Industries</button><div class="nav__menu nav__menu--2">{ind}</div></div>'
            f'{links}<a class="btn" href="{up}#book">Book a call</a></nav></div></header>')

def footer(up):
    col = lambda title, items: f'<div><b>{title}</b>' + ''.join(f'<a href="{h}"{x}>{t}</a>' for h, t, x in items) + '</div>'
    soc = ''.join(f'<a href="{h}" rel="noopener" aria-label="{n}">{s}</a>' for h, s, n in SOCIAL)
    return (f'<footer class="ft"><div class="wrap"><div class="ft__g">'
            f'<div><a class="logo" href="{up}">AFTAB <span>AHMED</span></a><p>AI automation, ads and lead follow-up for US service businesses.</p><div class="ft__soc">{soc}</div></div>'
            + col('Services', [(up + h, t, '') for h, t, d in SERVICES])
            + col('Industries', [(up + h, t, '') for h, t in INDUSTRIES[:4]] + [(up + 'industries/', 'All industries →', '')])
            + col('Resources', [(up + 'blog/', 'Blog', ''), (up + 'case-studies/', 'Case studies', ''), (up + 'tools/missed-call-calculator/', 'Missed call calculator', ''), (up + 'about/', 'About', '')])
            + col('Contact', [('mailto:hello@iamaftabahmed.com', 'hello@iamaftabahmed.com', ''), (up + '#book', 'Book a free call', ''), (up + 'privacy/', 'Privacy', '')])
            + f'</div><div class="ft__b"><span>© 2026 Aftab Ahmed · AI, Automation &amp; Marketing</span><span>Serving businesses across the United States</span></div></div></footer>\n'
            f'<script src="{up}blog/site.js" defer></script>')

if __name__ == '__main__':
    n = 0
    for p in sorted(glob.glob(f'{ROOT}/**/index.html', recursive=True)):
        rel = os.path.relpath(p, ROOT)
        if rel == 'index.html' or rel.startswith(('_', '.', 'node_modules')): continue
        up = '../' * rel.count('/')
        s = open(p).read()
        t = re.sub(r'<header class="top">.*?</header>', lambda m: nav(up), s, 1, flags=re.S)
        t = re.sub(r'<footer[^>]*>.*?</footer>(\s*<script src="[^"]*site\.js" defer></script>)?', lambda m: footer(up), t, 1, flags=re.S)
        if t != s: open(p, 'w').write(t); n += 1
    print('updated', n, 'pages')

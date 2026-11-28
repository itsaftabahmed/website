# Shared menu and footer for every inner page (not the homepage, which has its own).
# Edit the lists below, then run: python3 _tools/chrome.py   (rewrites the header/footer of all inner pages)
# gen_industries.py and mkpost.py import nav() and footer() from here.
import glob, os, re
from social_icons import SOCIAL3D, SOCIAL_MONO
from tool_icons import topic_icon
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SERVICES = [('services/ai-automation/', 'AI Automation &amp; AI Chatbots', 'Answer, qualify and book leads 24/7'),
            ('services/lead-generation/', 'Lead Generation Systems', 'Landing pages, CRM and follow-up'),
            ('services/google-ads/', 'Get Found on Google', 'Show up when locals search'),
            ('services/facebook-ads/', 'Win Customers on Social Media', 'Offers that fill your calendar')]
SOLUTIONS = [('solutions/missed-calls/', 'Stop missed calls', 'AI receptionist and instant text back'),
             ('solutions/lead-follow-up/', 'Fix slow follow-up', 'Reply to every lead in seconds'),
             ('solutions/no-shows/', 'Reduce no-shows', 'Reminders and easy rescheduling'),
             ('solutions/ads-not-converting/', 'Fix ads that don’t convert', 'Offer, page, tracking and follow-up'),
             ('solutions/busywork/', 'Automate busywork', 'Onboarding, admin, reviews and reports')]
INDUSTRIES = [('industries/dental/', 'Dental &amp; medical'), ('industries/real-estate/', 'Real estate'),
              ('industries/home-services/', 'Home services'), ('industries/law/', 'Law firms'),
              ('industries/med-spa/', 'Med spas'), ('industries/accounting/', 'Accounting &amp; CPA'),
              ('industries/chiropractic/', 'Chiropractic &amp; PT'), ('industries/insurance/', 'Insurance agencies'),
              ('industries/flooring/', 'Flooring companies')]
LINKS = [('pricing/', 'Pricing'), ('case-studies/', 'Case studies'), ('tools/', 'Free tools')]
SOCIAL = [('https://www.linkedin.com/in/iamaftabahmed/', 'in', 'LinkedIn'), ('https://www.youtube.com/@ItsAftab_Ahmed', 'YT', 'YouTube'),
          ('https://www.instagram.com/itsaftab.ahmed/', 'IG', 'Instagram'), ('https://www.tiktok.com/@itsaftab_ahmed', 'TT', 'TikTok')]

# A blog index card: <a class="card[ tc]" href="slug/"> [icon tile] <div class="kicker">label</div> <h2>title</h2>
CARD_RE = r'<a class="card(?: tc)?" href="([^"]+)">\s*(?:<div class="tc__art">.*?</div>\s*)?<div class="kicker">([^<]*)</div>\s*<h2>([^<]+)</h2>'

def tile(text, tag='div'):
    """Icon tile for a guide card (same look as the Free tools cards), picked from the guide's label and title."""
    return f'<{tag} class="tc__art"><span class="tc__ico">{topic_icon(text)}</span></{tag}>'

def latest_post():
    """Newest blog post (title, path) from the blog index, so the announcement stays current."""
    b = open(f'{ROOT}/blog/index.html').read()
    m = re.search(CARD_RE, b)
    return (m.group(3), 'blog/' + m.group(1)) if m else ('Latest guides', 'blog/')

def latest_guides(n=3):
    """Newest n posts for the homepage "Latest guides" list: (kicker, title, path, date, read)."""
    b = open(f'{ROOT}/blog/index.html').read()
    out = []
    for m in re.finditer(CARD_RE, b):
        post = open(f'{ROOT}/blog/{m.group(1)}index.html').read()
        d = re.search(r'"datePublished": "(\d{4})-(\d\d)-(\d\d)"', post)
        mins = re.search(r'(\d+) min read', post)
        mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(d.group(2)) - 1] if d else ''
        out.append((m.group(2), m.group(3), 'blog/' + m.group(1), f'{mon} {int(d.group(3))}, {d.group(1)}' if d else '', mins.group(1) if mins else ''))
        if len(out) == n: break
    return out

def guides_html():
    arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg>'
    return ''.join(f'<a class="lg tc" href="{h}">{tile(k + " " + t, "span")}<span class="lg__k">{k}</span><b>{t}</b><small>{d}{" · " + r + " min read" if r else ""}</small><i>{arrow}</i></a>' for k, t, h, d, r in latest_guides())

def short(t, n=34):
    t = re.split(r'[:?(]', t)[0].strip()
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'

def news():
    """Messages for the announcement capsule and the homepage bot: (path, short text, long text, emoji)."""
    title, path = latest_post()
    crumb = re.search(r'<nav class="crumbs".*?</a><span>/</span>([^<]+)</nav>', open(f'{ROOT}/{path}index.html').read(), re.S)
    label = crumb.group(1).strip() if crumb else short(title, 26)   # the post's short breadcrumb title
    guide = 'New guide: ' + (label if label[:2].isupper() else label[:1].upper() + label[1:])   # keep acronyms like AI
    return [('tools/no-show-cost-calculator/', 'New: No-show cost tool', 'New free tool: No-show cost calculator', 'calc'),
            (path, guide, guide, 'guide'),
            ('#book', 'Taking new clients this month', 'Taking new clients: book a free call', 'cal')]

# The top announcement is pinned to one message (owner's choice, Nov 2026). news() still feeds the homepage bot.
ANN = ('tools/missed-call-calculator/', 'Calculate how much missed calls are costing your business')

def ann(up):
    h, t = ANN
    return (f'<div class="ann"><a class="ann__in" href="{up}{h}"><span class="ann__new">NEW</span>'
            f'<span class="ann__msgs"><span class="ann__m on" data-href="{up}{h}">{t} <b>→</b></span></span></a></div>')

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

def footer(up, bare=False):   # bare: markup only (the homepage loads its own scripts)
    col = lambda title, items: f'<div><b>{title}</b>' + ''.join(f'<a href="{h}"{x}>{t}</a>' for h, t, x in items) + '</div>'
    soc = ''.join(f'<a href="{h}" rel="noopener" aria-label="{n}">{SOCIAL_MONO[n.lower()]}</a>' for h, s, n in SOCIAL)
    return (f'<footer class="ft"><div class="wrap">'
            f'<div class="ft__cta"><div><span class="ft__k">Let\'s talk</span><b>Ready for a business that <br>keeps working when you\'re not?</b></div><a class="btn" href="{up}#book">Book a free 30-minute call →</a></div>'
            f'<div class="ft__g">'
            f'<div><a class="logo" href="{up}">AFTAB <span>AHMED</span></a><p>AI automation, ads and lead follow-up for US service businesses.</p><div class="ft__soc">{soc}</div></div>'
            + col('Solutions', [(up + h, t, '') for h, t, d in SOLUTIONS])
            + col('Services', [(up + h, t, '') for h, t, d in SERVICES])
            + col('Industries', [(up + h, t, '') for h, t in INDUSTRIES[:4]] + [(up + 'industries/', 'All industries →', '')])
            + col('Resources', [(up + 'blog/', 'Blog', ''), (up + 'case-studies/', 'Case studies', ''), (up + 'tools/', 'Free tools', ''), (up + 'pricing/', 'Pricing', ''), (up + 'about/', 'About', '')])
            + col('Contact', [('mailto:hello@iamaftabahmed.com', 'hello@iamaftabahmed.com', ''), (up + '#book', 'Book a free call', ''), (up + 'privacy/', 'Privacy', '')])
            + f'</div><div class="ft__big" aria-hidden="true">AFTAB AHMED</div><div class="ft__b"><span>© 2026 Aftab Ahmed · AI, Automation &amp; Marketing</span><span>Serving businesses across the United States</span></div></div></footer>'
            + ('' if bare else f'\n<script src="{up}blog/site.js" defer></script><script src="{up}blog/ann.js" defer></script><script src="{up}blog/book.js?v=3" defer></script><script src="{up}blog/btn.js" defer></script>'))

def author(up):
    """"Written by" card in every blog post header (owner's pick, Nov 2026). Facts only from the homepage."""
    return (f'<aside class="pauth" aria-label="About the author"><img class="pauth__ph" src="{up}images/aftab-avatar.webp" alt="Aftab Ahmed" width="84" height="84" loading="lazy">'
            f'<div><small>Written by</small><b>Aftab Ahmed</b><p>I set up AI receptionists, lead follow-up and ads for US service businesses.</p>'
            f'<ul><li>8+ years in design and marketing</li><li>1,500+ projects delivered</li></ul><a href="{up}about/">More about me&nbsp;→</a></div></aside>')

def post_header(s, up):
    """Wrap a blog post's header text in .pmain and add (or refresh) the author card next to it."""
    m = re.search(r'<section class="hero"><div class="wrap">(.*?)</div></section>', s, re.S)
    if not m or 'class="meta"' not in m.group(1): return s
    inner = re.sub(r'<aside class="pauth".*?</aside>', '', m.group(1), flags=re.S)
    inner = re.sub(r'^<div class="pmain">(.*)</div>$', r'\1', inner, flags=re.S)
    return s[:m.start(1)] + f'<div class="pmain">{inner}</div>{author(up)}' + s[m.end(1):]

def blog_tiles(s):
    """Add an icon tile to every blog index card that has none yet (new posts from mkpost.py)."""
    return re.sub(r'<a class="card" href="([^"]+)">(\s*)<div class="kicker">([^<]*)</div>(\s*)<h2>([^<]+)</h2>',
                  lambda m: f'<a class="card tc" href="{m.group(1)}">{m.group(2)}{tile(m.group(3) + " " + m.group(5))}{m.group(2)}<div class="kicker">{m.group(3)}</div>{m.group(4)}<h2>{m.group(5)}</h2>', s)

def apply():
    n = 0
    for p in sorted(glob.glob(f'{ROOT}/**/index.html', recursive=True)):
        rel = os.path.relpath(p, ROOT)
        if rel == 'index.html' or rel.startswith(('_', '.', 'node_modules')): continue
        up = '../' * rel.count('/')
        s = open(p).read()
        t = re.sub(r'(<div class="ann">.*?</a></div>)?<header class="top">.*?</header>', lambda m: nav(up), s, 1, flags=re.S)
        t = re.sub(r'<footer[^>]*>.*?</footer>(\s*(?:<script src="[^"]*blog/(?:site|ann|book|btn)\.js[^"]*" defer></script>)+)?', lambda m: footer(up), t, 1, flags=re.S)
        if rel.startswith('blog/') and rel != 'blog/index.html': t = post_header(t, up)
        if rel == 'blog/index.html': t = blog_tiles(t)
        if t != s: open(p, 'w').write(t); n += 1
    p = f'{ROOT}/404.html'; s = open(p).read()   # 404 is served from any path, so it uses absolute links
    t = re.sub(r'(<div class="ann">.*?</a></div>)?<header class="top">.*?</header>', lambda m: nav('/'), s, 1, flags=re.S)
    t = re.sub(r'<footer[^>]*>.*?</footer>(\s*(?:<script src="[^"]*blog/(?:site|ann|book|btn)\.js[^"]*" defer></script>)+)?', lambda m: footer('/'), t, 1, flags=re.S)
    if t != s: open(p, 'w').write(t); n += 1
    # homepage: announcement capsule + bot news (between markers)
    p = f'{ROOT}/index.html'; s = open(p).read()
    t = re.sub(r'<!--ann-->.*?<!--/ann-->', lambda m: '<!--ann-->' + ann('') + '<!--/ann-->', s, 1, flags=re.S)
    import json
    t = re.sub(r'<!--guides-->.*?<!--/guides-->', lambda m: '<!--guides-->' + guides_html() + '<!--/guides-->', t, 1, flags=re.S)   # homepage latest guides
    t = re.sub(r'<!--ft-->.*?<!--/ft-->', lambda m: '<!--ft-->' + footer('', bare=True) + '<!--/ft-->', t, 1, flags=re.S)   # homepage uses the shared footer
    t = re.sub(r'/\*news\*/.*?/\*/news\*/', lambda m: '/*news*/' + json.dumps([{'href': h, 'text': l, 'icon': e} for h, x, l, e in news()], ensure_ascii=False) + '/*/news*/', t, 1, flags=re.S)
    if t != s: open(p, 'w').write(t); n += 1
    print('updated', n, 'pages')

if __name__ == '__main__':
    apply()

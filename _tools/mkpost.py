# Builds a blog post from a config file and updates every listing.
# Usage: python3 _tools/mkpost.py <config.py>   (config defines C = dict(...); keep configs outside the repo)
# Keys: slug, date, date_h, date_s, rfc, read, title, ttag (<=60), desc (140-160), card, keywords, crumb, kicker,
#       fpost_tag, topic_prefix, llms, lead, takeaways, toc [(id,text)], body (HTML, h2 ids match toc), faq [(q,a)],
#       sources [(title,url)], related [(href,text)], cta_h, cta_p, social; optional posts_key + industry_slug.
# After running: add a link to the new post from an older post or service page (WRITING_GUIDE step 6b),
# and run `python3 _tools/gen_industries.py` if posts_key was set.
import json, os, re, sys, subprocess, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = 'https://iamaftabahmed.com/'
ns = {}; exec(open(sys.argv[1]).read(), ns); c = ns['C']
slug, date = c['slug'], c['date']
url = f'{U}blog/{slug}/'
img = f'{U}images/og/{slug}.png'
e = lambda t: html.escape(t, quote=False)
a = lambda t: html.escape(t, quote=True)

def rd(p): return open(f'{ROOT}/{p}').read()
def wr(p, s): open(f'{ROOT}/{p}', 'w').write(s)
def sub(p, old, new):
    s = rd(p); assert old in s, (p, old[:60]); wr(p, s.replace(old, new, 1))

# Template: tracking scripts, author box and footer come from an existing post.
tpl = rd('blog/hvac-missed-calls/index.html')
track = tpl[tpl.index('<head>') + 6:tpl.index('<title>')]
body_track = tpl[tpl.index('<body>') + 6:tpl.index('<header')]
icon = re.search(r'<link rel="icon"[^>]*>', tpl).group(0)
abox = re.search(r'  <div class="abox">.*?</div></div>\n', tpl, re.S).group(0)
footer = chrome.footer('../../')

person = {"@type": "Person", "@id": f"{U}#person", "name": "Aftab Ahmed", "url": f"{U}about/", "jobTitle": "AI Automation & Marketing Specialist"}
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "BlogPosting", "headline": c['title'], "description": c['desc'], "datePublished": date, "dateModified": date,
     "mainEntityOfPage": url, "image": img, "citation": [u for t, u in c['sources']], "inLanguage": "en-US",
     "author": person, "publisher": {"@type": "Person", "@id": f"{U}#person", "name": "Aftab Ahmed"}, "keywords": c['keywords']},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": U},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{U}blog/"},
        {"@type": "ListItem", "position": 3, "name": c['crumb'], "item": url}]},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', x)}} for q, x in c['faq']]}]}

toc = ''.join(f'      <li><a href="#{i}">{e(t)}</a></li>\n' for i, t in c['toc'] + [('faq', 'FAQ')])
faq = ''.join(f'  <h3>{e(q)}</h3>\n  <p>{x}</p>\n' for q, x in c['faq'])
srcs = ''.join(f'<li><a href="{a(u)}" rel="noopener">{e(t)}</a></li>' for t, u in c['sources'])
rel = ''.join(f'    <li><a href="{h}">{e(t)}</a></li>\n' for h, t in c['related'])
tk = ''.join(f'<li>{e(t)}</li>' for t in c['takeaways'])

TOOL = '    <div class="toc__tool"><b>Free tool</b><span>See what missed calls cost you each month.</span><a href="../../tools/missed-call-calculator/">Open the calculator →</a></div>\n'
MID = '  <div class="midcta"><div><b>Want this set up for you?</b><p>Book a free 30-minute call and I\'ll show you how it would work in your business.</p></div><a class="btn" href="../../#book">Book a free call →</a></div>\n\n'
body = c['body'].rstrip()
_h = [m.start() for m in re.finditer(r'  <h2 id="', body)]
if len(_h) >= 4: body = body[:_h[len(_h) // 2]] + MID + body[_h[len(_h) // 2]:]   # booking prompt mid-post

page = f'''<!doctype html>
<html lang="en">
<head>{track}<title>{e(c['ttag'])}</title>
<meta name="description" content="{a(c['desc'])}">
<meta name="author" content="Aftab Ahmed">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Aftab Ahmed">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="article:published_time" content="{date}">
<meta property="article:author" content="Aftab Ahmed">
<meta name="theme-color" content="#0A0A0A">
<meta property="og:type" content="article">
<meta property="og:title" content="{a(c['title'])}">
<meta property="og:description" content="{a(c['card'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{img}">
{icon}
<link rel="alternate" type="application/rss+xml" title="Aftab Ahmed Blog" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="../blog.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False)}
</script>
</head>
<body>{body_track}{chrome.nav('../../')}

<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a><span>/</span><a href="../">Blog</a><span>/</span>{e(c['crumb'])}</nav>
  <div class="kicker">{e(c['kicker'])}</div>
  <h1>{e(c['title'])}</h1>
  <p class="lead">{e(c['lead'])}</p>
  <p class="meta">By <a href="../../about/" style="color:inherit">Aftab Ahmed</a> · {c['date_h']} · {c['read']} min read</p>
</div></section>

<article>
  <div class="takeaways"><b>Key takeaways</b><ul>{tk}</ul></div>

  <div class="toc"><b>In this guide</b>
    <ol>
{toc}    </ol>
{TOOL}  </div>

{body}

  <h2 id="faq">FAQ</h2>
{faq}
  <div class="sources"><b>Sources and further reading</b><ul>{srcs}</ul></div>
{abox}  <div class="related"><b>Related</b><ul>
{rel}  </ul></div>

  <div class="cta">
    <h2>{e(c['cta_h'])}</h2>
    <p>{e(c['cta_p'])}</p>
    <a class="btn" href="../../#book">Book a free call →</a>
  </div>
</article>

{footer}
</body>
</html>
'''
os.makedirs(f'{ROOT}/blog/{slug}', exist_ok=True)
wr(f'blog/{slug}/index.html', page)

# Blog index card
sub('blog/index.html', '  <!-- NEW POSTS GO HERE (newest first) -->\n', f'''  <!-- NEW POSTS GO HERE (newest first) -->
  <a class="card" href="{slug}/">
    <div class="kicker">{e(c['kicker'])}</div>
    <h2>{e(c['title'])}</h2>
    <p>{e(c['card'])}</p>
    <span>Read the guide →</span>
  </a>
''')
# Homepage "From the blog": newest first, keep 3
s = rd('index.html')
m = re.search(r'(<div class="fblog__list">\n)((?:        <a class="fpost".*\n)*)', s)
posts = m.group(2).splitlines(keepends=True)
new = f'        <a class="fpost" href="blog/{slug}/"><span class="fpost__tag">{e(c["fpost_tag"])}</span><b>{e(c["title"])}</b><small>{c["date_s"]} · {c["read"]} min read</small></a>\n'
s = s[:m.start(2)] + ''.join(([new] + posts)[:3]) + s[m.end(2):]
wr('index.html', s)
# RSS
s = rd('feed.xml')
s = re.sub(r'<lastBuildDate>[^<]*</lastBuildDate>', f'<lastBuildDate>{c["rfc"]}</lastBuildDate>', s, 1)
s = s.replace('<!-- NEW ITEMS GO HERE (newest first) -->\n', f'''<!-- NEW ITEMS GO HERE (newest first) -->
  <item>
    <title>{e(c['title'])}</title>
    <link>{url}</link>
    <guid isPermaLink="true">{url}</guid>
    <pubDate>{c['rfc']}</pubDate>
    <dc:creator>Aftab Ahmed</dc:creator>
    <description>{e(c['card'])}</description>
  </item>
''', 1)
wr('feed.xml', s)
# llms.txt
sub('llms.txt', '<!-- NEW POSTS GO HERE -->\n', f'<!-- NEW POSTS GO HERE -->\n- [{c["title"]}]({url}): {c["llms"]}\n')
# Sitemap
s = rd('sitemap.xml')
s = re.sub(r'(<loc>https://iamaftabahmed.com/blog/</loc><lastmod>)[^<]*(</lastmod></url>\n)', rf'\g<1>{date}\g<2>', s, 1)
if f'<loc>{url}</loc>' not in s:
    blog_line = re.search(r'  <url><loc>https://iamaftabahmed.com/blog/</loc>.*\n', s)
    s = s[:blog_line.end()] + f'  <url><loc>{url}</loc><lastmod>{date}</lastmod></url>\n' + s[blog_line.end():]
wr('sitemap.xml', s)
# Topic queue: move to Published
s = rd('blog/topics.md')
line = next(l for l in s.splitlines() if l.startswith('- [ ] ' + c['topic_prefix']))
s = s.replace(line + '\n', '', 1).replace('## Published\n', '## Published\n' + line.replace('- [ ]', '- [x]', 1) + '\n', 1)
wr('blog/topics.md', s)
# Industry page Related list
if c.get('posts_key'):
    k, ind = c['posts_key'], c['industry_slug']
    s = rd('_tools/gen_industries.py')
    if f"'{k}':" not in s:
        s = s.replace("POSTS = {", f"POSTS = {{'{k}': ({c['title']!r}, 'blog/{slug}/'),\n         ", 1)
    m = re.search(rf"dict\(slug='{ind}'.*?\n  rel=\[([^\]]*)\]", s, re.S)
    keys = [x.strip().strip("'") for x in m.group(1).split(',')]
    svc = [x for x in keys if x in ('ai', 'ga', 'fb', 'lg')][:2]
    pk = [k] + [x for x in keys if x not in svc and x != k]
    s = s[:m.start(1)] + ','.join(repr(x) for x in svc + pk[:3]) + s[m.end(1):]
    wr('_tools/gen_industries.py', s)
# Social drafts
os.makedirs(f'{ROOT}/_tools/social', exist_ok=True)
wr(f'_tools/social/{date}-{slug}.md', c['social'])
# Share image
subprocess.run(['node', f'{ROOT}/_tools/og.js', slug], check=True, env={**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()})

text = re.sub('<[^>]+>', ' ', c['body'] + c['lead'] + ' '.join(x for q, x in c['faq']))
bad = [w for w in ('delve', 'game-changer', 'unlock', 'leverage', 'seamless', 'cutting-edge', 'in today', 'revolutioniz', 'skyrocket') if w in text.lower()]
print(slug, 'words', len(text.split()), 'title', len(c['ttag']), 'desc', len(c['desc']), 'emdash', page.count('—'), 'bad', bad)

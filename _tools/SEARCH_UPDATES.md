# Weekly search & AI-search update check

Runs every week. Goal: catch changes from Google, Bing and the AI search engines early, and adjust the site and the writing rules when something actually matters. Full background: the research report from 2026-10-25 (kept outside the published site).

The sandbox usually can't open these sites directly, so use **web search** (standard first, extended if results are thin) and check the official page in the results.

## 1. Check these sources for anything from the last 7 days

Official (highest weight):
- Google Search Status Dashboard: core, spam and ranking updates (status.search.google.com, feed: /en/feed.atom)
- Google Search Central Blog (developers.google.com/search/blog) and "Latest Google Search documentation updates" (developers.google.com/search/updates)
- Google guide to optimizing for generative AI features and AI Overviews / AI Mode announcements
- Bing Webmaster Blog (blogs.bing.com/webmaster), including Bing Webmaster Tools AI Performance report and IndexNow news
- Crawler docs for changes to bot names or rules: OpenAI (developers.openai.com/api/docs/bots), Anthropic (support.claude.com crawler article), Perplexity (docs.perplexity.ai perplexity-crawlers), Apple (support.apple.com/en-us/119829), Google crawlers (developers.google.com/crawling)
- Google Search Central on X (@googlesearchc). The old Search Liaison account has been inactive since Aug 2025.

Industry (to spot things early, confirm with an official source before acting):
- Search Engine Roundtable, Search Engine Land, Search Engine Journal
- Major studies on AI citations (Ahrefs, Semrush, BrightEdge) only when they have large samples

## 2. Decide what matters for this site

Act only on changes that affect a small static service-business site:
- New/removed structured data types, or rich result changes (update `_tools/gen_industries.py`, post templates, `blog/WRITING_GUIDE.md`)
- New or renamed AI crawler user agents (update `robots.txt`; keep search and user-triggered bots allowed)
- Spam policy changes (check the blog routine and topic queue still comply, especially the scaled-content policy)
- Core update in progress: don't make big site changes until it finishes; note it and compare Search Console after it ends
- New Search Console or Bing Webmaster Tools reports: tell the owner what to look at

Ignore hype (e.g. "llms.txt boosts rankings", AI-specific rewriting tricks) unless an official source confirms it.

## 3. Finish

- If a change is confirmed, also update the matching file in `.claude/skills/seo/references/` (and the snapshot date) so the SEO skill stays current.
- Add a dated entry to the log below: what changed, source URL, and what (if anything) was done.
- If site files changed: test (390px, one H1, valid JSON-LD, no broken links), commit as `Search update check: <date>` and push to the working branch and `main`.
- Reply with a 3–5 line summary. If nothing relevant happened, say so in one line.

## Log
- 2026-11-10: weekly check. No confirmed Google core or spam update (one is widely expected; SER noted possible unconfirmed volatility around Nov 9). Search Console: performance report now lets you select several device types at once (Nov 5); a reported click spike in the performance report around Nov 2-4 may be a bug, so don't read much into it. OpenAI is reportedly building a Search Console-style tool for businesses to track how they appear in ChatGPT (not launched); sign up when it opens. Google reportedly testing changes to the AI Mode button and a "continue with this search" prompt (no site action). No crawler user-agent changes found for OpenAI, Anthropic, Perplexity or Apple. No site files changed. Sources: seroundtable.com recaps Nov 2-9, 2026.
- 2026-11-03: weekly check. No confirmed Google core or spam update (unconfirmed ranking volatility reported Oct 24 and Oct 27). Google announced it plans to support a shared AI-training opt-out token in robots.txt (IETF AIPREF work) with other AI providers in 2027; Google-Extended keeps working and the token doesn't affect Search ranking or indexing. No action now: the site doesn't opt out of training. Google also updated its robots.txt guidance (Oct 23) and its user-generated spam document (Oct 26); the site has no user-generated content, so no action. No dated crawler user-agent changes from OpenAI, Anthropic, Perplexity or Apple found. Site note: DNS moved to Cloudflare this week; Cloudflare's "Bot Preference Sync" (it prepends rules to robots.txt) was turned off so the site's own robots.txt applies. Sources: developers.google.com/search/blog/2026/10/ai-training-control, seroundtable.com recaps Oct 26-30, 2026.
- 2026-10-27: weekly check. No confirmed Google core/spam update or AI-crawler doc change in the last 7 days. Logged recent items: Sept spam update completed Oct 8; Google dropped review snippets for healthcare pages (Oct 7, site uses no review markup); Google testing tracking parameters on AI Overviews/AI Mode links (Oct 2, would help GA4 attribution); crawl-rate doc added Retry-After info (no action). Updated SEO skill references. Sources: seroundtable.com headlines for Oct 2-8, 2026.
- 2026-10-25: set up after deep research. Applied: logo + Organization details in homepage schema, static counter values, H1 spacing, shorter titles, sitemap dates for changed pages, research folders excluded from Jekyll.

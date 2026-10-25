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

- Add a dated entry to the log below: what changed, source URL, and what (if anything) was done.
- If site files changed: test (390px, one H1, valid JSON-LD, no broken links), commit as `Search update check: <date>` and push to the working branch and `main`.
- Reply with a 3–5 line summary. If nothing relevant happened, say so in one line.

## Log
- 2026-10-25: set up after deep research. Applied: logo + Organization details in homepage schema, static counter values, H1 spacing, shorter titles, sitemap dates for changed pages, research folders excluded from Jekyll.

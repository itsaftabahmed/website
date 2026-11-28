# Automated blog: how to publish one post

Audience: US small-business owners (dental, real estate, accounting, home services, med spa, law, local services).
Author voice: Aftab Ahmed, 8+ years in design and marketing, now AI, automation and marketing. Plain, direct, practical. "No hype."

Pace (owner decision, 2026-11-23, after the November 2026 core update hit sites publishing AI content at scale): **one new post a week (Monday)**. **Thursday is an improvement run**: make one existing post clearly better instead of adding a page (see "Thursday: improve one post" below). Google ranks helpful, original content, not volume; its scaled-content policy targets sites publishing lots of low-value pages, and its guidance on AI content says to fact-check and review AI-written text before publishing. Each post should be the most useful answer on its topic: specific steps, a worked example, real sources and the author's view.

## Owner's experience in every post (human review)

Every post needs first-hand input from Aftab, because Google rewards real experience and asks for human review of AI-assisted content. Never invent his experience, clients or results.
- When you publish a new post, add one short question for Aftab to the top of `_tools/OWNER_QUESTIONS.md` (post title, URL path, the question). Make it easy to answer in one or two lines from his work, e.g. "What is the most common follow-up mistake you see HVAC owners make?" Put the question in your final reply too.
- When a question in that file has an answer, the next Thursday run adds it to the post as a short callout `<div class="callout"><b>From my work:</b> ...</div>` in the most relevant section, in his words (light grammar fixes only), and moves the question to "Answered".
- Until it is answered, the post goes live without the callout. Never write one yourself.
- **Authorship must stay honest.** Google's people-first content guidance (updated Oct 1, 2026) calls fabricated creator profiles (invented names, AI-generated headshots, false credentials) deceptive and a low-quality signal. Posts are bylined to Aftab, the real owner, with his real photo and the About page. Never add other author names, invented credentials or claims that he personally did something he did not confirm. His "From my work" answers are what make the byline accurate.

## Thursday: improve one post

Do this instead of writing a new post on Thursdays.
1. Pick the post: first any post whose question in `_tools/OWNER_QUESTIONS.md` has been answered but not added; otherwise the post improved least recently in the log at the bottom of `_tools/OWNER_QUESTIONS.md` (never improved counts as oldest).
2. Make real improvements, not cosmetic ones. Changing the date alone counts as nothing. Do at least three of these:
   - Add the owner's answer as a "From my work" callout (when available).
   - Answer 1 or 2 missing buyer questions from `_tools/DECISION_MAP.md` or "People also ask".
   - Check the basics the update rewards: the main search phrase in the title, H1, URL and the first sentence; the answer to the searcher's question in the first paragraph, above the fold.
   - Replace vague lines with specifics (exact settings, steps, numbers with confirmed sources).
   - Check every source link still works and every statistic is still current; fix or remove anything that isn't.
   - Cut filler and repetition so the post reads faster.
   - Add links to newer related posts, tools and the pricing page where they genuinely help.
3. Update `dateModified` in the post's JSON-LD and the visible "Updated" date if the template has one, plus its `sitemap.xml` lastmod. Add a line to the log in `_tools/OWNER_QUESTIONS.md`.
4. Test (site check and headless Chromium at 1366 and 390), commit as `Improve post: <title>`, push to both branches.

## Steps (do all of them, in this order)

Shortcut: write the post as a config file outside the repo and run `python3 _tools/mkpost.py <config.py>` (keys listed at the top of the script). It builds the page from the template and does steps 3, 5, 5a, 6, 6a (POSTS/rel), 6c, 6d, 6e, 7 and 8. You still do 6b, run `python3 _tools/gen_industries.py` when the post belongs to an industry, test, and commit.

1. Open `blog/topics.md` and take the **first line that starts with `- [ ]`**. The part before `|` is the title; after `|` is the main search phrase.
2. Make a URL slug from the title: lowercase, words joined by `-`, no stop-word clutter, max ~7 words (e.g. `facebook-ads-cost-small-business`).
3. Create `blog/<slug>/index.html` by **copying the structure (including the Google Analytics tag right after `<head>`, the Google Tag Manager, Meta Pixel and Clarity tracking codes at the top of `<head>` and the GTM `<noscript>` right after `<body>`, unchanged) of `blog/facebook-ads-clicks-but-no-calls/index.html` exactly** (same head tags, fonts, `../blog.css`, header, hero, table of contents, article, FAQ, CTA box, footer). Replace:
   - `<title>`: under ~60 characters, includes the search phrase, ends with "(2026)" only when the topic is time-sensitive.
   - meta description: 140–160 characters, includes the search phrase, promises a concrete answer.
   - og:title / og:description, JSON-LD `BlogPosting` (headline, description, today's date for datePublished and dateModified, keywords) and `FAQPage` (the same 3 questions as the FAQ section).
   - hero kicker (2 topic tags), H1, lead paragraph, byline date (today, "Month D, YYYY") and read time.
4. Article content rules:
   - 1,200–1,800 words. Answer the search in the first 2 paragraphs.
   - **Search & AI-answer format (Google, AI Overviews, ChatGPT, Perplexity, Copilot):**
     - Start the article with a `<div class="takeaways"><b>Key takeaways</b><ul>…</ul></div>` box: 3–5 one-sentence answers a reader (or an AI engine) could quote on their own.
     - Write most `<h2>` headings as the questions people actually ask ("How much does…", "Why does…", "What is…"), and make the first 1–2 sentences under each heading a direct, self-contained answer before the detail.
     - Use lists, numbered steps and short tables where they make an answer clearer; define terms in plain English the first time they appear.
     - Tables: wrap every table in `<div class="tw">`. A table with sentences in its cells uses `<table class="wrap cols3">` (`class="wrap"` for 2 columns), so it fits phones and reads left to right. Only number tables use a plain `<table>` (numbers right-aligned; on phones they scroll with a "Swipe to see all columns" hint).
     - A text link that ends in an arrow uses `&nbsp;→` so the arrow never wraps onto its own line.
     - Do not add an author box or a card picture by hand: `python3 _tools/chrome.py` adds the "Written by" card to the post header and an icon tile to the blog page card. If the new topic gets an unsuitable icon, add a keyword rule to `TOPIC_RULES` in `_tools/tool_icons.py`.
     - Keep the byline link to `../../about/` and the author `url` in JSON-LD pointing to `https://iamaftabahmed.com/about/`.
   - 5–8 `<h2>` sections with ids, listed in the "In this guide" box; one practical checklist (`<ul class="check">`) and one `<div class="callout">` tip.
   - Include a step-by-step plan or checklist the reader can use today.
   - FAQ with 3 real questions people search, each answered in 2–3 sentences.
   - End with the CTA box: heading related to the topic, one sentence, button to `../../#book`.
   - Internal links (important for SEO):
     - In the body, link naturally to the **most relevant service page** at least once: `../../services/facebook-ads/`, `../../services/google-ads/`, `../../services/lead-generation/` or `../../services/ai-automation/`, using descriptive anchor text (e.g. "Google Ads management for small businesses"), never "click here".
     - If the post is about or clearly useful to one industry, also link its industry page: `../../industries/dental/` (dental & medical), `../../industries/real-estate/` (real estate & property), `../../industries/accounting/` (accounting & CPA), `../../industries/home-services/` (HVAC, plumbing, roofing, etc.), `../../industries/med-spa/` (med spas & aesthetics), `../../industries/law/` (law firms) `../../industries/chiropractic/` (chiropractors & physical therapy) `../../industries/insurance/` (insurance agencies) or `../../industries/flooring/` (flooring stores and installers).
     - Link to 1–2 earlier posts on this blog where genuinely relevant (relative links like `../other-slug/`).
     - Keep the "Related" box above the CTA with the 2–3 most relevant service pages / posts.
   - Keep the template's breadcrumb (`Home / Blog / <short title>`), canonical URL (`https://iamaftabahmed.com/blog/<slug>/`), og:url, article:published_time and the `BreadcrumbList` JSON-LD, updated for the new post.
   - **Sources (helps Google trust and AI citations):** link 2–4 authoritative primary sources where they genuinely support a claim (government agencies such as IRS, FTC, HHS, FCC; official platform help docs from Google or Meta; professional bodies such as the ABA or CTIA; original research). Link them inline where the claim is made and list them in the `<div class="sources"><b>Sources and further reading</b><ul>…</ul></div>` box above the author box, and add the same URLs to a `citation` array in the BlogPosting JSON-LD. Only use URLs you have confirmed exist (via web search results); never guess a URL. No links to competitors' sales pages.
   - Keep the `<div class="abox">` "About the author" box (copied from the template) between the sources box and the Related box.
   - **Never invent statistics, studies, client names, case results or quotes.** Prefer ranges and "typically", and say costs vary. No fake testimonials, no "we helped X get Y%".
   - No keyword stuffing; use the search phrase naturally in the H1, first paragraph, one H2 and the meta description.
   - US spelling and US context (dollars, US platforms and rules).
5a. Share image: run `NODE_PATH=$(npm root -g) node _tools/og.js <slug>` to create `images/og/<slug>.png` (1200x630), and set `og:image`, `twitter:image` and the JSON-LD `image` to `https://iamaftabahmed.com/images/og/<slug>.png` (the template already has the width/height tags).
5. Add a card for the post at the **top** of the list in `blog/index.html`, right under `<!-- NEW POSTS GO HERE (newest first) -->`, using the same `<a class="card">` markup.
6. (Automatic.) The homepage "Latest guides" list shows the 3 newest posts from `blog/index.html`; `python3 _tools/chrome.py` (run at the end of `mkpost.py`) refreshes it.
6a. If the post is about one industry, also add it to that industry page's Related box: in `_tools/gen_industries.py` add `'<short-key>': ('<Title>', 'blog/<slug>/')` to `POSTS`, put the key first in that industry's `rel` list (keep at most 3 post keys, drop the oldest), and run `python3 _tools/gen_industries.py`.
6b. Once the new post is live, add one contextual link to it from an older related post or from the matching service page's "Related" list, so every post is linked from somewhere other than the blog index.
6c. Add the post to the top of `feed.xml` (right under `<!-- NEW ITEMS GO HERE (newest first) -->`, same `<item>` format with title, link, guid, pubDate in RFC-822 GMT, dc:creator and description) and update `<lastBuildDate>`.
6d. Add a line for the post at the top of the blog list in `llms.txt` (under `<!-- NEW POSTS GO HERE -->`): `- [Title](https://iamaftabahmed.com/blog/<slug>/): one-line summary`.
6e. Write a ready-to-post social draft at `_tools/social/<YYYY-MM-DD>-<slug>.md` in the same format as the existing files there: a LinkedIn version (hook line, 3–5 short points from the post, link) and a short X/Threads version (under 280 characters with link). Same quality rules: no hype words, no em dashes, no hashtag stuffing (0–2 hashtags max).
7. Add the post URL to `sitemap.xml` (`https://iamaftabahmed.com/blog/<slug>/`, lastmod today) and update the `/blog/` lastmod.
8. In `blog/topics.md`, change that topic's `- [ ]` to `- [x]`.
8b. After pushing (step 9), notify search engines instantly via IndexNow (Bing, Yandex, Seznam, Naver; also feeds ChatGPT/Copilot search). Run, best effort; if the network blocks it, just continue:
   `curl -s -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json' -d '{"host":"iamaftabahmed.com","key":"1f05e2226886949432f94aa509ff16b9","keyLocation":"https://iamaftabahmed.com/1f05e2226886949432f94aa509ff16b9.txt","urlList":["https://iamaftabahmed.com/blog/<slug>/","https://iamaftabahmed.com/blog/","https://iamaftabahmed.com/sitemap.xml"]}'`
9. Commit with message `Blog: <title>` and push to **both** the working branch and `main` (`git push origin HEAD:main`). Retry pushes on network errors.


## Focus industries (owner decision, 2026-11-22)

Most new posts should serve the focus industries: **home services** (HVAC, roofing, flooring, plumbing), **dental and medical practices**, **real estate** and **insurance**, or be general posts every service business can use. When the next unchecked topic in `blog/topics.md` is for a non-focus industry and a focus or general topic is further down, take the focus or general one first (tick it) and leave the other in place. When adding new topics, add them for focus industries or general use only.

## Google AI search rules (from Neil Patel, "Google's New Rules for Getting Customers", Nov 2026)

Google's AI Mode runs several hidden searches for one question ("query fan-out") and lifts single paragraphs out of pages to build its answer. Every page must work for that:

- **Cover the decision, not one keyword.** Before writing, check `_tools/DECISION_MAP.md` for the buyer question this page belongs to. Answer the sub-questions this topic owns, link to the pages that answer the others, and add any unanswered sub-question to `blog/topics.md`. Never create thin pages just to target sub-questions: Google treats scaled, low-value pages made mainly for AI answers as spam. Fewer pages with real answers win.
- **Every key paragraph must work when copied out alone.** The first paragraph under each H2, the lead and every FAQ answer must name the subject (the service, tool, industry or setting), say who it is for, and put the limit or condition right next to the claim. Never start one with "It", "This", "That" or "They". Test: paste the paragraph into a blank document. If it needs the paragraph above to make sense, rewrite it.
- **Proof that names things.** Use specific, real results and named (confirmed) customers where we have them. Never invent them. Hypothetical examples stay labelled.
- **No AI gimmicks.** Google says special "AI markup", llms.txt files and chopping content into tiny chunks are not needed for its AI features. Keep normal schema and `llms.txt` (other AI tools may read it) but never spend effort on "AI schema".

## Quality rules (what Google actually rewards)

Google ranks pages on how helpful and original they are, not on who or what wrote them. Generic, interchangeable content is what fails. Every post must pass these:

- **One original angle.** Include at least one thing a generic article wouldn't: a specific setup Aftab would actually build, a worked example with realistic (clearly hypothetical) numbers, a mistake he sees often, or a clear opinion with the reason behind it. Write it in first person ("When I set this up for a service business, I…") only for general practice, never for invented client stories.
- **Specific over vague.** Name the actual setting, field, tool or step ("turn on the 'Higher intent' form type in Meta Lead Ads") instead of "optimize your forms".
- **No filler phrases.** Never use: "In today's fast-paced world", "in the digital age", "unlock", "unleash", "elevate", "game-changer", "dive in/deep dive", "navigate the landscape", "it's important to note", "in conclusion", "whether you're X or Y", "look no further", "seamless", "robust", "leverage" (as a verb), "supercharge".
- **No em dashes (—).** Use commas, periods or parentheses.
- **Vary rhythm.** Mix short and long sentences; don't start consecutive paragraphs the same way; avoid groups of exactly three adjectives in a row.
- **Comparison posts.** When the topic is an "X vs Y" or "best X for Y" question, include a fair comparison table, say who each option suits, and give a clear recommendation with the reason. Don't trash competitors or name specific vendors you can't describe accurately.
- **No repeated structure across posts.** Change the order of sections, the example industry and the opening style (a question, a scenario, a direct answer, a common myth) from post to post.
- **Plain text only.** Type normal characters; never paste invisible or special Unicode characters.
- **Fact-check claims.** Platform features, policies and settings must be current; if unsure, describe the principle rather than a specific button.

If every topic is checked, write 20 new topics in the same format and style at the end of `blog/topics.md` (new searches US small-business owners make about ads, leads, follow-up and AI automation, not duplicates), then publish the first one.

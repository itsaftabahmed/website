# Automated blog: how to publish one post

Audience: US small-business owners (dental, real estate, accounting, home services, med spa, law, local services).
Author voice: Aftab Ahmed, 8+ years in design and marketing, now AI, automation and marketing. Plain, direct, practical. "No hype."

## Steps (do all of them, in this order)

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
     - Keep the byline link to `../../about/` and the author `url` in JSON-LD pointing to `https://iamaftabahmed.com/about/`.
   - 5–8 `<h2>` sections with ids, listed in the "In this guide" box; one practical checklist (`<ul class="check">`) and one `<div class="callout">` tip.
   - Include a step-by-step plan or checklist the reader can use today.
   - FAQ with 3 real questions people search, each answered in 2–3 sentences.
   - End with the CTA box: heading related to the topic, one sentence, button to `../../#book`.
   - Internal links (important for SEO):
     - In the body, link naturally to the **most relevant service page** at least once: `../../services/facebook-ads/`, `../../services/google-ads/`, `../../services/lead-generation/` or `../../services/ai-automation/`, using descriptive anchor text (e.g. "Google Ads management for small businesses"), never "click here".
     - If the post is about or clearly useful to one industry, also link its industry page: `../../industries/dental/` (dental & medical), `../../industries/real-estate/` (real estate & property), `../../industries/accounting/` (accounting & CPA), `../../industries/home-services/` (HVAC, plumbing, roofing, etc.), `../../industries/med-spa/` (med spas & aesthetics) or `../../industries/law/` (law firms).
     - Link to 1–2 earlier posts on this blog where genuinely relevant (relative links like `../other-slug/`).
     - Keep the "Related" box above the CTA with the 2–3 most relevant service pages / posts.
   - Keep the template's breadcrumb (`Home / Blog / <short title>`), canonical URL (`https://iamaftabahmed.com/blog/<slug>/`), og:url, article:published_time and the `BreadcrumbList` JSON-LD, updated for the new post.
   - **Never invent statistics, studies, client names, case results or quotes.** Prefer ranges and "typically", and say costs vary. No fake testimonials, no "we helped X get Y%".
   - No keyword stuffing; use the search phrase naturally in the H1, first paragraph, one H2 and the meta description.
   - US spelling and US context (dollars, US platforms and rules).
5. Add a card for the post at the **top** of the list in `blog/index.html`, right under `<!-- NEW POSTS GO HERE (newest first) -->`, using the same `<a class="card">` markup.
6. In the root `index.html`, add a matching `<a class="fpost">` card at the **top** of `<div class="fblog__list">` and keep **only the 3 newest** `fpost` cards there (delete the oldest beyond 3). Leave the `<a class="fnext">` "Coming soon" card as the last item; never delete it (it hides itself once there are 3 posts).
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

## Quality rules (what Google actually rewards)

Google ranks pages on how helpful and original they are, not on who or what wrote them. Generic, interchangeable content is what fails. Every post must pass these:

- **One original angle.** Include at least one thing a generic article wouldn't: a specific setup Aftab would actually build, a worked example with realistic (clearly hypothetical) numbers, a mistake he sees often, or a clear opinion with the reason behind it. Write it in first person ("When I set this up for a service business, I…") only for general practice, never for invented client stories.
- **Specific over vague.** Name the actual setting, field, tool or step ("turn on the 'Higher intent' form type in Meta Lead Ads") instead of "optimize your forms".
- **No filler phrases.** Never use: "In today's fast-paced world", "in the digital age", "unlock", "unleash", "elevate", "game-changer", "dive in/deep dive", "navigate the landscape", "it's important to note", "in conclusion", "whether you're X or Y", "look no further", "seamless", "robust", "leverage" (as a verb), "supercharge".
- **No em dashes (—).** Use commas, periods or parentheses.
- **Vary rhythm.** Mix short and long sentences; don't start consecutive paragraphs the same way; avoid groups of exactly three adjectives in a row.
- **No repeated structure across posts.** Change the order of sections, the example industry and the opening style (a question, a scenario, a direct answer, a common myth) from post to post.
- **Plain text only.** Type normal characters; never paste invisible or special Unicode characters.
- **Fact-check claims.** Platform features, policies and settings must be current; if unsure, describe the principle rather than a specific button.

If every topic is checked, write 20 new topics in the same format and style at the end of `blog/topics.md` (new searches US small-business owners make about ads, leads, follow-up and AI automation, not duplicates), then publish the first one.

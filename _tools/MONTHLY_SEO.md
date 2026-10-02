# Monthly SEO & AI-visibility check

Runs once a month. Goal: keep the site technically clean, connect it to every profile that mentions Aftab, and keep content fresh. Follow the "Quality rules" in `blog/WRITING_GUIDE.md` for any text you write.

## 1. Find profiles and mentions, and connect them
- Use web search for: `"iamaftabahmed.com"`, `"Aftab Ahmed" AI automation`, and `"Aftab Ahmed"` on clutch.co, upcity.com, designrush.com, goodfirms.co, expertise.com, sortlist.com.
- For every profile that clearly belongs to Aftab (it links to iamaftabahmed.com or matches the name, services and email), add its URL to the `sameAs` lists in the homepage JSON-LD (both the `Person` and the `ProfessionalService` entries) and to the `Person` on `about/index.html`. Don't add duplicates. Never add a profile you can't confirm is his.
- Record what was found (and what wasn't) in the log below.

## 2. Technical check
- Run the Playwright check over every page in the sitemap: no horizontal scroll at 390px, one H1, valid JSON-LD, no broken internal links, no JS errors. Fix anything that fails.
- Confirm every published page is in `sitemap.xml` and every sitemap URL exists.
- Confirm `robots.txt`, `llms.txt` and `feed.xml` are consistent with the published pages (every blog post and industry page listed in llms.txt).

## 3. Refresh one older post
- Pick the oldest blog post not refreshed in the last 3 months (see log).
- Improve it: sharpen the answer under each heading, add one useful FAQ or example, update anything outdated on the platforms, and add internal links to newer posts and the matching industry page.
- Update its `dateModified` (JSON-LD), the sitemap lastmod, and note it in the log.

## 4. Finish
- Commit as `Monthly SEO check: <month YYYY>` and push to the working branch and `main` (`git push origin HEAD:main`).
- IndexNow ping (best effort) for any changed URLs, same format as in the writing guide.
- Reply with a short summary: profiles found/connected, issues fixed, post refreshed.

## Log
- 2026-10-02: set up. Directory profiles created by owner (Clutch, UpCity, DesignRush, GoodFirms, Expertise.com); not yet indexed by search, so not yet in sameAs.

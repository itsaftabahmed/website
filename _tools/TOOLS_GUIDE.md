# Automated free tools: how to launch one tool

One new free tool goes live each week at `/tools/<slug>/`. Tools bring search traffic ("X calculator", "X generator") and turn visitors into leads.

Audience: US small-business owners (dental, real estate, home services, med spa, law, insurance, local services). Voice: Aftab Ahmed, plain, direct, practical. Follow the "Quality rules" in `blog/WRITING_GUIDE.md` (no filler phrases, no em dashes, US spelling, no emojis).

## Queue (next tool first)

Format: `slug | Tool name | main search phrase | what it does`

- [ ] ai-receptionist-cost-calculator | AI receptionist cost calculator | ai receptionist cost calculator | Enter monthly calls and average call length; compares the bill on the four pricing models (flat, per minute, per call, bundle plus overage) with editable rates.
- [ ] speed-to-lead-calculator | Speed to lead calculator | speed to lead calculator | Enter leads per month, current reply time and close rate; shows how many leads wait too long and what faster replies could be worth.
- [ ] no-show-cost-calculator | No-show cost calculator | no show cost calculator | Enter appointments per week, no-show rate and average visit value; shows the monthly and yearly cost and the effect of cutting no-shows.
- [ ] google-ads-budget-calculator | Google Ads budget calculator | google ads budget calculator small business | Enter target new customers, close rate, conversion rate and cost per click; works back to the monthly budget and cost per customer.
- [ ] automation-quiz | What should you automate first? (quiz) | what to automate in my business | 7 short questions; scores the five problems (missed calls, slow follow-up, no-shows, ads, busywork) and recommends the first fix with a link to its solution page.
- [ ] missed-call-text-back-generator | Missed call text back message generator | missed call text back message examples | Pick industry and tone, enter business name; produces 5 ready-to-copy text messages.
- [ ] review-request-generator | Review request message generator | review request text message template | Pick industry and channel (SMS or email); produces polite review request messages with a copy button.
- [ ] lead-follow-up-sequence-builder | Lead follow-up sequence builder | lead follow up sequence template | Pick industry and lead source; builds a day-by-day text, email and call plan to copy or print.
- [ ] appointment-reminder-schedule-builder | Appointment reminder schedule builder | appointment reminder schedule | Pick appointment type and lead time; outputs a reminder timeline with sample wording.
- [ ] ad-break-even-calculator | Ad break-even calculator | break even cost per lead calculator | Enter job value, margin and close rate; shows the highest cost per lead and cost per click that still makes money.
- [ ] lead-value-calculator | Lead value calculator | how much is a lead worth calculator | Enter average job value, repeat visits and close rate; shows what one lead and one customer are worth.
- [ ] after-hours-coverage-checker | After-hours call coverage checker | after hours answering small business | Enter opening hours and when calls come in; shows the share of the week nobody answers and options to cover it.

When every tool is checked, add 8 new ideas in the same format (calculators, generators or checkers that US service-business owners search for, not duplicates), then build the first one.

## SEO and lead rules (apply to every tool)

The goal of each tool is search traffic that turns into leads. A tool that works but does not rank or capture leads is not done.

**Before building (10 minutes of research)**
- Read `_tools/KEYWORDS.md` for the priority phrases, then search the web for the tool's main phrase and 2 or 3 close variants. Note what the top results offer, what questions appear in "People also ask", and what is missing. Build the tool to answer the search better: more specific, faster to use, clearer result.
- Pick one main phrase and 3 to 5 supporting phrases (include "free", "for small business", and the question form such as "how to calculate ..."). Use the main phrase in the title, H1, first paragraph, one H2, the URL slug and the meta description. Use the supporting phrases in H2 questions and FAQ. No keyword stuffing.

**On the page**
- Answer first: one or two sentences under the H1 that say what the tool calculates and for whom, before the tool.
- The tool sits high on the page, usable without scrolling far on a phone.
- Include a "How to calculate <thing>" section with the formula in words and one worked example (hypothetical numbers, labelled). This is what search engines and AI answers quote.
- Include one small table of 3 or 4 example scenarios (for example small, medium and busy business), labelled as examples.
- Industry presets where they make sense (dental, HVAC, law, med spa, real estate and so on) and one short paragraph per 3 or 4 industries, each linking to its `/industries/` page. This lets the page match searches like "<tool> for dentists".
- FAQ: 4 or 5 real questions people search (use the "People also ask" questions found in research), each answered in 2 or 3 sentences, mirrored in `FAQPage` JSON-LD.
- Link 2 to 4 confirmed primary sources where a claim needs one, listed in a Sources box.
- Shareable results: read inputs from the URL (`?calls=300&mins=2`) and add a "Copy link to this result" button, so people can share and link to results.
- Page must stay fast: no libraries, no external requests, no layout shift.

**Internal links (hub and spoke)**
- Tool page links to: the matching `/solutions/` page, the matching service page, 1 or 2 blog posts and 1 or 2 other tools ("Related tools").
- Links into the tool: the tools hub, the homepage or footer via `chrome.py` where it fits, the most relevant solution page, and every blog post on the same topic (add a "Free tool" line near the top of those posts).
- Add one companion blog topic to the **top** of the unchecked list in `blog/topics.md` (for example "How to calculate what an AI receptionist will cost you"), so the next blog post targets the same keyword and links to the tool.

**Lead capture**
- Results are always free and visible. Never hide a result behind a form.
- Right under the result, one action that fits the result: "Email me this result and a plan" (`form[data-lead="tool-<slug>"]`, sends inputs and results in `leadExtra`).
- A second, softer step next to it: "Try the AI receptionist demo" or "Book a free call" (`../../#book`), chosen by what the result shows (for example a large loss leads to the booking button).
- Track use: push `{event:'tool_used', tool:'<slug>'}` to `dataLayer` the first time a visitor changes an input, and `{event:'tool_result_shared'}` on copy link.

**After launch**
- Every 4th run, also improve one existing tool against this checklist (start with `tools/missed-call-calculator/`) and note it in the log.

## Every run

1. `git fetch origin main && git merge origin/main` first.
2. Take the **first unchecked** tool in the queue and do the research in "SEO and lead rules" above.
3. Build `tools/<slug>/index.html`:
   - Copy the structure of `tools/missed-call-calculator/index.html` exactly: tracking codes at the top of `<head>` and the GTM `<noscript>` after `<body>` (unchanged), fonts, `../../blog/blog.css`, breadcrumb (`Home / Free tools / <name>`), hero, the tool, explanation text, FAQ, lead form, CTA. Header and footer come from `_tools/chrome.py` (run it at the end; never hand-edit them).
   - `<title>` under 60 characters with the search phrase; meta description 140 to 160 characters; canonical `https://iamaftabahmed.com/tools/<slug>/`; og and twitter tags; share image via `NODE_PATH=$(npm root -g) node _tools/og.js <slug>` if the script supports the page, otherwise reuse the calculator's image tags pattern.
   - JSON-LD: `WebApplication` (name, url, applicationCategory "BusinessApplication", offers price 0), `BreadcrumbList`, and `FAQPage` matching the on-page FAQ.
   - The tool itself: plain JavaScript in the page, no libraries, no external requests. It must work with the keyboard, on a 390px phone, and with sensible example values filled in. Results update as the visitor types.
   - **Honesty rules:** every default number is an example and is labelled as one ("Example values, change them to yours"). Show the formula in one line under the result. Never present an industry statistic unless it links to a confirmed primary source. No invented client results.
   - Under the tool: 500 to 800 useful words that answer the search (how to use it, how to calculate it, example scenarios table, what a good number looks like in ranges, industry notes), written as question headings, plus 4 or 5 FAQ questions. Follow every point in "SEO and lead rules".
   - Lead capture: a `form[data-lead="tool-<slug>"]` ("Send me a plan") like the calculator's, with `form.leadExtra` returning the visitor's inputs and results; load `../../blog/lead.js`.
   - Links: at least one link to the matching `/solutions/` page, one to a related blog post, one to another tool. Close with a CTA button to `../../#book`.
   - Use the site's icon style (inline SVG line icons or the 3D icons), never emojis.
4. Tools hub `tools/index.html`:
   - If it does not exist, create it (same page shell as `industries/index.html`): H1 "Free tools for service businesses", one rounded card per tool (name, one line, "Open the tool" link), newest first, including the missed call calculator and the AI receptionist demo (`../demo/`). Add `https://iamaftabahmed.com/tools/` to `sitemap.xml` and `llms.txt`. In `_tools/chrome.py` change the `LINKS` entry `('tools/missed-call-calculator/', 'Free tools')` to `('tools/', 'Free tools')`, and change the homepage nav "Free tools" link in `index.html` to `tools/`.
   - Add the new tool's card at the top of the hub.
5. Add the tool to `sitemap.xml` (lastmod today) and to the tools list in `llms.txt` (one line: name, URL, what it does).
6. Add one contextual link to the new tool from the most relevant existing page (a solution page via `_tools/gen_solutions.py`, a blog post, or the other calculator), so it is linked from somewhere besides the hub.
7. In `_tools/chrome.py` `news()`, point the first announcement item at the new tool (path, short label under 30 characters starting with "New free tool:" or the tool name, icon `calc`), then run `python3 _tools/chrome.py`.
8. Write a social draft at `_tools/social/<YYYY-MM-DD>-tool-<slug>.md` (LinkedIn version and a short X/Threads version, same rules as blog drafts).
9. Check the box in the queue above.
10. Test: `NODE_PATH=$(npm root -g) node .claude/skills/seo/scripts/site_check.js . https://iamaftabahmed.com` must report 0 issues. Also open the new page in headless Chromium at 1366px and 390px: no JS errors, no horizontal scroll, change two inputs and confirm the result changes, and confirm the lead form is wired. Keep screenshots out of the repo.
11. Commit as `Tool: <tool name>` and push to **both** the working branch and `main`. Retry pushes on network errors.
12. Best effort IndexNow ping for the new URL and `/tools/` (same command as in `blog/WRITING_GUIDE.md` step 8b). If the network blocks it, continue.

## Log

Add one line per run: date, tool, path.

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

## Every run

1. `git fetch origin main && git merge origin/main` first.
2. Take the **first unchecked** tool in the queue.
3. Build `tools/<slug>/index.html`:
   - Copy the structure of `tools/missed-call-calculator/index.html` exactly: tracking codes at the top of `<head>` and the GTM `<noscript>` after `<body>` (unchanged), fonts, `../../blog/blog.css`, breadcrumb (`Home / Free tools / <name>`), hero, the tool, explanation text, FAQ, lead form, CTA. Header and footer come from `_tools/chrome.py` (run it at the end; never hand-edit them).
   - `<title>` under 60 characters with the search phrase; meta description 140 to 160 characters; canonical `https://iamaftabahmed.com/tools/<slug>/`; og and twitter tags; share image via `NODE_PATH=$(npm root -g) node _tools/og.js <slug>` if the script supports the page, otherwise reuse the calculator's image tags pattern.
   - JSON-LD: `WebApplication` (name, url, applicationCategory "BusinessApplication", offers price 0), `BreadcrumbList`, and `FAQPage` matching the on-page FAQ.
   - The tool itself: plain JavaScript in the page, no libraries, no external requests. It must work with the keyboard, on a 390px phone, and with sensible example values filled in. Results update as the visitor types.
   - **Honesty rules:** every default number is an example and is labelled as one ("Example values, change them to yours"). Show the formula in one line under the result. Never present an industry statistic unless it links to a confirmed primary source. No invented client results.
   - Under the tool: 300 to 500 words that answer the search (how to use it, how the math works, what a good number looks like in ranges), written as question headings, plus 3 FAQ questions.
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

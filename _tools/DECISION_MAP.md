# Decision map (Neil Patel, rule 1: win the searches they never typed)

Google's AI Mode turns one question into several hidden searches. For each main buying question below, these are the questions a buyer needs answered before saying yes, and the page that answers each one. **GAP** means no page answers it yet: the blog, industry and tool routines should fill gaps first, one real page at a time (never thin pages made only for AI answers).

Update this file whenever a page is added. Paths are relative to the site root.

## 1. "How do I stop missing calls and losing customers?"
| Buyer sub-question | Answered on |
|---|---|
| How much are missed calls costing me? | `tools/missed-call-calculator/` |
| AI receptionist or answering service? | `blog/ai-receptionist-vs-answering-service/` |
| How much does an AI receptionist cost? | `blog/ai-receptionist-cost/`, `tools/ai-receptionist-cost-calculator/` |
| Per minute, flat rate or per call? | `blog/ai-receptionist-pricing-models/` |
| What is missed call text back and is it legal to text callers? | `blog/missed-call-text-back/` |
| Can I keep my phone number? | `solutions/missed-calls/` FAQ |
| What does it sound like to callers? | `demo/` |
| Is it HIPAA-safe for a practice? | `industries/dental/` FAQ (short). **GAP:** full guide "AI receptionist for dental offices: what it handles and what it shouldn't" (in topics queue) |
| How long does setup take and what do I need to provide? | **GAP** |

## 2. "How do I reply to leads faster and follow up properly?"
| Buyer sub-question | Answered on |
|---|---|
| Does reply speed really matter? | `blog/speed-to-lead/`, `tools/speed-to-lead-calculator/` |
| How do I measure my lead response time? | `blog/lead-response-time/` |
| What should the follow-up sequence look like? | `blog/automated-lead-follow-up/` |
| What do I actually say? (scripts) | `blog/real-estate-follow-up-scripts/` (real estate only). **GAP:** scripts for home services and practices |
| Do I need a new CRM? | `solutions/lead-follow-up/` FAQ |
| Is it legal to text leads automatically? | `solutions/lead-follow-up/` FAQ (short). **GAP:** plain-English consent and opt-out guide |

## 3. "How do I cut no-shows?"
| Buyer sub-question | Answered on |
|---|---|
| What do no-shows cost me? | **GAP** (no-show cost calculator is next in the tools queue) |
| How many reminders and when? | `solutions/no-shows/` FAQ, `blog/reduce-dental-no-shows/`, `blog/med-spa-no-shows/` |
| Should I take deposits? | `blog/med-spa-no-shows/` (med spa). **GAP:** deposits for other industries |
| What can reminders say without breaking privacy rules? | `solutions/no-shows/` FAQ |

## 4. "Why aren't my ads bringing customers?"
| Buyer sub-question | Answered on |
|---|---|
| Why do I get clicks but no calls? | `blog/facebook-ads-clicks-but-no-calls/` |
| How much should I spend? | `blog/facebook-ads-cost-small-business/`, `services/google-ads/` FAQ |
| Google Ads or Facebook Ads for my business? | `blog/facebook-ads-for-home-services/` (short table). **GAP:** full comparison post |
| Ads for my industry | `blog/facebook-ads-for-dentists/`, `blog/facebook-ads-for-real-estate-agents/`, `blog/facebook-ads-for-home-services/` |
| How do I know which leads from ads become customers? | **GAP:** guide to sending lead quality back to Google Ads and Meta (Neil Patel rule 5) |
| Should I turn on Google's AI Max? What can it change? | **GAP:** guide with a pre-launch page audit (Neil Patel rule 4) |

## 5. "What should I automate in my business?"
| Buyer sub-question | Answered on |
|---|---|
| What can be automated? | `solutions/busywork/` |
| Client onboarding (accounting) | `blog/accounting-client-onboarding-automation/` |
| Intake (law firms) | `blog/law-firm-client-intake/` |
| Where do I start? | **GAP** ("What should you automate first?" quiz is in the tools queue) |
| Freelancer or agency? What does it cost per month? | `solutions/*` pages ("Plans start from $297/month"). **GAP:** honest comparison page |

## How to use this
- Blog run: before writing, find the topic's row here; answer that sub-question fully and link to the rows next to it.
- New topics: turn a GAP into a line in `blog/topics.md` (or `_tools/TOOLS_GUIDE.md` for a tool). Remove the GAP mark once the page is live.

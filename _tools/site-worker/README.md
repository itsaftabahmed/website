# Site Worker (Cloudflare): AI demo + lead capture

Live at `https://site-api.itsaftabahmedhere.workers.dev` (Worker name `site-api`, owner's Cloudflare account). Set up 2026-11-12.

- `POST /demo`: AI receptionist demo replies (Workers AI). Used by `demo/demo.js`.
- `POST /lead`: saves a lead in D1 database `leads` and emails it to the owner. Used by `blog/lead.js`
  (homepage contact form, calculator "Send me a plan", homepage bot "Leave your email").
- `GET /leads?key=ADMIN_KEY` and `/leads.csv?key=ADMIN_KEY`: private lead list for the owner. Never put the key in the repo.

Bindings: `DB` (D1 `leads`), `AI` (Workers AI), `EMAIL` (Email Service). Variables: `NOTIFY_TO`, `FROM`, `ADMIN_KEY` (secret).

To update: change `worker.js` here, then the owner pastes it into Cloudflare (site-api → Edit code → Deploy).
Only requests from iamaftabahmed.com are accepted. Any new form: add `data-lead="<kind>"` to a `<form class="lead">` and load `blog/lead.js`.

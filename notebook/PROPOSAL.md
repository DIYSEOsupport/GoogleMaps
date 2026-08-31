# The Google Maps Fix — Product Proposal

*Synthesized from: `Biz Plan/business-plan.md`, `Biz Plan/onboarding-email.txt`, `Biz Plan/promo-posts.txt`, `Biz Plan/sales-page.html`, `interactive-playbook-v20-launch-ready.html`, `gbp-category-geo-keyword-blueprint-launch-ready.pdf`, `no-tech-quick-start-guide-launch-ready.pdf`, `outreach-sales-swipe-kit-launch-ready.pdf`, `seo-printable-companion-v8-launch-ready.pdf`.*

---

## 1. Executive Summary & Core Value Proposition

**Product:** "The 30-Minute Google Maps Fix" (a.k.a. "The Google Maps Fix") — a local visibility/ranking system for small businesses, delivered as a self-contained interactive HTML tool plus a set of companion PDF references.

**Core promise (sales page):** "In one afternoon, without hiring anyone, fix the concrete things Google actually weighs (profile completeness, categories, photos, reviews) and get a repeatable weekly/monthly habit so the fix sticks — with your own before/after numbers to prove it worked."

**Positioning:** Not a course, not an agency retainer. "A working tool — a single page you check boxes on." Direct competitive framing against SEO agencies: FAQ claims it replaces "what an agency charges $300–$1000/mo for on the basics," for a single-location business.

**Headline test variants (sales-page A/B set):**
1. "Why Your Competitor Outranks You on Google Maps (And the 30-Minute Fix)"
2. "The Google Business Profile Checklist Local Shops Wish They Had Sooner"
3. "Stop Losing Customers to the Shop Down the Street With a Better Google Listing"

**Headline metric used to open the pitch:** Google reports **42% more direction requests and 35% more website clicks** for listings with photos.

---

## 2. Target Audience & Customer Persona

**Single persona: the DIY Local Business Owner.** This product is sold directly to the business owner to fix and grow their own listing — there is no agency/reseller customer and no resale model. One document (`outreach-sales-swipe-kit-launch-ready.pdf`) contained agency-facing resale language ("high-margin digital marketing agencies and small business consultants," a "Confidential – Commercial License" mark, a productized "30-Minute Local Visibility Fix" resale offer) — **resolved**: rewritten as `revised-swipe-kit.html`, owner-facing only, agency/resale content replaced. See §3.

- Solo/family-run local business, 1–15 employees, no marketing staff, no agency budget.
- Revenue roughly $150K–$1.5M/yr. Fix budget: $0–$50 one-time, not a monthly retainer.
- Verticals: trades, food, personal-care, retail — plumber, lawn care, hair salon, boutique, diner, auto shop (playbook's Primary Category Cheat Sheet expands this to 10 named verticals; the geo-keyword blueprint PDF covers 55 niches).
- Explicitly non-technical: "You don't need a computer science degree" (no-tech quick-start guide); "If you can check a box and type into a Google Business Profile, you can do this" (sales-page FAQ).
- Identity-based framing acknowledged in-product: family-owned, small business, women-led, LGBTQ+-owned, veteran-led.
- Accommodates both storefront businesses and Service-Area Businesses (SAB — no public storefront, e.g. mobile trades).

---

## 3. Product Architecture & Interactive Features

The flagship deliverable is `interactive-playbook-v20-launch-ready.html` — a single self-contained HTML file, offline-capable, no install required. It supersedes the file named in the root `CLAUDE.md` (`the-30-minute-google-maps-fix.html`) as the current "launch-ready" build; that older file's known broken sync-panel issue has resurfaced here too and is now slated for removal (see §5).

### Table of contents / modules (in order)
1. **How To Use This Kit** — orientation.
2. **Score Your Listing (Pre-Audit)** — 10-question diagnostic quiz.
3. **Section 1: The 15-Minute Profile Audit** — includes Primary Category Cheat Sheet + 10-Photo High-Trust Shot List.
4. **Section 2: The Local Trust Signals List** — citations/directories (Chamber, Bing Places, Apple Maps, Nextdoor, etc.).
5. **Section 3: The Review Snowball System** — review-request workflow.
6. **Section 4: The Weekly Maintenance Tracker** — 20 min/week habit loop.
7. **Section 5: The "Am I Improving?" Ranking Log** — monthly rank tracking + trend chart.
8. **Plain-English Local SEO Glossary** — 10 term cards.

### Interactive features (calculators, checklists, audits)
- **Diagnostic Sieve**: scores the 10-item quiz (0–3 Critical / 4–7 Moderate / 8–10 Strong) and auto-dims sections the user has already mastered.
- **Sticky progress bar**: live % of all checklist items completed.
- Four section checklists (Profile Audit 14 items, Shot List 10 items, Trust Signals 9 items, Review Snowball 6 items).
- **QR code generator** for the business's Google review link, with live-updating SMS/email script placeholders.
- **Copy-to-clipboard** buttons on all outreach scripts and Google Post templates.
- Three **editable, auto-growing tracker tables**: Review Outreach Tracker, Weekly Maintenance Tracker, Ranking Log (color-coded rank cells).
- **Interactive SVG ranking-trend chart**, auto-drawn from the Ranking Log table, non-linear Y-axis, highlighted "Target Zone" (top-3).
- **localStorage autosave** of all checkbox/table state (`gmf-progress` key).
- ~~Peer-to-peer device pairing/sync (QR/short-code join flow)~~ — **removed** per §5 fix; no backend to support it, out of scope for this product.
- **Save Editable HTML** and **Download PDF Summary** export buttons.
- 5 **collapsible "What If" troubleshooting appendices**, one per core section.
- Two CSS-only features present in styling but **not wired to any markup/JS** — dead code, not user-facing: a "Sprint Mode" countdown-timer focus banner, and a segmented pill-toggle control group.

### Companion PDF modules (bundled/upsell reference material)
| PDF | Pages | Role |
|---|---|---|
| `gbp-category-geo-keyword-blueprint` | 4 | Superseded by `gbp-category-geo-keyword-blueprint.html` — same 55-niche table, styled to match v20, adds a live niche search filter |
| `no-tech-quick-start-guide` | 1 | Superseded by `no-tech-quick-start-guide.html` — same 3-habit content, styled to match v20, adds per-habit weekly checkboxes |
| `outreach-sales-swipe-kit` | 6 | Superseded by `revised-swipe-kit.html` (owner-facing rewrite, see below) |
| `seo-printable-companion` (v8) | 8 | Superseded by `seo-printable-companion.html` — citation matrix, review funnel, and all 3 logs styled to match v20, now checkable/fillable with autosave and an interactive ranking chart |

The Review Outreach Tracker copy ("Peak Delight / Gentle Nudge / Value Check-In") is duplicated near-verbatim between the interactive tool, the SEO Printable Companion, and the Outreach Swipe Kit — confirmed shared content module reused across three deliverables.

**Resolved:** `outreach-sales-swipe-kit-launch-ready.pdf` has been rewritten and rebuilt as `revised-swipe-kit.html`, styled to match v20 (Fraunces/Inter, gradient tables, coral upsell/script styling) with working copy-to-clipboard buttons on every script. Section 1 (review-request scripts) and Section 2 (social post swipe copy) keep the original content — already owner-facing. Section 3, the original agency-to-business-owner cold-sales sequence ("30-Minute Local Visibility Fix" resale pitch, "Confidential – Commercial License," booking-link close), is replaced with a **Local Partner Cross-Promotion Outreach** — a 3-touchpoint script for the business owner to build referral relationships with nearby non-competing businesses. `REVISED_SWIPE_KIT.md` (the plain-text draft) stays as the source-of-truth copy; the `.html` is the styled, shippable version.

[TODO: Need Decision] — `revised-swipe-kit.html` is a drafted replacement, not yet swapped into the actual product bundle in place of the original PDF. Confirm it before the PDF is retired/replaced in the shipped deliverable set.

---

## 4. Tier Breakdown & Pricing Strategy

**Resolved:** no live/human-delivered calls in this product. `business-plan.md:12` and `sales-page.html:65` both describe Tier 3 as "kit + 15-min live listing audit call" — that live-call offer is cut. Tier 3 is the $37 "Done-For-You" bundle (Premium Copywriting Swipe File + 50-Citation Rolodex) already shipped inside `interactive-playbook-v20-launch-ready.html`, since it needs no human time and matches what's actually live on Gumroad today. Priced low and kept simple per direction — no new build, no added maintenance.

**Resolved:** `business-plan.md` and `sales-page.html` rewritten — both now show $9/$27/$37 with no live-call language, and `sales-page.html` CTAs point at the actual product files for pre-Gumroad testing.

### Tier ladder (final)

| Tier | Price | Deliverable | Positioning |
|---|---|---|---|
| 1 | **$9** | `the-15-minute-profile-audit-checklist.html` — Section 1 only (Profile Audit checklist, Category Cheat Sheet, 10-Photo Shot List), static build, `localStorage` autosave, no trackers/quiz/PDF export | Impulse buy, top-of-funnel |
| 2 | **$27** | Full kit — checklist + tracker + score tool + PDF export (the interactive HTML tool) | Standalone anchor price; matches comparable Etsy digital templates ($15–$35) |
| 3 | **$37** | Kit + Done-For-You bundle: Premium Copywriting Swipe File + 50-Citation Rolodex | Upsell after $27 purchase, sold in-app via Gumroad (`itml37.gumroad.com/l/local-seo-bundle`), no live/human delivery. Low, simple price bump from $27 — no new build, no ongoing maintenance |

Four other in-app upsell boxes (Sections 1–4 of the interactive tool) point to the same Gumroad bundle without restating a price — treat these as pointing at the $37 Tier 3 above, not a separate SKU.

**Resolved:** Tier 1's "checklist only" had no matching artifact — `interactive-playbook-v20-launch-ready.html` is one monolithic file with no stripped-down build. Fixed by hand-authoring `the-15-minute-profile-audit-checklist.html`: Section 1 content only (Profile Audit checklist, Category Cheat Sheet, 10-Photo Shot List), static HTML with basic checkbox `localStorage` autosave, no score quiz, trackers, charts, QR/sync, or PDF export. Links to the $27 full kit as its own upgrade path.

Per direction, this stays a simple, one-time build with no ongoing maintenance commitment — no formal process to keep it in sync with Section 1 of the main tool. If Section 1's content changes later, updating this file is optional, not a standing obligation.

### Deliverable matrix (as currently supportable by existing files)

| | Tier 1 — $9 | Tier 2 — $27 | Tier 3 — $37 |
|---|---|---|---|
| Interactive HTML checklist tool | `the-15-minute-profile-audit-checklist.html` (Section 1 only — built, resolves prior gap) | Full tool | Full tool |
| Score Your Listing quiz | — | ✓ | ✓ |
| Weekly/Monthly trackers | — | ✓ | ✓ |
| PDF export | — | ✓ | ✓ |
| GBP Category & Geo-Keyword Blueprint (55 niches) | — | [TODO: Need Decision] | [TODO: Need Decision] |
| No-Tech Quick-Start Guide | — | [TODO: Need Decision] | [TODO: Need Decision] |
| SEO Printable Companion (50-citation matrix + fillable logs) | — | [TODO: Need Decision] | [TODO: Need Decision] |
| Outreach Swipe Kit (`revised-swipe-kit.html`, owner-facing) | — | [TODO: Need Decision] | [TODO: Need Decision] |
| Premium Copywriting Swipe File + 50-Citation Rolodex | — | — | ✓ |

[TODO: Need Decision] — None of the four companion PDFs are explicitly assigned to a tier anywhere in the source docs. The business plan's own bonus idea — "add a '50 business types' category cheat sheet pack as a bonus PDF to raise perceived value at $27+" — implies the Geo-Keyword Blueprint PDF was meant to be a Tier 2/3 bonus, but this is never confirmed as final.

### Bonus/upsell idea (business plan, unconfirmed as shipped)
"Add a '50 business types' category cheat sheet pack as a bonus PDF to raise perceived value at $27+" — this appears to already exist as the 55-niche Geo-Keyword Blueprint PDF, suggesting the idea *was* executed, just never formally assigned to a tier in writing.

---

## 5. Delivery Mechanism & Tech Stack

- **Format:** Single self-contained `.html` file. No build step, no backend, no external dependencies at delivery time (per root `CLAUDE.md` and `business-plan.md`). Current flagship file is ~141KB (`interactive-playbook-v20-launch-ready.html`).
- **Access:** Direct download link via the sales platform (Gumroad/LemonSqueezy handle delivery natively) — not an email attachment.
- **Usage:** Opens in any browser ("double-click it, or drag into a Chrome tab"), works fully offline once open.
- **State persistence:** Client-side `localStorage` only (`gmf-progress` key), wrapped in a `SafeStorage` helper to fail gracefully in `file://` or private-browsing contexts where `localStorage` may be blocked.
- **Export paths:** "Save Editable HTML" (downloads a copy of the tool with state baked in) and "Download PDF Summary" (client-side PDF generation via jsPDF).
- **Third-party client libraries used:** a QR-code generator (`qrcode-generator`) and `jsPDF`, both loaded client-side.

### Known technical issue — fixed (high priority)
`business-plan.md` flags an explicit pre-launch blocker: an older version of the product (`the-30-minute-google-maps-fix.html`, per root `CLAUDE.md`) loads a missing `gmf-core.js` and calls `fetch('/api/sync/' + code)` for a device-pairing sync feature with **no backend to support it**. The instruction was to "strip the device-sync/pairing panel... or replace with a note 'sync coming in a future update.'"

The current flagship file (`interactive-playbook-v20-launch-ready.html`) still ships a working-looking "Pair This Device" peer-to-peer sync flow (`pushToServer()`, `pullFromServer()`, `joinWithCode()`) with no confirmed backend — the same dead-backend problem, resurfaced in the new file. There is no product need for cross-device sync in a $9–$37 static checklist tool, and it contradicts the "no backend, self-contained file" delivery promise (§5, root `CLAUDE.md`, `business-plan.md`).

**Decision: strip the sync/pairing panel entirely** — no stub, no "coming in a future update" note. `localStorage` autosave + the "Save Editable HTML" export already cover the one real use case (moving progress to a new session), and matches `onboarding-email.txt`'s existing offline-only framing ("It works fully offline once open... Your progress auto-saves to this device") with no rewrite needed there.

[TODO: Need Decision] — Confirm with whoever built `interactive-playbook-v20-launch-ready.html` that removing `pushToServer()`/`pullFromServer()`/`joinWithCode()` and the "Pair This Device" UI doesn't break anything else wired to that state object.

---

## 6. Distribution & Marketing Strategy

### Sales channels (from `business-plan.md`)
| Platform | Pros | Cons |
|---|---|---|
| Gumroad (recommended start) | Zero setup, instant checkout, built-in discounts | 10% + payment fee |
| Etsy Digital | Huge search traffic for small-business templates | $0.20 listing + 6.5% fee, DIY/craft-skewed audience |
| LemonSqueezy | Auto tax/VAT handling | Smaller organic discovery |
| Shopify page | Full control, no marketplace cut | Must supply own traffic, monthly fee |

Recommendation: launch on Gumroad first (no monthly fee, fastest), add Etsy once copy is proven. The in-app upsell links already point to a live Gumroad URL (`itml37.gumroad.com/l/local-seo-bundle`), so Gumroad is effectively already the operative channel.

### Organic/free channels
r/smallbusiness (self-promo threads only), Facebook local-business groups, local Chamber of Commerce newsletter, Nextdoor Business posts, personalized cold email.

### Paid channel guidance
Margin is thin at $27 for cold traffic. Test Meta ads at $10/day for 5–7 days ($50–70 total) before scaling; prove organic conversion first. Google Search ads not recommended at this budget (cheaper/more precise targeting on Meta).

### Ready-made promotional copy (already drafted, `promo-posts.txt`)
- Facebook local-group post, Reddit self-promo post, and a personalized cold-email template all exist and are launch-ready.
- **Contradiction found:** the Facebook post calls the product "**free-ish**" with no price stated, while the cold-email template in the same file explicitly states "**$27, no subscription**." [TODO: Need Decision] — align the Facebook post's framing with the real $27 price (or clarify if "free-ish" was intentional soft-launch bait-and-price copy).
- **Unverified proof claim:** both the sales page's "Proof" callout and the Reddit post use the claim "page 3 to top 3 map results in about 6 weeks." The sales page explicitly labels this a **placeholder** ("swap in a real customer quote once you have one"), while the Reddit post presents it as the author's own first-person, already-happened result. [TODO: Need Decision] — confirm whether this is a real result that can be used as a verified testimonial, or must be removed/softened until a real customer quote exists, since using it in live promo copy as-is risks presenting a placeholder as fact.

### 14-Day launch sequence (from `business-plan.md`)
Days 1–2: fix sync-panel issue, finalize copy, set up Gumroad at $27, test buyer flow.
Days 3–4: post in 1–2 Facebook groups, email Chamber contact.
Days 5–6: send 10–15 personalized cold emails, track replies.
Day 7: review week-1 numbers, adjust headline/price if conversion is near zero.
Days 8–9: list on Etsy Digital.
Days 10–11: post in allowed Reddit thread, Nextdoor Business.
Days 12–13: if organic conversion proves out, start $10/day Meta ad test.
Day 14: full review — sales by channel, best-performing copy, decide on $47 tier next.

### Onboarding (post-purchase, `onboarding-email.txt`)
Subject: "Your Google Maps Fix — start here." Instructs the buyer to open the file in-browser, complete Section 1 today (15 min, highest-impact section), and explains the Save Editable Copy / Download PDF buttons. Reply-to-email is the support channel — no other support infrastructure is defined.

---

## 7. Ongoing Maintenance & Google Algorithm Update Plan

**No document in the source set addressed this before the critique pass.** No content-refresh cadence, no versioning plan, no process for reacting to Google Business Profile ranking-factor changes existed anywhere in the source material.

**Fixed (high priority): quarterly review, no subscription.** A one-time purchase stays sustainable without turning this into a retainer product (which would contradict the core sales pitch — "$0–$50 one-time, not a monthly retainer," "no agency required"). Plan:
- **Owner:** whoever maintains the product (single owner, no team needed at this scale).
- **Cadence:** quarterly (4x/year) review of the two things that actually go stale:
  - The 50-site citation matrix (now `seo-printable-companion.html`) — check directory URLs still resolve, spot-check DA scores.
  - The 55-niche GBP category table (now `gbp-category-geo-keyword-blueprint.html`) — check for renamed/merged Google categories.
- **Distribution:** re-issue the updated file(s) as a free re-download to existing buyers via the sales platform's update mechanism (Gumroad supports pushing file updates to past purchasers at no extra cost) — not a new purchase, not a subscription.
- **Trust signal:** stamp a "Content last verified: [date]" line into the product itself (interactive tool footer + each PDF footer) so buyers can see freshness without asking. Doubles as the versioning practice implied but never formalized by the existing "v8"/"v20" filename suffixes.
- **Ranking-factor claims** (the 42%/35% photo-engagement stat, the BrightLocal citation) get checked at the same quarterly pass — if a source goes dead or outdated, soften the claim rather than leave a now-false stat live.

[TODO: Need Decision] — What happens if the Gumroad-hosted "Premium Growth Bundle" upsell page changes URL or is discontinued — the in-app upsell links are hardcoded into a static HTML file already in buyers' hands with no update mechanism. Low priority relative to the fixes above, but worth a stable-URL policy (e.g. never change the Gumroad slug) rather than a technical fix.

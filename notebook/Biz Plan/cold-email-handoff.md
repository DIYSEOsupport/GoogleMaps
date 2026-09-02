# Lead Research & Cold Email Campaign — Handoff Notes

## Next task: research a new batch of leads

The prior 100-lead batch is fully sent (see status below). The next session should **research and qualify a new batch of leads** using these two methods, then send cold emails to them the same way as before.

### Where to look for leads (all sourcing channels)
- **Google Maps search** — the method used for all 100 leads so far (see qualification criteria below).
- **Craigslist** — not yet used this campaign, user asked to add as a lead source.
- **Angie's List** — not yet used this campaign, user asked to add as a lead source.

### Google Maps qualification method (for the new batch)
1. Skip the top-3 Local Pack results. Click "More businesses," scroll to page 2–4 (roughly positions #15–#40).
2. Target the **"sweet spot" lead**: 4.5+ star rating, 20+ reviews, but still buried on page 3 or later — established, well-reviewed businesses with bad Maps visibility.
3. Prioritize leads showing any of these weak-listing signals:
   - **No website link** on their Maps listing (phone number present, but no "Website" button).
   - **Zero or low photos** — only the generic Street View image, no interior/team photos.
   - **No recent reviews** — last review 8+ months old.
   - **"Keyword stuffing" opportunity** — business uses its bare legal name (e.g. "J&J Enterprises") while competitors use optimized names (e.g. "J&J Roofing & Repair"); this is a fixable-with-our-checklist signal.

### Workflow for the new batch
1. Research leads via the channels/criteria above (target similar batch size to prior rounds, e.g. 15–50).
2. Log each lead into the tracker (see below) with source link.
3. Draft/send using the existing `Biz Plan/emails/cold-email-template.html` — do not restructure the body copy, only personalize business name/niche per lead as done previously.
4. Send one at a time (not parallel-blasted), label each real send with the Gmail "Cold Emails" label.
5. Periodically check `diyseo.support@gmail.com` for bounce notifications and update the tracker.

## Status as of 2026-09-02 (prior batch)

**Sent:** 100/100 real cold emails sent, ~95 delivered (5 confirmed bounces).
**Bounced leads (don't resend):** Ultimate Lawn Services, JVA Home Services, Hair For You Salon, Thai Gourmet, The Moving Company LLC.
**Sending account:** `diyseo.support@gmail.com`. Personal test account: `isthismylife37@gmail.com`.
**Product:** $9 "Get Found on Google Maps" Google Business Profile checklist. Link: `https://diyseosupport.gumroad.com/l/zodcm`.

## Tracker and logs — where all lead data lives

**Durable source of truth (use this):** the published HTML tracker artifact — variant, business, niche, email, status, sent date, source link, all 100 leads:
https://claude.ai/code/artifact/ae9eb51d-6b3c-4890-8c93-b5c617665f58
Add new-batch leads to this same tracker (read it back with the Artifact tool, edit, republish).

**Stale backup, don't trust as current:** a plain CSV/Sheets copy from mid-campaign:
https://docs.google.com/spreadsheets/d/1xzvJ-NjXixu1_AFHP0XJ1JyYl4cWB9lE7N5AW_ar48E/edit

**Raw working logs (likely gone — session-local scratch, not part of this repo):** earlier in this campaign, lead research was staged in CSV files (`cold-email-log.csv`, `cold-email-log2.csv`, `cold-email-log3.csv`) inside a previous session's scratchpad directory (a `/tmp/.../scratchpad/` path tied to a different, now-closed session). Scratchpad directories are cleaned up between sessions, so treat these as very likely no longer accessible — the artifact tracker above is the only durable record. If a future session can somehow still reach them, they hold the original raw research notes (legend, subject-line variants, per-lead opener text) behind what's already been folded into the tracker.

## Email template

`Biz Plan/emails/cold-email-template.html` — canonical HTML email template (navy/gold DIYSEO branding, "What's Inside" 6-step card, CTA button, promo badge). Body copy is approved as-is; only edit specific requested elements.

Promo badge (added 2026-09-02, placed after the CTA button, before the footer):
- `Biz Plan/promo-code-findme.png` (static, 320x280) and `Biz Plan/promo-code-findme.gif` (animated pulse on CTA, same size) — inline `cid:promo-badge` reference in the template.
- Rendered natively at 320x280 with DejaVu Sans Bold — no resize/downscale step (that caused blur). Template `<img width>` must match the file's actual pixel width exactly or email clients rescale it and it blurs again.
- Design source of truth (interactive, editable): https://claude.ai/code/artifact/86a7d864-8f66-4999-862a-893889b41f2c — re-extract from this artifact if editing again in a future session (local scratchpad paths don't persist).
- Font: system Arial/Helvetica (canvas) matched by DejaVu Sans Bold (raster export). Don't reintroduce Google Fonts (Fraunces/Inter) — caused a mismatch between the interactive preview and the exported image.

## Standing instructions

- Space out real sends one at a time; label every real send "Cold Emails" in Gmail.
- Add source/website or Facebook link for new leads going forward.
- Test any email design change to `isthismylife37@gmail.com` first — never send a design/copy change live to a real lead without an approved test pass.
- Don't restructure the email template's body copy when asked to add a small element — only touch what's asked.

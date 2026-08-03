---
title: AI Maintenance Guide
type: meta
---

# AI Maintenance Guide

Rules for any AI assistant editing this vault. They exist so the vault stays
trustworthy and readable by a human who didn't watch the edit happen.

## 1. One article per thing

Before creating a note, **search for it**. If an article for the entity exists,
edit it. If the name differs, add an alias to the existing note — do not create a
second article. Duplicate articles are the primary failure mode of this vault.

## 2. Lead sentence, always

Every note opens with one plain sentence defining the thing, before any heading.
If you can't write that sentence, you don't understand the note well enough to
edit it.

## 3. Current state vs. log

Article bodies state what is **true now**. Superseded facts move to `## Log` with a
date, or into `Logs/` if the volume is high. Never leave two contradictory claims
in a body.

## 4. Links, not frontmatter relationship fields

Use inline `[[wikilinks]]`. Do **not** maintain parallel `related_*` frontmatter
lists — the same relationship recorded twice by hand drifts, and drifting Dataview
tables are worse than no tables because they fail silently. Obsidian's backlinks
pane already gives you the reverse direction for free.

Frontmatter carries only what a query actually needs: `title`, `aliases`, `type`,
`tags`, and `domain`/`date` on logs.

## 5. Don't hand-maintain `updated:`

Dataview reads `file.mtime`. A hand-written `updated:` field is one more thing to
forget, and when it's wrong the staleness report lies. It has been removed from
the templates deliberately.

## 6. New note placement

- Any entity — device, service, concept, howto → `Notes/` (flat, no subfolders)
- Anything dated and repeating → `Logs/`, with `domain:` set
- A person → `People/`
- A new area entry point → `MOCs/`

## 7. Never silently delete from `Notes/`

Move to `Archive/` with a dated line saying why. The one exception is `Inbox/`,
where deletion after mining is the intended workflow.

## 8. Log every session

Append a dated line to `_AI/Changelog.md`: what changed, why. This is how the
human audits without re-reading every file.

## 9. Ask before restructuring

Renaming folders, merging articles, or changing the frontmatter schema affects
everything. Propose, get a yes, then do it.

## 10. Write for a human

Short, plain, no filler. Bullets over paragraphs. No hedging language in an
article body — if something is uncertain, say so explicitly and date it.

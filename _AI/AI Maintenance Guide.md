---
title: AI Maintenance Guide
type: meta
---

# AI Maintenance Guide

> **The rules moved.** Structure, frontmatter schema, writing conventions, the import
> workflow, and sensitive-material handling are now in **[[VAULT]]**, the canonical spec.
> This file used to hold its own copy of them, which is exactly how the vault ended up with
> two documents describing `Library/` in opposite terms. One copy now.

Start with [[VAULT]] — particularly §3 (frontmatter), §4 (writing conventions), and §7
(maintenance). [[CLAUDE]] is the short version, loaded automatically by agent sessions.

## What's specific to working here as an assistant

These are behavioural, not structural, which is why they aren't in the spec.

### Write for a human who didn't watch the edit happen
Everything you change should be readable and checkable by Mac later, cold. That's the whole
reason the vault is plain markdown.

### Propose before you restructure
Renaming folders, merging articles, changing the schema, or bulk-editing more than a handful
of files: propose, get a yes, then act ([[VAULT]] §7.3). Applying a spec rule to files that
predate it is still a bulk edit — say what you're about to touch and how many.

### Log accurately, including your own mistakes
Append a dated entry to [[Changelog]] every session ([[VAULT]] §7.2). If a previous entry
was wrong, correct it in place rather than quietly moving on — the log is the audit
mechanism, and a log that overstates what happened is worse than no log. There is already
one correction of this kind in there, from 2026-07-31.

### Verify before reporting
Two bugs shipped here by assuming rather than checking:

- a link scanner that stripped fenced code blocks but not inline code spans, which reported
  four broken links that were never broken;
- a changelog entry claiming `related_*` fields had been removed when 22 files still had
  them.

Check the files. When something is uncertain, say so and say why, rather than asserting it
and being wrong later.

### Don't destroy information while applying a rule
Before stripping a field or reformatting, check whether it holds anything not recorded
elsewhere. When `related_*` was removed, four notes had relationships that existed *only* in
frontmatter; those had to be written into the bodies first or they'd have been lost silently.

### Preserve the two-layer distinction
`Notes/` is authoritative and editable. `Library/` is verbatim and append-only. Never edit a
transcript body, never delete one, never cite one as fact ([[VAULT]] §1, §5).

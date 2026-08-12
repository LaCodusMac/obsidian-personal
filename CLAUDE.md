# CLAUDE.md

This is a personal Obsidian vault. **Read `VAULT.md` before editing anything in it.** It is
the canonical spec — structure, frontmatter schema, writing conventions, import workflow,
and sensitive-material handling. If another document contradicts it, `VAULT.md` wins.

## The short version

**Two layers, and confusing them is the main way to damage this vault:**

- `Notes/`, `People/`, `MOCs/`, `Logs/` — curated articles. Authoritative. State what is
  **true now**. Edit these freely under the rules in `VAULT.md`.
- `Library/` — 584 verbatim AI conversation transcripts. **Append-only. Never edit a body,
  never delete one, never cite one as fact.** They record what was *said*, not what is true.

Promote from `Library/` into an article when something is worth stating as settled fact. The
transcript stays.

## Before you write

1. **Search first.** One article per thing, forever. If it exists, edit it; if the name
   differs, add an `aliases:` entry rather than creating a second article.
2. **Search `Library/` before researching from scratch.** 2023–2026 of prior context is
   already there. Verify against the article — if they disagree, the article wins and the
   disagreement is worth mentioning.
3. **Lead sentence, not a heading.** Every note opens with one plain sentence saying what the
   thing is, before any `#`.

## Hard rules

- **Never delete.** Move to `Archive/` with a dated reason. No exceptions.
- **No `related_*` or `updated:` frontmatter.** Both banned — use `[[wikilinks]]` and
  `file.mtime`. See `VAULT.md` §3.
- **Filenames use spaces, not underscores** — links resolve by filename, so `Foo_Bar.md`
  silently breaks `[[Foo Bar]]`.
- **Sensitive transcripts must be named `*.private.md`.** That suffix is what keeps them out
  of git. A sensitive file without it looks completely normal and gets committed.
- **Ask before restructuring.** Renaming folders, merging articles, or changing the schema
  affects everything. Propose, get a yes, then act.
- **Log every session** to `_AI/Changelog.md` — accurately. That log is how the human audits
  without re-reading every file; a false entry is worse than none.

## Tooling

```bash
python3 _AI/regenerate_index.py   # rebuild Library indexes; checks sensitive-file integrity
```

Run it after any `Library/` import. Never hand-edit `Conversation Index.md` or
`Private Index.private.md`.

## Verify, don't assume

Two bugs got shipped here by assuming instead of checking: a link scanner that ignored
inline-code spans reported four false breakages, and a changelog entry claimed a cleanup that
never ran. Check your work against the files before reporting it done, and say plainly when
something is uncertain.

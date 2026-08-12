# Personal Vault

A personal wiki (`Notes/`) plus a permanent AI-conversation corpus (`Library/`).

> **The spec is [[VAULT]].** Structure, frontmatter, writing conventions, imports, and
> sensitive-material handling all live there. This file is setup only — if it and `VAULT.md`
> ever disagree, `VAULT.md` is right.

## Setup

**1. Install a query engine.** `Home.md` is raw query blocks without one. Two options:

- **Dataview** (Settings → Community Plugins → Browse). All existing queries are written
  for it. Third-party, so it carries abandonment risk.
- **Bases** — already built in (`bases: true` in your core plugins). No third-party
  dependency. Most queries here are simple enough to translate, but Home's orphan check
  (`length(file.inlinks) = 0`) may have no equivalent — verify that one before committing.

Undecided. Everything else in the vault works either way.

**2. Leave `Library/` searchable.** An earlier version of this file told you to add it to
Settings → Files & Links → Excluded files. Don't — that was written when the folder was
disposable quarantine. A memory store you can't search isn't one.

The original concern was real: 584 transcripts do crowd the quick switcher when you're
reaching for an article. If that gets annoying, scope your searches (`path:Notes`) rather
than excluding the folder.

**3. Use aliases.** On by default. `aliases:` in frontmatter is the redirect mechanism and
the highest-value habit here — see `Notes/Synology NAS.md`.

**4. Templater** (optional) — one-click new notes from `Templates/`.

## The three rules that keep this from rotting

1. **Search before you create.** One article per thing, forever. If it exists, edit it; add
   an alias instead of a second article.
2. **Lead sentence first.** Every note opens with one plain line saying what the thing is,
   before any heading.
3. **Promote from `Library/`, don't drain it.** When a conversation contains something worth
   stating as fact, write it into the relevant article in your own words. The transcript
   stays. There is no review queue and no backlog to feel guilty about.

## Working with an AI assistant

`CLAUDE.md` is loaded automatically by Claude Code and Cowork sessions pointed at this
folder. It points to `VAULT.md` and summarizes the hard rules. `_AI/Changelog.md` is the
audit log of what an assistant has changed.

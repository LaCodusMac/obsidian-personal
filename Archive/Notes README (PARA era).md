> **Archived 2026-08-03.** Superseded by `VAULT.md` and the root `README.md`.
> Kept as a record of the original PARA-era design — it describes `01-Projects/`,
> `02-People/`, `03-Areas/`, `04-Resources/`, `05-Archive/`, none of which exist,
> and the `related_*` linking model, which is now banned. Do not follow it.

# Jacob Vault — Setup & Concept

This is a starter Obsidian vault built to hold **all of your main projects** and link them together — like a personal wiki where every project, person, and idea is connected.

## 1. Open it in Obsidian
- Unzip this folder somewhere permanent (not Downloads).
- Open Obsidian → "Open folder as vault" → select this folder.

## 2. Install two free community plugins (Settings → Community Plugins → Browse)
- **Dataview** — powers the auto-generated tables on the Home page (project lists, recent updates). Without it, Home.md will show raw query blocks instead of tables.
- **Templater** (optional but recommended) — lets you create a new project from `Templates/Project Template.md` with one click instead of copy-pasting.

## 3. Folder structure
```
Home.md            ← start here every time
01-Projects/        ← one note per project
02-People/           ← collaborators, clients, stakeholders
03-Areas/            ← ongoing responsibilities that aren't "projects" (e.g. Finances, Health)
04-Resources/        ← reference material, links, notes that support projects
05-Archive/          ← finished/paused projects, moved here but never deleted
Templates/           ← reusable note skeletons
_AI/                 ← rules and logs for how an AI assistant maintains this vault
```

## 4. How "AI-controlled" works in practice
Obsidian vaults are just folders of plain markdown files, so any AI with file access can read and edit them directly. A few ways to run this:

- **Claude Desktop / Cowork**, pointed at this folder — you ask it to add a project, update a status, or reorganize, and it edits the actual files.
- **Claude Code**, if you're comfortable with a terminal — same idea, more scriptable (e.g. a scheduled job that reviews recent notes and updates Home.md).
- **Manual + Claude in chat** — you paste updates into a conversation, Claude drafts the note, you paste it in. Slower, but zero setup.

Whichever you use, point it at `_AI/AI Maintenance Guide.md` first — that file is the "constitution" for how it should behave in this vault (naming rules, what to log, what never to delete).

## 5. Everything links, nothing is orphaned
Every project note has a `related_projects`, `related_people`, and `related_areas` field in its frontmatter, plus inline `[[wikilinks]]` in the body. Home.md's Dataview tables surface anything that's gone stale (not updated in a while) so the web doesn't quietly rot.

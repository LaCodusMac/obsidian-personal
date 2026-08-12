---
title: "Vault Git Reconciliation"
aliases: [git reconciliation, vault sync repair, uncommitted vault]
type: runbook
status: not-started
priority: high
tags: [runbook, obsidian, git, backups]
---

Procedure for getting this vault's eight days of uncommitted work safely into git, without losing anything and without clobbering whatever the P3 Mini may have pushed. Written 2026-08-11 after discovering the vault on `jacobs-macbook-air` had exactly one commit.

## The situation, as measured

On `jacobs-macbook-air`, `/Users/jacobmcnamara/obsidian-personal`:

| | |
|---|---|
| Commits, total | **1** — `916aa22 "Initial vault"`, 2026-08-03 |
| Untracked files | 616 |
| Modified files | 626 |
| Deleted (unstaged) | 598 |
| `origin/main` (fetched 2026-08-11) | `23ca9ab` — one commit ahead, fast-forward, adds only `.gitignore` |

The single commit contains 629 files and these top-level entries: `Home.md`, `Inbox/`, `MOCs/`, `Notes/`, `README.md`, `Templates/`, `_AI/`. That is the **pre-restructure** vault. Everything from the 2026-08-03 and 2026-08-08 sessions is uncommitted: `Library/`, `VAULT.md`, `CLAUDE.md`, `People/`, `Archive/`, `Logs/`, and every rename.

## Nothing is lost — verified, not assumed

The 598 deletions look alarming and are not. They were checked file by file:

- **588** are `Inbox/*` — **586 of them match a file of the same name now in `Library/`**. That's the Inbox→Library move; git will detect these as renames once staged.
- The **2** unmatched are `Inbox/README.md` and `Inbox/Staging_README.md` — staging docs deliberately superseded by [[VAULT]] and `About the Library`.
- The remaining **10** are the documented 2026-08-03 moves: underscore→space renames, `Mom`/`Nana` into `People/`, `Home_old` into `Archive/`.

`Library/`'s 649 files account for cleanly: 584 transcripts + `Conversation Index` + `Import Schema` (both moved from Inbox) + `About the Library` (written fresh) + 62 `.private.md`.

## The one genuinely alarming finding

**The 62 `.private.md` transcripts exist only on this laptop, and by design git will never back them up.**

The `.gitignore` wildcard that keeps them out of the repo is working correctly — verified: 62 private files on disk, 0 tracked, 0 stageable. That is the intended behaviour ([[VAULT]] §6). But it means the sensitive-material safety mechanism and the backup mechanism are the same mechanism, pointed in opposite directions. Committing everything below will **not** protect these 62 files. They need a non-git backup path — restic to [[Synology NAS]] is the obvious one, and it's already the top item in [[Backups]].

Note also that none of the 62 correspond to a deleted `Inbox/` filename, meaning they entered `Library/` by a different route than the bulk import. Worth understanding before designing their backup.

## Secondary finding — which turned out to be the primary one

`.gitignore` is **itself untracked**, and the version that *is* on the remote is a weaker one with no private-file rule at all. See step 2. This is worse than it first appeared: it is not merely "absent from a fresh clone," it is "actively replaced by a version that protects nothing."

Also worth noting: the local rule is `Library/*.private.md`, **path-anchored to `Library/`**. All 62 private files currently live there, so it works — verified 2026-08-11, zero private files outside `Library/`. But a sensitive note saved anywhere else would not be caught. An unanchored `*.private.md` would be more robust. That is a change to a load-bearing rule described in [[VAULT]] §6, so it is **proposed here, not applied** — it needs a deliberate yes.

## Procedure

### 0. Back up outside git first — non-negotiable

Every step below is a git operation on the only copy of eight days' work. Take a plain copy first.

```bash
cp -a ~/obsidian-personal ~/obsidian-personal.backup-$(date +%F)
```

Do not skip this because the later steps look safe. The cost is 12 MB and thirty seconds.

### 1. Remote state — determined 2026-08-11

Fetched. The answer is better than feared, with one sharp edge:

```
commits remote has, we don't:  1     (23ca9ab)
commits we have, remote doesn't: 0
HEAD is an ancestor of origin/main → fast-forward, NOT a divergence
```

The one commit is `auto-sync: 2026-08-03 21:05:09`, and it adds exactly one file: `.gitignore`.

**So there is no divergence to reconcile.** No parallel restructure happened on the P3. The MacBook is simply one commit behind, with a very dirty working tree, and it holds the only copy of the `Library/` corpus.

### ⚠️ 2. The sharp edge — read before pulling

**The remote's `.gitignore` does not exclude private files.** It is 11 lines of Obsidian / macOS / iCloud rules and contains no `private` pattern at all. The local untracked `.gitignore` — the one with the `Library/*.private.md` line and the reasoning comments — was **never committed**, which is why the auto-sync pushed the weaker version.

Consequences, in order of severity:

1. **The P3's auto-sync timer is armed with a `.gitignore` that protects nothing.** If that machine ever receives the `Library/` corpus and the hourly timer fires, it commits and pushes all 62 sensitive transcripts to GitHub. Per [[VAULT]] §6, deleting them afterwards does not remove them from history, and repo visibility can change retroactively. **This is the single most consequential finding in this runbook.**
2. A plain `git pull` will **refuse** — "untracked working tree file `.gitignore` would be overwritten by merge." That refusal is protective. The danger is in resolving it carelessly: deleting the local file, or forcing the pull, silently drops the private exclusion, and the next `git add -A` stages all 62.

**Neither version is a superset of the other**, so this needs a union, not a pick:

| Rule | Local | Remote |
|---|---|---|
| `Library/*.private.md` | ✅ | ❌ |
| `.obsidian/workspace.json` / `-mobile.json` | ✅ | ✅ |
| `.trash/`, `.DS_Store` | ✅ | ✅ |
| `.obsidian/plugins/` | ❌ | ✅ |
| `*.icloud` | ❌ | ✅ |

`*.icloud` is worth keeping given this vault's history with iCloud Drive — see [[Obsidian Brain]]. `.obsidian/plugins/` is a real decision: ignoring it keeps the repo small; committing it makes the vault reproducible on a new machine but adds megabytes of third-party JavaScript and a conflict surface. Recommend keeping it ignored.

### 3. The procedure

```bash
# a. safety copy first (see step 0)

# b. write the union .gitignore — keep the local file's comment block,
#    then add the two rules only the remote had:
printf '\n# ── From remote auto-sync ──────────────────────────────────────────────\n.obsidian/plugins/\n*.icloud\n' >> .gitignore

# c. commit .gitignore BEFORE anything else touches the corpus
git add .gitignore
git commit -m "Add .gitignore with private-file exclusion (union of local + remote)"

# d. now the pull is safe — .gitignore is tracked, so the merge resolves normally
git pull --no-rebase origin main
#    if it conflicts on .gitignore, keep ours: git checkout --ours .gitignore && git add .gitignore

# e. THE LOAD-BEARING CHECK — must return nothing at all
git add -A
git status --porcelain -uall | grep -i private
```

**If step (e) prints anything, stop.** Do not commit, do not push. A sensitive transcript is one command from entering a remote repository permanently.

```bash
# f. only if (e) was silent
git commit -m "Vault restructure: Inbox -> Library, VAULT.md spec, People/Archive/Logs"
git push origin main
```

### 4. Then fix the P3 before its timer runs again

Once the corpus is on the remote, the P3 will pull it on its next sync. Confirm **before that happens** that the P3's working copy has the corrected `.gitignore` — it will, once it pulls, but verify rather than assume:

```bash
# on llamaswithhats
cd <vault path> && git pull && grep private .gitignore
find . -name '*.private.md' | head        # should exist locally
git status --porcelain -uall | grep -i private   # must be empty
```

### 3. Fix the cause, not just the symptom

Committing once doesn't stop this recurring. The open question is *why* eight days went uncommitted when there are two mechanisms that should have caught it — the Obsidian Git plugin (auto-commit) and the hourly `obsidian-sync.sh` timer on the P3. Determine which of these was supposed to cover this machine, and whether it is running here at all. See [[Obsidian Brain]].

A weekly check is cheap insurance — but **use `-uall`**:

```bash
cd ~/obsidian-personal && git status --porcelain -uall | wc -l
```

Without `-uall`, git collapses each untracked *directory* into one line, so the number badly
under-reports. Measured 2026-08-11: plain `--porcelain` returned **653** (598 deleted, 28
modified, 27 untracked) — but a single one of those 27 lines was `?? Library/`, standing in
for 649 files. The true figure was roughly **1,300**.

**This check is meaningless until step 2 is done.** The current baseline is 653/~1,300, so
"has it drifted?" cannot be answered while the vault is already fully drifted. Run it after
reconciliation, when the expected reading is 0–5, and any sustained growth means the
auto-commit path has stopped working again.

## Related

- [[Obsidian Brain]] · [[Backups]] · [[Backup — Obsidian Vault]] · [[Synology NAS]] · [[VAULT]]

## Log

- 2026-08-11 — Runbook written after a `git status` run (incidental to unrelated vault work) revealed one commit total and 8 days of uncommitted restructure. Deletions audited file-by-file and confirmed benign. Remote state could not be checked from the agent sandbox — no SSH keys, and `git fetch` failed on host key verification — so step 1 has to be run by hand on the Mac.

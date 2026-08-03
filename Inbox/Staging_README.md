# Staging

Drop newly-exported conversations here before they're categorized and filed into `Library/`.

Each file should already follow the frontmatter schema in `Import Schema.md` (date, source,
title, tags, status, sensitive, flagged_reason). Once a batch is staged:

1. Assign a `category` to each file (see the taxonomy in `Import Schema.md`).
2. Move `sensitive: true` files to `Library/Private/<Category>/`, everything else to
   `Library/<Category>/`.
3. Add the new notes to `Conversation Index.md` (or `Library/Private/Private Index.md`).
4. Delete the file from Staging once it's filed.

This folder should be empty between import batches — it's a workbench, not a permanent home.

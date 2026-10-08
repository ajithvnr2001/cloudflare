---
url: https://developers.cloudflare.com/sandbox/sdk/concepts/backup-restore/
title: Directory backups (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:22.690505+00:00
---

# Directory backups (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/concepts/backup-restore/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Concepts](https://developers.cloudflare.com/sandbox/sdk/concepts/)
  5. /Directory backups



# Directory backups

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/concepts/backup-restore/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProduction restoreLocal restoreCross-device renamesRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Backup and restore snapshot a sandbox directory into an R2 archive, then bring that tree back later. The public API is the same in production and in `wrangler dev`. The restore mechanism is not.

Use backups when you want a project directory such as `/workspace` to return later. Use [bucket mounts](https://developers.cloudflare.com/sandbox/sdk/guides/mount-buckets/) when a separate storage path such as `/data` should persist independently of the sandbox filesystem.

## Production restore

In production, `restoreBackup()` mounts the squashfs archive with FUSE overlayfs:

  * The backup is a read-only lower layer.
  * New writes go to a writable upper layer.
  * The original archive in R2 does not change.
  * Restoring the same handle again discards the upper layer.



The overlay exists only while the container is running. When the sandbox sleeps or the container restarts, the mount is gone and the directory is empty. Store the `DirectoryBackup` handle and restore again.

## Local restore

With `localBucket: true`, `wrangler dev` extracts the archive with `unsquashfs`. The target directory is replaced. There is no overlay, so local restore does not reproduce production FUSE behavior.

## Cross-device renames

Overlayfs treats the lower and upper layers as different devices. A rename that moves a directory from the restored lower layer into the writable upper layer can fail with `EXDEV` (`cross-device link not permitted`).

Vite does this with `node_modules/.vite/deps`. Omit that directory from the backup, or delete it after restore.

For the procedure, refer to [Exclude generated caches](https://developers.cloudflare.com/sandbox/sdk/guides/backup-restore/#exclude-generated-caches).

## Related resources

  * [Backup and restore](https://developers.cloudflare.com/sandbox/sdk/guides/backup-restore/) \- Create, restore, and exclude caches
  * [Backups API](https://developers.cloudflare.com/sandbox/sdk/api/backups/) \- Method signatures and options
  * [Sandbox lifecycle](https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/) \- What happens when a sandbox sleeps



[PreviousSecurity model](https://developers.cloudflare.com/sandbox/sdk/concepts/security/)[NextOverview](https://developers.cloudflare.com/sandbox/sdk/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/concepts/backup-restore.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

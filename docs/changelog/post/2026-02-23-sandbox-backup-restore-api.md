---
url: https://developers.cloudflare.com/changelog/post/2026-02-23-sandbox-backup-restore-api/
title: Backup and restore API for Sandbox SDK \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.413670+00:00
---

# Backup and restore API for Sandbox SDK · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-23-sandbox-backup-restore-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 23, 2026

## Backup and restore API for Sandbox SDK

[Agents](https://developers.cloudflare.com/agents/)[R2](https://developers.cloudflare.com/r2/)[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) now support `createBackup()` and `restoreBackup()` methods for creating and restoring point-in-time snapshots of directories.

This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step. Unfortunately `git clone` and `npm install` can take minutes, and you don't want to run these steps every time the user starts their sandbox.

Now, after the initial setup, you can just call `createBackup()`, then `restoreBackup()` the next time this environment is needed. This makes it practical to pick up exactly where a user left off, even after days of inactivity, without repeating expensive setup steps.
    
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    
    // Make non-trivial changes to the file system
    await sandbox.gitCheckout(endUserRepo, { targetDir: "/workspace" });
    await sandbox.exec("npm install", { cwd: "/workspace" });
    
    // Create a point-in-time backup of the directory
    const backup = await sandbox.createBackup({ dir: "/workspace" });
    
    // Store the handle for later use
    await env.KV.put(`backup:${userId}`, JSON.stringify(backup));
    
    // ... in a future session...
    
    // Restore instead of re-cloning and reinstalling
    await sandbox.restoreBackup(backup);

Backups are stored in [R2](https://developers.cloudflare.com/r2) and can take advantage of [R2 object lifecycle rules](https://developers.cloudflare.com/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup) to ensure they do not persist forever.

Key capabilities:

  * **Persist and reuse across sandbox sessions** — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions
  * **Usable across multiple instances** — Fork a backup across many sandboxes for parallel work
  * **Named backups** — Provide optional human-readable labels for easier management
  * **TTLs** — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed



Note

Backup and restore currently uses a FUSE overlay. Soon, native snapshotting at a lower level will be added to Containers and Sandboxes, improving speed and ergonomics. The current backup functionality provides a significant speed improvement over manually recreating a file system, but it will be further optimized in the future. The new snapshotting system will use a similar API, so changing to this system will be simple once it is available.

To get started, refer to the [backup and restore guide](https://developers.cloudflare.com/sandbox/guides/backup-restore/) for setup instructions and usage patterns, or the [Backups API reference](https://developers.cloudflare.com/sandbox/api/backups/) for full method documentation.

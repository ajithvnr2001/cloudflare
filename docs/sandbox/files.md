---
url: https://developers.cloudflare.com/sandbox/files/
title: Work with files in a sandbox \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:18.315936+00:00
---

# Work with files in a sandbox · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/files/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /Work with files



# Work with files in a sandbox

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/files/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPersistenceCombine approachesRelated resources

The `Files` class from `@cloudflare/sandbox` moves files between your Worker and a running sandbox, and provides common file system operations. For more information, refer to [Move files in and out of a sandbox](https://developers.cloudflare.com/sandbox/files/manage-files/).

Each sandbox name maps to a Durable Object, which starts a Linux instance when needed. Stopping the instance deletes the files on its disk. For more information, refer to [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/#files-and-processes-end-with-the-instance).

## Persistence

You can keep files from a sandbox in several ways, from a snapshot of the whole disk to one directory kept in R2:

Goal | Guide | Trade-off  
---|---|---  
Continue an agent workspace in a later session | [Save and restore a sandbox with snapshots](https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/) | Saves the whole disk for 30 days after the last save or restore  
Keep a workspace without explicit save calls | [Save a sandbox automatically](https://developers.cloudflare.com/sandbox/files/save-a-sandbox-automatically/) | Same as snapshots, plus an alarm in your Durable Object  
Keep a project across images, or beyond 30 days | [Back up a directory to R2](https://developers.cloudflare.com/sandbox/files/back-up-a-directory-to-r2/) | Saves one directory, and your Durable Object stores each backup record  
Share job inputs and outputs with other systems | [Mount an R2 bucket](https://developers.cloudflare.com/sandbox/files/mount-an-r2-bucket/) | Renames, locks, and permissions do not work as they do on a local disk  
  
## Combine approaches

Snapshots do not include mounted directories, so a sandbox can use both. For example, a coding agent can keep its repository and dependencies in a snapshot, and write results to a mounted bucket for other Workers to read. For more information, refer to [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/#mounted-buckets-outlive-every-instance).

## Related resources

  * [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/)
  * [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/)
  * [Files API](https://developers.cloudflare.com/sandbox/reference/files/)
  * [DirectoryBackup API](https://developers.cloudflare.com/sandbox/reference/directory-backups/)
  * [S3Mount API](https://developers.cloudflare.com/sandbox/reference/s3-mounts/)



[PreviousOpen a terminal](https://developers.cloudflare.com/sandbox/commands/open-a-terminal-in-the-browser/)[NextMove files](https://developers.cloudflare.com/sandbox/files/manage-files/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/files/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

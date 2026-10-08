---
url: https://developers.cloudflare.com/r2/objects/
title: Objects \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:47.366211+00:00
---

# Objects · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/objects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /Objects



# Objects

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/objects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrefixes and foldersManage objectsOther resources

Objects are individual files or data that you store in an R2 bucket. Each object is identified by its key, a string like `images/photo.png`.

## Prefixes and folders

R2 uses a flat storage structure. There are no real directories or folders. The `/` character in an object key is used as a delimiter to group objects by prefix.

The R2 dashboard groups objects that share a common prefix into folders when the **View prefixes as directories** checkbox is selected. For example, objects with keys `logs/jan.csv` and `logs/feb.csv` appear under a `logs/` folder. These folders are a visual grouping and do not exist as separate resources in your bucket.

## Manage objects

  * [Upload objects](https://developers.cloudflare.com/r2/objects/upload-objects/)
  * [Download objects](https://developers.cloudflare.com/r2/objects/download-objects/)
  * [Delete objects](https://developers.cloudflare.com/r2/objects/delete-objects/)



## Other resources

For information on R2 Workers Binding API, refer to [R2 Workers API reference](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/).

[PreviousStorage classes](https://developers.cloudflare.com/r2/buckets/storage-classes/)[NextUpload objects](https://developers.cloudflare.com/r2/objects/upload-objects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/objects/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/
title: Import from S3 \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:37.806818+00:00
---

# Import from S3 · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Storage

  4. /Upload images
  5. /Import from S3



# Import from S3

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCheck storage class support

Import from S3 lets you define one or more sources of images to bulk import from Amazon S3. You can reuse a source to import only new images into your Cloudflare Images account.

Imports skip unsupported objects and files in the source. You can also target paths, define image prefixes, and view error logs.

## Check storage class support

Use Import from S3 for buckets that contain images in non-archival storage classes. Import from S3 skips images in [archival storage classes ↗︎](https://aws.amazon.com/s3/storage-classes/#Archive), which require a separate import.

Import from S3 skips images stored using S3 Glacier tiers (not including Glacier Instant Retrieval) and logs them in the migration log. It also skips and logs images stored using S3 Intelligent Tiering in the Deep Archive tier.

[PreviousUpload via batch API](https://developers.cloudflare.com/images/storage/upload-images/images-batch/)[NextImport images from S3](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/enable/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/upload-images/import-from-s3/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

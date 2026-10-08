---
url: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/enable/
title: Import images from S3 \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:37.879862+00:00
---

# Import images from S3 · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/enable/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

StorageUpload images

  4. /[Import from S3](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/)
  5. /Import images from S3



# Import images from S3

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/enable/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDefine an import sourceCreate an import jobNext steps

Configure a source to start importing images from your Amazon S3 account.

To create an import job, you must first define an import source.

## Define an import source

  1. In the Cloudflare dashboard, go to **Hosted Images** > **Import from S3**.

[ Go to **Import from S3** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted/import)
  2. Select **Create Source** to create an import source.

  3. In **Source name** , enter a name for your source.

  4. In **Bucket name** , enter the S3 bucket name where your images are stored.

  5. In **Credentials** , enter your Amazon S3 credentials. This connects Cloudflare Images to your source. Refer to [Credentials](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/) to set up credentials.

  6. Select **Save**.




## Create an import job

  1. In the Cloudflare dashboard, go to **Hosted Images** > **Import from S3**.

[ Go to **Import from S3** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted/import)
  2. Select **Import images** to create an import job.

  3. In **Source** , select a source you defined.

  4. (Optional) In **Amazon S3 root path** , enter the Amazon S3 path that contains the images you want to import.

  5. (Optional) In **Add a prefix to your delivery path** , enter a prefix for imported images.

  6. In **Overwrite images** , choose to overwrite existing images with changed source files or skip the changed files and keep existing images.

  7. Select **Start Import**.




Your import job is now created. You can review its status on the **Import from S3** page, including discovered objects, imported images, and errors.

Note

Cloudflare Images warns you when you approach the storage quota for your plan. Import jobs stop when you exhaust the available storage. If you see this warning on the **Import from S3** page, select **View plan** to change your plan limits.

## Next steps

Refer to [Edit source details](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/edit/) to edit existing sources or abort running import jobs.

[PreviousOverview](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/)[NextEdit sources](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/edit/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/upload-images/import-from-s3/enable.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

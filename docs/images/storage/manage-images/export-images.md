---
url: https://developers.cloudflare.com/images/storage/manage-images/export-images/
title: Export images \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:37.089694+00:00
---

# Export images · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/manage-images/export-images/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Storage

  4. /Manage hosted images
  5. /Export images



# Export images

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/storage/manage-images/export-images/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExport images via the Cloudflare dashboardExport images via the API

Cloudflare Images supports image exports via the Cloudflare dashboard and API which allows you to get the original version of your image.

## Export images via the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to the **Hosted Images** page.

[ Go to **Hosted images** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted)
  2. Find the image or images you want to export.

  3. To export a single image, select **Export** from its menu. To export several images, select the checkbox next to each image and then select **Export selected**.




Your images are downloaded to your machine.

## Export images via the API

Make a `GET` request as shown in the example below. `<IMAGE_ID>` must be fully URL encoded in the API call URL.

`GET accounts/<ACCOUNT_ID>/images/v1/<IMAGE_ID>/blob`

[PreviousEdit images](https://developers.cloudflare.com/images/storage/manage-images/edit-images/)[NextDelete images](https://developers.cloudflare.com/images/storage/manage-images/delete-images/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/manage-images/export-images.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

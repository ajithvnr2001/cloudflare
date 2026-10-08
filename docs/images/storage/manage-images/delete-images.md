---
url: https://developers.cloudflare.com/images/storage/manage-images/delete-images/
title: Delete images \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:37.127634+00:00
---

# Delete images · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/manage-images/delete-images/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Storage

  4. /Manage hosted images
  5. /Delete images



# Delete images

Last updated Jun 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/storage/manage-images/delete-images/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDelete images via the Cloudflare dashboardDelete images via the API

You can delete an image from the Cloudflare Images storage using the dashboard, the API, or from a Worker via the [Images binding](https://developers.cloudflare.com/images/storage/binding/#imageimageiddelete).

## Delete images via the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to the **Hosted Images** page.

[ Go to **Hosted images** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted)
  2. Find the image you want to remove and select **Delete**.

  3. (Optional) To delete more than one image, select the checkbox next to the images you want to delete and then **Delete selected**.




Your image will be deleted from your account.

## Delete images via the API

Make a `DELETE` request to the [delete image endpoint](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/delete/). `{image_id}` must be fully URL encoded in the API call URL.
    
    
    curl --request DELETE https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/{image_id} \
    --header "Authorization: Bearer <API_TOKEN>"

After the image has been deleted, the response returns `"success": true`.

[PreviousExport images](https://developers.cloudflare.com/images/storage/manage-images/export-images/)[NextManage with Workers](https://developers.cloudflare.com/images/storage/binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/manage-images/delete-images.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

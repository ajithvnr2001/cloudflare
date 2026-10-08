---
url: https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/
title: Serve uploaded images \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:35.330757+00:00
---

# Serve uploaded images · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Hosted images
  5. /Serve uploaded images



# Serve uploaded images

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOptimize format

To serve images uploaded to Cloudflare Images, you must have:

  * Your Images account hash
  * Image ID
  * Variant or flexible variant name



Assuming you have at least one image uploaded to Images, you will find the basic URL format from the Images dashboard under Developer Resources.

![Developer Resources section within the Images product form the Cloudflare Dashboard.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2678,height=992,format=webp/_astro/image-delivery-url.D7G6zX-5.png)

A typical image delivery URL looks similar to the example below.

`https://imagedelivery.net/<ACCOUNT_HASH>/<IMAGE_ID>/<VARIANT_NAME>`

In the example, you need to replace `<ACCOUNT_HASH>` with your Images account hash, along with the `<IMAGE_ID>` and `<VARIANT_NAME>`, to begin serving images.

You can select **Preview** next to the image you want to serve to preview the image with an Image URL you can copy. The link will have a fully formed **Images URL** and will look similar to the example below.

In this example:

  * `ZWd9g1K7eljCn_KDTu_MWA` is the Images account hash.
  * `083eb7b2-5392-4565-b69e-aff66acddd00` is the image ID. You can also use Custom IDs instead of the generated ID.
  * `public` is the variant name.



When a user requests an image, Cloudflare Images chooses the optimal format, which is determined by client headers and the image type.

## Optimize format

Cloudflare Images automatically transcodes uploaded PNG, JPEG and GIF files to the more efficient AVIF and WebP formats. This happens whenever the customer browser supports them. If the browser does not support AVIF, Cloudflare Images will fall back to WebP. If there is no support for WebP, then Cloudflare Images will serve compressed files in the original format.

Uploaded SVG files are served as [sanitized SVGs](https://developers.cloudflare.com/images/get-started/limits/#svg).

[PreviousPreserve Content Credentials](https://developers.cloudflare.com/images/optimization/transformations/preserve-content-credentials/)[NextCreate predefined variants](https://developers.cloudflare.com/images/optimization/hosted-images/create-variants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/hosted-images/serve-uploaded-images.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

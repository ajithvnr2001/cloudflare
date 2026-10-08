---
url: https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/
title: New in Images: text rasterization and updates to the binding \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.280140+00:00
---

# New in Images: text rasterization and updates to the binding · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2026

## New in Images: text rasterization and updates to the binding

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've added more ways to manage and manipulate images with the [Images binding](https://developers.cloudflare.com/images/optimization/binding/). Here's what's new:

**Render text into an image.** Output a string of text into its own image or draw it over another image.

  * Use the [`.text()`](https://developers.cloudflare.com/images/optimization/binding/#textcontent-options) method to rasterize text with the Images binding.
  * Style content using the `font`, `size`, and `color` options.
  * The [`draw`](https://developers.cloudflare.com/images/optimization/draw-overlays/#draw-with-cfimage) array in `cf.image` now accepts a `text` key.



**Manage hosted images without an API token.**

  * **Metadata filtering:** Pass `filter.metadata` to [`.list()`](https://developers.cloudflare.com/images/storage/binding/#listoptions) to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, `priority: { gte: 2, lte: 5 }`.
  * **Server-side signing:** Get a signed URL for a private image with [`.signedUrl()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidsignedurloptions).
  * **User uploads:** Create a Direct Creator Upload link with [`.createDirectUpload()`](https://developers.cloudflare.com/images/storage/binding/#createdirectuploadoptions) so that a client can upload an image to your storage.



**Set headers in a single call.**

  * Pass a `headers` option to [`.response()`](https://developers.cloudflare.com/images/optimization/binding/#responseoptions) to set headers without rebuilding the `Response`.
  * `Content-Type` is always taken from the optimized image and can't be overridden by a specified header.
  * Set `Cache-Control` with [Workers Cache](https://developers.cloudflare.com/workers/cache/) to cache your optimized image at the edge.



For more information, refer to [Optimize with Workers](https://developers.cloudflare.com/images/optimization/binding/), [Draw overlays and watermarks](https://developers.cloudflare.com/images/optimization/draw-overlays/), and [Manage hosted images with Workers](https://developers.cloudflare.com/images/storage/binding/).

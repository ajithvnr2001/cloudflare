---
url: https://developers.cloudflare.com/images/polish/cf-polished-statuses/
title: Cf-Polished statuses \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:36.394411+00:00
---

# Cf-Polished statuses · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/polish/cf-polished-statuses/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /[Cloudflare Polish](https://developers.cloudflare.com/images/polish/)
  4. /Cf-Polished statuses



# Cf-Polished statuses

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/polish/cf-polished-statuses/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If a `Cf-Polished` header is not returned, try [using single-file cache purge](https://developers.cloudflare.com/cache/how-to/purge-cache) to purge the image. The `Cf-Polished` header may also be missing if the origin is sending non-image `Content-Type`, or non-cacheable `Cache-Control`.

  * `input_too_large`: The input image is too large or complex to process, and needs a lower resolution. Cloudflare recommends using PNG or JPEG images that are less than 4,000 pixels in any dimension, and smaller than 20 MB.
  * `not_compressed` or `not_needed`: The image was fully optimized at the origin server and no compression was applied.
  * `webp_bigger`: Polish attempted to convert to WebP, but the WebP image was not better than the original format. Because the WebP version does not exist, the status is set on the JPEG/PNG version of the response. Refer to [the reasons why Polish chooses not to use WebP](https://developers.cloudflare.com/images/polish/no-webp/).
  * `cannot_optimize` or `internal_error`: The input image is corrupted or incomplete at the origin server. Upload a new version of the image to the origin server.
  * `format_not_supported`: The input image format is not supported (for example, BMP or TIFF) or the origin server is using additional optimization software that is not compatible with Polish. Try converting the input image to a web-compatible format (like PNG or JPEG) and/or disabling additional optimization software at the origin server.
  * `vary_header_present`: The origin web server has sent a `Vary` header with a value other than `accept-encoding`. If the origin web server is attempting to support WebP, disable WebP at the origin web server and let Polish perform the WebP conversion. Polish will still work if `accept-encoding` is the only header listed within the `Vary` header. Polish skips image URLs processed by [Cloudflare Images](https://developers.cloudflare.com/images/optimization/transformations/overview).



[PreviousPolish compression](https://developers.cloudflare.com/images/polish/compression/)[NextWebP may be skipped](https://developers.cloudflare.com/images/polish/no-webp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/polish/cf-polished-statuses.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

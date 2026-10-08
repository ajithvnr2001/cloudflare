---
url: https://developers.cloudflare.com/speed/optimization/images/mirage/
title: Cloudflare Mirage (deprecated) \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:35.280766+00:00
---

# Cloudflare Mirage (deprecated) · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/images/mirage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

Settings

  4. /Image optimization
  5. /Mirage



# Cloudflare Mirage (deprecated)

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/images/mirage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat was Mirage?Why was it deprecated?Migration path

Deprecation notice

Mirage was deprecated on September 15, 2025 and is no longer available.

As an alternative, Cloudflare recommends using [lazy loading](https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/) and [responsive images](https://developers.cloudflare.com/images/optimization/make-responsive-images/) to optimize image performance for all devices.

## What was Mirage?

Cloudflare Mirage was a mobile image optimization feature that reduced bandwidth usage and accelerated image loading on slow mobile connections and HTTP/1.

Mirage worked by:

  * Replacing images with low-resolution thumbnails bundled together into one file.
  * Acting as a lazy loader, deferring loading of higher-resolution images until they become visible.



## Why was it deprecated?

Modern web standards and browser capabilities have evolved to provide native support for many of Mirage's features:

  * Native lazy loading with the `loading="lazy"` HTML attribute.
  * Responsive images using `srcset` and `<picture>` elements.
  * HTTP/2 and HTTP/3 providing better performance.
  * Improved mobile networks reducing the need for aggressive optimization.



## Migration path

Instead of Mirage, use:

  * **[Polish](https://developers.cloudflare.com/images/polish/)** \- Seamlessly optimizes images for all browsers, not only mobile, and keeps images at full resolution.
  * **[Image Resizing](https://developers.cloudflare.com/images/optimization/transformations/overview/)** \- Combined with `loading="lazy"` and `srcset` HTML attributes, provides modern responsive image delivery.
  * **[Lazy loading guide](https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/)** \- Learn how to implement native lazy loading.
  * **[Responsive images guide](https://developers.cloudflare.com/images/optimization/make-responsive-images/)** \- Create images that adapt to different devices.



[PreviousPolish ↗︎](https://developers.cloudflare.com/images/polish/)[NextImage optimization on optimized images](https://developers.cloudflare.com/speed/optimization/images/troubleshooting/multiple-optimizations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/images/mirage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

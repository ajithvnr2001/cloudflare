---
url: https://developers.cloudflare.com/images/get-started/introduction/
title: Introduction \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:34.076966+00:00
---

# Introduction · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/get-started/introduction/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /Get started
  4. /Introduction



# Introduction

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/get-started/introduction/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy optimize images?How do I get started with Images? Optimize remote images Upload and deliver with ImagesShould I store with Images or R2?

Cloudflare provides a platform for building and scaling media applications with Images. On this page, we'll answer the following questions:

  * Why optimize images?
  * How do I get started with Images?
  * Should I store with Images or R2?



* * *

## Why optimize images?

Loading images in their original resolution and format quickly becomes a bottleneck for app performance — especially on mobile.

Meanwhile, creating and storing multiple versions of the same image adds complexity and overhead, along with storage costs.

When you serve large amounts of media, image optimization provides:

  * **Streamlined infrastructure** — Simplify your workflow and reduce infrastructure costs by dynamically generating optimized versions on request.
  * **Smaller file sizes** — Automatically deliver images in modern formats like AVIF and WebP, which improves page speed and lowers bandwidth.
  * **Responsive sizing** — Crop and resize for any use case, from square thumbnails to landscape banners, using the same original image in storage.
  * **Visual effects** — Apply blur, overlays, background fills, and more at the edge.



## How do I get started with Images?

There are two ways to use Images, depending on where your images are stored:

### Optimize remote images

Keep your images on your own origin, in [R2](https://developers.cloudflare.com/r2), or with any storage provider. Cloudflare pulls the original image, applies optimizations at the edge, and caches the optimized image.

You can define an [origin allowlist](https://developers.cloudflare.com/images/optimization/transformations/sources/) to control which source images can be transformed on your zone.

To start, [enable transformations on your zone](https://developers.cloudflare.com/images/optimization/transformations/overview/).

### Upload and deliver with Images

Store, optimize, and deliver images globally with zero infrastructure management.

If your app centers around user-uploaded content, then you can use the [Direct Creator Upload API](https://developers.cloudflare.com/images/storage/upload-images/direct-creator-upload/) to securely accept images directly from your users.

To start, set up [predefined variants](https://developers.cloudflare.com/images/optimization/hosted-images/create-variants/) to configure how hosted images should be served.

## Should I store with Images or R2?

**Store in[R2](https://developers.cloudflare.com/r2/) and use Images for transformations** if you want to build your own custom image pipeline or need fine-grained control over storage, such as [bucket-level access management](https://developers.cloudflare.com/r2/buckets/) or [object lifecycle rules](https://developers.cloudflare.com/r2/buckets/object-lifecycles/). This is typically the most cost-effective approach for image optimization.

**Store in Images** if you want a fully managed solution with the least configuration. Our built-in features include a [shared delivery domain](https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/), [predefined variants](https://developers.cloudflare.com/images/optimization/hosted-images/create-variants/), and automatic cache invalidation when you update original images in storage.

Each use case has a separate pricing model. To learn more, refer to [Pricing](https://developers.cloudflare.com/images/pricing/).

[PreviousOverview](https://developers.cloudflare.com/images/)[NextKey concepts](https://developers.cloudflare.com/images/get-started/key-concepts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/get-started/introduction.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

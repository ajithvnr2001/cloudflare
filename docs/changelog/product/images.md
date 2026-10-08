---
url: https://developers.cloudflare.com/changelog/product/images/
title: Cloudflare Images Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:46.854356+00:00
---

# Cloudflare Images Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/images/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Sep 23, 2026

## [View transformation analytics in Images](https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can now view account-level analytics for your Images transformation usage.

Go to **Images & Stream** > **Transformations** > **Analytics** to view sampled estimates of image transformation request traffic, including:

  * Requests by source, split between URL-based transformations and Images binding transformations
  * Top zones, transformation configurations, and origin hosts for URL-based requests
  * Top Worker scripts for Images binding requests



Use these analytics to identify the zones, configurations, origins, and Workers generating the most image transformation requests.

Sep 2, 2026

## [New in Images: text rasterization and updates to the binding](https://developers.cloudflare.com/changelog/post/2026-09-02-images-binding-updates/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

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

Jul 1, 2026

## [Images binding is now billed per unique transformation](https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

The [Images binding](https://developers.cloudflare.com/images/optimization/binding/) is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.

Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.

Calls to [`.info()`](https://developers.cloudflare.com/images/optimization/binding/#infostream) are no longer billed.

For more information, refer to [Images pricing](https://developers.cloudflare.com/images/pricing/#images-transformed) and the [Images binding documentation](https://developers.cloudflare.com/images/optimization/binding/).

Jun 16, 2026

## [New optimization features in Images](https://developers.cloudflare.com/changelog/post/2026-06-16-new-optimization-features/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

These updates introduce new features for optimizing and manipulating with Images:

  * **New`composite` option:** Control how [overlays are blended](https://developers.cloudflare.com/images/optimization/draw-overlays/#composite) with the base image.
  * **Percentage widths:** Set the dimensions of an overlay as [a fraction of the dimensions](https://developers.cloudflare.com/images/optimization/draw-overlays/#width-and-height) of the base image.
  * **New`fit` modes:** Use [`aspect-crop`](https://developers.cloudflare.com/images/optimization/features/#aspect-crop) to always preserve the target aspect ratio or [`scale-up`](https://developers.cloudflare.com/images/optimization/features/#scale-up) to always enlarge images.
  * **New`upscale` parameter:** Apply [AI upscaling](https://developers.cloudflare.com/images/optimization/features/#upscale) to produce sharper, more detailed results when enlarging images.



Jun 10, 2026

## [Manage hosted images with the Images binding](https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.

The `env.IMAGES.hosted` namespace supports the following storage and management operations:

  * [`.upload(image, options)`](https://developers.cloudflare.com/images/storage/binding/#uploadimage-options) — Upload a new image to your account.
  * [`.list(options)`](https://developers.cloudflare.com/images/storage/binding/#listoptions) — List images with pagination.
  * [`.image(imageId).details()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddetails) — Get image metadata.
  * [`.image(imageId).bytes()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidbytes) — Stream the original image bytes.
  * [`.image(imageId).update(options)`](https://developers.cloudflare.com/images/storage/binding/#imageimageidupdateoptions) — Update metadata or access controls.
  * [`.image(imageId).delete()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddelete) — Delete an image.



For example, you can upload an image from a request body and return its metadata:
    
    
    const image = await env.IMAGES.hosted.upload(request.body, {
    	filename: "upload.jpg",
    	metadata: { source: "worker" },
    });
    
    return Response.json(image);

Or retrieve and serve the original bytes of a hosted image:
    
    
    const bytes = await env.IMAGES.hosted.image("IMAGE_ID").bytes();
    return new Response(bytes);

For more information, refer to the [Images binding](https://developers.cloudflare.com/images/storage/binding/).

May 27, 2026

## [Transformation flows in Images](https://developers.cloudflare.com/changelog/post/2026-05-27-transformation-flows/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

![Custom flow configuration panel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1654,height=1398,format=webp/_astro/custom-flow.DeAGR8BY.png)

Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.

There are two modes for transformation flows:

  * **[Provider flows](https://developers.cloudflare.com/images/optimization/transformations/flows/#set-up-a-provider-flow)** — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.
  * **[Custom flows](https://developers.cloudflare.com/images/optimization/transformations/flows/#set-up-a-custom-flow)** — Define your own conditions and actions for use cases like automatic format conversion, [responsive sizing](https://developers.cloudflare.com/images/optimization/make-responsive-images/#using-widthauto) with `width=auto`, or directory-based optimization.



To get started, go to **Images** > **Transformations** > **Automation** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/images/transformations).

Learn more about [transformation flows](https://developers.cloudflare.com/images/optimization/transformations/flows/).

Jul 8, 2025

## [HEIC support in Cloudflare Images](https://developers.cloudflare.com/changelog/post/heic-support/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can use Images to ingest HEIC images and serve them in supported output formats like AVIF, WebP, JPEG, and PNG.

When inputting a HEIC image, dimension and sizing limits may still apply. Refer to our documentation to see limits for [uploading to Images](https://developers.cloudflare.com/images/storage/upload-images/methods/) or [transforming a remote image](https://developers.cloudflare.com/images/optimization/transformations/overview/).

Feb 24, 2025

## [Bind the Images API to your Worker](https://developers.cloudflare.com/changelog/post/2025-02-21-images-bindings-in-workers/)

[Cloudflare Images](https://developers.cloudflare.com/images/)

You can now [interact with the Images API](https://developers.cloudflare.com/images/optimization/binding/) directly in your Worker.

This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.

The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:
    
    
    {
    	"images": {
    		"binding": "IMAGES", // i.e. available in your Worker on env.IMAGES
    	},
    }
    
    
    [images]
    binding = "IMAGES"

Within your Worker code, you can interact with this binding by using `env.IMAGES`.

Here's how you can rotate, resize, and blur an image, then output the image as AVIF:
    
    
    const info = await env.IMAGES.info(stream);
    // stream contains a valid image, and width/height is available on the info object
    
    const response = (
    	await env.IMAGES.input(stream)
    		.transform({ rotate: 90 })
    		.transform({ width: 128 })
    		.transform({ blur: 20 })
    		.output({ format: "image/avif" })
    ).response();
    
    return response;

For more information, refer to [Images Bindings](https://developers.cloudflare.com/images/optimization/binding/).

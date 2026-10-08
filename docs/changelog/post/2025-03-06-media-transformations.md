---
url: https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/
title: Introducing Media Transformations from Cloudflare Stream \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:05.671952+00:00
---

# Introducing Media Transformations from Cloudflare Stream · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 6, 2025

## Introducing Media Transformations from Cloudflare Stream

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-06-media-transformations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are thrilled to announce Media Transformations, a new service that brings the magic of [Image Transformations](https://developers.cloudflare.com/images/optimization/transformations/overview/) to _short-form video files,_ wherever they are stored!

For customers with a huge volume of short video — generative AI output, e-commerce product videos, social media clips, or short marketing content — uploading those assets to Stream is not always practical. Sometimes, the greatest friction to getting started was the thought of all that migrating. Customers want a simpler solution that retains their current storage strategy to deliver small, optimized MP4 files. Now you can do that with Media Transformations.

To transform a video or image, [enable transformations](https://developers.cloudflare.com/stream/transform-videos/#getting-started) for your zone, then make a simple request with a specially formatted URL. The result is an MP4 that can be used in an HTML video element without a player library. If your zone already has Image Transformations enabled, then it is ready to optimize videos with Media Transformations, too.

URL formattext
    
    
    https://example.com/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>

For example, we have a short video of the mobile in Austin's office. The original is nearly 30 megabytes and wider than necessary for this layout. Consider a simple width adjustment:

Example URLtext
    
    
    https://example.com/cdn-cgi/media/width=640/<SOURCE-VIDEO>
    https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4

The result is less than 3 megabytes, properly sized, and delivered dynamically so that customers do not have to manage the creation and storage of these transformed assets.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

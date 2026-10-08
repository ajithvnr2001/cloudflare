---
url: https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/
title: Introducing Origin Restrictions for Media Transformations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:12.246132+00:00
---

# Introducing Origin Restrictions for Media Transformations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 14, 2025

## Introducing Origin Restrictions for Media Transformations

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-14-media-transformations-origin-restrictions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are adding [source origin restrictions](https://developers.cloudflare.com/stream/transform-videos/sources/) to the Media Transformations beta. This allows customers to restrict what sources can be used to fetch images and video for transformations. This feature is the same as --- and uses the same settings as --- [Image Transformations sources](https://developers.cloudflare.com/images/optimization/transformations/sources/).

When transformations is first enabled, the default setting only allows transformations on images and media from the same website or domain being used to make the transformation request. In other words, by default, requests to `example.com/cdn-cgi/media` can only reference originals on `example.com`.

![Enable allowed origins from the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1664,height=872,format=webp/_astro/allowed-origins.4hu5lHws.png)

Adding access to other sources, or allowing any source, [is easy to do](https://developers.cloudflare.com/images/optimization/transformations/sources/) in the **Transformations** tab under **Stream**. Click each domain enabled for Transformations and set its sources list to match the needs of your content. The user making this change will need permission to edit zone settings.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

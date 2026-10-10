---
url: https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/
title: Store larger custom metadata values in AI Search \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.306626+00:00
---

# Store larger custom metadata values in AI Search · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2026

## Store larger custom metadata values in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.

For details, refer to [Metadata attributes](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

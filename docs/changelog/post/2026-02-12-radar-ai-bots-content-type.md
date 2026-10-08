---
url: https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/
title: Content Type Dimension for AI Bots in Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:36.973131+00:00
---

# Content Type Dimension for AI Bots in Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 12, 2026

## Content Type Dimension for AI Bots in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes content type insights for AI bot and crawler traffic. The new `content_type` dimension and filter shows the distribution of content types returned to AI crawlers, grouped by MIME type category.

The content type dimension and filter are available via the following API endpoints:

  * [`/ai/bots/summary/content_type`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/)
  * [`/ai/bots/timeseries_groups/content_type`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/)



Content type categories:

  * **HTML** \- Web pages (`text/html`)
  * **Images** \- All image formats (`image/*`)
  * **JSON** \- JSON data and API responses (`application/json`, `*+json`)
  * **JavaScript** \- Scripts (`application/javascript`, `text/javascript`)
  * **CSS** \- Stylesheets (`text/css`)
  * **Plain Text** \- Unformatted text (`text/plain`)
  * **Fonts** \- Web fonts (`font/*`, `application/font-*`)
  * **XML** \- XML documents and feeds (`text/xml`, `application/xml`, `application/rss+xml`, `application/atom+xml`)
  * **YAML** \- Configuration files (`text/yaml`, `application/yaml`)
  * **Video** \- Video content and streaming (`video/*`, `application/ogg`, `*mpegurl`)
  * **Audio** \- Audio content (`audio/*`)
  * **Markdown** \- Markdown documents (`text/markdown`)
  * **Documents** \- PDFs, Office documents, ePub, CSV (`application/pdf`, `application/msword`, `text/csv`)
  * **Binary** \- Executables, archives, WebAssembly (`application/octet-stream`, `application/zip`, `application/wasm`)
  * **Serialization** \- Binary API formats (`application/protobuf`, `application/grpc`, `application/msgpack`)
  * **Other** \- All other content types



Additionally, individual [bot information pages ↗︎](https://radar.cloudflare.com/bots/directory/gptbot) now display content type distribution for AI crawlers that exist in both the Verified Bots and AI Bots datasets.

![Screenshot of the Content Type Distribution chart on the AI Insights page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=874,format=webp/_astro/ai-bots-content-type.B7xP9p4S.png)

Check out the [AI Insights page ↗︎](https://radar.cloudflare.com/ai-insights#content-type) to explore the data.

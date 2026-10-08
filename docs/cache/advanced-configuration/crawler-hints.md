---
url: https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/
title: Crawler Hints \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:40.752127+00:00
---

# Crawler Hints · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Advanced configuration
  4. /Crawler Hints



# Crawler Hints

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundBenefitsAvailabilityEnable Crawler HintsPrevent indexing for a specific page

Crawler Hints uses Cloudflare cache signals to tell search engines when your content has likely changed, so they crawl your site at the right time instead of guessing.

## Background

Search engines and similar services operate massive networks of bots that crawl the Internet to identify the content most relevant to a user query. Content on the web is always changing though, and search engine crawlers must continually wander the Internet and guess how frequently they should check a site for content updates.

With Crawler Hints, Cloudflare can proactively tell a crawler about the best time to index or when content changes. Additionally, Crawler Hints supports [IndexNow ↗︎](https://www.indexnow.org/), which allows websites to notify search engines whenever content on their website content is created, updated, or deleted. Crawler Hints uses cache-status [`MISS`](https://developers.cloudflare.com/cache/concepts/cache-responses/#miss) to determine when content has likely been updated and sends it to IndexNow's crawler. If an asset's response has an HTTP status code greater than 4xx, the Crawler hints will not report that to [IndexNow ↗︎](https://www.indexnow.org/).

## Benefits

Crawler Hints help search engines and other bot-powered services serve the freshest version of your content, which can improve search rankings.

Crawler Hints also reduces unnecessary crawl traffic to your origin, lowering resource consumption and improving site performance.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## Enable Crawler Hints

  1. In the Cloudflare dashboard, go to the **Configuration** page.

[ Go to **Configuration** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/caching/configuration)
  2. Enable **Crawler Hints**.




After enabling Crawler Hints, Cloudflare will begin sending hints to search engines about when they should crawl particular parts of your website.

## Prevent indexing for a specific page

When enabled, Crawler Hints is a global setting for your entire website. You can stop a specific page from being indexed by either:

  * Having the origin server send through the header `X-Robots-Tag: noindex` on any pages that should not be indexed.
  * Including `<meta name="robots" content="noindex, nofollow" />` in the HTML of any pages that should not be indexed.
  * Creating a [Response header Transform Rule](https://developers.cloudflare.com/rules/transform/response-header-modification/) in Cloudflare to add the `X-Robots-Tag: noindex` header instead of doing it from the origin server.



[PreviousCache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/)[NextEarly Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/advanced-configuration/crawler-hints.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

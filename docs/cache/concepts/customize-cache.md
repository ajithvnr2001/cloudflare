---
url: https://developers.cloudflare.com/cache/concepts/customize-cache/
title: Customize cache \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:41.541101+00:00
---

# Customize cache · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/concepts/customize-cache/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Concepts
  4. /Customize cache



# Customize cache

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/concepts/customize-cache/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a directory for static content at your origin web serverAppend a unique file extension to static pagesAdd a query string to a resource’s URL to mark the content as static

Some possible combinations of origin web server settings and Cloudflare [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/) include:

## Create a directory for static content at your origin web server

For example, create a `/static/` subdirectory at your origin web server and a Cache Everything Cache Rule matching the following expression:

  * Using the Expression Builder: `Hostname contains "example.com" AND URI Path starts with "/static"`
  * Using the Expression Editor: `(http.host contains "example.com" and starts_with(http.request.uri.path, "/static"))`



## Append a unique file extension to static pages

For example, create a `.shtml` file extension for resources at your origin web server and a Cache Everything Cache Rule matching the following expression:

  * Using the Expression Builder: `Hostname contains "example.com" AND URI Path ends with ".shtml"`
  * Using the Expression Editor: `(http.host contains "example.com" and ends_with(http.request.uri.path, ".shtml"))`



## Add a query string to a resource’s URL to mark the content as static

For example, add a `static=true` query string for resources at your origin web server and a Cache Everything Cache Rule matching the following expression:

  * Using the Expression Builder: `Hostname contains "example.com" AND URI Query String contains "static=true"`
  * Using the Expression Editor: `(http.host contains "example.com" and http.request.uri.query contains "static=true")`



Resources that match a Cache Everything Cache Rule are still not cached if the origin web server sends a Cache-Control header of `max-age=0`, `private`, `no-cache`, or an `Expires` header with an already expired date. Include the [Edge Cache TTL](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#edge-ttl) setting within the Cache Everything Cache Rule to additionally override the `Cache-Control` headers from the origin web server.

[PreviousCloudflare cache responses](https://developers.cloudflare.com/cache/concepts/cache-responses/)[NextDefault cache behavior](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/concepts/customize-cache.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

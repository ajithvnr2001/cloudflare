---
url: https://developers.cloudflare.com/cache/how-to/set-caching-levels/
title: Caching levels \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:45.260419+00:00
---

# Caching levels · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/set-caching-levels/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Cache configuration
  4. /Caching levels



# Caching levels

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/set-caching-levels/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI Caching level values

Caching levels determine how much of your website’s static content Cloudflare should cache. Cloudflare’s CDN caches static content according to the levels below.

  * **No Query String** : Delivers resources from cache when there is no query string. Example URL: `example.com/pic.jpg`
  * **Ignore Query String** : Delivers the same resource to everyone independent of the query string. Example URL: `example.com/pic.jpg?ignore=this-query-string`
  * **Standard (Default)** : Delivers a different resource each time the query string changes. Example URL: `example.com/pic.jpg?with=query`



You can adjust the caching level from the dashboard under **Caching** > **Configuration** > **Caching level**.

Note

Ignore Query String only disregards the query string for static file extensions. For example, Cloudflare serves the `style.css` resource to requests for either `style.css?this` or `style.css?that`.

## API Caching level values

If you are using the API to change the cache level, the values will differ from those shown in the dashboard. Refer to the table below to see how the API values map to the values shown in the dashboard.

Dashboard | API  
---|---  
No Query String | Basic  
Ignore Query String | Simplified  
Standard (Default) | Aggressive  
  
[PreviousCache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/)[NextTiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/set-caching-levels.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

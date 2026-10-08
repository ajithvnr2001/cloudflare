---
url: https://developers.cloudflare.com/logs/reference/clientrequestsource/
title: ClientRequestSource field \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:16.830461+00:00
---

# ClientRequestSource field · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/reference/clientrequestsource/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Reference](https://developers.cloudflare.com/logs/reference/)
  4. /ClientRequestSource field



# ClientRequestSource field

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/reference/clientrequestsource/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The possible values for the `ClientRequestSource` field are the following:

Value | Request source | Description  
---|---|---  
`0` | unknown | Should never happen.  
`1` | eyeball | A request from an end user. If you want to count requests made the Cloudflare Edge, the query should filter on `requestSource=eyeball`.  
`2` | purge | A request made by Cloudflare's purge system.  
`3` | alwaysOnline | A request made by Cloudflare's Always Online crawler.  
`4` | healthcheck | A request made by Cloudflare's Health Check system.  
`5` | edgeWorkerFetch | A fetch request made from an edge Worker.  
`6` | edgeWorkerCacheAPI | A cache API call made from an edge Worker.  
`7` | edgeWorkerKV | A KV call made from an edge Worker.  
`8` | imageResizing | Requests made by Cloudflare's Image Resizing product.  
`9` | orangeToOrange | A request that comes from another orange clouded zone.  
`10` | sslDetector | A request made by Cloudflare's [SSL Detector system ↗︎](https://blog.cloudflare.com/ssl-tls-recommender/).  
`11` | earlyHintsCache | An [Early Hint request ↗︎](https://blog.cloudflare.com/early-hints/).  
`12` | inBrowserChallenge | An end user request caused by a Cloudflare security product (Challenges, JavaScript Detections). These requests never reach the origin.  
  
[PreviousWAF fields](https://developers.cloudflare.com/logs/reference/waf-fields/)[Next2023-02-01 - Updates to security fields](https://developers.cloudflare.com/logs/reference/change-notices/2023-02-01-security-fields-updates/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/reference/clientrequestsource.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

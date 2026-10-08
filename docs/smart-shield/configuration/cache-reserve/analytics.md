---
url: https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/
title: Cache Reserve analytics \u00b7 Cloudflare Smart Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:31.338970+00:00
---

# Cache Reserve analytics · Cloudflare Smart Shield docs

> Source: https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Smart Shield](https://developers.cloudflare.com/smart-shield/)
  3. /…

Configuration

  4. /[Cache Reserve](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/)
  5. /Analytics



# Cache Reserve analytics

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cache Reserve Analytics provides insights regarding your Cache Reserve usage. It allows you to check what content is stored in Cache Reserve, how often it is being accessed, how long it has been there and how much egress from your origin it is saving you.

You have access to the following metrics:

  * **Egress savings (bandwidth)** \- is an estimation based on response bytes served from Cache Reserve that did not need to be served from your origin server. These are represented as cache hits.
  * **Requests served by Cache Reserve** \- is the number of requests served by Cache Reserve (total).
  * **Data storage summary** \- is based on a representative sample of requests. Refer to [Sampling](https://developers.cloudflare.com/analytics/graphql-api/sampling/) for more details about how Cloudflare samples data. 
    * **Current data stored** \- is the data stored (currently) over time.
    * **Aggregate storage usage** \- is the total of storage used for the selected timestamp.
  * **Operations** \- Class A (writes) and Class B (reads) operations over time.



[PreviousOperations](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/operations/)[NextArgo Smart Routing](https://developers.cloudflare.com/smart-shield/configuration/argo/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/smart-shield/configuration/cache-reserve/analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

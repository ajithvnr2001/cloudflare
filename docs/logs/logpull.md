---
url: https://developers.cloudflare.com/logs/logpull/
title: Logpull \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:09.852214+00:00
---

# Logpull · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpull/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /Logpull



# Logpull

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpull/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailability Limitation

Cloudflare Logpull is a REST API for consuming request logs over HTTP. These logs contain data related to the connecting client, the request path through the Cloudflare network, and the response from the origin web server. This data is useful for enriching existing logs on an origin server. Logpull is available to customers on the Enterprise plan.

Caution

Logpull is considered a legacy feature and we recommend using [Logpush](https://developers.cloudflare.com/logs/logpush/) or [Logs Engine](https://developers.cloudflare.com/logs/r2-log-retrieval/) instead for better performance and functionality.

Review the following content to learn more about Logpull.

  * [Understanding the basics](https://developers.cloudflare.com/logs/logpull/understanding-the-basics/)
  * [Enabling log retention](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/)
  * [Requesting logs](https://developers.cloudflare.com/logs/logpull/requesting-logs/)
  * [Additional details](https://developers.cloudflare.com/logs/logpull/additional-details/)



## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | No | No | Yes  
  
### Limitation

Logpull is unavailable when the Customer Metadata Boundary (CMB) is set outside the US region. Specifically, it does not work when CMB is restricted to the EU-only setting. For more details, refer to the [Cloudflare Data Localization](https://developers.cloudflare.com/data-localization/) documentation.

[PreviousLogs Engine](https://developers.cloudflare.com/logs/r2-log-retrieval/)[NextUnderstanding the basics](https://developers.cloudflare.com/logs/logpull/understanding-the-basics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpull/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

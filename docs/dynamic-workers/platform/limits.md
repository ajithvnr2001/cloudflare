---
url: https://developers.cloudflare.com/dynamic-workers/platform/limits/
title: Limits \u00b7 Cloudflare Dynamic Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:10.964702+00:00
---

# Limits · Cloudflare Dynamic Workers docs

> Source: https://developers.cloudflare.com/dynamic-workers/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)
  3. /Platform
  4. /Limits



# Limits

Last updated Aug 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dynamic-workers/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare limits the number of distinct Dynamic Workers with in-flight requests. Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.

Context | Concurrent Dynamic Workers  
---|---  
Worker request | 4  
[Durable Object](https://developers.cloudflare.com/durable-objects/) | 10 (previously 4)  
  
In a Worker, each request has its own input/output (I/O) context. Each request can therefore have up to four distinct Dynamic Workers with in-flight requests.

A Durable Object shares one I/O context across all concurrent requests to the same object. Those requests can collectively have up to ten distinct Dynamic Workers with in-flight requests. To set lower CPU time or subrequest limits, refer to [Custom resource limits](https://developers.cloudflare.com/dynamic-workers/usage/limits/).

[PreviousPricing](https://developers.cloudflare.com/dynamic-workers/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dynamic-workers/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

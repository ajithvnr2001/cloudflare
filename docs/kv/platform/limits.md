---
url: https://developers.cloudflare.com/kv/platform/limits/
title: Limits \u00b7 Cloudflare Workers KV docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:29.499438+00:00
---

# Limits · Cloudflare Workers KV docs

> Source: https://developers.cloudflare.com/kv/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[KV](https://developers.cloudflare.com/kv/)
  3. /Platform
  4. /Limits



# Limits

Last updated Oct 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWorkers KVWorkers KV InstantAdditional limits

## Workers KV

Feature | Free | Paid  
---|---|---  
Reads | 100,000 reads per day | Unlimited  
Writes to different keys | 1,000 writes per day | Unlimited  
Writes to same key | 1 per second | 1 per second  
Operations/Worker invocation 1 | 1000 | 1000  
Namespaces per account | 1,000 | 1,000  
Storage/account | 1 GB | Unlimited  
Storage/namespace | 1 GB | Unlimited  
Keys/namespace | Unlimited | Unlimited  
Key size | 512 bytes | 512 bytes  
Key metadata | 1024 bytes | 1024 bytes  
Value size | 25 MiB | 25 MiB  
Minimum [`cacheTtl`](https://developers.cloudflare.com/kv/api/read-key-value-pairs/#cachettl-parameter) 2 | 30 seconds | 30 seconds  
  
## Workers KV Instant

Note

Workers KV Instant is currently in private beta. To enroll, contact your Cloudflare account team or [sign up ↗︎](https://www.cloudflare.com/resource/workers-kv-instant-beta/) and tell us about your use case.

Feature | Limit  
---|---  
Writes/namespace | 1 per second  
Storage/namespace | 1 MB  
Keys/namespace | 10,000  
Key size | 300 bytes  
Key metadata | Not supported  
Value size | Any size that keeps the total namespace within 1 MB  
List pagination | Not supported. All matching keys are returned in one response.  
  
## Additional limits

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). If the limit can be increased, Cloudflare will contact you with next steps.

Free versus Paid plan pricing

Refer to [KV pricing](https://developers.cloudflare.com/kv/platform/pricing/) to review the specific KV operations you are allowed under each plan with their pricing.

Workers KV REST API limits

Using the REST API to access Cloudflare Workers KV is subject to the [rate limits that apply to all operations of the Cloudflare REST API](https://developers.cloudflare.com/fundamentals/api/reference/limits).

## Footnotes

  1. Within a single invocation, a Worker can make up to 1,000 operations to external services (for example, 500 Workers KV reads and 500 R2 reads). A bulk request to Workers KV counts for 1 request to an external service. ↩

  2. The maximum value is [`Number.MAX_SAFE_INTEGER` ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER). ↩




[PreviousPricing](https://developers.cloudflare.com/kv/platform/pricing/)[NextChoose a data or storage product ↗︎](https://developers.cloudflare.com/workers/platform/storage-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/kv/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

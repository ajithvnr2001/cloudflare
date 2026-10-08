---
url: https://developers.cloudflare.com/r2/platform/limits/
title: Limits \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:48.093258+00:00
---

# Limits · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /Platform
  4. /Limits



# Limits

Last updated Jun 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRate limiting on managed public buckets through r2.devCloudflare REST API

Feature | Limit  
---|---  
Data storage per bucket | Unlimited  
Number of objects per bucket | Unlimited  
Maximum number of buckets per account | 1,000,000  
Maximum rate of bucket management operations per bucket 1 | 50 per second  
Number of custom domains per bucket | 100  
Object key length | 1,024 bytes  
Object metadata size | 8,192 bytes  
Object size | 5 TiB per object 2  
Maximum upload size 3 | 5 GiB (single-part) / 4.995 TiB (multi-part) 4  
Maximum upload parts | 10,000  
Maximum concurrent writes to the same object name (key) | 1 per second 5  
  
Limits specified in MiB (mebibyte), GiB (gibibyte), or TiB (tebibyte) are storage units of measurement based on base-2. 1 GiB (gibibyte) is equivalent to 230 bytes (or 10243 bytes). This is distinct from 1 GB (gigabyte), which is 109 bytes (or 10003 bytes).

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). If the limit can be increased, Cloudflare will contact you with next steps.

## Rate limiting on managed public buckets through `r2.dev`

Managed public bucket access through an `r2.dev` subdomain is not intended for production usage and has a variable rate limit applied to it. The `r2.dev` endpoint for your bucket is designed to enable testing.

  * If you exceed the rate limit (hundreds of requests/second), requests to your `r2.dev` endpoint will be temporarily throttled and you will receive a `429 Too Many Requests` response.
  * Bandwidth (throughput) may also be throttled when using the `r2.dev` endpoint.



For production use cases, connect a [custom domain](https://developers.cloudflare.com/r2/buckets/public-buckets/#custom-domains) to your bucket. Custom domains allow you to serve content from a domain you control (for example, `assets.example.com`), configure fine-grained caching, set up redirect and rewrite rules, mutate content via [Cloudflare Workers](https://developers.cloudflare.com/workers/), and get detailed URL-level analytics for content served from your R2 bucket.

## Cloudflare REST API

The [Cloudflare REST API](https://developers.cloudflare.com/api/resources/r2/) is rate limited to 1,200 requests per five minutes across all R2 REST API operations on your account.

For high-throughput object operations, use the [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or [Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/) instead. The Cloudflare REST API is best suited for lower-volume management and configuration operations.

## Footnotes

  1. Bucket management operations include creating, deleting, listing, and configuring buckets. This limit does _not_ apply to reading or writing objects to a bucket. ↩

  2. The object size limit is 5 GiB less than 5 TiB, so 4.995 TiB. ↩

  3. Max upload size applies to uploading a file via one request, uploading a part of a multipart upload, or copying into a part of a multipart upload. If you have a Worker, its inbound request size is constrained by [Workers request limits](https://developers.cloudflare.com/workers/platform/limits#request-limits). The max upload size limit does not apply to subrequests. ↩

  4. The max upload size is 5 MiB less than 5 GiB, so 4.995 GiB. ↩

  5. Concurrent writes to the same object name (key) at a higher rate return HTTP 429 (rate limited) responses. ↩




[PreviousAudit Logs](https://developers.cloudflare.com/r2/platform/audit-logs/)[NextMetrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

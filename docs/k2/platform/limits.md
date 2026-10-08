---
url: https://developers.cloudflare.com/k2/platform/limits/
title: Limits \u00b7 Cloudflare K2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:39.134796+00:00
---

# Limits · Cloudflare K2 docs

> Source: https://developers.cloudflare.com/k2/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[K2](https://developers.cloudflare.com/k2/)
  3. /Platform
  4. /Limits



# Limits

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/k2/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccount limitsStreamsProduce recordsSubscriptions and consuming records

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). If the limit can be increased, Cloudflare will contact you with next steps.

## Account limits

During the public beta, each account can store up to 10 GB across all streams.

## Streams

Feature | Limit  
---|---  
Maximum streams per account | 20  
Minimum retention period | 1 hour (`3600` seconds)  
Maximum retention period | 30 days (`2592000` seconds)  
Default retention period | 7 days (`604800` seconds)  
  
Higher retention limits are available by request.

## Produce records

Feature | Limit  
---|---  
Maximum produce throughput per stream | 30 MB/s  
Maximum request size | 5 MB (5,000,000 bytes)  
Maximum record size | ~1 MB (1,000,000 bytes)  
Maximum headers per record | 32  
Maximum header name size | 256 bytes  
Maximum header value size | 8 KiB (8,192 bytes)  
Maximum total header size per record | 64 KiB (65,536 bytes)  
  
The maximum request size applies to the HTTP request body both before and after gzip decompression + a small amount of internal metadata. For the Workers binding, it applies to the total size of the records in a single `send()` call.

The maximum record size applies to the decoded record content, and to the record content and headers combined. Header sizes are measured in UTF-8 bytes.

There is no limit on the number of records in a request, other than the maximum request size.

The maximum produce throughput applies to the total data produced to a stream across all producers. To request a higher limit, refer to limit increases.

## Subscriptions and consuming records

Feature | Limit  
---|---  
Maximum `max_records` per consume request | 10,000  
Maximum data per consume response | 10 MB  
`worker_id` length | 1 to 256 characters  
Maximum active leases per subscription | 128  
Maximum subscriptions per stream | 100  
  
[PreviousPricing](https://developers.cloudflare.com/k2/platform/pricing/)[NextChoose a data or storage product ↗︎](https://developers.cloudflare.com/workers/platform/storage-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/k2/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

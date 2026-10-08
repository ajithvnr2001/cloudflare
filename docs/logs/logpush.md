---
url: https://developers.cloudflare.com/logs/logpush/
title: Logpush \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:10.081737+00:00
---

# Logpush · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /Logpush



# Logpush

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEstimating log volume Quick sizing for HTTP Requests Daily storage by traffic volumeLimitsAvailability

Logpush delivers logs in batches as quickly as possible, with no minimum batch size, potentially delivering files more than once per minute. This capability enables Cloudflare to provide information almost in real time, in smaller file sizes.

The push frequency is automatic and cannot be adjusted—Cloudflare pushes logs in batches as soon as possible. However, users can configure the batch size [using the API](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#max-upload-parameters) for improved control in case the log destination has specific requirements.

Important limitation

Logpush only pushes logs once as they become available and cannot backfill historical data. If your job is disabled or fails, logs generated during that period are permanently lost. This is why configuring [health notifications](https://developers.cloudflare.com/logs/logpush/logpush-health/) is essential for early detection of issues.

Logpush does not offer storage or search functionality for logs; its primary aim is to send logs as quickly as they arrive.

Cloudflare Logpush supports pushing logs to storage services, SIEMs, and log management providers via the Cloudflare dashboard or API.

## Estimating log volume

Before setting up a Logpush job, you can estimate the total volume of data that will be pushed to your destination. The volume depends on your traffic, selected fields, and compression.

### Quick sizing for HTTP Requests

A quick sizing estimate for an [HTTP Requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) dataset:

  * ~100–250 bytes per request (compressed, depending on fields selected)
  * 1M requests/day → ~100–250 MB/day
  * 30M requests/month → ~3–7.5 GB/month



### Daily storage by traffic volume

  * 100k req/day → ~25–50 MB/day
  * 1M req/day → ~250–500 MB/day
  * 10M req/day → ~2.5–5 GB/day
  * 100M req/day → ~25–50 GB/day



These ranges reflect field selection, compression, and whether you include extra fields or [custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/). Other datasets (Firewall, Workers, Load Balancing) add volume separately.

For precise estimates, you can [sample your logs via Logpull](https://developers.cloudflare.com/logs/logpull/additional-details/#estimating-daily-data-volume) using a 1-hour sample.

## Limits

There is currently a max limit of **4 Logpush jobs per zone**. Trying to create a job once the limit has been reached will result in an error message: `creating a new job is not allowed: exceeded max jobs allowed`.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
Dataset availability depends on the Cloudflare products on your account. Workers Trace Events Logpush requires the [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/#workers-trace-events-logpush) plan and retains separate request-based pricing.

For usage rates and included monthly usage, refer to [Pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

[PreviousFAQ](https://developers.cloudflare.com/logs/faq/)[NextPermissions](https://developers.cloudflare.com/logs/logpush/permissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/cloudflare-one/insights/logs/
title: Zero Trust logs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:50.536312+00:00
---

# Zero Trust logs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)
  4. /Logs



# Logs

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLog retentionLog Explorer Customer Metadata BoundaryData privacy

Review detailed logs for your Zero Trust organization.

  * [Dashboard logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)
  * [Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/)



## Log retention

Cloudflare stores Zero Trust logs for different periods of time based on the service and plan type:

| Free | Standard | Access | Gateway | Enterprise  
---|---|---|---|---|---  
**Admin logs** | 18 months | 18 months | 18 months | 18 months | 18 months  
**Access logs** | 24 hours | 30 days | 30 days | 24 hours | 180 days  
**DNS logs** | 24 hours | 30 days | 24 hours | 30 days | 180 days1  
**Network logs** | 24 hours | 30 days | 24 hours | 30 days | 30 days  
**HTTP logs** | 24 hours | 30 days | 24 hours | 30 days | 30 days  
**DEX logs** | 7 days | 7 days | 7 days | 7 days | 7 days  
**Device posture logs** | 30 days | 30 days | 30 days | 30 days | 30 days  
  
## Log Explorer Beta

Log Explorer users can store Zero Trust logs directly within Cloudflare in an [R2 bucket](https://developers.cloudflare.com/r2/) and access them with the dashboard or API. Log Explorer supports the following Zero Trust datasets:

  * [Access requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/) (`FROM access_requests`)
  * [CASB Findings](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/) (`FROM casb_findings`)
  * [Device posture results](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/device_posture_results/) (`FROM device_posture_results`)
  * [Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/) (`FROM gateway_dns`)
  * [Gateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/) (`FROM gateway_http`)
  * [Gateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/) (`FROM gateway_network`)
  * [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) (`FROM zero_trust_network_sessions`)



For more information, refer to [Log Explorer](https://developers.cloudflare.com/log-explorer/).

## Customer Metadata Boundary

You can use Cloudflare Zero Trust with the Data Localization Suite to restrict data storage to a specific geographic region. For more information, refer to [Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/).

## Data privacy

For more information on how we use this data, refer to our [Privacy Policy ↗︎](https://www.cloudflare.com/application/privacypolicy/).

## Footnotes

  1. Enterprise users on per query plans cannot store DNS logs via Cloudflare. You can still export logs via [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/). For more information, contact your account team. ↩




[PreviousBuckets](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/buckets/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/logs/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/
title: New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.700896+00:00
---

# New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-09-log-fields-updated/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 9, 2026

## New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has added new fields across multiple [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New dataset

  * **MCP Portal Logs** : A new dataset with fields including `ClientCountry`, `ClientIP`, `ColoCode`, `Datetime`, `Error`, `Method`, `PortalAUD`, `PortalID`, `PromptGetName`, `ResourceReadURI`, `ServerAUD`, `ServerID`, `ServerResponseDurationMs`, `ServerURL`, `SessionID`, `Success`, `ToolCallName`, `UserEmail`, and `UserID`.



#### New fields in existing datasets

  * **DEX Application Tests** : `HTTPRedirectEndMs`, `HTTPRedirectStartMs`, `HTTPResponseBody`, and `HTTPResponseHeaders`.
  * **DEX Device State Events** : `ExperimentalExtra`.
  * **Firewall Events** : `FraudUserID`.
  * **Gateway HTTP** : `AppControlInfo` and `ApplicationStatuses`.
  * **Gateway DNS** : `InternalDNSDurationMs`.
  * **HTTP Requests** : `FraudEmailRisk`, `FraudUserID`, and `PayPerCrawlStatus`.
  * **Network Analytics Logs** : `DNSQueryName`, `DNSQueryType`, and `PFPCustomTag`.
  * **WARP Toggle Changes** : `UserEmail`.
  * **WARP Config Changes** : `UserEmail`.
  * **Zero Trust Network Session Logs** : `SNI`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

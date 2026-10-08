---
url: https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/
title: New WebSocket Analytics Logpush dataset and updated fields \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:59.383177+00:00
---

# New WebSocket Analytics Logpush dataset and updated fields · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 24, 2026

## New WebSocket Analytics Logpush dataset and updated fields

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **WebSocket Analytics** : A new dataset with fields including `BytesReceivedClient`, `BytesReceivedOrigin`, `BytesSentClient`, `BytesSentOrigin`, `ClientASN`, `ClientIP`, `ClientRequestHost`, `ClientRequestPath`, `ClientRequestUserAgent`, `ColoCode`, `ConnectionCloseReason`, `ConnectionCloseSource`, `ConnectionID`, `ConnectionTransportCloseCode`, `EdgeEndTimestamp`, `EdgeStartTimestamp`, and `RayID`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `ZoneName`. The Firewall events dataset is now also available for [account-scope Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/), in addition to the existing zone scope.
  * **Email Security Alerts** (added): `BCC`, `DKIMResult`, `DMARCPolicy`, `DMARCResult`, and `SPFResult`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

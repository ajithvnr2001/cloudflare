---
url: https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/
title: New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:09.793328+00:00
---

# New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 20, 2026

## New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **Account Abuse Protection Events** : A new dataset with fields including `AuthenticationIdentityProvider`, `AuthenticationMethod`, `AuthenticationStatus`, `BotScore`, `ClientASN`, `ClientCity`, `ClientCountry`, `ClientIP`, `Email`, `EphemeralID`, `EventSource`, `EventType`, `FraudEmailRisk`, `Host`, `JA4`, `RayID`, `Timestamp`, `UserAgent`, and `UserID`.
  * **Magic BGP Logs** : A new dataset with fields including `Direction`, `EventData`, `EventKind`, `EventTimestamp`, `TunnelID`, and `TunnelName`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `AISecurityCustomTopicCategories`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.
  * **Gateway HTTP** (added): `ExperimentalFeatures` and `PackageInfo`.
  * **HTTP requests** (added): `AISecurityCustomTopicCategories`, `ClientTLSKeyExchangeGroup`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

---
url: https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/
title: New TenantID and Firewall for AI fields in Logpush datasets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.325001+00:00
---

# New TenantID and Firewall for AI fields in Logpush datasets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 15, 2026

## New TenantID and Firewall for AI fields in Logpush datasets

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has added new fields to multiple [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### TenantID field

The following Gateway and Zero Trust datasets now include a `TenantID` field:

  * **[Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/#tenantid)** : Identifies the tenant ID of the DNS request, if it exists.
  * **[Gateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/#tenantid)** : Identifies the tenant ID of the HTTP request, if it exists.
  * **[Gateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/#tenantid)** : Identifies the tenant ID of the network session, if it exists.
  * **[Zero Trust Network Sessions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#tenantid)** : Identifies the tenant ID of the network session, if it exists.



#### Firewall for AI fields

The following datasets now include [Firewall for AI](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/#firewall-for-ai) fields:

  * **[Firewall Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/)** :

    * `FirewallForAIInjectionScore`: The score indicating the likelihood of a prompt injection attack in the request.
    * `FirewallForAIPIICategories`: List of PII categories detected in the request.
    * `FirewallForAITokenCount`: The number of tokens in the request.
    * `FirewallForAIUnsafeTopicCategories`: List of unsafe topic categories detected in the request.
  * **[HTTP Requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/)** :

    * `FirewallForAIInjectionScore`: The score indicating the likelihood of a prompt injection attack in the request.
    * `FirewallForAIPIICategories`: List of PII categories detected in the request.
    * `FirewallForAITokenCount`: The number of tokens in the request.
    * `FirewallForAIUnsafeTopicCategories`: List of unsafe topic categories detected in the request.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

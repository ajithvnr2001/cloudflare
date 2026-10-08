---
url: https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/
title: TAXII support added to Threat Events API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:52.493981+00:00
---

# TAXII support added to Threat Events API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 6, 2026

## TAXII support added to Threat Events API

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudforce One Threat Events API now supports [**TAXII** ↗︎](https://www.cloudflare.com/en-gb/learning/security/what-is-stix-and-taxii/) as an output format, enabling standardized, automated sharing of cyber threat intelligence with your existing security stack.

#### Why this matters

  * You can now ingest Cloudforce One threat data directly into your SIEM, TIP or SOAR tools that prefer TAXII-formatted streams without needing custom translation scripts.
  * By supporting the TAXII format parameter in our API, security teams can automate the synchronization of indicator data, reducing the manual overhead of updating blocklists and detection rules.
  * This alignment with industry standards ensures that your threat data remains consistent across different security ecosystems and partner integrations.



#### How to use it

When calling the Threat Events API, you can now specify `taxii` in the `format` query parameter:

`GET /accounts/{account_id}/cloudforce_one/threat_events?format=taxii`

You can find the updated documentation in the [Cloudflare API Reference ↗︎](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list#%28resource%29%20cloudforce_one.threat_events%20%3E%20%28method%29%20list%20%3E%20%28params%29%20default%20%3E%20%28param%29%20format%20%3E%20%28schema%29).

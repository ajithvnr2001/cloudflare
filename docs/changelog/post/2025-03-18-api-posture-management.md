---
url: https://developers.cloudflare.com/changelog/post/2025-03-18-api-posture-management/
title: New API Posture Management for API Shield \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:06.683024+00:00
---

# New API Posture Management for API Shield · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-18-api-posture-management/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 18, 2025

## New API Posture Management for API Shield

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-18-api-posture-management/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, API Shield **automatically** labels your API inventory with API-specific risks so that you can track and manage risks to your APIs.

View these risks in [Endpoint Management](https://developers.cloudflare.com/api-shield/management-and-monitoring/) by label:

![A list of endpoint management labels](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2172,height=936,format=webp/_astro/endpoint-management-label.BDmf8Ai1.png)

...or in [Security Center Insights](https://developers.cloudflare.com/security/security-insights/):

![An example security center insight](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2250,height=1316,format=webp/_astro/posture-management-insight.7vB7mzGI.png)

API Shield will scan for risks on your API inventory daily. Here are the new risks we're scanning for and automatically labelling:

  * **cf-risk-sensitive** : applied if the customer is subscribed to the [sensitive data detection ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/sensitive-data-detection/) and the WAF detects sensitive data returned on an endpoint in the last seven days.
  * **cf-risk-missing-auth** : applied if the customer has configured a session ID and no successful requests to the endpoint contain the session ID.
  * **cf-risk-mixed-auth** : applied if the customer has configured a session ID and some successful requests to the endpoint contain the session ID while some lack the session ID.
  * **cf-risk-missing-schema** : added when a learned schema is available for an endpoint that has no active schema.
  * **cf-risk-error-anomaly** : added when an endpoint experiences a recent increase in response errors over the last 24 hours.
  * **cf-risk-latency-anomaly** : added when an endpoint experiences a recent increase in response latency over the last 24 hours.
  * **cf-risk-size-anomaly** : added when an endpoint experiences a spike in response body size over the last 24 hours.



In addition, API Shield has two new 'beta' scans for **Broken Object Level Authorization (BOLA) attacks**. If you're in the beta, you will see the following two labels when API Shield suspects an endpoint is suffering from a BOLA vulnerability:

  * **cf-risk-bola-enumeration** : added when an endpoint experiences successful responses with drastic differences in the number of unique elements requested by different user sessions.
  * **cf-risk-bola-pollution** : added when an endpoint experiences successful responses where parameters are found in multiple places in the request.



We are currently accepting more customers into our beta. Contact your account team if you are interested in BOLA attack detection for your API.

Refer to the [blog post ↗︎](https://blog.cloudflare.com/cloudflare-security-posture-management/) for more information about Cloudflare's expanded posture management capabilities.

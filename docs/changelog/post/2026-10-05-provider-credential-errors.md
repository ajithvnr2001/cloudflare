---
url: https://developers.cloudflare.com/changelog/post/2026-10-05-provider-credential-errors/
title: Standardize provider credential error responses in AI Gateway \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.330958+00:00
---

# Standardize provider credential error responses in AI Gateway · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-05-provider-credential-errors/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 6, 2026

## Standardize provider credential error responses in AI Gateway

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway's REST API now returns consistent responses when an AI provider rejects credentials. The change applies to [`POST /ai/run` ↗︎](https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT_ID%7D/ai/run).

Scenario | Previous AI Gateway response | New AI Gateway response  
---|---|---  
ElevenLabs | Provider-specific `UserCredentialsError` with HTTP `403` | HTTP `401` with error code `2009`  
Google Vertex | HTTP `500` for rejected credentials, with upstream retries | HTTP `401` with error code `2009`; the request fails without retrying the provider  
All other providers | HTTP `402` or another provider-specific status for rejected credentials | HTTP `401` with error code `2009`  
When using [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), the provider rejects the credentials | Provider-specific authentication error | HTTP `503`  
  
Update applications that handle AI Gateway REST API errors to treat HTTP `401` as an invalid or rejected provider credential.

For details about providing provider credentials, refer to [Bring your own provider keys](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-key/).

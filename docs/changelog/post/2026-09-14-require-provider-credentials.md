---
url: https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/
title: Prevent Unified Billing fallback for BYOK third-party providers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.408919+00:00
---

# Prevent Unified Billing fallback for BYOK third-party providers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-14-require-provider-credentials/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 14, 2026

## Prevent Unified Billing fallback for BYOK third-party providers

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.

Turn on **Require provider credentials** in your gateway settings. To use the API, set `byok_only` to `true` in the request body of a [`PUT` request to update the gateway](https://developers.cloudflare.com/api/resources/ai_gateway/methods/update/):
    
    
    {
    	"byok_only": true
    }

To require provider credentials for one third-party request, set the `cf-aig-no-wholesale` header to `true`. This header cannot relax the gateway setting.

Requests without applicable credentials then return an HTTP `400` response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.

For configuration details and request-level controls, refer to [Prevent Unified Billing fallback for BYOK third-party providers](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers).

---
url: https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/
title: Send CASB posture finding instances with webhooks \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.900970+00:00
---

# Send CASB posture finding instances with webhooks · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-09-casb-webhooks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 9, 2026

## Send CASB posture finding instances with webhooks

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use **CASB webhooks** in Cloudflare One to send posture finding instances to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.

This gives security teams a simple way to route CASB posture findings into the tools and workflows they already use for triage and response.

To get started, go to **Integrations** > **Webhooks** in the Cloudflare One dashboard to create a webhook destination. After you configure a webhook, open a posture finding instance and select **Send webhook** to send it.

#### Key capabilities

  * **Flexible authentication** — Configure destinations using **None** , **Basic Auth** , **Bearer Auth** , **Static Headers** , or **HMAC-Signing**.
  * **Built-in testing** — Use **Test delivery** to send a test request before sending a live finding instance.
  * **Posture finding workflows** — Send posture finding instances directly from the finding details workflow in **Cloud & SaaS findings**.
  * **HTTPS destinations** — Configure webhook destinations with public `https://` URLs.



#### Learn more

  * Configure [CASB webhooks](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/) in Cloudflare.
  * Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare.



CASB webhooks are now available in Cloudflare One.

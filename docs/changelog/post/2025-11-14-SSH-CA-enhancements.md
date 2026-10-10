---
url: https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/
title: Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.636184+00:00
---

# Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-14-SSH-CA-enhancements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 14, 2025

## Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

SSH with [Cloudflare Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/) allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.

Previously, users had to generate this certificate by using the [Cloudflare API ↗︎](https://developers.cloudflare.com/api/) directly. With this update, you can now create and manage this certificate in the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com) from the **Access controls** > **Service credentials** page.

![Navigate to Access controls and then Service credentials to see where you can generate an SSH CA](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2710,height=1180,format=webp/_astro/SSH-CA-generation.DYa9RnX1.png)

For more details, refer to [Generate a Cloudflare SSH CA](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca).

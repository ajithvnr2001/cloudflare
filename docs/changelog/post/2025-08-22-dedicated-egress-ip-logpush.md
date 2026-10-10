---
url: https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/
title: Dedicated Egress IP for Logpush \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.753043+00:00
---

# Dedicated Egress IP for Logpush · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-22-dedicated-egress-ip-logpush/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 22, 2025

## Dedicated Egress IP for Logpush

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with [Aegis IP](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/), your log destination only needs to allow Aegis IPs making setup more secure.

Highlights:

  * Fixed egress IPs ensure your destination only accepts traffic from known addresses.
  * Works with any supported Logpush destination.
  * Recommended to use a dedicated zone as a proxy for easier management.



To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the [Logpush documentation](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/).

---
url: https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/
title: Steer Traffic by AS Number in Load Balancing Custom Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.112379+00:00
---

# Steer Traffic by AS Number in Load Balancing Custom Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 15, 2025

## Steer Traffic by AS Number in Load Balancing Custom Rules

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.

This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.

![Create a Load Balancing Custom Rule using AS Num](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2554,height=1472,format=webp/_astro/asnum-custom-rule.CtcHu_zj.png)

To get started, create a [Custom Rule ↗︎](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/) in your Load Balancer and select **AS Num** from the **Field** dropdown.

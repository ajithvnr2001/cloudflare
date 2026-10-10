---
url: https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/
title: FQDN Filtering For Gateway Egress Policies \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.700189+00:00
---

# FQDN Filtering For Gateway Egress Policies · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 28, 2025

## FQDN Filtering For Gateway Egress Policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.

  * Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.
  * During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation. 
    * For WARP client support, additional configuration is required. For more information, refer to the [WARP client configuration documentation](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#limitations).

![Egress by FQDN and Hostname](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=841,height=1045,format=webp/_astro/Gateway-Egress-FQDN-Policy-preview.Civon5p8.png)

This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.

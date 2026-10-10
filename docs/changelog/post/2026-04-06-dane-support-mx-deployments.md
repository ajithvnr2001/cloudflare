---
url: https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/
title: DANE Support for MX Deployments \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.087058+00:00
---

# DANE Support for MX Deployments · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 6, 2026

## DANE Support for MX Deployments

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email Security now supports DANE (DNS-based Authentication of Named Entities) for MX deployments. This enhancement strengthens email transport security by enabling DNSSEC-backed certificate verification for our regional MX records.

  * Regional MX hostnames now publish DANE TLSA records backed by DNSSEC, enabling DANE-capable SMTP senders to cryptographically validate certificate identities before establishing TLS connections—moving beyond opportunistic encryption to verified encrypted delivery.
  * DANE support is automatically available for all customers using regional MX deployments. No additional configuration is required; DANE-capable mail infrastructure will automatically validate MX certificates using the published records.



This applies to all Email Security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



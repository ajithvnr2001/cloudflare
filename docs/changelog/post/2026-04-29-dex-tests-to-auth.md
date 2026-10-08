---
url: https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/
title: Digital experience tests to authenticated resources and enhanced configuration \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:50.237547+00:00
---

# Digital experience tests to authenticated resources and enhanced configuration · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 29, 2026

## Digital experience tests to authenticated resources and enhanced configuration

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Digital experience tests](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via [Cloudflare Secret Store](https://developers.cloudflare.com/secrets-store/).

Digital experience tests also have enhanced configuration options including:

  * New HTTP methods (DELETE, PATCH, POST, PUT)
  * Secret Store headers, custom plain text headers, and custom request bodies
  * Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates

![Digital experience test configuration for Cloudflare Access applications](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1374,format=webp/_astro/dex_test_auth_config.CD3G3zb_.png)![Digital experience enhanced test configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1496,format=webp/_astro/dex_test_enhanced_config.Nsv7Vcob.png)

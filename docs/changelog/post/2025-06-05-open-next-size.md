---
url: https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/
title: Performance and size optimization for the Cloudflare adapter for Open Next \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.860357+00:00
---

# Performance and size optimization for the Cloudflare adapter for Open Next · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-05-open-next-size/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 5, 2025

## Performance and size optimization for the Cloudflare adapter for Open Next

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

With the release of the Cloudflare adapter for Open Next v1.0.0 in May 2025, we already had followups plans [to improve performance and size ↗︎](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/#1-0-and-the-road-ahead).

`@opennextjs/cloudflare` v1.2 released on June 5, 2025 delivers on these enhancements. By removing `babel` from the app code and dropping a dependency on `@ampproject/toolbox-optimizer`, we were able to reduce generated bundle sizes. Additionally, by stopping preloading of all app routes, we were able to improve the cold start time.

This means that users will now see a decrease from 14 to 8MiB (2.3 to 1.6MiB gzipped) in generated bundle size for a Next app created via create-next-app, and typically 100ms faster startup times for their medium-sized apps.

Users only need to update to the latest version of `@opennextjs/cloudflare` to automatically benefit from these improvements.

Note that we published [CVE-2005-6087 ↗︎](https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m) for a SSRF vulnerability in the `@opennextjs/cloudflare` package. The vulnerability has been fixed from `@opennextjs/cloudflare` v1.3.0 onwards. Please update to any version after this one.

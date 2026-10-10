---
url: https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/
title: Build image policies for Workers Builds and Cloudflare Pages \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.199039+00:00
---

# Build image policies for Workers Builds and Cloudflare Pages · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-01-build-image-policies-dev-plat/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 18, 2025

## Build image policies for Workers Builds and Cloudflare Pages

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've published build image policies for [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#build-image-policy) and [Cloudflare Pages](https://developers.cloudflare.com/pages/configuration/build-image/#build-image-policy), which establish:

  * **Minor version updates** : We typically update preinstalled software to the latest available minor version without notice. For tools that don't follow semantic versioning (e.g., Bun or Hugo), we provide 3 months’ notice.
  * **Major version updates** : Before preinstalled software reaches end-of-life, we update to the next stable LTS version with 3 months’ notice.
  * **Build image version deprecation (Pages only)** : We provide 6 months’ notice before deprecation. Projects on v1 or v2 will be automatically moved to v3 on their specified deprecation dates.



To prepare for updates, monitor the [Cloudflare Changelog ↗︎](https://developers.cloudflare.com/changelog/), dashboard notifications, and email. You can also [override default versions](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#overriding-default-versions) to maintain specific versions.

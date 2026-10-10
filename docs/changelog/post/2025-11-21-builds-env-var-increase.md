---
url: https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/
title: Environment variable limits increase for Workers Builds \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.521530+00:00
---

# Environment variable limits increase for Workers Builds · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-21-builds-env-var-increase/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 21, 2025

## Environment variable limits increase for Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) now supports up to 64 environment variables, and each environment variable can be up to 5 KB in size. The previous limit was 5 KB total across all environment variables.

This change enables better support for complex build configurations, larger application settings, and more flexible CI/CD workflows.

For more details, refer to the [build limits documentation](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/#definitions).

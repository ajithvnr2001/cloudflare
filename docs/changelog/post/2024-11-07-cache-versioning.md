---
url: https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/
title: Stage and test cache configurations safely \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:59.691963+00:00
---

# Stage and test cache configurations safely · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 7, 2024

## Stage and test cache configurations safely

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-07-cache-versioning/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now stage and test cache configurations before deploying them to production. Versioned environments let you safely validate cache rules, purge operations, and configuration changes without affecting live traffic.

#### How it works

With versioned environments, you can:

  1. **Create staging versions** of your cache configuration.
  2. **Test cache rules** in a non-production environment.
  3. **Purge staged content** independently from production.
  4. **Validate changes** before promoting to production.



This capability integrates with Cloudflare's broader [versioning system](https://developers.cloudflare.com/version-management/), allowing you to manage cache configurations alongside other zone settings.

#### Benefits

  * **Risk-free testing** : Validate configuration changes without impacting production.
  * **Independent purging** : Clear staging cache without affecting live content.
  * **Deployment confidence** : Catch issues before they reach end users.
  * **Team collaboration** : Multiple team members can work on different versions.



#### Get started

To get started, refer to the [version management documentation](https://developers.cloudflare.com/version-management/).

Important limitation

Cache Reserve is only supported for your production environment. Staged environments can use standard cache functionality, but Cache Reserve persistence is limited to production deployments.

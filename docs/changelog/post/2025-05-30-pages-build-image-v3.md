---
url: https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/
title: Cloudflare Pages builds now provide Node.js v22 by default \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:13.297409+00:00
---

# Cloudflare Pages builds now provide Node.js v22 by default · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 30, 2025

## Cloudflare Pages builds now provide Node.js v22 by default

[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you use the built-in build system that is part of [Cloudflare Pages](https://developers.cloudflare.com/pages/), the [Build Image](https://developers.cloudflare.com/pages/configuration/build-image/) now includes Node.js v22. Previously, Node.js v18 was provided by default, and Node.js v18 is now end-of-life (EOL).

If you are creating a new Pages project, the new V3 build image that includes Node.js v22 will be used by default. If you have an existing Pages project, you can update to the latest build image by navigating to Settings > Build & deployments > Build system version in the Cloudflare dashboard for a specific Pages project.

Note that you can always specify a particular version of Node.js or other built-in dependencies by [setting an environment variable](https://developers.cloudflare.com/pages/configuration/build-image/#override-default-versions).

For more, refer to the [developer docs for Cloudflare Pages builds](https://developers.cloudflare.com/pages/configuration/build-image)

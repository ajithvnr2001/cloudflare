---
url: https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/
title: Node.js 24 is now the default for Workers Builds \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.003379+00:00
---

# Node.js 24 is now the default for Workers Builds · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-30-workers-builds-nodejs-24/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 30, 2026

## Node.js 24 is now the default for Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers Builds now uses Node.js 24.18.0 by default. The build image preinstalls Node.js 22.23.2 and 24.18.0.

You can continue to override the default with the `NODE_VERSION` environment variable, an `.nvmrc` file, or a `.node-version` file. For more information, refer to [Override default versions](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#overriding-default-versions).

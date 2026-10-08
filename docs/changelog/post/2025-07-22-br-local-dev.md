---
url: https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/
title: Browser Rendering now supports local development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:17.325573+00:00
---

# Browser Rendering now supports local development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 22, 2025

## Browser Rendering now supports local development

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-22-br-local-dev/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run your Browser Rendering locally using `npx wrangler dev`, which spins up a browser directly on your machine before deploying to Cloudflare's global network. By running tests locally, you can quickly develop, debug, and test changes without needing to deploy or worry about usage costs.

Get started with this [example guide](https://developers.cloudflare.com/browser-run/how-to/deploy-worker/) that shows how to use Cloudflare's [fork of Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/) (you can also use [Playwright](https://developers.cloudflare.com/browser-run/playwright/)) to take screenshots of webpages and store the results in [Workers KV](https://developers.cloudflare.com/kv/).

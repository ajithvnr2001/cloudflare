---
url: https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/
title: Quick Editor devtools replaced with log viewer \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.980781+00:00
---

# Quick Editor devtools replaced with log viewer · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 16, 2026

## Quick Editor devtools replaced with log viewer

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has deprecated the Workers Quick Editor dev tools inspector and replaced it with a lightweight log viewer.

This aligns our logging with `wrangler tail` and gives us the opportunity to focus our efforts on bringing benefits from the work we have invested in observability, which would not be possible otherwise.

We have made improvements to this logging viewer based on your feedback such that you can log object and array types, and easily clear the list of logs. This does not include class instances. Limitations are documented in the [Workers Playground docs](https://developers.cloudflare.com/workers/playground/).

If you do need to develop your Worker with a remote inspector, you can still do this using Wrangler locally. Cloning a project from your quick editor to your computer for local development can be done with the `wrangler init --from-dash` command. For more information, refer to [Wrangler commands](https://developers.cloudflare.com/workers/wrangler/commands/general/#init).

---
url: https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/
title: Capture Wrangler command output in structured format \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.184468+00:00
---

# Capture Wrangler command output in structured format · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2025

## Capture Wrangler command output in structured format

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now capture Wrangler command output in a structured [ND-JSON ↗︎](https://github.com/ndjson/ndjson-spec) format by setting the [`WRANGLER_OUTPUT_FILE_PATH`](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/#supported-environment-variables) or [`WRANGLER_OUTPUT_FILE_DIRECTORY`](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/#supported-environment-variables) environment variables. This feature is particularly useful for CI/CD pipelines and automation tools that need programmatic access to deployment information such as worker names, version IDs, deployment URLs, and error details. Commands that support this feature include [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy), [`wrangler versions upload`](https://developers.cloudflare.com/workers/wrangler/commands/#versions), [`wrangler versions deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#versions), and [`wrangler pages deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy-1).

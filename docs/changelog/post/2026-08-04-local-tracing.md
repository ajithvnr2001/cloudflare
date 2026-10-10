---
url: https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/
title: AI agents can debug Workers with local tracing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.638450+00:00
---

# AI agents can debug Workers with local tracing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2026

## AI agents can debug Workers with local tracing

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`wrangler dev` and `vite dev` automatically capture structured OpenTelemetry traces and correlated console logs during local Worker invocations.

#### Debug with AI agents

When the tooling detects an AI agent session, it prints a terminal hint pointing to the [Local Explorer API](https://developers.cloudflare.com/workers/local-development/local-explorer/#api) at `/cdn-cgi/local/explorer/api`. The API serves an OpenAPI schema and exposes a read-only observability query endpoint for discovering telemetry, querying traces and logs, and inspecting binding state.

The agent can identify the exact failing operation, fix the code, rerun the request, and verify the result. This debug loop requires no deployment or temporary logs.

#### Inspect traces in Local Explorer

Humans can inspect the same [traces](https://developers.cloudflare.com/workers/observability/traces/) and correlated console logs in the Local Explorer browser UI. Each trace shows spans, timing, attributes, and errors.

![Local Explorer showing a failed Worker trace with spans, timing, and errors](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2048,height=847,format=webp/_astro/local-trace-failed-request.Bf0avznU.png)

Automatic spans cover handler calls, outbound `fetch()` calls, and binding calls. Custom spans appear alongside these automatic spans.

For more details, refer to the [Local Explorer documentation](https://developers.cloudflare.com/workers/local-development/local-explorer/).

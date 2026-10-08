---
url: https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/
title: Browser Run adds WebMCP to Kitesurf and moves to document.modelContext \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:16.758169+00:00
---

# Browser Run adds WebMCP to Kitesurf and moves to document.modelContext · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 28, 2026

## Browser Run adds WebMCP to Kitesurf and moves to document.modelContext

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/) now works in [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) sessions as well as [Lab sessions](https://developers.cloudflare.com/browser-run/features/webmcp/#get-started). Both backends use the `document.modelContext` API from the [WebMCP Community Group draft ↗︎](https://webmachinelearning.github.io/webmcp/). Lab sessions no longer expose `navigator.modelContextTesting`.

To list and run page tools:

  * **Chrome DevTools** : Use the **Application** > **WebMCP** panel in the live view of a Lab session or in the [Kitesurf playground ↗︎](https://kitesurf.dev/).
  * **AI agents** : Start [Chrome DevTools MCP](https://developers.cloudflare.com/browser-run/features/webmcp/#using-an-ai-agent) with the `--category-experimental-webmcp` flag to add the `list_webmcp_tools` and `execute_webmcp_tool` tools.
  * **CDP clients** : Use the `WebMCP` CDP domain.



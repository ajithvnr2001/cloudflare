---
url: https://developers.cloudflare.com/workers/observability/dev-tools/
title: DevTools \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:34.183384+00:00
---

# DevTools · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/observability/dev-tools/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Observability](https://developers.cloudflare.com/workers/observability/)
  4. /DevTools



# DevTools

Last updated Jun 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/observability/dev-tools/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUsing DevToolsOpening DevTools Wrangler Vite Dashboard editor & playgroundRelated resources

## Using DevTools

When running your Worker locally using the [Wrangler CLI ↗︎](https://developers.cloudflare.com/workers/wrangler/) (`wrangler dev`) or using [Vite ↗︎](https://vite.dev/) with the [Cloudflare Vite plugin ↗︎](https://developers.cloudflare.com/workers/vite-plugin/), you automatically have access to [Cloudflare's implementation ↗︎](https://github.com/cloudflare/workers-sdk/tree/main/packages/chrome-devtools-patches) of [Chrome DevTools ↗︎](https://developer.chrome.com/docs/devtools/overview).

You can use Chrome DevTools to:

  * View logs directly in the Chrome console
  * [Debug code by setting breakpoints](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/)
  * [Profile CPU usage](https://developers.cloudflare.com/workers/observability/dev-tools/cpu-usage/)
  * [Observe memory usage and debug memory leaks in your code that can cause out-of-memory (OOM) errors](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/)



## Opening DevTools

### Wrangler

  * Run your Worker locally, by running `wrangler dev`
  * Press the `D` key from your terminal to open DevTools in a browser tab



### Vite

  * Run your Worker locally by running `vite`
  * In a new Chrome tab, open the debug URL that shows in your console (for example, `http://localhost:5173/__debug`)



### Dashboard editor & playground

Both the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and the [Worker's Playground ↗︎](https://workers.cloudflare.com/playground) include DevTools in the UI.

## Related resources

  * [Local development](https://developers.cloudflare.com/workers/local-development/) \- Develop your Workers and connected resources locally via Wrangler and workerd, for a fast, accurate feedback loop.



[PreviousKnown limitations](https://developers.cloudflare.com/workers/observability/traces/known-limitations/)[NextBreakpoints](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/observability/dev-tools/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

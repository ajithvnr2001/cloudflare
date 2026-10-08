---
url: https://developers.cloudflare.com/workers/runtime-apis/handlers/
title: Handlers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:44.100298+00:00
---

# Handlers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/handlers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)
  4. /Handlers



# Handlers

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/handlers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHandlers in Python Workers

Handlers are methods on Workers that can receive and process external inputs, and can be invoked from outside your Worker. For example, the `fetch()` handler receives an HTTP request, and can return a response:
    
    
    export default {
    	async fetch(request, env, ctx) {
    		return new Response('Hello World!');
    	},
    };

The following handlers are available within Workers:

  * [Alarm Handler](https://developers.cloudflare.com/durable-objects/api/alarms/)
  * [Email Handler](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/)
  * [Fetch Handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/)
  * [Queue Handler](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer)
  * [Scheduled Handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/)
  * [Tail Handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/)



## Handlers in Python Workers

When you [write Workers in Python](https://developers.cloudflare.com/workers/languages/python/), handlers are placed in a class named `Default` that extends the [`WorkerEntrypoint` class](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/) (which you can import from the `workers` SDK module).

[PreviousFetch](https://developers.cloudflare.com/workers/runtime-apis/fetch/)[NextAlarm Handler ↗︎](https://developers.cloudflare.com/durable-objects/api/alarms/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/handlers/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

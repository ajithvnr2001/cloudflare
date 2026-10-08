---
url: https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/
title: Fetch Handler \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:44.187059+00:00
---

# Fetch Handler · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/)
  5. /Fetch Handler



# Fetch Handler

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackground Parameters

## Background

Incoming HTTP requests to a Worker are passed to the `fetch()` handler as a [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) object. To respond to the request with a response, return a [`Response`](https://developers.cloudflare.com/workers/runtime-apis/response/) object:
    
    
    export default {
    	async fetch(request, env, ctx) {
    		return new Response('Hello World!');
    	},
    };

Note

The Workers runtime does not support `XMLHttpRequest` (XHR). Learn the difference between `XMLHttpRequest` and `fetch()` in the [MDN ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) documentation.

### Parameters

  * `request` Request

    * The incoming HTTP request.
  * `env` object

    * The [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) available to the Worker. As long as the [environment](https://developers.cloudflare.com/workers/wrangler/environments/) has not changed, the same object (equal by identity) may be passed to multiple requests. You can also [import `env` from `cloudflare:workers`](https://developers.cloudflare.com/workers/runtime-apis/bindings/#importing-env-as-a-global) to access bindings from anywhere in your code.
  * `ctx.waitUntil(promisePromise)` : void

    * Refer to [`waitUntil`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil).
  * `ctx.passThroughOnException()` : void

    * Refer to [`passThroughOnException`](https://developers.cloudflare.com/workers/runtime-apis/context/#passthroughonexception).



[PreviousEmail Handler ↗︎](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/)[NextQueue Handler ↗︎](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/handlers/fetch.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

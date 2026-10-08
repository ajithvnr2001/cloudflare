---
url: https://developers.cloudflare.com/workers/testing/miniflare/core/standards/
title: Web Standards \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:54.962290+00:00
---

# Web Standards · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/core/standards/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Core
  5. /Web Standards



# Web Standards

Last updated Jan 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/standards/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMocking Outbound fetch RequestsSubrequests

  * [Web Standards Reference](https://developers.cloudflare.com/workers/runtime-apis/web-standards)
  * [Encoding Reference](https://developers.cloudflare.com/workers/runtime-apis/encoding)
  * [Fetch Reference](https://developers.cloudflare.com/workers/runtime-apis/fetch)
  * [Request Reference](https://developers.cloudflare.com/workers/runtime-apis/request)
  * [Response Reference](https://developers.cloudflare.com/workers/runtime-apis/response)
  * [Streams Reference](https://developers.cloudflare.com/workers/runtime-apis/streams)
  * [Web Crypto Reference](https://developers.cloudflare.com/workers/runtime-apis/web-crypto)



## Mocking Outbound `fetch` Requests

When using the API, Miniflare allows you to substitute custom `Response`s for `fetch()` calls using `undici`'s [`MockAgent` API ↗︎](https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentgetorigin). This is useful for testing Workers that make HTTP requests to other services. To enable `fetch` mocking, create a [`MockAgent` ↗︎](https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentgetorigin) using the `createFetchMock()` function, then set this using the `fetchMock` option.
    
    
    import { Miniflare, createFetchMock } from "miniflare";
    
    // Create `MockAgent` and connect it to the `Miniflare` instance
    const fetchMock = createFetchMock();
    const mf = new Miniflare({
    	modules: true,
    	script: `
      export default {
        async fetch(request, env, ctx) {
          const res = await fetch("https://example.com/thing");
          const text = await res.text();
          return new Response(\`response:\${text}\`);
        }
      }
      `,
    	fetchMock,
    });
    
    // Throw when no matching mocked request is found
    // (see https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentdisablenetconnect)
    fetchMock.disableNetConnect();
    
    // Mock request to https://example.com/thing
    // (see https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentgetorigin)
    const origin = fetchMock.get("https://example.com");
    // (see https://undici.nodejs.org/#/docs/api/MockPool?id=mockpoolinterceptoptions)
    origin
    	.intercept({ method: "GET", path: "/thing" })
    	.reply(200, "Mocked response!");
    
    const res = await mf.dispatchFetch("http://localhost:8787/");
    console.log(await res.text()); // "response:Mocked response!"

## Subrequests

Miniflare does not support limiting the amount of [subrequests](https://developers.cloudflare.com/workers/platform/limits#account-plan-limits). Please keep this in mind if you make a large amount of subrequests from your Worker.

[PreviousVariables and Secrets](https://developers.cloudflare.com/workers/testing/miniflare/core/variables-secrets/)[NextWebSockets](https://developers.cloudflare.com/workers/testing/miniflare/core/web-sockets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/core/standards.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

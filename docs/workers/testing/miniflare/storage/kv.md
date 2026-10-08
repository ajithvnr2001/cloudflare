---
url: https://developers.cloudflare.com/workers/testing/miniflare/storage/kv/
title: KV \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:56.283365+00:00
---

# KV · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/storage/kv/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Storage
  5. /KV



# KV

Last updated Jan 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/storage/kv/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNamespacesManipulating Outside Workers

  * [KV Reference](https://developers.cloudflare.com/kv/api/)



## Namespaces

Specify KV namespaces to add to your environment as follows:
    
    
    const mf = new Miniflare({
    	kvNamespaces: ["TEST_NAMESPACE1", "TEST_NAMESPACE2"],
    });

You can now access KV namespaces in your workers:
    
    
    export default {
    	async fetch(request, env) {
    		return new Response(await env.TEST_NAMESPACE1.get("key"));
    	},
    };

Miniflare supports all KV operations and data types.

## Manipulating Outside Workers

For testing, it can be useful to put/get data from KV outside a worker. You can do this with the `getKVNamespace` method:
    
    
    import { Miniflare } from "miniflare";
    
    const mf = new Miniflare({
    	modules: true,
    	script: `
      export default {
        async fetch(request, env, ctx) {
          const value = parseInt(await env.TEST_NAMESPACE.get("count")) + 1;
          await env.TEST_NAMESPACE.put("count", value.toString());
          return new Response(value.toString());
        },
      }
      `,
    	kvNamespaces: ["TEST_NAMESPACE"],
    });
    
    const ns = await mf.getKVNamespace("TEST_NAMESPACE");
    await ns.put("count", "1");
    
    const res = await mf.dispatchFetch("http://localhost:8787/");
    console.log(await res.text()); // 2
    console.log(await ns.get("count")); // 2

[PreviousDurable Objects](https://developers.cloudflare.com/workers/testing/miniflare/storage/durable-objects/)[NextR2](https://developers.cloudflare.com/workers/testing/miniflare/storage/r2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/storage/kv.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

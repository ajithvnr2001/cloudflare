---
url: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/
title: Service bindings - HTTP \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:42.308734+00:00
---

# Service bindings - HTTP · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)[Bindings (env)](https://developers.cloudflare.com/workers/runtime-apis/bindings/)

  4. /[Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)
  5. /HTTP



# HTTP

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Worker A that declares a Service binding to Worker B can forward a [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) object to Worker B, by calling the `fetch()` method that is exposed on the binding object.

For example, consider the following Worker that implements a [`fetch()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/):
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "worker_b",
    	"main": "./src/workerB.js"
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "worker_b"
    main = "./src/workerB.js"
    
    
    export default {
      async fetch(request, env, ctx) {
        return new Response("Hello World!");
      }
    }

The following Worker declares a binding to the Worker above:
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "worker_a",
    	"main": "./src/workerA.js",
    	"services": [
    		{
    			"binding": "WORKER_B",
    			"service": "worker_b"
    		}
    	]
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "worker_a"
    main = "./src/workerA.js"
    
    [[services]]
    binding = "WORKER_B"
    service = "worker_b"

And then can forward a request to it:
    
    
    export default {
    	async fetch(request, env) {
    		return await env.WORKER_B.fetch(request);
    	},
    };

Note

If you construct a new request manually, rather than forwarding an existing one, ensure that you provide a valid and fully-qualified URL with a hostname. For example:
    
    
    export default {
      async fetch(request, env) {
        // provide a valid URL
        let newRequest = new Request("https://valid-url.com", { method: "GET" });
        let response = await env.WORKER_B.fetch(newRequest);
        return response;
      }
    };

[PreviousOverview](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)[NextRPC (WorkerEntrypoint)](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/bindings/service-bindings/http.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

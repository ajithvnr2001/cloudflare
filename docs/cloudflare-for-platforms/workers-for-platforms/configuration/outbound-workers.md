---
url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/
title: Outbound Workers \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:04.628414+00:00
---

# Outbound Workers · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

  4. /Configuration
  5. /Outbound Workers



# Outbound Workers

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGeneral Use CasesUse Outbound Workers

Outbound Workers sit between your customer's Workers and the public Internet. They give you visibility into all outgoing `fetch()` requests from user Workers.

![Outbound Workers diagram information](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1100,height=400,format=webp/_astro/outbound-worker-diagram.BSvN4KG0.png)

## General Use Cases

Outbound Workers can be used to:

  * Log all subrequests to identify malicious domains or usage patterns.
  * Create, allow, or block lists for hostnames requested by user Workers.
  * Configure authentication to your APIs behind the scenes (without end developers needing to set credentials).



Note

When an Outbound Worker is enabled, your customer's Worker will no longer be able to use the [`connect() API`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#connect) to create outbound TCP Sockets. This is to ensure all outbound communication goes through the Outbound Worker's `fetch` method.

## Use Outbound Workers

To use Outbound Workers:

  1. Create a Worker intended to serve as your Outbound Worker.
  2. Outbound Worker can be specified as an optional parameter in the [dispatch namespaces](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/) binding in a project's [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). Optionally, to pass data from your dynamic dispatch Worker to the Outbound Worker, the variable names can be specified under **parameters**.



Make sure that you have `wrangler@3.3.0` or later [installed](https://developers.cloudflare.com/workers/wrangler/install-and-update/).
    
    
    {
    	"dispatch_namespaces": [
    		{
    			"binding": "dispatcher",
    			"namespace": "<NAMESPACE_NAME>",
    			"outbound": {
    				"service": "<SERVICE_NAME>",
    				"parameters": [
    					"params_object"
    				]
    			}
    		}
    	]
    }
    
    
    [[dispatch_namespaces]]
    binding = "dispatcher"
    namespace = "<NAMESPACE_NAME>"
    
      [dispatch_namespaces.outbound]
      service = "<SERVICE_NAME>"
      parameters = [ "params_object" ]

  3. Edit your dynamic dispatch Worker to call the Outbound Worker and declare variables to pass on `dispatcher.get()`.


    
    
    export default {
    	async fetch(request, env) {
    		try {
    			// parse the URL, read the subdomain
    			let workerName = new URL(request.url).host.split(".")[0];
    
    			let context_from_dispatcher = {
    				customer_name: workerName,
    				url: request.url,
    			};
    
    			let userWorker = env.dispatcher.get(
    				workerName,
    				{},
    				{
    					// outbound arguments. object name must match parameters in the binding
    					outbound: {
    						params_object: context_from_dispatcher,
    					},
    				},
    			);
    			return await userWorker.fetch(request);
    		} catch (e) {
    			if (e.message.startsWith("Worker not found")) {
    				// we tried to get a worker that doesn't exist in our dispatch namespace
    				return new Response("", { status: 404 });
    			}
    			return new Response(e.message, { status: 500 });
    		}
    	},
    };

  4. The Outbound Worker will now be invoked on any `fetch()` requests from a user Worker. The user Worker will trigger a [FetchEvent](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/) on the Outbound Worker. The variables declared in the binding can be accessed in the Outbound Worker through `env.<VAR_NAME>`.



The following is an example of an Outbound Worker that logs the fetch request from user Worker and creates a JWT if the fetch request matches `api.example.com`.
    
    
    export default {
    	// this event is fired when the dispatched Workers make a subrequest
    	async fetch(request, env, ctx) {
    		// env contains the values we set in `dispatcher.get()`
    		const customer_name = env.customer_name;
    		const original_url = env.url;
    
    		// log the request
    		ctx.waitUntil(
    			fetch("https://logs.example.com", {
    				method: "POST",
    				body: JSON.stringify({
    					customer_name,
    					original_url,
    				}),
    			}),
    		);
    
    		const url = new URL(original_url);
    		if (url.host === "api.example.com") {
    			// pre-auth requests to our API
    			const jwt = make_jwt_for_customer(customer_name);
    
    			let headers = new Headers(request.headers);
    			headers.set("Authorization", `Bearer ${jwt}`);
    
    			// clone the request to set new headers using existing body
    			let new_request = new Request(request, { headers });
    
    			return fetch(new_request);
    		}
    
    		return fetch(request);
    	},
    };

Note

Outbound Workers do not intercept fetch requests made from [Durable Objects](https://developers.cloudflare.com/durable-objects/) or [mTLS certificate bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls/).

[PreviousObservability](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/observability/)[NextStatic assets](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

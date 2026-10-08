---
url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/
title: Custom limits \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:04.578743+00:00
---

# Custom limits · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

  4. /Configuration
  5. /Custom limits



# Custom limits

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet Custom limits

Custom limits allow you to programmatically enforce limits on your customers' Workers' resource usage. You can set limits for the maximum CPU time and number of subrequests per invocation. If a user Worker hits either of these limits, the user Worker will immediately throw an exception.

## Set Custom limits

Custom limits can be set in the dynamic dispatch Worker:
    
    
    export default {
    	async fetch(request, env) {
    		try {
    			// parse the URL, read the subdomain
    			let workerName = new URL(request.url).host.split(".")[0];
    			let userWorker = env.dispatcher.get(
    				workerName,
    				{},
    				{
    					// set limits
    					limits: { cpuMs: 10, subRequests: 5 },
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

[PreviousBindings](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/)[NextObservability](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/observability/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

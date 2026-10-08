---
url: https://developers.cloudflare.com/rules/snippets/examples/serve-different-origin/
title: Route to a different origin based on origin response \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:54.351270+00:00
---

# Route to a different origin based on origin response · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/serve-different-origin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Serve Different Origin



# Route to a different origin based on origin response

If response to the original request is not `200 OK` or a redirect, send to another origin.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/serve-different-origin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Send original request to the origin
    		const response = await fetch(request);
    
    		// If response is not 200 OK or a redirect, send to another origin
    		if (!response.ok && !response.redirected) {
    			// First, clone the original request to construct a new request
    			const newRequest = new Request(request);
    			// Add a header to identify a re-routed request at the new origin
    			newRequest.headers.set("X-Rerouted", "1");
    			// Clone the original URL
    			const url = new URL(request.url);
    			// Send request to a different origin / hostname
    			url.hostname = "example.com";
    			// Serve response to the new request from the origin
    			return await fetch(url, newRequest);
    		}
    
    		// If response is 200 OK or a redirect, serve it
    		return response;
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/serve-different-origin.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

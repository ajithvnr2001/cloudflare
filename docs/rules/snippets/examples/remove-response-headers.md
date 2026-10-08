---
url: https://developers.cloudflare.com/rules/snippets/examples/remove-response-headers/
title: Remove response headers \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.841111+00:00
---

# Remove response headers · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/remove-response-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Remove Response Headers



# Remove response headers

Remove from response all headers that start with a certain name.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/remove-response-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Define the prefix of the headers you want to remove
    		const headerPrefix = "x-header-";
    
    		// Receive response from the origin
    		const response = await fetch(request);
    
    		// Create a new Headers object to modify response headers
    		const newHeaders = new Headers(response.headers);
    
    		// Remove headers that start with the specified prefix
    		for (const [key] of newHeaders.entries()) {
    			if (key.startsWith(headerPrefix)) {
    				newHeaders.delete(key);
    			}
    		}
    
    		// Return the modified response with updated headers
    		return new Response(response.body, {
    			status: response.status,
    			headers: newHeaders,
    		});
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/remove-response-headers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/rules/snippets/examples/define-cors-headers/
title: Define CORS headers \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.072564+00:00
---

# Define CORS headers · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/define-cors-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Define Cors Headers



# Define CORS headers

Adjust [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) headers and handle preflight requests.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/define-cors-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    // Define CORS headers
    const corsHeaders = {
    	"Access-Control-Allow-Origin": "*", // Replace * with your allowed origin(s)
    	"Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS", // Adjust allowed methods as needed
    	"Access-Control-Allow-Headers": "Content-Type, Authorization", // Adjust allowed headers as needed
    	"Access-Control-Max-Age": "86400", // Adjust max age (in seconds) as needed
    };
    
    export default {
    	async fetch(request) {
    		// Make a copy of the request to modify its headers
    		const modifiedRequest = new Request(request);
    
    		// Handle preflight requests (OPTIONS)
    		if (request.method === "OPTIONS") {
    			return new Response(null, {
    				headers: {
    					...corsHeaders,
    				},
    				status: 200, // Respond with OK status for preflight requests
    			});
    		}
    
    		// Pass the modified request through to the origin
    		const response = await fetch(modifiedRequest);
    
    		// Make a copy of the response to modify its headers
    		const modifiedResponse = new Response(response.body, response);
    
    		// Set CORS headers on the response
    		Object.keys(corsHeaders).forEach((header) => {
    			modifiedResponse.headers.set(header, corsHeaders[header]);
    		});
    
    		return modifiedResponse;
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/define-cors-headers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

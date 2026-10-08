---
url: https://developers.cloudflare.com/rules/snippets/examples/hex-timestamp/
title: Add HEX timestamp to a request header \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.279755+00:00
---

# Add HEX timestamp to a request header · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/hex-timestamp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Hex Timestamp



# Add HEX timestamp to a request header

Add a custom header to requests sent to the origin server with the current timestamp in hexadecimal format.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/hex-timestamp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Get the current timestamp
    		const timestamp = Date.now();
    
    		// Convert the timestamp to hexadecimal format
    		const hexTimestamp = timestamp.toString(16);
    
    		// Clone the request and add the custom header
    		const modifiedRequest = new Request(request, {
    			headers: new Headers(request.headers),
    		});
    		modifiedRequest.headers.set("X-Hex-Timestamp", hexTimestamp);
    
    		// Log the custom header for debugging
    		console.log(`X-Hex-Timestamp: ${hexTimestamp}`);
    
    		// Pass the modified request to the origin
    		const response = await fetch(modifiedRequest);
    
    		return response;
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/hex-timestamp.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

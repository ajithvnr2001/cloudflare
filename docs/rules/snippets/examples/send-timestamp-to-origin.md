---
url: https://developers.cloudflare.com/rules/snippets/examples/send-timestamp-to-origin/
title: Send timestamp to origin as a custom header \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:54.161896+00:00
---

# Send timestamp to origin as a custom header · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/send-timestamp-to-origin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Send Timestamp To Origin



# Send timestamp to origin as a custom header

Convert timestamp to hexadecimal format and send it as a custom header to the origin.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/send-timestamp-to-origin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
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

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/send-timestamp-to-origin.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

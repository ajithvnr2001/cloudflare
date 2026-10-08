---
url: https://developers.cloudflare.com/rules/snippets/examples/remove-fields-api-response/
title: Remove fields from API response \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.554687+00:00
---

# Remove fields from API response · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/remove-fields-api-response/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Remove Fields Api Response



# Remove fields from API response

If origin responds with `JSON`, parse the response and delete fields to return a modified response.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/remove-fields-api-response/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Send original request to the origin
    		const response = await fetch(request);
    		// Check if origin responded with JSON
    		try {
    			// Parse API response as JSON
    			var api_response = response.json();
    			// Specify the fields you want to delete. For example, to delete "botManagement" array from parsed JSON:
    			delete api_response.botManagement;
    			// Serve modified API response
    			return Response.json(api_response);
    		} catch (err) {
    			// On failure, serve unmodified origin's response
    			return response;
    		}
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/remove-fields-api-response.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

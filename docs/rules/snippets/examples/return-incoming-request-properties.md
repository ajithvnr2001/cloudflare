---
url: https://developers.cloudflare.com/rules/snippets/examples/return-incoming-request-properties/
title: Return information about the incoming request \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.960703+00:00
---

# Return information about the incoming request · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/return-incoming-request-properties/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Return Incoming Request Properties



# Return information about the incoming request

Respond with information about the incoming request provided by Cloudflare’s global network.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/return-incoming-request-properties/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// For any request, respond with JSON object containing all incoming request properties provided by Cloudflare network
    		return Response.json(request.cf, {
    			// Add new header to identify request was served by Snippets
    			headers: {
    				"x-snippets-hello": "Hello from Cloudflare Snippets",
    			},
    		});
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/return-incoming-request-properties.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

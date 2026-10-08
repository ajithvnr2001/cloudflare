---
url: https://developers.cloudflare.com/rules/snippets/examples/bots-to-honeypot/
title: Send suspect bots to a honeypot \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.955714+00:00
---

# Send suspect bots to a honeypot · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/bots-to-honeypot/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Bots To Honeypot



# Send suspect bots to a honeypot

Use the [bot score field](https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties) to send bots to a honeypot.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/bots-to-honeypot/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		const response = await fetch(request);
    
    		// Clone the response so that it is no longer immutable
    		const newResponse = new Response(response.body, response);
    
    		if (request.cf.botManagement.score < 30) {
    			const honeypot = "https://example.com/";
    			return await fetch(honeypot, request);
    		} else {
    			return newResponse;
    		}
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/bots-to-honeypot.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

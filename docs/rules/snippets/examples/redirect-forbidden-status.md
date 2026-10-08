---
url: https://developers.cloudflare.com/rules/snippets/examples/redirect-forbidden-status/
title: Redirect 403 Forbidden to a different page \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.802253+00:00
---

# Redirect 403 Forbidden to a different page · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/redirect-forbidden-status/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Redirect Forbidden Status



# Redirect 403 Forbidden to a different page

If origin responded with `403 Forbidden` error code, redirect to different page.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/redirect-forbidden-status/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Send original request to the origin
    		const response = await fetch(request);
    		// Check if origin responded with 403 status code
    		if (response.status == 403) {
    			// If so, redirect to this URL
    			const destinationURL = "https://example.com";
    			// With this status code
    			const statusCode = 301;
    			// Serve redirect
    			return Response.redirect(destinationURL, statusCode);
    		}
    		// Otherwise, serve origin's response
    		else {
    			return response;
    		}
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/redirect-forbidden-status.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

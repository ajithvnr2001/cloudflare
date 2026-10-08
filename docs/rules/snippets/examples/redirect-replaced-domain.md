---
url: https://developers.cloudflare.com/rules/snippets/examples/redirect-replaced-domain/
title: Redirect from one domain to another \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.703349+00:00
---

# Redirect from one domain to another · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/redirect-replaced-domain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Redirect Replaced Domain



# Redirect from one domain to another

Redirect all requests from one domain to another domain.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/redirect-replaced-domain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Define variables to use in the response redirect.
    		const base = "https://example.com";
    		const statusCode = 301;
    
    		// Clone the original URL.
    		const url = new URL(request.url);
    
    		// Define a "pathname" and "search" variables, extracting their values from the cloned URL.
    		const { pathname, search } = url;
    
    		// Define the destination URL using the variables you declared previously.
    		const destinationURL = `${base}${pathname}${search}`;
    		console.log(destinationURL);
    
    		// Respond with the redirect.
    		return Response.redirect(destinationURL, statusCode);
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/redirect-replaced-domain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

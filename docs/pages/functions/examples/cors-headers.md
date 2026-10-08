---
url: https://developers.cloudflare.com/pages/functions/examples/cors-headers/
title: Adding CORS headers \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:32.510012+00:00
---

# Adding CORS headers · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/examples/cors-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

[Functions](https://developers.cloudflare.com/pages/functions/)

  4. /Examples
  5. /Adding CORS headers



# Adding CORS headers

A Pages Functions for appending CORS headers.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/examples/cors-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example is a snippet from our Cloudflare Pages Template repo.
    
    
    // Respond to OPTIONS method
    export const onRequestOptions: PagesFunction = async () => {
    	return new Response(null, {
    		status: 204,
    		headers: {
    			"Access-Control-Allow-Origin": "*",
    			"Access-Control-Allow-Headers": "*",
    			"Access-Control-Allow-Methods": "GET, OPTIONS",
    			"Access-Control-Max-Age": "86400",
    		},
    	});
    };
    
    // Set CORS to all /api responses
    export const onRequest: PagesFunction = async (context) => {
    	const response = await context.next();
    	response.headers.set("Access-Control-Allow-Origin", "*");
    	response.headers.set("Access-Control-Max-Age", "86400");
    	return response;
    };

[PreviousA/B testing with middleware](https://developers.cloudflare.com/pages/functions/examples/ab-testing/)[NextMiddleware](https://developers.cloudflare.com/pages/functions/middleware/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/examples/cors-headers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/rules/snippets/examples/bulk-redirect-map/
title: Bulk redirect based on a map object \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.459768+00:00
---

# Bulk redirect based on a map object · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/bulk-redirect-map/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Bulk Redirect Map



# Bulk redirect based on a map object

Redirect requests to certain URLs based on a mapped object to the request's URL.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/bulk-redirect-map/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Define a variable with the hostname that needs to be redirected.
    		const externalHostname = "example.com";
    
    		// Define the map object. Replace the sources (/pathX) and targets (/redirectX) with ones that apply to your case.
    		const redirectMap = new Map([
    			["/path1", "https://" + externalHostname + "/redirect1"],
    			["/path2", "https://" + externalHostname + "/redirect2"],
    			["/path3", "https://" + externalHostname + "/redirect3"],
    			["/path4", "https://cloudflare.com"],
    		]);
    
    		// Clone the original URL.
    		const requestURL = new URL(request.url);
    
    		// Check the request path against the map and redirect accordingly.
    		const path = requestURL.pathname;
    		const location = redirectMap.get(path);
    
    		if (location) {
    			return Response.redirect(location, 301);
    		}
    
    		// If request path not in map, return the original request.
    		return fetch(request);
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/bulk-redirect-map.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

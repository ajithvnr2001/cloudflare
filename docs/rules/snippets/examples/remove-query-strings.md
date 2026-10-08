---
url: https://developers.cloudflare.com/rules/snippets/examples/remove-query-strings/
title: Remove query strings before sending request to origin \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.897592+00:00
---

# Remove query strings before sending request to origin · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/remove-query-strings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Remove Query Strings



# Remove query strings before sending request to origin

Remove certain query strings from a request before passing to the origin.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/remove-query-strings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Define the query strings you want to remove
    		const queryStringsToRemove = ["utm_source", "utm_medium", "utm_campaign"];
    
    		// Get the URL from the request
    		const url = new URL(request.url);
    
    		// Remove the specified query strings
    		queryStringsToRemove.forEach((query) => {
    			url.searchParams.delete(query);
    		});
    
    		// Create a new request with the modified URL
    		const modifiedRequest = new Request(url, request);
    
    		// Pass the modified request to the origin
    		const response = await fetch(modifiedRequest);
    
    		return response;
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/remove-query-strings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

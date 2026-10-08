---
url: https://developers.cloudflare.com/rules/snippets/examples/ab-testing-same-url/
title: A/B testing with same-URL direct access \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.401751+00:00
---

# A/B testing with same-URL direct access · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/ab-testing-same-url/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Ab Testing Same Url



# A/B testing with same-URL direct access

Set up an A/B test by controlling what response is served based on cookies.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/ab-testing-same-url/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This version passes through requests for `/test/*` and `/control/*` URI paths to the origin server, bypassing random assignment.
    
    
    const NAME = "myExampleABTest";
    
    export default {
    	async fetch(request) {
    		// Clone the original URL
    		const url = new URL(request.url);
    
    		// Enable Passthrough to allow direct access to control and test routes.
    		if (url.pathname.startsWith("/control") || url.pathname.startsWith("/test"))
    			return fetch(request);
    
    		// Determine which group this requester is in.
    		const cookie = request.headers.get("cookie");
    
    		if (cookie && cookie.includes(`${NAME}=control`)) {
    			url.pathname = "/control" + url.pathname;
    		} else if (cookie && cookie.includes(`${NAME}=test`)) {
    			url.pathname = "/test" + url.pathname;
    		} else {
    			// If there is no cookie, this is a new client. Choose a group and set the cookie.
    			const group = Math.random() < 0.5 ? "test" : "control"; // 50/50 split
    			if (group === "control") {
    				url.pathname = "/control" + url.pathname;
    			} else {
    				url.pathname = "/test" + url.pathname;
    			}
    			// Reconstruct response to avoid immutability
    			let response = await fetch(url);
    			response = new Response(response.body, response);
    			// Set cookie to enable persistent A/B sessions.
    			response.headers.append("Set-Cookie", `${NAME}=${group}; path=/`);
    			return response;
    		}
    		return fetch(url);
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/ab-testing-same-url.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

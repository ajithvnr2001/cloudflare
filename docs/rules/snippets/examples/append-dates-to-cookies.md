---
url: https://developers.cloudflare.com/rules/snippets/examples/append-dates-to-cookies/
title: Append dates to cookies to use with A/B testing \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.670034+00:00
---

# Append dates to cookies to use with A/B testing · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/append-dates-to-cookies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Append Dates To Cookies



# Append dates to cookies to use with A/B testing

Dynamically set a cookie expiration and test group.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/append-dates-to-cookies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		const response = await fetch(request);
    
    		// Clone the response so that it is no longer immutable
    		const newResponse = new Response(response.body, response);
    
    		// Define the dynamic expiry time. 24 h * 60 m * 60 s * 1000 ms = 86,400,000 ms
    		const expiry = new Date(Date.now() + 7 * 86400000).toUTCString();
    		// Define the group variable. "A" if the request header "userGroup" is "premium", "B" if otherwise.
    		const group = request.headers.get("userGroup") == "premium" ? "A" : "B";
    
    		// Append the custom header with the values
    		newResponse.headers.append(
    			"Set-Cookie",
    			`testGroup=${group}; Expires=${expiry}; Path=/`,
    		);
    
    		return newResponse;
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/append-dates-to-cookies.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

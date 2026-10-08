---
url: https://developers.cloudflare.com/rules/snippets/examples/override-set-cookies-value/
title: Override a Set-Cookie header with a certain value \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.406283+00:00
---

# Override a Set-Cookie header with a certain value · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/override-set-cookies-value/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Override Set Cookies Value



# Override a Set-Cookie header with a certain value

Get a specific `Set-Cookie` header and update it with a certain value.

Last updated Nov 3, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/override-set-cookies-value/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Receive response from the origin
    		const response = await fetch(request);
    
    		// Create a new Headers object to modify response headers
    		const newHeaders = new Headers(response.headers);
    
    		// Get all Set-Cookie headers
    		const cookieArray = response.headers.getSetCookie();
    		if (cookieArray.length > 0) {
    			const updatedCookies = cookieArray.map((cookie) => {
    				// For example, replace the currency value with GBP
    				if (cookie.trim().startsWith("currency=")) {
    					return cookie.replace(/currency=[^;]+/, "currency=GBP");
    				}
    				return cookie;
    			});
    
    			// Delete the existing Set-Cookie headers
    			newHeaders.delete("Set-Cookie");
    
    			// Add the updated Set-Cookie headers individually
    			updatedCookies.forEach((cookie) => {
    				newHeaders.append("Set-Cookie", cookie.trim());
    			});
    		}
    
    		// Return the modified response with updated headers
    		return new Response(response.body, {
    			status: response.status,
    			headers: newHeaders,
    		});
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/override-set-cookies-value.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/rules/snippets/examples/security-headers/
title: Set security headers \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:54.076800+00:00
---

# Set security headers · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/security-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Security Headers



# Set security headers

Set common security headers such as X-XSS-Protection, X-Frame-Options, and X-Content-Type-Options.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/security-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOther common security headers
    
    
    export default {
    	async fetch(request) {
    		// Define an object with the security headers you want to set.
    		// Refer to https://developers.cloudflare.com/rules/snippets/examples/security-headers/#other-common-security-headers for more options.
    		const DEFAULT_SECURITY_HEADERS = {
    			"X-Content-Type-Options": "nosniff",
    			"Referrer-Policy": "strict-origin-when-cross-origin",
    			"Cross-Origin-Embedder-Policy": 'require-corp; report-to="default";',
    			"Cross-Origin-Opener-Policy": 'same-site; report-to="default";',
    			"Cross-Origin-Resource-Policy": "same-site",
    		};
    
    		// You can also define headers to be deleted.
    		const BLOCKED_HEADERS = [
    			"Public-Key-Pins",
    			"X-Powered-By",
    			"X-AspNet-Version",
    		];
    
    		// Receive response from the origin.
    		let response = await fetch(request);
    
    		// Create a new Headers object to modify response headers
    		let newHeaders = new Headers(response.headers);
    
    		// This sets the headers for HTML responses:
    		if (
    			newHeaders.has("Content-Type") &&
    			!newHeaders.get("Content-Type").includes("text/html")
    		) {
    			return new Response(response.body, {
    				status: response.status,
    				statusText: response.statusText,
    				headers: newHeaders,
    			});
    		}
    
    		// Use DEFAULT_SECURITY_HEADERS object defined above to set the new security headers.
    		Object.keys(DEFAULT_SECURITY_HEADERS).map((name) => {
    			newHeaders.set(name, DEFAULT_SECURITY_HEADERS[name]);
    		});
    
    		// Use the BLOCKED_HEADERS object defined above to delete headers you wish to block.
    		BLOCKED_HEADERS.forEach((name) => {
    			newHeaders.delete(name);
    		});
    
    		return new Response(response.body, {
    			status: response.status,
    			statusText: response.statusText,
    			headers: newHeaders,
    		});
    	},
    };

## Other common security headers

  * Content-Security-Policy headers: Enabling these headers will permit content from a trusted domain and all its subdomains. Refer to [Content-Security-Policy ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) for details.


    
    
    "Content-Security-Policy": "default-src 'self' example.com *.example.com",

  * Strict-Transport-Security headers: These are not automatically set because your website might get added to Chrome's HSTS preload list.


    
    
    "Strict-Transport-Security" : "max-age=63072000; includeSubDomains; preload",

  * Permissions-Policy header: Allow or deny the use of browser features, such as opting out of FLoC.


    
    
    "Permissions-Policy": "interest-cohort=()",

  * X-XSS-Protection header: Prevents a page from loading if an XSS attack is detected. Refer to [X-XSS-Protection ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-XSS-Protection) for details.


    
    
    "X-XSS-Protection": "0",

  * X-Frame-Options header: Prevents click-jacking attacks. Refer to [X-Frame-Options ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options).


    
    
    "X-Frame-Options": "DENY",

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/security-headers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

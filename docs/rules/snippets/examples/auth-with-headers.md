---
url: https://developers.cloudflare.com/rules/snippets/examples/auth-with-headers/
title: Auth with headers \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.628407+00:00
---

# Auth with headers · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/auth-with-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Auth With Headers



# Auth with headers

Allow or deny a request based on a known pre-shared key in a header. This is not meant to replace the [WebCrypto API](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/).

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/auth-with-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Caution when using in production

The example code contains a generic header key and value of `X-Custom-PSK` and `mypresharedkey`. To best protect your resources, change the header key and value in the Snippets editor before saving your code.
    
    
    export default {
    	async fetch(request) {
    		/**
    		 * @param {string} PRESHARED_AUTH_HEADER_KEY Custom header to check for key
    		 * @param {string} PRESHARED_AUTH_HEADER_VALUE Hard-coded key value
    		 */
    		const PRESHARED_AUTH_HEADER_KEY = "X-Custom-PSK";
    		const PRESHARED_AUTH_HEADER_VALUE = "mypresharedkey";
    		const psk = request.headers.get(PRESHARED_AUTH_HEADER_KEY);
    
    		if (psk === PRESHARED_AUTH_HEADER_VALUE) {
    			// Correct preshared header key supplied. Fetch request from origin.
    			return fetch(request);
    		}
    
    		// Incorrect key supplied. Reject the request.
    		return new Response("Sorry, you have supplied an invalid key.", {
    			status: 403,
    		});
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/auth-with-headers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/rules/snippets/examples/country-code-redirect/
title: Country code redirect \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.122399+00:00
---

# Country code redirect · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/country-code-redirect/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Country Code Redirect



# Country code redirect

Redirect a response based on the country code in the header of a visitor.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/country-code-redirect/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		/**
    		 * A map of the URLs to redirect to
    		 * @param {Object} countryMap
    		 */
    		const countryMap = {
    			// Replace the country codes and target URLs with ones that apply to your case.
    			US: "https://example.com/us",
    			EU: "https://example.com/eu",
    		};
    
    		// Use the cf object to obtain the country of the request
    		// more on the cf object: https://developers.cloudflare.com/workers/runtime-apis/request#incomingrequestcfproperties
    		const country = request.cf.country;
    
    		// If country is not null and is defined in the country map above, redirect.
    		if (country != null && country in countryMap) {
    			const url = countryMap[country];
    			// Remove this logging statement from your final output.
    			console.log(
    				`Based on ${country}-based request, your user would go to ${url}.`,
    			);
    			return Response.redirect(url);
    
    			// If request country not in map, return another page.
    		} else {
    			return fetch("https://example.com", request);
    		}
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/country-code-redirect.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

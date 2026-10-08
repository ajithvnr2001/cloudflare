---
url: https://developers.cloudflare.com/rules/snippets/examples/follow-redirects/
title: Follow redirects from the origin \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.011795+00:00
---

# Follow redirects from the origin · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/follow-redirects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Follow Redirects



# Follow redirects from the origin

Modify the fetch request to follow redirects from the origin, ensuring the client receives the final response.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/follow-redirects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Define fetch options to follow redirects
    		const fetchOptions = {
    			redirect: "follow", // Ensure fetch follows redirects automatically. Each subrequest in a redirect chain counts against the subrequest limit.
    		};
    
    		// Make the fetch request to the origin
    		const response = await fetch(request, fetchOptions);
    
    		// Log the final URL after redirects (optional, for debugging)
    		console.log(`Final URL after redirects: ${response.url}`);
    
    		// Return the final response to the client
    		return response;
    	},
    };

This template is ready for use and should fit most redirect-following scenarios.

It ensures the Snippet transparently follows redirects issued by the origin server. The `redirect: "follow"` option of the [Fetch API](https://developers.cloudflare.com/workers/runtime-apis/fetch/) ensures automatic handling of `3xx` redirects, returning the final response. If the origin response is not a redirect, the original content is returned.

Note

Snippets have a [maximum number of subrequests per invocation](https://developers.cloudflare.com/rules/snippets/#availability) which depends on your plan. If the origin server issues multiple redirects, each redirect subrequest will count towards this limit. When the number of subrequests exceeds the limit for your Cloudflare plan, you will receive a [1202 error](https://developers.cloudflare.com/rules/snippets/errors/#error-1202-snippets-exceeded-subrequests-limit). Ensure your origin configuration minimizes unnecessary redirects.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/follow-redirects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/rules/snippets/examples/bot-data-to-origin/
title: Send Bot Management information to origin \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.486596+00:00
---

# Send Bot Management information to origin · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/bot-data-to-origin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Bot Data To Origin



# Send Bot Management information to origin

Send [Bots](https://developers.cloudflare.com/bots/) information to your origin. Refer to [Bot Management variables](https://developers.cloudflare.com/bots/reference/bot-management-variables/) for a full list of available fields.

Last updated Mar 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/bot-data-to-origin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Clone the original request to construct a new request
    		const newRequest = new Request(request);
    		// Set Bot Management headers on a new request to the origin: https://developers.cloudflare.com/bots/reference/bot-management-variables/#workers-variables
    		newRequest.headers.set("bot-score", request.cf.botManagement.score); // bot score (integer)
    		newRequest.headers.set(
    			"verified-bot",
    			request.cf.botManagement.verifiedBot,
    		); // verified bot (boolean)
    		newRequest.headers.set("ja4", request.cf.botManagement.ja4); // JA4 fingerprint hash (string)
    		// Serve response to the new request from the origin
    		return await fetch(newRequest);
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/bot-data-to-origin.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

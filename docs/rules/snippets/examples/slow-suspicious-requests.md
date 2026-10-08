---
url: https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/
title: Slow down suspicious requests \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:54.621347+00:00
---

# Slow down suspicious requests · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Slow Suspicious Requests



# Slow down suspicious requests

Define a delay to be used when incoming requests match a rule you consider suspicious based on the bot score.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/slow-suspicious-requests/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSnippet codeSnippet rule

## Snippet code
    
    
    export default {
    	async fetch(request) {
    		// Define delay
    		const delay_in_seconds = 5;
    		// Introduce a delay
    		await new Promise((resolve) =>
    			setTimeout(resolve, delay_in_seconds * 1000),
    		); // Set delay in milliseconds
    
    		// Pass the request to the origin
    		const response = await fetch(request);
    		return response;
    	},
    };

## Snippet rule

Configure a custom filter expression:

Field | Operator | Value  
---|---|---  
Bot Score | less than | `10`  
  
If you are using the Expression Editor, enter the following expression:
    
    
    (cf.bot_management.score lt 10)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/slow-suspicious-requests.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

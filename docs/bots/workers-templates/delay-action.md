---
url: https://developers.cloudflare.com/bots/workers-templates/delay-action/
title: Delay action \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:35.010423+00:00
---

# Delay action · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/workers-templates/delay-action/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Workers templates
  4. /Delay action



# Delay action

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/workers-templates/delay-action/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Customers with a Bot Management and a [Workers](https://developers.cloudflare.com/workers/) subscription can use the template below to introduce a delay to requests that are likely from bots.

The template sets a minimum and maximum delay, and delays requests where the bot score is less than 30 and the URI path starts with `/exampleURI`.
    
    
    // Configurable Variables
    const PATH_START = "/exampleURI";
    const DELAY_FROM = 5; // in seconds
    const DELAY_TO = 10; // in seconds
    
    export default {
    	async fetch(request, env, ctx) {
    		const url = new URL(request.url);
    		const botScore = request.cf.botManagement.score;
    
    		if (url.pathname.startsWith(PATH_START) && botScore < 30) {
    			// Random delay between DELAY_FROM and DELAY_TO seconds
    			const delay =
    				Math.floor(Math.random() * (DELAY_TO - DELAY_FROM + 1)) + DELAY_FROM;
    			await new Promise((resolve) => setTimeout(resolve, delay * 1000));
    
    			// Fetch the original request
    			return fetch(request);
    		}
    
    		// Fetch the original request without delay
    		return fetch(request);
    	},
    };

Workers templatets
    
    
    // Configurable Variables
    const PATH_START = '/exampleURI';
    const DELAY_FROM = 5; // in seconds
    const DELAY_TO = 10; // in seconds
    
    export default {
      async fetch(request, env, ctx): Promise<Response> {
        const url = new URL(request.url);
        const botScore = request.cf.botManagement.score
    
        if (url.pathname.startsWith(PATH_START) && botScore < 30) {
          // Random delay between DELAY_FROM and DELAY_TO seconds
          const delay = Math.floor(Math.random() * (DELAY_TO - DELAY_FROM + 1)) + DELAY_FROM;
          await new Promise(resolve => setTimeout(resolve, delay * 1000));
    
          // Fetch the original request
          return fetch(request);
        }
    
        // Fetch the original request without delay
        return fetch(request);
      },
    } satisfies ExportedHandler<Env>;

[PreviousBusiness Insights](https://developers.cloudflare.com/bots/business-insights/)[NextAccount Abuse Protection](https://developers.cloudflare.com/bots/account-abuse-protection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/workers-templates/delay-action.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/
title: Workflows now supports delay functions when retrying \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.213184+00:00
---

# Workflows now supports delay functions when retrying · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 9, 2026

## Workflows now supports delay functions when retrying

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

With [Workflows](https://developers.cloudflare.com/workflows/), you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as `constant`, `linear`, or `exponential`.

Step retries now support dynamic delay functions. Instead of choosing only a base delay and backoff strategy, pass a function to `retries.delay` and calculate the next delay from the failed attempt and thrown error.

This is useful when retries should depend on the failure. Your Workflow may need to wait longer after a rate-limit error, but retry sooner after a short network failure. The delay function can also accommodate provider guidance if, for example, a downstream API returns a `Retry-After` value in its error messaging.
    
    
    await step.do(
    	"sync customer",
    	{
    		retries: {
    			limit: 5,
    			delay: ({ ctx, error }) => {
    				if (error.message.includes("rate limit")) {
    					return `${ctx.attempt * 30} seconds`;
    				}
    
    				return "10 seconds";
    			},
    		},
    	},
    	async () => {
    		await syncCustomer();
    	},
    );
    
    
    await step.do(
    	"sync customer",
    	{
    		retries: {
    			limit: 5,
    			delay: ({ ctx, error }) => {
    				if (error.message.includes("rate limit")) {
    					return `${ctx.attempt * 30} seconds`;
    				}
    
    				return "10 seconds";
    			},
    		},
    	},
    	async () => {
    		await syncCustomer();
    	},
    );

Dynamic delay functions can return a duration string, a number, or a promise that resolves to a duration. Use them to add adaptive retry behavior without writing separate queue or scheduling logic. For more information, refer to [Sleeping and retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/).

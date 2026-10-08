---
url: https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/
title: Rollback support now available in Workflows \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:56.507305+00:00
---

# Rollback support now available in Workflows · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 5, 2026

## Rollback support now available in Workflows

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) now supports saga-style rollbacks, allowing you to add compensating logic to each `step.do()` in case of downstream failures. If the instance fails, the rollback handlers will execute in reverse `step-start` order.

This is useful for multi-step operations that touch external systems, such as inventory reservations, payment authorization, ticket creation, or infrastructure provisioning. Instead of writing all cleanup logic in a top-level `catch`, you can keep each compensating action next to the step it undoes.

Rollback handlers support their own retry and timeout configuration, and Workflows now exposes rollback outcomes in instance status responses. Workflows analytics also emits rollback lifecycle events, making it easier to distinguish a forward execution failure from a rollback failure when debugging production workflows.
    
    
    await step.do(
    	"provision resource",
    	async () => {
    		const resource = await provisionResource();
    		return { resourceId: resource.id };
    	},
    	{
    		rollback: async ({ output }) => {
    			const { resourceId } = output;
    			await deleteResource(resourceId);
    		},
    		rollbackConfig: {
    			retries: { limit: 3, delay: "15 seconds", backoff: "linear" },
    			timeout: "2 minutes",
    		},
    	},
    );
    
    
    await step.do(
    	"provision resource",
    	async () => {
    		const resource = await provisionResource();
    		return { resourceId: resource.id };
    	},
    	{
    		rollback: async ({ output }) => {
    			const { resourceId } = output as { resourceId: string };
    			await deleteResource(resourceId);
    		},
    		rollbackConfig: {
    			retries: { limit: 3, delay: "15 seconds", backoff: "linear" },
    			timeout: "2 minutes",
    		},
    	},
    );

Refer to [rollback options](https://developers.cloudflare.com/workflows/build/workers-api/#rollback-options) to learn more.

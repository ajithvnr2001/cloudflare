---
url: https://developers.cloudflare.com/changelog/post/2026-06-02-cron-workflows/
title: Schedule Workflow instances directly from your Workflow binding \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:55.968280+00:00
---

# Schedule Workflow instances directly from your Workflow binding · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-02-cron-workflows/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 2, 2026

## Schedule Workflow instances directly from your Workflow binding

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-02-cron-workflows/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now attach cron schedules directly to a Workflow binding in `wrangler.jsonc`. Each scheduled run creates a new Workflow instance automatically, so you do not need to define a separate Worker with a `scheduled` handler just to trigger your Workflow on an interval.

For example, you can configure hourly, every-15-minute, or weekday schedules on the same Workflow:
    
    
    {
    	"workflows": [
    		{
    			"name": "my-scheduled-workflow",
    			"binding": "MY_WORKFLOW",
    			"class_name": "MyScheduledWorkflow",
    			"schedules": ["0 * * * *", "*/15 * * * *", "0 9 * * MON-FRI"],
    		},
    	],
    }

Cron workloads get all the same benefits of Workflows with built-in retries, multi-step durable execution, and configurable timeouts of Workflows.
    
    
    import {
    	WorkflowEntrypoint,
    	WorkflowEvent,
    	WorkflowStep,
    } from "cloudflare:workers";
    
    // Runs automatically on each cron schedule defined for the MY_WORKFLOW binding in wrangler.jsonc.
    export class MyScheduledWorkflow extends WorkflowEntrypoint<Env> {
    	async run(event: WorkflowEvent, step: WorkflowStep) {
    		const data = await step.do("fetch source data", async () => {
    			return await fetchSourceData();
    		});
    
    		// If this step fails, only this step is retried with the custom logic below
    		await step.do(
    			"process and store results",
    			{
    				retries: { limit: 5, delay: "30 seconds", backoff: "exponential" },
    				timeout: "10 minutes",
    			},
    			async () => {
    				await processAndStore(data);
    			},
    		);
    	}
    }

This makes it easier to build recurring, scheduled jobs such as database backups, invoice generation, report aggregation, and cleanup tasks without wiring up a separate Cron Trigger entrypoint.

For more information, refer to [Trigger Workflows](https://developers.cloudflare.com/workflows/build/trigger-workflows/).

---
url: https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/
title: Stream Workflow instance events in your Worker or via the API with .subscribe() \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.934374+00:00
---

# Stream Workflow instance events in your Worker or via the API with .subscribe() · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 15, 2026

## Stream Workflow instance events in your Worker or via the API with .subscribe()

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now stream Workflow instance events via `WorkflowInstance.subscribe()` and the `GET /subscribe` API endpoint. Workers and HTTP clients can react to [workflow](https://developers.cloudflare.com/workflows/build/events-and-parameters/) and [step](https://developers.cloudflare.com/workflows/build/step-context/#workflowstepcontext) events, including attempts, sleeps, waits, and rollbacks, without polling for instance status.

A subscription first streams the entire event history of the Workflow instance. After streaming past events, the subscription waits for new events as the instance runs. You can use `filter` to receive only specific event types or `cursor` to start a subscription at a specific event.

Use `.subscribe()` to update Workflow status in user-facing dashboards, send notifications when steps complete, or trigger follow-up work for specific events.
    
    
    const instance = await env.MY_WORKFLOW.get("report-123");
    
    using subscription = await instance.subscribe();
    
    while (true) {
    	const { value, done } = await subscription.next();
    	if (done) {
    		break;
    	}
    
    	console.log(value.type, value);
    }
    
    
    const instance = await env.MY_WORKFLOW.get("report-123");
    
    using subscription = await instance.subscribe();
    
    while (true) {
    	const { value, done } = await subscription.next();
    	if (done) {
    		break;
    	}
    
    	console.log(value.type, value);
    }

For event types, available fields, and subscription options, refer to [Subscribe to events](https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/).

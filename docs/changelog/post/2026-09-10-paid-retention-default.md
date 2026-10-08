---
url: https://developers.cloudflare.com/changelog/post/2026-09-10-paid-retention-default/
title: Default instance retention for new Workflows on Workers Paid is seven days \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.331534+00:00
---

# Default instance retention for new Workflows on Workers Paid is seven days · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-10-paid-retention-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 10, 2026

## Default instance retention for new Workflows on Workers Paid is seven days

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-10-paid-retention-default/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) created on or after September 10, 2026, on the Workers Paid plan retain completed and errored instance state for seven days by default (previously 30 days). The seven day default helps to reduce storage costs by default. The maximum retention [limit](https://developers.cloudflare.com/workflows/reference/limits/) remains 30 days.

The retention period for existing Workflows is unchanged. The Workers Free plan retains its three-day default and limit.

To set the retention period for a Workflow instance, specify `successRetention`, `errorRetention`, or both:
    
    
    const instance = await env.MY_WORKFLOW.create({
    	retention: {
    		successRetention: "2 days",
    		errorRetention: "30 days",
    	},
    });
    
    
    const instance = await env.MY_WORKFLOW.create({
    	retention: {
    		successRetention: "2 days",
    		errorRetention: "30 days",
    	},
    });

You can also set the retention period per Workflow and per instance in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/workflows).

For retention details, refer to [Workflows pricing](https://developers.cloudflare.com/workflows/reference/pricing/) and the [`WorkflowInstanceCreateOptions` API reference](https://developers.cloudflare.com/workflows/build/workers-api/#workflowinstancecreateoptions).

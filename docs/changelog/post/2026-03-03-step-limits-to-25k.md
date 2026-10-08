---
url: https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/
title: Workflows step limit increased to 25,000 steps per instance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:39.561189+00:00
---

# Workflows step limit increased to 25,000 steps per instance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 3, 2026

## Workflows step limit increased to 25,000 steps per instance

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Each Workflow on Workers Paid now supports 10,000 steps by default, configurable up to 25,000 steps in your `wrangler.jsonc` file:
    
    
    {
    	"workflows": [
    		{
    			"name": "my-workflow",
    			"binding": "MY_WORKFLOW",
    			"class_name": "MyWorkflow",
    			"limits": {
    				"steps": 25000
    			}
    		}
    	]
    }

Previously, each instance was limited to 1,024 steps. Now, Workflows can support more complex, long-running executions without the additional complexity of recursive or child workflow calls.

Note that the maximum persisted state limit per Workflow instance remains **100 MB** for Workers Free and **1 GB** for Workers Paid. Refer to [Workflows limits](https://developers.cloudflare.com/workflows/reference/limits/) for more information.

---
url: https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/
title: Run Workers for up to 5 minutes of CPU-time \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:07.421342+00:00
---

# Run Workers for up to 5 minutes of CPU-time · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 26, 2025

## Run Workers for up to 5 minutes of CPU-time

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run a Worker for up to 5 minutes of CPU time for each request.

Previously, each Workers request ran for a maximum of 30 seconds of CPU time — that is the time that a Worker is actually performing a task (we still allowed unlimited wall-clock time, in case you were waiting on slow resources). This meant that some compute-intensive tasks were impossible to do with a Worker. For instance, you might want to take the cryptographic hash of a large file from R2. If this computation ran for over 30 seconds, the Worker request would have timed out.

By default, Workers are still limited to 30 seconds of CPU time. This protects developers from incurring accidental cost due to buggy code.

By changing the `cpu_ms` value in your Wrangler configuration, you can opt in to any value up to 300,000 (5 minutes).
    
    
    {
    	// ...rest of your configuration...
    	"limits": {
    		"cpu_ms": 300000,
    	},
    	// ...rest of your configuration...
    }
    
    
    [limits]
    cpu_ms = 300_000

Note

CPU time is the amount of time the CPU actually spends doing work during a given request. If a Worker's request makes a sub-request and waits for that request to come back before doing additional work, this time spent waiting **is not** counted towards CPU time.

Worker requests could run for more than 30 seconds of total time prior to this change — only CPU time was limited.

For more information on the updates limits, see the documentation on [Wrangler configuration for `cpu_ms`](https://developers.cloudflare.com/workers/wrangler/configuration/#limits) and on [Workers CPU time limits](https://developers.cloudflare.com/workers/platform/limits/#cpu-time).

For building long-running tasks on Cloudflare, we also recommend checking out [Workflows](https://developers.cloudflare.com/workflows/) and [Queues](https://developers.cloudflare.com/queues/).

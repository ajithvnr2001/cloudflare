---
url: https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/
title: Additional step context and ReadableStream support now available in Workflows step.do() \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:48.370874+00:00
---

# Additional step context and ReadableStream support now available in Workflows step.do() · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 21, 2026

## Additional step context and ReadableStream support now available in Workflows step.do()

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) now provides additional context inside `step.do()` callbacks and supports returning `ReadableStream` to handle larger step outputs.

#### Step context properties

The `step.do()` callback receives a context object with new properties [alongside](https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/) `attempt`:

  * **`step.name`** — The name passed to `step.do()`
  * **`step.count`** — How many times a step with that name has been invoked in this instance (1-indexed) 
    * Useful when running the same step in a loop.
  * **`config`** — The resolved step configuration, including `timeout` and `retries` with defaults applied


    
    
    type ResolvedStepConfig = {
    	retries: {
    		limit: number;
    		delay: WorkflowDelayDuration | number;
    		backoff?: "constant" | "linear" | "exponential";
    	};
    	timeout: WorkflowTimeoutDuration | number;
    };
    
    type WorkflowStepContext = {
    	step: {
    		name: string;
    		count: number;
    	};
    	attempt: number;
    	config: ResolvedStepConfig;
    };

#### ReadableStream support in `step.do()`

Steps can now return a `ReadableStream` directly. Although non-stream step outputs are [limited to 1 MiB](https://developers.cloudflare.com/workflows/reference/limits/), streamed outputs support much larger payloads.
    
    
    const largePayload = await step.do("fetch-large-file", async () => {
    	const object = await env.MY_BUCKET.get("large-file.bin");
    	return object.body;
    });

Note that streamed outputs are still considered part of the Workflow instance storage limit.

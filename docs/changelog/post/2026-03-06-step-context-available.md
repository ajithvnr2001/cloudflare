---
url: https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/
title: Workflow steps now expose retry attempt number via step context \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.615041+00:00
---

# Workflow steps now expose retry attempt number via step context · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-06-step-context-available/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 6, 2026

## Workflow steps now expose retry attempt number via step context

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Workflows allows you to configure specific retry logic for each step in your workflow execution. Now, you can access **which** retry attempt is currently executing for calls to `step.do()`:
    
    
    await step.do("my-step", async (ctx) => {
    	// ctx.attempt is 1 on first try, 2 on first retry, etc.
    	console.log(`Attempt ${ctx.attempt}`);
    });

You can use the step context for improved logging & observability, progressive backoff, or conditional logic in your workflow definition.

Note that the current attempt number is 1-indexed. For more information on retry behavior, refer to [Sleeping and Retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/).

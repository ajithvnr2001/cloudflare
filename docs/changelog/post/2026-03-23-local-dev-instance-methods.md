---
url: https://developers.cloudflare.com/changelog/post/2026-03-23-local-dev-instance-methods/
title: Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.741235+00:00
---

# Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-23-local-dev-instance-methods/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 23, 2026

## Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workflow instance methods `pause()`, `resume()`, `restart()`, and `terminate()` are now available in local development when using `wrangler dev`.

You can now test the full Workflow instance lifecycle locally:
    
    
    const instance = await env.MY_WORKFLOW.create({
    	id: "my-instance-id",
    });
    
    await instance.pause(); // pauses a running workflow instance
    await instance.resume(); // resumes a paused instance
    await instance.restart(); // restarts the instance from the beginning
    await instance.terminate(); // terminates the instance immediately

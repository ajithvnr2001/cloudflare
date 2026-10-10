---
url: https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/
title: Build durable multi-step applications in Python with Workflows (now in beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.776508+00:00
---

# Build durable multi-step applications in Python with Workflows (now in beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 22, 2025

## Build durable multi-step applications in Python with Workflows (now in beta)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now build [Workflows](https://developers.cloudflare.com/workflows/) using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the [Python Workers](https://developers.cloudflare.com/workers/languages/python/) runtime.

Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable [DAG (Directed Acyclic Graph) workflows](https://developers.cloudflare.com/workflows/python/dag/), where you can define complex dependencies between steps using the depends parameter.

Here’s a simple example:
    
    
    from workers import Response, WorkflowEntrypoint
    
    class PythonWorkflowStarter(WorkflowEntrypoint):
        async def run(self, event, step):
            @step.do("my first step")
            async def my_first_step():
                # do some work
                return "Hello Python!"
    
            await my_first_step()
    
            await step.sleep("my-sleep-step", "10 seconds")
    
            @step.do("my second step")
            async def my_second_step():
                # do some more work
                return "Hello again!"
    
            await my_second_step()
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            await self.env.MY_WORKFLOW.create()
            return Response("Hello Workflow creation!")

Note

Python Workflows requires a `compatibility_date = "2025-08-01"`, or lower, in your wrangler toml file.

Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.

To learn more and get started, refer to [Python Workflows documentation](https://developers.cloudflare.com/workflows/python/).

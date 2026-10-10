---
url: https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/
title: Python Workers handlers now live in an entrypoint class \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.084212+00:00
---

# Python Workers handlers now live in an entrypoint class · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 14, 2025

## Python Workers handlers now live in an entrypoint class

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are changing how Python Workers are structured by default. Previously, handlers were defined at the top-level of a module as `on_fetch`, `on_scheduled`, etc. methods, but now they live in an entrypoint class.

Here's an example of how to now define a Worker with a fetch handler:
    
    
    from workers import Response, WorkerEntrypoint
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            return Response("Hello World!")

To keep using the old-style handlers, you can specify the `disable_python_no_global_handlers` compatibility flag in your wrangler file:
    
    
    {
    	"compatibility_flags": [
    		"disable_python_no_global_handlers"
    	]
    }
    
    
    compatibility_flags = [ "disable_python_no_global_handlers" ]

Consult the [Python Workers documentation](https://developers.cloudflare.com/workers/languages/python/) for more details.

---
url: https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/
title: Python Workers now support WSGI web frameworks like Django and Flask \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.734898+00:00
---

# Python Workers now support WSGI web frameworks like Django and Flask · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2026

## Python Workers now support WSGI web frameworks like Django and Flask

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Python web frameworks following the [Web Server Gateway Interface (WSGI) ↗︎](https://peps.python.org/pep-3333/) or [Asynchronous Server Gateway Interface (ASGI) ↗︎](https://asgi.readthedocs.io/) specification can now be used in Python Workers.

#### Using web frameworks with Python Workers

Based on the web framework you are using, you can use either `wsgi` or `asgi` from the `workers` module.

#### WSGI frameworks

For WSGI frameworks like Django or Flask:
    
    
    from workers import wsgi
    
    from django.core.wsgi import get_wsgi_application
    
    app = get_wsgi_application()
    Default = wsgi.entrypoint(app)

The `wsgi.entrypoint` is equivalent to creating a `WorkerEntrypoint` class and using the `wsgi.fetch` method. If you want more control over the `WorkerEntrypoint` class, you can do so:
    
    
    from workers import wsgi, WorkerEntrypoint
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            return await wsgi.fetch(app, request, self.env)

#### ASGI frameworks

For ASGI frameworks like FastAPI or Starlette:
    
    
    from workers import asgi
    
    from fastapi import FastAPI
    
    app = FastAPI()
    Default = asgi.entrypoint(app)

For more information about using individual web frameworks, refer to the [packages documentation in Python Workers](https://developers.cloudflare.com/workers/languages/python/packages/).

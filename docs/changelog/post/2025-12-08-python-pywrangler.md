---
url: https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/
title: Easy Python package management with Pywrangler \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:31.105073+00:00
---

# Easy Python package management with Pywrangler · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 8, 2025

## Easy Python package management with Pywrangler

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-08-python-pywrangler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are introducing a brand new tool called Pywrangler, which simplifies package management in Python Workers by automatically installing Workers-compatible Python packages into your project.

With Pywrangler, you specify your Worker's Python dependencies in your `pyproject.toml` file:
    
    
    [project]
    name = "python-beautifulsoup-worker"
    version = "0.1.0"
    description = "A simple Worker using beautifulsoup4"
    requires-python = ">=3.12"
    dependencies = [
        "beautifulsoup4"
    ]
    
    [dependency-groups]
    dev = [
      "workers-py",
      "workers-runtime-sdk"
    ]

You can then develop and deploy your Worker using the following commands:
    
    
    uv run pywrangler dev
    uv run pywrangler deploy

Pywrangler automatically downloads and vendors the necessary packages for your Worker, and these packages are bundled with the Worker when you deploy.

Consult the [Python packages documentation](https://developers.cloudflare.com/workers/languages/python/packages/) for full details on Pywrangler and Python package management in Workers.

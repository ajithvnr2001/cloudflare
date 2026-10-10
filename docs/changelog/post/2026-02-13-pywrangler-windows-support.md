---
url: https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/
title: Better Windows support for Python Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.651073+00:00
---

# Better Windows support for Python Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-13-pywrangler-windows-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 25, 2026

## Better Windows support for Python Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Pywrangler ↗︎](https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler), the CLI tool for managing Python Workers and packages, now supports Windows, allowing you to develop and deploy Python Workers from Windows environments. Previously, Pywrangler was only available on macOS and Linux.

You can install and use Pywrangler on Windows the same way you would on other platforms. [Specify your Worker's Python dependencies](https://developers.cloudflare.com/workers/languages/python/packages/) in your `pyproject.toml` file, then use the following commands to develop and deploy:
    
    
    uvx --from workers-py pywrangler dev
    uvx --from workers-py pywrangler deploy

All existing Pywrangler functionality, including package management, local development, and deployment, works on Windows without any additional configuration.

#### Requirements

This feature requires the following minimum versions:

  * `wrangler` >= 4.64.0
  * `workers-py` >= 1.72.0
  * `uv` >= 0.9.28



To upgrade `workers-py` (which includes Pywrangler) in your project, run:
    
    
    uv tool upgrade workers-py

To upgrade `wrangler`, run:
    
    
    npm install -g wrangler@latest

To upgrade `uv`, run:
    
    
    uv self update

To get started with Python Workers on Windows, refer to the [Python packages documentation](https://developers.cloudflare.com/workers/languages/python/packages/) for full details on Pywrangler.

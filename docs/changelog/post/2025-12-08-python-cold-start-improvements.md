---
url: https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/
title: Python cold start improvements \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.178134+00:00
---

# Python cold start improvements · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 8, 2025

## Python cold start improvements

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Python Workers now feature improved cold start performance, reducing initialization time for new Worker instances. This improvement is particularly noticeable for Workers with larger dependency sets or complex initialization logic.

Every time you deploy a Python Worker, a memory snapshot is captured after the top level of the Worker is executed. This snapshot captures all imports, including package imports that are often costly to load. The memory snapshot is loaded when the Worker is first started, avoiding the need to reload the Python runtime and all dependencies on each cold start.

We set up a benchmark that imports common packages ([httpx ↗︎](https://www.python-httpx.org/), [fastapi ↗︎](https://fastapi.tiangolo.com/) and [pydantic ↗︎](https://docs.pydantic.dev/latest/)) to see how Python Workers stack up against other platforms:

Platform | Mean Cold Start (ms)  
---|---  
Cloudflare Python Workers | 1027  
AWS Lambda | 2502  
Google Cloud Run | 3069  
  
These benchmarks run continuously. You can view the results and the methodology on our [benchmark page ↗︎](https://cold.edgeworker.net).

In additional testing, we have found that without any memory snapshot, the cold start for this benchmark takes around 10 seconds, so this change improves cold start performance by roughly a factor of 10.

To get started with Python Workers, check out our [Python Workers overview](https://developers.cloudflare.com/workers/languages/python/).

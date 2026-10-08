---
url: https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/
title: Increased vCPU for Workers Builds on paid plans \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:22.331890+00:00
---

# Increased vCPU for Workers Builds on paid plans · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 18, 2025

## Increased vCPU for Workers Builds on paid plans

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-07-builds-increased-cpu-paid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We recently [increased the available disk space](https://developers.cloudflare.com/changelog/2025-08-04-builds-increased-disk-size/) from 8 GB to 20 GB for **all** plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to **4 vCPU**.

These changes continue our focus on making [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) faster and more reliable.

Metric | Free Plan | Paid Plans  
---|---|---  
CPU | 2 vCPU | **4 vCPU**  
  
#### Performance Improvements

  * **Fast build times** : Even single-threaded workloads benefit from having more vCPUs
  * **2x faster multi-threaded builds** : Tools like [esbuild ↗︎](https://esbuild.github.io/) and [webpack ↗︎](https://webpack.js.org/) can now utilize additional cores, delivering near-linear performance scaling



All other [build limits](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/) — including memory, build minutes, and timeout remain unchanged.

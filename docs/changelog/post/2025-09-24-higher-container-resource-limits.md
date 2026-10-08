---
url: https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/
title: Run more Containers with higher resource limits \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:23.638363+00:00
---

# Run more Containers with higher resource limits · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2025

## Run more Containers with higher resource limits

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-24-higher-container-resource-limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run more Containers concurrently with higher limits on CPU, memory, and disk.

Limit | New Limit | Previous Limit  
---|---|---  
Memory for concurrent live Container instances | 400GiB | 40GiB  
vCPU for concurrent live Container instances | 100 | 20  
Disk for concurrent live Container instances | 2TB | 100GB  
  
You can now run 1000 instances of the `dev` instance type, 400 instances of `basic`, or 100 instances of `standard` concurrently.

This opens up new possibilities for running larger-scale workloads on Containers.

See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container, and the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

---
url: https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/
title: Run 15x more Containers with higher resource limits \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:38.831419+00:00
---

# Run 15x more Containers with higher resource limits · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 25, 2026

## Run 15x more Containers with higher resource limits

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run more [Containers](https://developers.cloudflare.com/containers/) concurrently with significantly higher limits on memory, vCPU, and disk.

Limit | Previous Limit | New Limit  
---|---|---  
Memory for concurrent live Container instances | 400GiB | 6TiB  
vCPU for concurrent live Container instances | 100 | 1,500  
Disk for concurrent live Container instances | 2TB | 30TB  
  
This 15x increase enables larger-scale workloads on Containers. You can now run 15,000 instances of the `lite` instance type, 6,000 instances of `basic`, over 1,500 instances of `standard-1`, or over 1,000 instances of `standard-2` concurrently.

Refer to [Limits](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

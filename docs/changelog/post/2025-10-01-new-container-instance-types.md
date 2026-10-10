---
url: https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/
title: Larger Container instance types \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.206420+00:00
---

# Larger Container instance types · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-01-new-container-instance-types/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2025

## Larger Container instance types

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

New instance types provide up to 4 vCPU, 12 GiB of memory, and 20 GB of disk per container instance.

Instance Type | vCPU | Memory | Disk  
---|---|---|---  
lite | 1/16 | 256 MiB | 2 GB  
basic | 1/4 | 1 GiB | 4 GB  
standard-1 | 1/2 | 4 GiB | 8 GB  
standard-2 | 1 | 6 GiB | 12 GB  
standard-3 | 2 | 8 GiB | 16 GB  
standard-4 | 4 | 12 GiB | 20 GB  
  
The `dev` and `standard` instance types are preserved for backward compatibility and are aliases for `lite` and `standard-1`, respectively. The `standard-1` instance type now provides up to 8 GB of disk instead of only 4 GB.

See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container, and the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/) for more details on the available instance types and limits.

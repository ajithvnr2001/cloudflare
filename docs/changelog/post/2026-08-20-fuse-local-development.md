---
url: https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/
title: Use FUSE in local Containers development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:09.533857+00:00
---

# Use FUSE in local Containers development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 20, 2026

## Use FUSE in local Containers development

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to `wrangler dev`, the Cloudflare Vite plugin, and direct Miniflare use.

Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when `/dev/fuse` is available.

Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.

For requirements and troubleshooting, refer to [FUSE support during local development](https://developers.cloudflare.com/containers/guides/local-dev/#fuse-support). For a complete example, refer to [Mount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/).

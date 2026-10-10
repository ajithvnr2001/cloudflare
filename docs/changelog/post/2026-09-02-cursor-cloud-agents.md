---
url: https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/
title: Run Cursor Cloud Agents on Cloudflare via self-hosted machines \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.806745+00:00
---

# Run Cursor Cloud Agents on Cloudflare via self-hosted machines · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2026

## Run Cursor Cloud Agents on Cloudflare via self-hosted machines

[Sandboxes](https://developers.cloudflare.com/sandbox/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cursor self-hosted machines ↗︎](https://cursor.com/docs/cloud-agent/self-hosted) let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by [Cloudflare Containers](https://developers.cloudflare.com/containers/).

![Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3308,height=1916,format=webp/_astro/cursor-cloud-agents-self-hosted-pool.XNeWCXB2.png)

Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source [Cursor Cloudflare Workers template ↗︎](https://github.com/anysphere/cloudflare-workers) deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.

To get started, refer to [Run Cursor Cloud Agents on Cloudflare via self-hosted machines](https://developers.cloudflare.com/sandbox/coding-agents/cursor/).

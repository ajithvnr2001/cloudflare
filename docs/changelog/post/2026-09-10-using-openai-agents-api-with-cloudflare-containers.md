---
url: https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/
title: Use Cloudflare Containers with Codex via the OpenAI Agents API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.396745+00:00
---

# Use Cloudflare Containers with Codex via the OpenAI Agents API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 10, 2026

## Use Cloudflare Containers with Codex via the OpenAI Agents API

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The OpenAI Agents API gives your application access to Codex through an OpenAI-managed API.

OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and uses Cloudflare Containers as the execution environment.

Cloudflare Containers can now provide self-hosted execution environments for the OpenAI Agents API. The open-source [OpenAI Agents API Workers template ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api) provides a reference implementation. The Worker maintains a Cloudflare Container for each Codex session, keeps active work running, reconnects on follow-up input, and shuts down automatically when idle.

You can configure the reference implementation to meet your needs by extending the Container to provide controlled access to data and the network or by integrating it with other Cloudflare products.

To get started, refer to [Run Codex on Cloudflare using the OpenAI Agents API](https://developers.cloudflare.com/sandbox/tutorials/openai-agents-api/).

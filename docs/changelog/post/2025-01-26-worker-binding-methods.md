---
url: https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/
title: AI Gateway Introduces New Worker Binding Methods \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:01.145599+00:00
---

# AI Gateway Introduces New Worker Binding Methods · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 30, 2025

## AI Gateway Introduces New Worker Binding Methods

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We have released new [Workers bindings API methods](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.

To add an AI binding to your Worker, include the following in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):

![Add an AI binding to your Worker.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=754,height=135,format=webp/_astro/add-binding.BoYTiyon.png)

With the new AI Gateway binding methods, you can now:

  * Send feedback and update metadata with `patchLog`.
  * Retrieve detailed log information using `getLog`.
  * Execute [universal requests](https://developers.cloudflare.com/ai-gateway/usage/universal/) to any AI Gateway provider with `run`.



For example, to send feedback and update metadata using `patchLog`:

![Send feedback and update metadata using patchLog:](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=736,height=235,format=webp/_astro/send-feedback.BGRzKmd9.png)

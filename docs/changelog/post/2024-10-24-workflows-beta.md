---
url: https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/
title: Workflows is now in open beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.935630+00:00
---

# Workflows is now in open beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 24, 2024

## Workflows is now in open beta

[Workers](https://developers.cloudflare.com/workers/)[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workflows is now in open beta, and available to any developer a free or paid Workers plan.

Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.

#### Get started

You can get started with Workflows by [following our get started guide](https://developers.cloudflare.com/workflows/get-started/guide/) and/or using `npm create cloudflare` to pull down the starter project:
    
    
    npm create cloudflare@latest workflows-starter -- --template "cloudflare/workflows-starter"

You can open the `src/index.ts` file, extend it, and use `wrangler deploy` to deploy your first Workflow. From there, you can:

  * Learn the [Workflows API](https://developers.cloudflare.com/workflows/build/workers-api/)
  * [Trigger Workflows](https://developers.cloudflare.com/workflows/build/trigger-workflows/) via your Workers apps.
  * Understand the [Rules of Workflows](https://developers.cloudflare.com/workflows/build/rules-of-workflows/) and how to adopt best practices



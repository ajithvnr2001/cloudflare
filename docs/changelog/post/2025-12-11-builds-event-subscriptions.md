---
url: https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/
title: Get notified when your Workers builds succeed or fail \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.833088+00:00
---

# Get notified when your Workers builds succeed or fail · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 9, 2026

## Get notified when your Workers builds succeed or fail

[Workers](https://developers.cloudflare.com/workers/)[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/).

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) publishes events to a [Queue](https://developers.cloudflare.com/queues/) that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.

You can deploy [this Worker ↗︎](https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template) to your own Cloudflare account to send build notifications to Slack:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template)

The template includes:

  * Build status with Preview/Live URLs for successful deployments
  * Inline error messages for failed builds
  * Branch, commit hash, and author name

![Slack notifications showing build events](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1700,height=1088,format=webp/_astro/builds-notifications-slack.rcRiU95L.png)

For setup instructions, refer to the [template README ↗︎](https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme) or the [Event Subscriptions documentation](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

---
url: https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/
title: Event subscriptions for Artifacts lifecycle events \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.046902+00:00
---

# Event subscriptions for Artifacts lifecycle events · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 19, 2026

## Event subscriptions for Artifacts lifecycle events

[Artifacts](https://developers.cloudflare.com/artifacts/)[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now receive [event notifications](https://developers.cloudflare.com/queues/event-subscriptions/) for [Artifacts](https://developers.cloudflare.com/artifacts/) repository changes and consume them from a Worker to build commit-driven automation.

This allows you to:

  * Run custom workflows when a repository is created or imported
  * Kick off a build and deploy a change when an agent pushes to a repo
  * Trigger a review agent on every push



Available events include:

  * **Account-level events** (`artifacts` source) — `repo.created`, `repo.deleted`, `repo.forked`, `repo.imported`
  * **Repository-level events** (`artifacts.repo` source) — `pushed`, `cloned`, `fetched`



To learn more, refer to [Artifacts documentation](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/).

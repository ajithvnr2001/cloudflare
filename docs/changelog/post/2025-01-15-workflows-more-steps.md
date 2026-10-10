---
url: https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/
title: Increased Workflows limits and improved instance queueing. \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.423653+00:00
---

# Increased Workflows limits and improved instance queueing. · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-15-workflows-more-steps/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 15, 2025

## Increased Workflows limits and improved instance queueing.

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) (beta) now allows you to define up to 1024 [steps](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstep). `sleep` steps do not count against this limit.

We've also added:

  * `instanceId` as property to the [`WorkflowEvent`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowevent) type, allowing you to retrieve the current instance ID from within a running Workflow instance
  * Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.
  * Support for [`pause` and `resume`](https://developers.cloudflare.com/workflows/build/workers-api/#pause) for Workflow instances in a queued state.



We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new `waitForEvent` API over the coming weeks.

---
url: https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/
title: New Pause & Purge APIs for Queues \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:07.402779+00:00
---

# New Pause & Purge APIs for Queues · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 27, 2025

## New Pause & Purge APIs for Queues

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Queues](https://developers.cloudflare.com/queues/) now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:

  * Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug
  * You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog
  * Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed



To pause a queue using [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run the `pause-delivery` command. Paused queues continue to receive messages. And you can easily unpause a queue using the `resume-delivery` command.

Pause and resume a queuebash
    
    
    $ wrangler queues pause-delivery my-queue
    Pausing message delivery for queue my-queue.
    Paused message delivery for queue my-queue.
    
    $ wrangler queues resume-delivery my-queue
    Resuming message delivery for queue my-queue.
    Resumed message delivery for queue my-queue.

Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:

Purge a queuebash
    
    
    $ wrangler queues purge my-queue
    ✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue
    Purged queue 'my-queue'

You can also do these operations using the [Queues REST API](https://developers.cloudflare.com/api/resources/queues/), or the dashboard page for a queue.

![Pause and purge using the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2200,height=574,format=webp/_astro/pause-purge.SQ7B3RCF.png)

This feature is available on all new and existing queues. Head over to the [pause and purge documentation](https://developers.cloudflare.com/queues/configuration/pause-purge) to learn more. And if you haven't used Cloudflare Queues before, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

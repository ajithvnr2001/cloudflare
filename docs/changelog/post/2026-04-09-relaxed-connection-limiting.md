---
url: https://developers.cloudflare.com/changelog/post/2026-04-09-relaxed-connection-limiting/
title: Relaxed simultaneous connection limiting for Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.810677+00:00
---

# Relaxed simultaneous connection limiting for Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-09-relaxed-connection-limiting/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 9, 2026

## Relaxed simultaneous connection limiting for Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [simultaneous open connections limit](https://developers.cloudflare.com/workers/platform/limits/#simultaneous-open-connections) has been relaxed. Previously, each Worker invocation was limited to six open connections at a time for the entire lifetime of each connection, including while reading the response body. Now, a connection is freed as soon as response headers arrive, so the six-connection limit only constrains how many connections can be in the initial "waiting for headers" phase simultaneously.

#### Before: New connections are blocked until an earlier connection fully completes

![A 7th fetch is queued until an earlier connection fully completes, including reading its entire response body](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=500,format=svg/_astro/connection-limit-before.BYti-Sxe.svg)

#### After: New connections can start as soon as response headers arrive

![A 7th fetch starts as soon as any earlier connection receives its response headers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=500,format=svg/_astro/connection-limit-after.BfVRyLE8.svg)

This means Workers can now have many more connections open at the same time without queueing, as long as no more than six are waiting for their initial response. This eliminates the `Response closed due to connection limit` exception that could previously occur when the runtime canceled stalled connections to prevent deadlocks.

Previously, the runtime used a deadlock avoidance algorithm that watched each open connection for I/O activity. If all six connections appeared idle — even momentarily — the runtime would cancel the least-recently-used connection to make room for new requests. In practice, this heuristic was fragile. For example, when a response used `Content-Encoding: gzip`, the runtime's internal decompression created brief gaps between read and write operations. During these gaps, the connection appeared stalled despite being actively read by the Worker. If multiple connections hit these gaps at the same time, the runtime could spuriously cancel a connection that was working correctly. By only counting connections during the waiting-for-headers phase — where the runtime is fully in control and there is no ambiguity about whether the connection is active — this class of bug is eliminated entirely.

#### Before: Connections could be canceled during brief internal pauses

![A connection with gaps from gzip decompression appears idle and is canceled by the runtime](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=260,format=svg/_astro/connection-cancel-before.D4As_PDP.svg)

#### After: Connections complete normally regardless of internal pauses

![The same connection completes normally because the body phase is no longer counted against the limit](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=230,format=svg/_astro/connection-cancel-after.RdmZLNge.svg)

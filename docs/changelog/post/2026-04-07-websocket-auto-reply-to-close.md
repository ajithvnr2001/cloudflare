---
url: https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/
title: WebSockets now automatically reply to Close frames \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.960080+00:00
---

# WebSockets now automatically reply to Close frames · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-07-websocket-auto-reply-to-close/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2026

## WebSockets now automatically reply to Close frames

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Workers runtime now automatically sends a reciprocal Close frame when it receives a Close frame from the peer. The `readyState` transitions to `CLOSED` before the `close` event fires. This matches the [WebSocket specification ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close_event) and standard browser behavior.

This change is enabled by default for Workers using compatibility dates on or after `2026-04-07` (via the [`web_socket_auto_reply_to_close`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close) compatibility flag). Existing code that manually calls `close()` inside the `close` event handler will continue to work — the call is silently ignored when the WebSocket is already closed.
    
    
    const [client, server] = Object.values(new WebSocketPair());
    server.accept();
    
    server.addEventListener("close", (event) => {
    	// readyState is already CLOSED — no need to call server.close().
    	console.log(server.readyState); // WebSocket.CLOSED
    	console.log(event.code); // 1000
    	console.log(event.wasClean); // true
    });

#### Half-open mode for WebSocket proxying

The automatic close behavior can interfere with WebSocket proxying, where a Worker sits between a client and a backend and needs to coordinate the close on both sides independently. To support this use case, pass `{ allowHalfOpen: true }` to `accept()`:
    
    
    const [client, server] = Object.values(new WebSocketPair());
    
    server.accept({ allowHalfOpen: true });
    
    server.addEventListener("close", (event) => {
    	// readyState is still CLOSING here, giving you time
    	// to coordinate the close on the other side.
    	console.log(server.readyState); // WebSocket.CLOSING
    
    	// Manually close when ready.
    	server.close(event.code, "done");
    });

For more information, refer to [WebSockets Close behavior](https://developers.cloudflare.com/workers/runtime-apis/websockets/#close-behavior).

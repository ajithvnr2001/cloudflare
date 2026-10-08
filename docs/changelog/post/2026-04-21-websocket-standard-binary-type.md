---
url: https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/
title: WebSocket binary messages now delivered as Blob by default \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:48.666444+00:00
---

# WebSocket binary messages now delivered as Blob by default · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 21, 2026

## WebSocket binary messages now delivered as Blob by default

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-websocket-standard-binary-type/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Binary frames received on a `WebSocket` are now delivered to the `message` event as [`Blob` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Blob) objects by default. This matches the [WebSocket specification ↗︎](https://websockets.spec.whatwg.org/) and standard browser behavior. Previously, binary frames were always delivered as [`ArrayBuffer` ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer). The [`binaryType`](https://developers.cloudflare.com/workers/runtime-apis/websockets/#binarytype) property on `WebSocket` controls the delivery type on a per-WebSocket basis.

This change has been active for Workers with compatibility dates on or after `2026-03-17`, via the [`websocket_standard_binary_type`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#websocket-standard-binary-type) compatibility flag. We should have documented this change when it shipped but didn't. We're sorry for the trouble that caused. If your Worker handles binary WebSocket messages and assumes `event.data` is an `ArrayBuffer`, the frames will arrive as `Blob` instead, and a naive `instanceof ArrayBuffer` check will silently drop every frame.

To opt back into `ArrayBuffer` delivery, assign `binaryType` before calling `accept()`. This works regardless of the compatibility flag:
    
    
    const resp = await fetch("https://example.com", {
    	headers: { Upgrade: "websocket" },
    });
    const ws = resp.webSocket;
    
    // Opt back into ArrayBuffer delivery for this WebSocket.
    ws.binaryType = "arraybuffer";
    ws.accept();
    
    ws.addEventListener("message", (event) => {
    	if (typeof event.data === "string") {
    		// Text frame.
    	} else {
    		// event.data is an ArrayBuffer because we set binaryType above.
    	}
    });

If you are not ready to migrate and want to keep `ArrayBuffer` as the default for all WebSockets in your Worker, add the `no_websocket_standard_binary_type` flag to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).

This change has no effect on the Durable Object hibernatable WebSocket [`webSocketMessage`](https://developers.cloudflare.com/durable-objects/best-practices/websockets/) handler, which continues to receive binary data as `ArrayBuffer`.

For more information, refer to [WebSockets binary messages](https://developers.cloudflare.com/workers/runtime-apis/websockets/#binary-messages).

---
url: https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/
title: Browser Run adds session and DevTools methods to browser bindings \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.817648+00:00
---

# Browser Run adds session and DevTools methods to browser bindings · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-21-browser-binding-methods/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 21, 2026

## Browser Run adds session and DevTools methods to browser bindings

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) browser bindings now provide typed methods for session management and DevTools operations. You can acquire a session, connect a browser client, create Live View URLs, manage targets, and close sessions without constructing HTTP requests.

The new `acquire()` and `launch()` methods also accept [`outboundByHost`](https://developers.cloudflare.com/browser-run/features/outbound-workers/). This lets you route requests for selected hostnames through another Worker, including a Worker that adds authentication or reaches a private service.
    
    
    const connection = await env.BROWSER.launch({
    	outboundByHost: {
    		"private.example.test": env.OUTBOUND,
    	},
    });
    
    
    const connection = await env.BROWSER.launch({
    	outboundByHost: {
    		"private.example.test": env.OUTBOUND,
    	},
    });

Use `connectSession(sessionId)` when you need to acquire and connect in separate steps. The method returns a session-pinned `webSocket` Fetcher for a CDP client.

The binding also includes session methods for Live View, active sessions, session history, limits, session details, and cleanup. The nested `devtools` binding provides typed methods for browser version information, protocol descriptions, and target operations such as listing, creating, activating, and closing targets.

Refer to the [Browser binding API documentation](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/) for method signatures and the [outbound Worker feature guide](https://developers.cloudflare.com/browser-run/features/outbound-workers/) for routing examples.

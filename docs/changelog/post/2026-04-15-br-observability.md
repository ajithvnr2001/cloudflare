---
url: https://developers.cloudflare.com/changelog/post/2026-04-15-br-observability/
title: Browser Run adds Live View, Human in the Loop, and Session Recordings \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:46.825614+00:00
---

# Browser Run adds Live View, Human in the Loop, and Session Recordings · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-15-br-observability/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 15, 2026

## Browser Run adds Live View, Human in the Loop, and Session Recordings

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-br-observability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When browser automation fails or behaves unexpectedly, it can be hard to understand what happened. We are shipping three new features in [Browser Run](https://developers.cloudflare.com/browser-run/) (formerly Browser Rendering) to help:

  * **[Live View](https://developers.cloudflare.com/browser-run/features/live-view/)** for real-time visibility
  * **[Human in the Loop](https://developers.cloudflare.com/browser-run/features/human-in-the-loop/)** for human intervention
  * **[Session Recordings](https://developers.cloudflare.com/browser-run/features/session-recording/)** for replaying sessions after they end



#### Live View

[Live View](https://developers.cloudflare.com/browser-run/features/live-view/) lets you see what your agent is doing in real time. The page, DOM, console, and network requests are all visible for any active browser session. Access Live View from the Cloudflare dashboard, via the hosted UI at `live.browser.run`, or using native Chrome DevTools.

#### Human in the Loop

When your agent hits a snag like a login page or unexpected edge case, it can hand off to a human instead of failing. With [Human in the Loop](https://developers.cloudflare.com/browser-run/features/human-in-the-loop/), a human steps into the live browser session through Live View, resolves the issue, and hands control back to the script.

Today, you can step in by opening the Live View URL for any active session. Next, we are adding a handoff flow where the agent can signal that it needs help, notify a human to step in, then hand control back to the agent once the issue is resolved.

![Browser Run Human in the Loop demo where an AI agent searches Amazon, selects a product, and requests human help when authentication is needed to buy](https://developers.cloudflare.com/images/browser-run/liveview.gif)

#### Session Recordings

[Session Recordings](https://developers.cloudflare.com/browser-run/features/session-recording/) records DOM state so you can replay any session after it ends. Enable recordings by passing `recording: true` when launching a browser. After the session closes, view the recording in the Cloudflare dashboard under **Browser Run** > **Runs** , or retrieve via API using the session ID. Next, we are adding the ability to inspect DOM state and console output at any point during the recording.

![Browser Run session recording showing an automated browser navigating the Sentry Shop and adding a bomber jacket to the cart](https://developers.cloudflare.com/images/browser-run/sessionrecording.gif)

To get started, refer to the documentation for [Live View](https://developers.cloudflare.com/browser-run/features/live-view/), [Human in the Loop](https://developers.cloudflare.com/browser-run/features/human-in-the-loop/), and [Session Recording](https://developers.cloudflare.com/browser-run/features/session-recording/).

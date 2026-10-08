---
url: https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/
title: Canvas Remoting optimizes performance for productivity applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:45.991595+00:00
---

# Canvas Remoting optimizes performance for productivity applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 10, 2026

## Canvas Remoting optimizes performance for productivity applications

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-10-canvas-remoting-performance/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Remote Browser Isolation now supports **Canvas Remoting** , improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.

#### Key improvements

  * **10x bandwidth reduction:** Microsoft Word and other Office apps use 90% less bandwidth
  * **Smooth performance:** Google Sheets maintains consistent 30fps rendering
  * **Responsive terminals:** Web-based development environments and AI notebooks work in real-time
  * **Zero configuration:** Enabled by default for all Browser Isolation customers



#### How it works

Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:

  1. Captures Canvas draw commands at the source
  2. Converts them to lightweight vector instructions
  3. Renders Canvas content on the client



This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.

#### Managing Canvas Remoting

To temporarily disable for troubleshooting:

  * Right-click the isolated webpage background
  * Select **Disable Canvas Remoting**
  * Re-enable the same way by selecting **Enable Canvas Remoting**



#### Limitations

Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to [Canvas Remoting](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/canvas-remoting/).

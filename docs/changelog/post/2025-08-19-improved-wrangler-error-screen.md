---
url: https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/
title: Easier debugging in Workers with improved Wrangler error screen \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:19.906088+00:00
---

# Easier debugging in Workers with improved Wrangler error screen · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2025

## Easier debugging in Workers with improved Wrangler error screen

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-19-improved-wrangler-error-screen/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler's error screen has received several improvements to enhance your debugging experience!

The error screen now features a refreshed design thanks to [youch ↗︎](https://www.npmjs.com/package/youch), with support for both light and dark themes, improved source map resolution logic that handles missing source files more reliably, and better error cause display.

Before | After (Light) | After (Dark)  
---|---|---  
![Old error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/old-error-screen.yurLWiKb.png) | ![New light theme error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/new-error-screen-light.CcroERTP.png) | ![New dark theme error screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=990,height=1500,format=webp/_astro/new-error-screen-dark.BIDA2RGg.png)  
  
Try it out now with `npx wrangler@latest dev` in your Workers project.

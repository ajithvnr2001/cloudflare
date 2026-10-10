---
url: https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/
title: Share local dev servers through Cloudflare Tunnel in Wrangler and Vite \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.128681+00:00
---

# Share local dev servers through Cloudflare Tunnel in Wrangler and Vite · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-18-local-dev-tunnels/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 18, 2026

## Share local dev servers through Cloudflare Tunnel in Wrangler and Vite

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now share local dev sessions through [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and get a public URL when using either [Wrangler](https://developers.cloudflare.com/workers/wrangler/) or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). This is useful when you need to share a preview, test a webhook, or access your app from another device.

![Vite local dev tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1000,height=678,format=webp/_astro/vite-local-dev-tunnel.CW4xpgIR.gif)

This lets you either:

  * start a temporary [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/) with a random `*.trycloudflare.com` hostname, or
  * use an existing [named tunnel](https://developers.cloudflare.com/tunnel/get-started/#create-a-tunnel) for a stable hostname and to restrict access with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/).



To start a tunnel, press `t` in Wrangler or `t + Enter` in Vite while your dev server is running. For details on setting up a named tunnel, refer to [Share a local dev server](https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/).

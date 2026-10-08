---
url: https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/
title: Manage Cloudflare Tunnels with Wrangler \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:41.720570+00:00
---

# Manage Cloudflare Tunnels with Wrangler · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 19, 2026

## Manage Cloudflare Tunnels with Wrangler

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-19-wrangler-tunnel-commands/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now manage [Cloudflare Tunnels](https://developers.cloudflare.com/tunnel/) directly from [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the CLI for the Cloudflare Developer Platform. The new [`wrangler tunnel`](https://developers.cloudflare.com/workers/wrangler/commands/tunnel/) commands let you create, run, and manage tunnels without leaving your terminal.

![Wrangler tunnel commands demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1094,format=webp/_astro/wrangler-tunnel.DOqrtGGg.gif)

Available commands:

  * `wrangler tunnel create` — Create a new remotely managed tunnel.
  * `wrangler tunnel list` — List all tunnels in your account.
  * `wrangler tunnel info` — Display details about a specific tunnel.
  * `wrangler tunnel delete` — Delete a tunnel.
  * `wrangler tunnel run` — Run a tunnel using the cloudflared daemon.
  * `wrangler tunnel quick-start` — Start a free, temporary tunnel without an account using [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).



Wrangler handles downloading and managing the [cloudflared](https://developers.cloudflare.com/tunnel/downloads/) binary automatically. On first use, you will be prompted to download `cloudflared` to a local cache directory.

These commands are currently experimental and may change without notice.

To get started, refer to the [Wrangler tunnel commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/tunnel/).

---
url: https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/
title: Configure origin application settings for Cloudflare Tunnel in the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:09.005904+00:00
---

# Configure origin application settings for Cloudflare Tunnel in the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 18, 2026

## Configure origin application settings for Cloudflare Tunnel in the dashboard

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/). These settings control how `cloudflared` connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.

![Configure origin application settings in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/tunnel-origin-settings-dashboard.CsC2RwFC.gif)

When editing a published application, expand **Additional application settings** to configure parameters organized into three categories:

  * **HTTP** — Set a custom HTTP Host header or disable chunked encoding.
  * **TLS** — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.
  * **Connection** — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)

For the full list of origin parameters, refer to [Origin parameters](https://developers.cloudflare.com/tunnel/reference/origin-parameters/).

---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/
title: Error 1033 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.633062+00:00
---

# Error 1033 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1033



# Error 1033

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1033: Cloudflare Tunnel error Common cause Resolution

## Error 1033: Cloudflare Tunnel error

This error indicates an issue with [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

### Common cause

You have requested a page on a website (`tunnel.example.com`) that is on the Cloudflare network. The host (`tunnel.example.com`) is configured with Cloudflare Tunnel, and Cloudflare is currently unable to resolve it.

### Resolution

A `1033` error indicates your tunnel is not connected to Cloudflare's network because Cloudflare's network cannot find a healthy `cloudflared` instance to receive the traffic.

First, review whether your tunnel is listed as `Active` in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) by going to **Networking** > **Tunnels** or run `cloudflared tunnel list`. If the tunnel is not `Active`, review the following and take the action necessary for your tunnel status:

Status | Meaning | Recommended Action  
---|---|---  
**Healthy** | The tunnel is active and serving traffic through four connections to the Cloudflare global network. | No action is required. Your tunnel is running correctly.  
**Inactive** | The tunnel has been created (via the API or dashboard) but the `cloudflared` connector has never been run to establish a connection. | Install and run `cloudflared` on your origin server to connect the tunnel to Cloudflare. You can find the installation command in the Cloudflare dashboard under **Networking** > **Tunnels** — select your tunnel, then on the **Overview** tab select **Add a replica**. For API-based setup, refer to [Install and run the tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#4-install-and-run-the-tunnel).  
**Down** | The tunnel was previously connected but is currently disconnected because the `cloudflared` process has stopped. | 1\. Ensure the `cloudflared` [service](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/) or process is actively running on your server.   
2\. Check for server-side issues, such as the machine being powered off, an application crash, or recent network changes.  
**Degraded** | The `cloudflared` connector is running and the tunnel is serving traffic, but at least one individual connection has failed. Further degradation in [tunnel availability](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) could risk the tunnel going down and failing to serve traffic. | 1\. Review your `cloudflared` [logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) for connection failures or error messages.   
2\. Investigate local network and firewall rules to ensure they are not blocking connections to the [Cloudflare Tunnel IPs and ports](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/).   
  
  
[PreviousError 1025](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1025/)[NextError 1034](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1034/)

Was this helpful?

YesNo

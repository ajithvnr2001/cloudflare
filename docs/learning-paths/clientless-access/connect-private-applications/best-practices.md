---
url: https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/best-practices/
title: Best practices \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:44.657999+00:00
---

# Best practices · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/best-practices/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Clientless Access

  4. /[Connect your private applications](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/)
  5. /Best practices



# Best practices

Last updated Sep 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/best-practices/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDeploy another instance of cloudflaredStandardize public hostnamesConfigure TLS verification(Optional) Add Host header to accommodate local traffic management toolsEnable tunnel notificationsUpdate cloudflared

We recommend following these best practices when you deploy Cloudflare Tunnel for clientless access.

## Deploy another instance of cloudflared

For an additional point of availability, add a [`cloudflared` replica](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) to another host machine in your network.

## Standardize public hostnames

To make your applications easier to manage, standardize the public hostnames that you publish your applications on. Here are a few examples of how customers manage their public hostnames:

  * Delegate a subdomain of your primary public website to use for internal applications (for example, `tools.dev.customer.com`).
  * If your internal DNS infrastructure is available for public use, register your internal primary DNS record on Cloudflare and use this domain for your public hostname routes. This allows you to present applications on identical private and public hostnames.
  * Specify some sort of internal logic that generates hostnames based on the type of tool you are connecting. For example, if you have a set of applications in a US-East datacenter allocated explicitly for production resources, you could create subdomains of `tools.us-east.prod.ztproject.com`.



## Configure TLS verification

If your public hostname route serves an `HTTPS` application, keep TLS certificate verification enabled. If the service URL uses `localhost` or an IP address but the certificate covers a hostname, set [**Origin Server Name**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#originservername) to the hostname covered by the certificate. If the origin uses a private certificate authority, set [**CA Pool**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#capool).

Turn on [**Disable TLS certificate verification**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#notlsverify) only for temporary testing while you fix the certificate configuration. For a complete HTTPS origin decision tree, refer to [Troubleshoot HTTPS origins with Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/troubleshooting/https-origins/).

## (Optional) Add `Host` header to accommodate local traffic management tools

If your target application sits behind a load balancer or similar, you may need to set [**HTTP Host Header**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#httphostheader) to the service hostname. Load balancers in between the origin service and `cloudflared` can be difficult to troubleshoot, and you can typically resolve the issue by adding a request header to match the way that the load balancer typically identifies traffic.

## Enable tunnel notifications

[Enable notifications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/) in the Cloudflare dashboard to monitor tunnel health.

## Update cloudflared

[Update `cloudflared`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/) regularly to get the latest features and bug fixes.

[PreviousCreate a Cloudflare Tunnel](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/)[NextOverview](https://developers.cloudflare.com/learning-paths/clientless-access/access-application/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/clientless-access/connect-private-applications/best-practices.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

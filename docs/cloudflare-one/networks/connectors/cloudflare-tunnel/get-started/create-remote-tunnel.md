---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/
title: Create a tunnel (dashboard) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:16.655183+00:00
---

# Create a tunnel (dashboard) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Get started](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/)
  5. /Create a tunnel (dashboard)



# Create a tunnel (dashboard)

Last updated Jun 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Create a tunnel2a. Publish an application2b. Connect a network3\. View your tunnel

Follow this step-by-step guide to create your first [remotely-managed tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/#remotely-managed-tunnel).

Tip

If your server is behind a restrictive firewall, verify it can reach Cloudflare on port `7844` before proceeding. Refer to [Connectivity pre-checks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/).

## 1\. Create a tunnel

  1. Log in to the Cloudflare dashboard and go to **Networking** > **Tunnels**.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Select **Create a tunnel**.

  3. Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, `enterprise-VPC-01`).

  4. Select **Create Tunnel**.

  5. Choose your operating system, then copy the installation command and run it in a terminal on your origin server.

  6. Wait for the tunnel to connect. Once the connection is established, select **Continue**.




The next steps depend on whether you want to publish an application to the Internet or connect a private network.

## 2a. Publish an application

Follow these steps to publish an application to the Internet. If you are looking to connect a private resource, skip to the Connect a network section.

Prerequisites

Before you publish an application through your tunnel, you must [add a website to Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/).

After creating your tunnel, add a published application route:

  1. Go to **Networking** > **Tunnels** , then select your tunnel.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. On the **Routes** tab, select **Add route** , then select **Published application**.

  3. Enter a subdomain and select a **Domain** from the drop-down menu. Specify any subdomain or path information.

Note

If you add a multi-level subdomain (more than one level of subdomain), you must [order an Advanced Certificate for the hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#i-see-this-site-cant-provide-a-secure-connection).

Path routing

Specifying a path routes matching requests to the service URL, but does not strip or rewrite the path. The service receives the complete request path. To strip or rewrite paths, configure [URL Rewrite Rules](https://developers.cloudflare.com/rules/transform/url-rewrite/) at the Cloudflare edge or use a local reverse proxy.

  4. In **Service URL** , enter the protocol and address of your application (for example, `http://localhost:8000`). Refer to [supported protocols](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/) for available options.

If your origin already serves HTTPS or redirects HTTP to HTTPS, refer to [Troubleshoot HTTPS origins with Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/troubleshooting/https-origins/) before choosing the service URL.

  5. Select **Add route**.




Anyone on the Internet can now access the application at the specified hostname. To allow or block specific users, [create an Access application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

## 2b. Connect a network

To connect a private network through your tunnel, add a CIDR route:

  1. Go to **Networking** > **Routes**.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)
  2. Select **Create route** , then choose **Tunnel CIDR**.

  3. Select the tunnel you just created.

  4. In **Network** , enter the private IP address or CIDR range of your service (for example, `10.0.0.1` or `10.0.0.0/24`).

  5. Select **Create route**.




`cloudflared` can now route traffic to these destination IPs. To configure Zero Trust policies and connect as a user, refer to [Connect an IP/CIDR](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/).

Note

If you would like to route to a private application using its hostname instead of its IP, refer to [Connect a private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/).

## 3\. View your tunnel

After saving the tunnel, you will be redirected to the **Networking** > **Tunnels** page. Your tunnel should be listed with a `Healthy` status. If your tunnel status is `Inactive`, `Down`, or `Degraded`, refer to the [troubleshooting documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status) for recommended next steps.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/)[NextCreate a tunnel (API)](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

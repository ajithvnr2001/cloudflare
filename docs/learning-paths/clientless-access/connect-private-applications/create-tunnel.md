---
url: https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/
title: Create a Cloudflare Tunnel \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:44.801478+00:00
---

# Create a Cloudflare Tunnel · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Clientless Access

  4. /[Connect your private applications](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/)
  5. /Create a Cloudflare Tunnel



# Create a Cloudflare Tunnel

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a tunnelPublish an applicationAdditional resources

To enable clientless access to your applications, you will need to create a Cloudflare Tunnel that publishes applications to a domain on Cloudflare. A published application creates a public DNS record that routes traffic to a specific address, protocol, and port associated with a private application. For example, you can define a public hostname (`mywebapp.example.com`) to provide access to a web server running on `https://localhost:8080`. When a user goes to `mywebapp.example.com` in their browser, their request will first route to a Cloudflare data center where it is inspected against your configured security policies. Cloudflare will then forward validated requests down your tunnel to the web server.

![How an HTTP request reaches a private application connected with Cloudflare Tunnel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1768,height=1102,format=webp/_astro/handshake.eh3a-Ml1.jpg)

## Create a tunnel

To create a Cloudflare Tunnel:

  1. Log in to the Cloudflare dashboard and go to **Networking** > **Tunnels**.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Select **Create a tunnel**.

  3. Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, `enterprise-VPC-01`).

  4. Select **Create Tunnel**.

  5. Choose your operating system, then copy the installation command and run it in a terminal on your origin server.

  6. Wait for the tunnel to connect. Once the connection is established, select **Continue**.




## Publish an application

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




All users on the Internet can now connect to this application via its public hostname. In [Module 4: Secure your applications](https://developers.cloudflare.com/learning-paths/clientless-access/access-application/), we will discuss how to restrict access to authorized users.

Note

If the tunnel is disconnected:

  * Ensure that your on-premise or cloud firewall allows egress traffic on the [required ports](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#required-for-tunnel-operation).
  * Ensure that the `cloudflared` host machine can connect to your internal applications and services. Verify that the host has the proper security group memberships and that no firewalls will block traffic between the host and the target services.



## Additional resources

For more control over how traffic routes through your tunnel, refer to the following links:

  * [DNS records](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/)
  * [Load balancer](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/)



[PreviousOverview](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/)[NextBest practices](https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/clientless-access/connect-private-applications/create-tunnel.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

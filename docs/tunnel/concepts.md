---
url: https://developers.cloudflare.com/tunnel/concepts/
title: Tunnel fundamentals \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:02.832530+00:00
---

# Tunnel fundamentals · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/concepts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /Concepts



# Tunnel fundamentals

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/concepts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewThe connection starts with cloudflaredTunnel identity and connectorsQuick tunnelsHow traffic reaches a resourceStart buildingRelated resources

A Cloudflare Tunnel is a secure link between Cloudflare's network and your infrastructure, with a stable identity in your Cloudflare account.

Tunnel connections begin inside your network and remain open to Cloudflare, so the resources behind them do not need public IP addresses or open inbound ports. Traffic can reach those resources through the tunnel instead of connecting to them directly over the Internet.

## The connection starts with `cloudflared`

_Connect out to Cloudflare while keeping your resources private._

`cloudflared` is the daemon that establishes and maintains a tunnel's connections to Cloudflare. It initiates those connections from inside your network, allowing requests and responses to travel in both directions without requiring your origin to expose a public address.

This is the central idea behind Tunnel: Cloudflare does not connect to a public address on your server. `cloudflared` connects to Cloudflare first, and Cloudflare uses those existing connections to reach resources in your network.

Enable tunnelSend request

The private network has no inbound connections.

`cloudflared` opens connections from a private network to Cloudflare, allowing traffic to reach resources through those connections. A request sent before the tunnel exists is refused at the network boundary, because nothing inside accepts inbound connections.

For more information, refer to [Configuration](https://developers.cloudflare.com/tunnel/configuration/).

## Tunnel identity and connectors

_Keep the tunnel you configure separate from the software that runs it._

When you create a tunnel, Cloudflare gives it a unique ID, like the `#123` in the figure below. Routes and other Cloudflare services use this ID to identify the tunnel.

Each running instance of `cloudflared` is called a connector, and it maintains several network connections to Cloudflare. A tunnel can scale beyond a single connector without changing its routes because every connector shares the same tunnel ID. Each additional connector is called a replica and usually runs on a separate host. If one connector becomes unavailable, Cloudflare can send new traffic through another.

Both connectors live

Stop connector B

Requests alternate between connector A and connector B under one tunnel identity.

Two `cloudflared` connectors share one stable tunnel identity, allowing traffic to continue when one connector stops. Stopping connector B sends every new request through connector A while the tunnel ID and its routes stay unchanged.

For more information, refer to [Replicas and high availability](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability) and [Load balancing](https://developers.cloudflare.com/tunnel/concepts/routing/#load-balancing).

## Quick tunnels

_Reach a local service without an account or configuration._

The tunnels above are persistent: each has a stable ID and stays in your account until you delete it. A quick tunnel skips that identity. It runs from a single command:
    
    
    cloudflared tunnel --url http://localhost:8080

Cloudflare assigns a random `trycloudflare.com` address that routes back through the tunnel to your service.

The connection still starts from inside your network, so your machine stays private. What changes is permanence: a quick tunnel exists only while `cloudflared` runs, and its address is different each time. This makes quick tunnels useful for temporary work, such as sharing a development preview or receiving a webhook, and unsuited to production traffic or routes you intend to keep.

Named · live

Quick tunnelStop cloudflared

Tunnel #123 is a record in your account, bound to app.example.com. cloudflared holds the connection.

A named tunnel keeps its identity as a record in your Cloudflare account, so stopping `cloudflared` leaves that record in place. A quick tunnel keeps the account empty: its address floats in Cloudflare's network, held up only by the live connection, so stopping `cloudflared` destroys it and the next run mints a different one.

For more information, refer to [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

## How traffic reaches a resource

_Connect traffic to resources through the tunnel._

A connected tunnel does not make a resource reachable on its own. Routing configuration determines which traffic uses the tunnel and which resource that traffic should reach.

  * **Published applications** connect public hostnames (for example, `app.example.com`) to services behind the tunnel.
  * **Private network routes** direct traffic for private hostnames, IP addresses, or network ranges through the tunnel.
  * **Workers VPC** lets Workers reach private services through the tunnel.



One tunnel can carry traffic for multiple resources, even when those resources use different types of routing. When traffic matches the routing configuration, Cloudflare sends it over an available tunnel connection. `cloudflared` receives the traffic and forwards it to a resource it can reach in your network.

The tunnel provides connectivity. Access to each resource is controlled separately.

Enable tunnelConnect hostnameSend request

No route or tunnel exists yet.

Routing configuration sends traffic through an available tunnel connection to `cloudflared`, which forwards it to a reachable resource. A request with no route fails immediately, and a routed request with no tunnel fails at Cloudflare's edge, because both the route and the tunnel are required.

For more information, refer to [Routing](https://developers.cloudflare.com/tunnel/concepts/routing/), [Private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/), and [Workers VPC](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/).

## Start building

When you are ready to build, choose how you want to use the tunnel.

### [Publish an application](https://developers.cloudflare.com/tunnel/get-started/)

Connect a public hostname to a service in your network.

### [Connect a private network](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/)

Route traffic from enrolled devices to private resources.

### [Connect Workers VPC](https://developers.cloudflare.com/workers-vpc/get-started/)

Let Workers call services in a private network.

### [Try a quick tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)

Share a local service from a single command, without an account or configuration.

## Related resources

  * [Configuration](https://developers.cloudflare.com/tunnel/configuration/): replicas, firewall rules, and connection settings.
  * [Routing](https://developers.cloudflare.com/tunnel/concepts/routing/): public hostnames, protocols, and load balancing.
  * [Observability](https://developers.cloudflare.com/tunnel/observability/): tunnel status, logs, metrics, and notifications.
  * [Troubleshooting](https://developers.cloudflare.com/tunnel/troubleshooting/): failures across the request path.



[PreviousQuick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)[NextRouting](https://developers.cloudflare.com/tunnel/concepts/routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/concepts/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

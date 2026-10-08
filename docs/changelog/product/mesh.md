---
url: https://developers.cloudflare.com/changelog/product/mesh/
title: Cloudflare Mesh Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:47.789073+00:00
---

# Cloudflare Mesh Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/mesh/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Sep 29, 2026

## [Identify Mesh, Workers VPC, and Cloudflare Tunnel replicas in network logs](https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

You can now tell a person on a laptop apart from a Mesh node or an AI agent running on Workers, without matching on connector email addresses or Mesh IP ranges — and see exactly which Cloudflare Tunnel and `cloudflared` replica received each session.

[Gateway network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs) and [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) now identify two new kinds of traffic:

  * **Mesh** — Traffic sent from or delivered to a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node. Previously, Mesh nodes were logged the same way as devices running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), because Mesh nodes run the client in headless mode.
  * **Workers VPC** — Traffic sent by a Worker through a [Workers VPC](https://developers.cloudflare.com/workers-vpc/) binding. Previously, Workers VPC sessions were not recorded in Network Session Logs.

![Viewing Mesh and Workers VPC traffic in Gateway network logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1439,height=796,format=webp/_astro/2026-09-28-mesh-workers-vpc-network-logs.iGvLKYk7.gif)

#### Gateway network logs

To view these values in the dashboard, go to **Zero Trust** > **Insights & Logs** > **Logs** > **Network logs** , select **Columns** , and turn on **Traffic Source** and **Traffic Destination**. Both values also appear under **Network query details** when you open a log entry.

#### Network Session Logs

The `zero_trust_network_sessions` dataset, available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/), includes the following fields:

Field | Description  
---|---  
`OnrampType` | How the session entered Cloudflare One. Values: `CF1_CLIENT`, `MESH`, `WORKERS_VPC`, `MAGIC`, `OTHER`.  
`Offramp` | Where the session was routed. Sessions routed to a Mesh node report `MESH`.  
`SourceName` | Name of the Worker that started the session. Only populated for Workers VPC sessions.  
`SourceID` | Stable identifier of the Worker that started the session. Only populated for Workers VPC sessions.  
`DestinationReplicaID` | The replica that served the session, such as a specific replica of a Mesh node or a `cloudflared` replica of a Cloudflare Tunnel.  
  
For example, `OnrampType = 'WORKERS_VPC' AND Offramp = 'MESH'` returns every session where a Worker reached a service behind a Mesh node, and `SourceName` tells you which Worker it was.

Redeploy your Workers

`SourceName` and `SourceID` are only populated for Workers deployed after 29 September 2026. To include them for an existing Worker, redeploy it — for example, with `npx wrangler deploy`. No code changes are required.

#### See which tunnel and replica received a session

With `DestinationReplicaID`, you can now confirm which [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and which `cloudflared` replica received traffic for a specific session. Combine it with the existing `DestinationTunnelID` field to trace a session to an exact tunnel replica — or Mesh node replica — when you run multiple replicas for high availability. The replica ID matches the **Connector ID** shown in the dashboard, so you can [stream that replica's logs](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) with `cloudflared tail --connector-id`.

Sessions logged before this change are not backfilled. For all available fields, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/).

Sep 23, 2026

## [Add Mesh participants with guided onboarding](https://developers.cloudflare.com/changelog/post/2026-09-23-mesh-participant-onboarding/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) now makes it faster to add and manage participants from the dashboard. Select **Add participant** from **Networking** > **Mesh** to deploy a [Mesh node](https://developers.cloudflare.com/mesh/get-started/) or find the information needed to connect a [client device](https://developers.cloudflare.com/mesh/guides/connect-client-devices/).

![Adding a Cloudflare Mesh node through the guided dashboard workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=680,format=webp/_astro/guided-participant-onboarding-clicks.B0r-5ElX.gif)

The updated dashboard includes the following improvements:

  * **More Mesh node deployment options** — Install a node on Linux, Kubernetes, Docker Compose, or Docker CLI. The dashboard provides requirements, commands, configuration, and links for each method. Refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/) for container deployment details.
  * **Client device installation guidance** — Access platform-specific [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) installers, mobile QR codes, and your Cloudflare One organization name. Use the organization name to log in from the client after installation.
  * **Unified participant management** — View [Mesh nodes and enrolled client devices](https://developers.cloudflare.com/mesh/guides/connect-client-devices/#1-enroll-the-cloudflare-one-client) in one table. Search devices, filter participants by type or status, open device details, and load additional results from each participant source. If one source fails, participants from the other source remain available while you retry the request.



You must still install the Cloudflare One Client, log in to your organization, and test the connection.

For complete setup instructions, refer to [Get started with Cloudflare Mesh](https://developers.cloudflare.com/mesh/get-started/).

Sep 2, 2026

## [Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once](https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now create multiple [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) routes from the Routes page in a single action, instead of submitting one route at a time.

![Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-tunnel-mesh-bulk.zu4fOWN3.gif)

When creating a route, you can now:

  * **Add multiple destinations at once** — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.
  * **Queue up multiple routes** — Select **Add another** to stage additional routes, including different types or connectors, before creating them all in one action.
  * **Retry only what failed** — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.



The same Routes UI already supports bulk creation for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

For setup steps, refer to [Add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/).

Aug 11, 2026

## [Hostname routing is now generally available, with a new public IP range for initial resolved IPs](https://developers.cloudflare.com/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Hostname routing ↗︎](https://blog.cloudflare.com/tunnel-hostname-routing/) is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:

  * **Cloudflare Tunnel** : route a [private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) (for example, `wiki.internal.local`) to a private application behind your tunnel, or a [public hostname](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) (for example, `bank.example.com`) to egress through a specific tunnel and anchor traffic to a dedicated exit node.
  * **Cloudflare Mesh** : attract a [private or public hostname's traffic](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) to a Mesh node.



Alongside GA, the default IPv4 range used for initial resolved IPs (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:

  * **IPv4** : `172.64.128.0/20`
  * **IPv6** : `2606:4700:0cf1:4000::/64`



This is the default range. You can [configure a custom initial resolved IP range](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/) for IPv4 if it conflicts with your existing network.

**Why this is changing:** Starting with [Chrome 142 ↗︎](https://developer.chrome.com/release-notes/142), Local Network Access (LNA) restrictions block background requests to CGNAT addresses (`100.64.0.0/10`), which included the previous initial resolved IP default (`100.80.0.0/16`). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.

**What is affected:** Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:

  * [Private](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and [public](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) hostname routing for Cloudflare Tunnel
  * [Hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) for Cloudflare Mesh
  * [Access private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) on non-HTTPS ports
  * [Egress policy host selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/host-selectors/) (Domain, Host, Application, and Content Categories)



You can check your account's current range, or configure a custom range, at any time from **Networking** > **IP addresses** > **Address space** > **Custom IPs** , or using the [Initial Resolved IP Subnet API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/#\(resource\)%20zero_trust.networks.subnets.initial_resolved_ip).

[ Go to **Custom IPs** ↗ ](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space/custom-ips)

For full instructions, refer to [Configure initial resolved IPs](https://developers.cloudflare.com/cloudflare-one/networks/routes/configure-initial-resolved-ips/). The IPv6 range (`2606:4700:0cf1:4000::/64`) is unchanged and is not affected by this restriction.

The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to [Automatically managed ranges](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges) for details.

If you were relying on a Chrome Enterprise policy workaround (such as `LocalNetworkAccessRestrictionsTemporaryOptOut`) while your account was still on the legacy CGNAT-based range, refer to [Google Chrome restricts access to private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames) for next steps.

Aug 7, 2026

## [Container image for Cloudflare Mesh](https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes can now run as Docker containers. The [`cloudflare/mesh` ↗︎](https://hub.docker.com/r/cloudflare/mesh) image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.

The image supports `amd64` and `arm64` architectures and includes built-in [source NAT](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/#source-nat) so return traffic routes correctly without VPC route table changes.

#### Deployment patterns

  * **Docker Compose** — add a `cloudflare-mesh` service to your `compose.yaml` and connect your entire stack to a private network.
  * **Kubernetes StatefulSet** — deploy a standalone Mesh node with persistent registration state.
  * **Kubernetes sidecar** — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.
  * **CI/CD** — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.



For [high availability](https://developers.cloudflare.com/mesh/features/high-availability/), run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, runtime configuration, and deployment examples, refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/).

Jul 9, 2026

## [Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026](https://developers.cloudflare.com/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

On **October 5, 2026** , two changes take effect across the [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) and [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/): the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the `connections` field. If you manage private network routes or read tunnel connection details through the API, `cloudflared`, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.

#### Route endpoints

The CIDR-encoded route endpoints are deprecated in favor of the standard, `route_id`-based endpoints that already exist today. Both sets of endpoints route a private network through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) or [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) (the API still refers to Mesh nodes as `warp_connector`) — only the request shape changes.

**Deprecated endpoints (removed October 5, 2026):**

  * Create a tunnel route (CIDR Endpoint): [`POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create/)
  * Update a tunnel route (CIDR Endpoint): [`PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit/)
  * Delete a tunnel route (CIDR Endpoint): [`DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete/)



**Replacement endpoints:**

  * Create a tunnel route: [`POST /accounts/{account_id}/teamnet/routes`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/)
  * Update a tunnel route: [`PATCH /accounts/{account_id}/teamnet/routes/{route_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit/)
  * Delete a tunnel route: [`DELETE /accounts/{account_id}/teamnet/routes/{route_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete/)



#### What is changing

| Deprecated (CIDR-encoded path) | Replacement  
---|---|---  
Route identifier | URL-encoded CIDR in the path (`/network/{ip_network_encoded}`) | `route_id` in the path (`network` moves to the request body on create)  
Create | `POST .../teamnet/routes/network/{ip_network_encoded}` | `POST .../teamnet/routes` with `network` and `tunnel_id` in the body  
Update | `PATCH .../teamnet/routes/network/{ip_network_encoded}` | `PATCH .../teamnet/routes/{route_id}`  
Delete | `DELETE .../teamnet/routes/network/{ip_network_encoded}` | `DELETE .../teamnet/routes/{route_id}`  
  
#### Action required

  1. Capture each route's `route_id` by calling [List tunnel routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/), or read it from the response the first time you create a route with the replacement endpoint.
  2. Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.
  3. If you manage routes with the `cloudflared tunnel route ip add | delete` commands, upgrade `cloudflared` to the [latest version ↗︎](https://github.com/cloudflare/cloudflared/releases).
  4. If you manage routes with Terraform, make sure you are on a current version of the [`cloudflare_zero_trust_tunnel_cloudflared_route` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route) resource and the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).


    
    
    # Before: create a route by URL-encoding the CIDR into the path
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \
         -H 'Content-Type: application/json' \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
         -d '{"tunnel_id": "'$TUNNEL_ID'", "comment": "Example comment for this route."}'
    
    # After: create a route with the network in the request body
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \
         -H 'Content-Type: application/json' \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
         -d '{"network": "172.16.0.0/16", "tunnel_id": "'$TUNNEL_ID'", "comment": "Example comment for this route."}'
    
    # After: update or delete a route using its route_id
    curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \
         -H 'Content-Type: application/json' \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
         -d '{"comment": "Updated comment for this route."}'
    
    curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

#### Cloudflare Tunnel and Cloudflare Mesh connections

Starting the same day, the `connections` array is removed from list and get responses for [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes (the `cfd_tunnel` and `warp_connector` API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.

This affects:

  * [`GET /accounts/{account_id}/cfd_tunnel`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/) — `connections` removed from each item in `result`
  * [`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/) — `connections` removed from `result`
  * [`GET /accounts/{account_id}/warp_connector`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/) — `connections` removed from each item in `result`
  * [`GET /accounts/{account_id}/warp_connector/{tunnel_id}`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/) — `connections` removed from `result`



#### Action required

Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call [`GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/). For Cloudflare Mesh, call [`GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/).
    
    
    # Before: read connections off the tunnel object
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    # After: query connections directly
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \
         -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Update any dashboards, monitoring scripts, or automation that parses `connections` from the tunnel list or get response. `cloudflared` and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.

#### Why we are making these changes

  * **Smaller, faster responses.** Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.
  * **A single way to identify a route.** Consolidating on `route_id` removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.
  * **Consistency across the API.** Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.



To learn more, refer to the [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/), the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/), and [Routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/) documentation.

Jul 2, 2026

## [Hostname routing for Cloudflare Mesh](https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now add [hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) to a Cloudflare Mesh node, in addition to CIDR routes.

  1. [Client device](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Requests `wiki.internal.local`

  2. DNS query↓
  3. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Returns a token IP, then rewrites the destination to the real private IP.

`172.64.128.0/20`

  4. [Hostname route](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes)↓
  5. [Mesh node](https://developers.cloudflare.com/mesh/)

Forwards traffic to the host on the local network

  6. ↓
  7. Private host

`wiki.internal.local` · `10.0.0.50`




Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:

  * **Private hostname** (for example, `wiki.internal.local`) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.
  * **Public hostname** (for example, `www.example.com`) — route that hostname's traffic through the node and egress via the node's public IP.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, prerequisites, and DNS options, refer to [Hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes).

Jun 19, 2026

## [Manage all your routes from one page in the dashboard](https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The **Routes** page in the Cloudflare dashboard now shows the routes across all of your connectors — [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) and [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) routes alongside [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) and [Magic Transit](https://developers.cloudflare.com/magic-transit/) static routes — in a single table, instead of a separate routes view per product.

![The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-06-19-unified-routes.B3igBY20.gif)

From the unified Routes page you can:

  * **Visualize your network with an interactive map** that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.
  * **See every route in one table** , with its destination, type, connector, priority, and source, and filter or sort to find what you need.
  * **Create, edit, and delete routes** of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by **connector name** instead of typing its IP.
  * **Manage[virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/)** from a dedicated tab.
  * **Test a route** to see which connector and next hop a destination resolves to before you commit a change.



To find it, go to **Networking** > **Routes** in the dashboard sidebar.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to [add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) and [manage virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/).

Jun 5, 2026

## [Filter Workers' public Internet traffic using Gateway policies](https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Workers using a [VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) binding with `network_id: "cf1:network"` now egress to public Internet destinations through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/). This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.

  1. [Worker](https://developers.cloudflare.com/workers/)

Calls `env.EGRESS.fetch()`

  2. [VPC binding](https://developers.cloudflare.com/workers-vpc/)↓
  3. [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Bind via [`cf1:network`](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/)

  4. ↓
  5. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Policies applied:

[DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)[HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/)[Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)

  6. ↓
  7. ↗Public Internet

Any public hostname or IP


[Gateway logsDNSHTTPNetwork](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)

What you get by default:

  * **Visibility.** Worker egress shows up in Gateway [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) logs alongside your other traffic, so you can audit what your Workers are calling and when.
  * **Enforcement.** Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.


    
    
    {
    	"vpc_networks": [
    		{
    			"binding": "EGRESS",
    			"network_id": "cf1:network",
    			"remote": true,
    		},
    	],
    }
    
    
    [[vpc_networks]]
    binding = "EGRESS"
    network_id = "cf1:network"
    remote = true
    
    
    // Egress to a public destination — subject to your Gateway policies and logged
    const response = await env.EGRESS.fetch("https://api.example.com/data");
    
    
    // Egress to a public destination — subject to your Gateway policies and logged
    const response = await env.EGRESS.fetch("https://api.example.com/data");

For configuration options, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/). For policy authoring, refer to [Cloudflare Gateway traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

May 28, 2026

## [High availability replica management for Cloudflare Mesh](https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) dashboard now shows per-replica details for [high availability](https://developers.cloudflare.com/mesh/features/high-availability/) nodes. You can see which replica is active, view each replica's Mesh IP and connection details, and manually trigger failover — all from the node detail page.

![Mesh HA replica tabs showing active and passive replicas with per-replica Mesh IPs and a manual failover option](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1155,format=webp/_astro/mesh-ha-replicas.Dvf1GMmQ.gif)

#### What's new

  * **Replica tabs** on the node detail page — switch between replicas to see each one's Mesh IP, edge data center, origin IP, platform, version, and uptime.
  * **Active/passive badges** identify which replica is currently routing traffic.
  * **Manual failover** — promote a passive replica to active with a single click. The previous active replica switches to standby.
  * **HA badge** in the overview table identifies nodes running multiple replicas.
  * **Active replica IP** shown in the overview table — the dashboard now resolves which replica is active and displays the correct Mesh IP.



#### Manual failover

To manually promote a passive replica:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/mesh), go to **Networking** > **Mesh**.
  2. Select an HA-enabled node.
  3. Select the passive replica tab.
  4. Select **Promote to active** and confirm.



Traffic reroutes to the promoted replica immediately. Refer to [High availability](https://developers.cloudflare.com/mesh/features/high-availability/) for details on failover behavior.

May 21, 2026

## [Granular permissions for Cloudflare Tunnel and Cloudflare Mesh](https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now scope Cloudflare permissions to individual [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the resource picker now lists [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes as scopable resource types. You can:

  * Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.
  * Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.
  * Scope a single policy to one or many Tunnels and Mesh nodes at once.



#### How it works

Granular permissions are a parallel layer to existing account-level roles — they do not replace them.

  * **Existing account-level roles continue to work.** A member with `Cloudflare Access` or `Cloudflare Zero Trust` retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.
  * **Granular permissions are additive.** For any API request on a specific Tunnel or Mesh node, access is granted if the principal has **either** the account-level role **or** a granular permission for that resource.
  * **Resource enumeration is authorization-aware.** Listing endpoints (`GET /accounts/{id}/cfd_tunnel`, `GET /accounts/{id}/warp_connector`) return only the resources the principal has at least read access to.



#### Get started

  * Configure [granular permissions for Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/guides/granular-permissions/).
  * Configure [granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One](https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/).
  * Review the [resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) on the Cloudflare role reference.



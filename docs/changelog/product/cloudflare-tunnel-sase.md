---
url: https://developers.cloudflare.com/changelog/product/cloudflare-tunnel-sase/
title: Cloudflare Tunnel for SASE Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:09.035154+00:00
---

# Cloudflare Tunnel for SASE Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/cloudflare-tunnel-sase/

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

Sep 18, 2026

## [cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027](https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of `cloudflared`. After the deprecation takes effect, Cloudflare will no longer publish new `cloudflared` releases for either architecture.

Windows 10, the last Windows release to support 32-bit systems, reached end of support in October 2025. Apple has also deprecated Intel-based Mac computers. macOS 26 Tahoe, released in September 2025, was the final macOS release to support Intel-based Macs. macOS 27, released in September 2026, no longer supports them.

Focusing development on currently supported architectures allows `cloudflared` to align with operating system support and continue receiving updates on supported platforms. For available downloads and supported platforms, refer to the [Cloudflare Tunnel downloads](https://developers.cloudflare.com/tunnel/downloads/) documentation.

Aug 18, 2026

## [Configure origin application settings for Cloudflare Tunnel in the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/). These settings control how `cloudflared` connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.

![Configure origin application settings in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/tunnel-origin-settings-dashboard.CsC2RwFC.gif)

When editing a published application, expand **Additional application settings** to configure parameters organized into three categories:

  * **HTTP** — Set a custom HTTP Host header or disable chunked encoding.
  * **TLS** — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.
  * **Connection** — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)

For the full list of origin parameters, refer to [Origin parameters](https://developers.cloudflare.com/tunnel/reference/origin-parameters/).

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

Aug 10, 2026

## [Stream live logs from Cloudflare Tunnel in the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Real-time Tunnel log streaming is now available in the Cloudflare dashboard under **Networking** > **Tunnels**. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.

![Stream live logs from a tunnel in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/tunnel-live-logs-core-dashboard.Dtm7Jg51.gif)

In the tunnel detail view, a new **Live logs** tab lets you:

  * **Stream logs from single or multiple connectors** — In [highly available](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability) deployments with multiple `cloudflared` replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.
  * **Filter by log level, event type, and HTTP method** — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or `cloudflared` internal), at any log level.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)

For more information, refer to [Tunnel observability](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) and [Tunnel log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/).

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

May 27, 2026

## [Cloudflare Tunnel now runs connectivity pre-checks at startup](https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting with [`cloudflared` version 2026.5.2 ↗︎](https://github.com/cloudflare/cloudflared/releases), [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) automates the entire [connectivity pre-checks workflow](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/) directly inside the binary. Previously, customers had to install `dig` and `netcat` and run those commands by hand to verify their environment. Now `cloudflared` does it natively at startup — and surfaces actionable remediation when something is blocked.

![cloudflared connectivity pre-checks output](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1012,format=webp/_astro/cloudflared-connectivity-prechecks.DRwN6tGe.gif)

On every `cloudflared tunnel run` (and `cloudflared tunnel diag`), the binary now natively checks:

  * **DNS resolution** — `region1.v2.argotunnel.com` and `region2.v2.argotunnel.com` resolve to valid Cloudflare IPs.
  * **Transport connectivity** — outbound `UDP (QUIC)` and `TCP (HTTP/2)` on port `7844`.
  * **Management API** — outbound `TCP/443` to `api.cloudflare.com` for software updates.



Results are printed in a scannable CLI table with three states:

  * ✅ **Pass** — the check succeeded.
  * ⚠️ **Warn** — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.
  * ❌ **Fail** — a blocking issue, with a specific remediation hint (for example, `Allow outbound UDP on port 7844`).



If DNS is unresolvable, or **both** UDP and TCP fail on port 7844, `cloudflared` exits early with the failure rather than looping on opaque `failed to dial` errors.

Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.

To get the new behavior, upgrade `cloudflared` to version `2026.5.2` or later. For more details, refer to the [Connectivity pre-checks documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/).

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



Mar 20, 2026

## [Stream logs from multiple replicas of Cloudflare Tunnel simultaneously](https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) of that tunnel and supports streaming logs from multiple replicas at once.

![View replicas and stream logs from multiple connectors](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1040,format=webp/_astro/tunnel-multiconn.DEOEaLlu.gif)

Previously, you could only stream logs from one replica at a time. With this update:

  * **Replicas on the tunnel overview** — All active replicas for the selected tunnel now appear on that tunnel's overview page under **Connectors**. Select any replica to stream its logs.
  * **Multi-connector log streaming** — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and go to **Networks** > **Connectors** > **Cloudflare Tunnels**. Select **View logs** next to the tunnel you want to monitor.



For more information, refer to [Tunnel log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) and [Deploy replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/).

Feb 20, 2026

## [Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard](https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) is now available in the main Cloudflare Dashboard at [Networking > Tunnels ↗︎](https://dash.cloudflare.com/?to=/:account/tunnels), bringing first-class Tunnel management to developers using Tunnel for securing origin servers.

![Manage Tunnels in the Core Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=894,format=webp/_astro/tunnel-core-dashboard.BGPqaHfo.gif)

This new experience provides everything you need to manage Tunnels for [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), including:

  * **Full Tunnel lifecycle management** : Create, configure, delete, and monitor all your Tunnels in one place.
  * **Native integrations** : View Tunnels by name when configuring [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) and [Workers VPC](https://developers.cloudflare.com/workers-vpc/) — no more copy-pasting UUIDs.
  * **Real-time visibility** : Monitor [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) and Tunnel [health status](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status) directly in the dashboard.
  * **Routing map** : Manage all ingress routes for your Tunnel, including [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/), [private CIDRs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/), and [Workers VPC services](https://developers.cloudflare.com/workers-vpc/), from a single interactive interface.



#### Choose the right dashboard for your use case

**Core Dashboard** : Navigate to [Networking > Tunnels ↗︎](https://dash.cloudflare.com/?to=/:account/tunnels) to manage Tunnels for:

  * Securing origin servers and [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/) with CDN, WAF, Load Balancing, and DDoS protection
  * Connecting [Workers to private services](https://developers.cloudflare.com/workers-vpc/) via Workers VPC



**Cloudflare One Dashboard** : Navigate to [Zero Trust > Networks > Connectors ↗︎](https://one.dash.cloudflare.com/?to=/:account/networks/connectors) to manage Tunnels for:

  * Securing your public applications with [Zero Trust access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)
  * Connecting users to [private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/)
  * Building a [private mesh network](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-networks)



Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.

#### Get started

New to Tunnel? Learn how to [get started with Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/) or explore advanced use cases like [securing SSH servers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/) or [running Tunnels in Kubernetes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/).

Jan 15, 2026

## [Verify WARP Connector connectivity with a simple ping](https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

We have made it easier to validate connectivity when deploying [WARP Connector](https://developers.cloudflare.com/mesh/) as part of your [software-defined private network](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-networks).

You can now `ping` the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.

Starting with [version 2025.10.186.0](https://developers.cloudflare.com/changelog/2026-01-13-warp-linux-ga/), WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.

Learn more about deploying [WARP Connector](https://developers.cloudflare.com/mesh/) and building private network connectivity with [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).

Nov 11, 2025

## [cloudflared proxy-dns command will be removed starting February 2, 2026](https://developers.cloudflare.com/changelog/post/2025-11-11-cloudflared-proxy-dns/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting February 2, 2026, the `cloudflared proxy-dns` command will be removed from all new `cloudflared` [releases](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/).

This change is being made to enhance security and address a potential vulnerability in an underlying DNS library. This vulnerability is specific to the `proxy-dns` command and does not affect any other `cloudflared` features, such as the core [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) service.

The `proxy-dns` command, which runs a client-side [DNS-over-HTTPS (DoH)](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/) proxy, has been an officially undocumented feature for several years. This functionality is fully and securely supported by our actively developed products.

Versions of `cloudflared` released before this date will not be affected and will continue to operate. However, note that our [official support policy](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#deprecated-releases) for any `cloudflared` release is one year from its release date.

#### Migration paths

We strongly advise users of this undocumented feature to migrate to one of the following officially supported solutions before February 2, 2026, to continue benefiting from secure [DNS-over-HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/).

#### End-user devices

The preferred method for enabling DNS-over-HTTPS on user devices is the [Cloudflare WARP client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/). The WARP client automatically secures and proxies all DNS traffic from your device, integrating it with your organization's [Zero Trust policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) and [posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/).

#### Servers, routers, and IoT devices

For scenarios where installing a client on every device is not possible (such as servers, routers, or IoT devices), we recommend using the [WARP Connector](https://developers.cloudflare.com/mesh/).

Instead of running `cloudflared proxy-dns` on a machine, you can install the WARP Connector on a single Linux host within your private network. This connector will act as a gateway, securely routing all DNS and network traffic from your [entire subnet](https://developers.cloudflare.com/mesh/features/routes/) to Cloudflare for [filtering and logging](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

Sep 18, 2025

## [Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel](https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

You can now route private traffic to [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is **free for all Cloudflare One customers**.

Previously, Tunnel routes could only be defined by IP address or [CIDR range](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/). This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.

![Hostname-based routing in Cloudflare Tunnel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1990,height=530,format=webp/_astro/tunnel-hostname-routing.DSi8MP_7.webp)

**What’s new:**

  * **Hostname & Domain Routing**: Create routes for individual hostnames (e.g., `payroll.acme.local`) or entire domains (e.g., `*.acme.local`) and direct their traffic to a specific Tunnel.
  * **Simplified Zero Trust Policies** : Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.
  * **Precise Egress Control** : Route traffic for public hostnames (e.g., `bank.example.com`) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.
  * **No More IP Lists** : This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.



Get started in the Tunnels section of the Zero Trust dashboard with your first [private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) or [public hostname](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) route.

Learn more in our [blog post ↗︎](https://blog.cloudflare.com/tunnel-hostname-routing/).

Sep 11, 2025

## [DNS filtering for private network onramps](https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

[Magic WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering) and [WARP Connector](https://developers.cloudflare.com/mesh/features/routes/#dns-filtering) users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.

Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including [Internal DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/#internal-dns) and [hostname-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites).

To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, `172.64.36.1` and `172.64.36.2`. Once you configure DNS resolution and filtering, you can use _Source Internal IP_ as a traffic selector in your [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) for routing private DNS traffic to your [Internal DNS](https://developers.cloudflare.com/dns/internal-dns/).

Sep 2, 2025

## [Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025](https://developers.cloudflare.com/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting **December 1, 2025** , list endpoints for the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.

No action is required if you already explicitly set `is_deleted=false` or if you only need to list active resources.

This change affects the following API endpoints:

  * List all tunnels: [`GET /accounts/{account_id}/tunnels`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/methods/list/)
  * List [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/): [`GET /accounts/{account_id}/cfd_tunnel`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/)
  * List [WARP Connector](https://developers.cloudflare.com/mesh/) tunnels: [`GET /accounts/{account_id}/warp_connector`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/)
  * List tunnel routes: [`GET /accounts/{account_id}/teamnet/routes`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/)
  * List subnets: [`GET /accounts/{account_id}/zerotrust/subnets`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/)
  * List virtual networks: [`GET /accounts/{account_id}/teamnet/virtual_networks`](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/)



#### What is changing?

The default behavior of the `is_deleted` query parameter will be updated.

Scenario | Previous behavior (before December 1, 2025) | New behavior (from December 1, 2025)  
---|---|---  
`is_deleted` parameter is omitted | Returns **active & deleted** tunnels, routes, subnets and virtual networks | Returns **only active** tunnels, routes, subnets and virtual networks  
  
#### Action required

If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the `is_deleted` parameter before **December 1, 2025**.

To get a list of only deleted resources, you must now explicitly add the `is_deleted=true` query parameter to your request:
    
    
    # Example: Get ONLY deleted Tunnels
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true" \
         -H "Authorization: Bearer $API_TOKEN"
    
    # Example: Get ONLY deleted Virtual Networks
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true" \
         -H "Authorization: Bearer $API_TOKEN"

Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using `is_deleted=false`) and one to get deleted items (`is_deleted=true`).

#### Why we’re making this change

This update is based on user feedback and aims to:

  * **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
  * **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
  * **Improve performance:** For most users, the default query result will now be smaller and more relevant.



To learn more, please visit the [Cloudflare Tunnel API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/) and [Zero Trust Networks API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/) documentation.

Jul 15, 2025

## [Faster, more reliable UDP traffic for Cloudflare Tunnel](https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Your real-time applications running over [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) are now faster and more reliable. We've completely re-architected the way `cloudflared` proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.

This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.

**What’s new:**

  * **Faster UDP performance** : We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.
  * **Greater reliability for mixed traffic** : UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.



Learn more about running [TCP or UDP applications](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-applications) and [private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/) through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

Dec 19, 2024

## [Troubleshoot tunnels with diagnostic logs](https://developers.cloudflare.com/changelog/post/2024-12-19-diagnostic-logs/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

The latest `cloudflared` build [2024.12.2 ↗︎](https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2) introduces the ability to collect all the diagnostic logs needed to troubleshoot a `cloudflared` instance.

A diagnostic report collects data from a single instance of `cloudflared` running on the local machine and outputs it to a `cloudflared-diag` file.

For more information, refer to [Diagnostic logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).

Jun 16, 2024

## [Explore product updates for Cloudflare One](https://developers.cloudflare.com/changelog/post/2024-06-16-cloudflare-one/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/)[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Network Flow](https://developers.cloudflare.com/network-flow/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Welcome to your new home for product updates on [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).

Our [new changelog](https://developers.cloudflare.com/changelog/) lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.

If you are looking for older product updates, refer to the following locations.

Older product updates

  * [Access](https://developers.cloudflare.com/cloudflare-one/changelog/access/)
  * [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/changelog/browser-isolation/)
  * [CASB](https://developers.cloudflare.com/cloudflare-one/changelog/casb/)
  * [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/changelog/tunnel/)
  * [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/changelog/dlp/)
  * [Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/changelog/dex/)
  * [Email security](https://developers.cloudflare.com/cloudflare-one/changelog/email-security/)
  * [Gateway](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/)
  * [Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/changelog/)
  * [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/changelog/)
  * [Magic Network Monitoring](https://developers.cloudflare.com/network-flow/changelog/)
  * [Magic Transit](https://developers.cloudflare.com/magic-transit/changelog/)
  * [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/changelog/)
  * [Network Interconnect](https://developers.cloudflare.com/network-interconnect/changelog/)
  * [Risk score](https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/)
  * [Cloudflare One Client](https://developers.cloudflare.com/changelog/cloudflare-one-client/)



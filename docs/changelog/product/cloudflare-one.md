---
url: https://developers.cloudflare.com/changelog/product/cloudflare-one/
title: Cloudflare One Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:09.668419+00:00
---

# Cloudflare One Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/cloudflare-one/

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

Oct 7, 2026

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 5, 2026

## [BGP over IPsec and GRE tunnels generally available](https://developers.cloudflare.com/changelog/post/2026-10-05-bgp-over-tunnels-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

BGP peering over IPsec and GRE tunnels is generally available for Cloudflare WAN and Magic Transit. You can use it for production workloads.

BGP peering exchanges routes dynamically between your devices and your Cloudflare virtual network routing table. You no longer need to update static routes manually as your network changes.

BGP over IPsec and GRE tunnels is available to all accounts that use [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). No enablement is required. BGP over CNI remains in closed beta.

For configuration details, refer to:

  * [Configure BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
  * [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)



Oct 2, 2026

## [New strict service token authentication setting for Access](https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The strict service token authentication setting applies consistent behavior to requests made with service tokens. When the setting is on for a Zero Trust organization, Access handles requests with service token headers as follows:

  * If authentication or authorization fails, Access always returns `401` or `403` instead of redirecting the client to the login page with `302`.
  * Only Service Auth policies can authorize the request. Access ignores Allow policies and any `CF_Authorization` cookie sent with the request.
  * Access does not return a `CF_Authorization` cookie to the client after successful authentication. Subsequent requests should continue to use service token headers.
  * Failed requests for recognized service tokens appear in [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#non-identity-authentication).



Zero Trust organizations created on or after October 5, 2026 have strict service token authentication turned on by default and cannot turn it off. Cloudflare recommends that existing organizations turn it on as well.

Organizations created before October 5, 2026 can configure the setting in the dashboard or through the API.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**.

[ Go to **Access settings** ↗ ](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
  2. Under **Manage service tokens** , turn on **Strict service token authentication**.

  3. In the confirmation dialog, select **Enable**.




To turn off strict service token authentication, turn off the setting and select **Disable**.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"strict_service_token_auth": true
    	}'

To turn off strict service token authentication, set `strict_service_token_auth` to `false`.

For behavior and configuration details, refer to [Strict service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#strict-service-token-authentication).

Oct 1, 2026

## [Simplified permissions for tagging targets with Access for Infrastructure](https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now tag [targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets) using only the `Zero Trust Write` API token permission. Previously, tagging targets through the API required both `Zero Trust Write` and `Tag Write` permissions on the API token.

This change applies to inline target tagging through the [Infrastructure Access Targets API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/). Tagging resources through the general [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/) still requires the `Tag Admin`, `Tag Write`, or equivalent role.

For more information, refer to [Tag targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets).

Sep 30, 2026

## [Role-based access control for Browser Isolation policies](https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) support role-based access control (RBAC). Because isolation policies are Gateway HTTP policies with the _Isolate_ action, Gateway's account-level and resource-scoped roles apply to them directly.

Use the `Zero Trust HTTP Policies Admin` account-level role to grant access to all HTTP policies in the account. You can also assign a [resource-scoped role](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) to let a team member manage a specific isolation policy without exposing other Gateway resources.

[Policy settings](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings) such as copy/paste, file download/upload, keyboard, and printing are part of the policy object and follow the same permissions.

For setup instructions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/).

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

Sep 24, 2026

## [MCP server portals are now generally available](https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) are now generally available to all Cloudflare customers. A portal gives users one endpoint for approved Model Context Protocol (MCP) servers. Cloudflare Access logs tool, prompt, and resource activity.

Since the open beta, MCP server portals have added:

  * [Gateway routing](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway) for HTTP logging and data loss prevention (DLP) scanning
  * [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies) that control how portals reduce tool definitions and token use
  * [Static OAuth client credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials) for providers that do not support Dynamic Client Registration
  * [Session management](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions) for reconnecting servers and changing authorizations from the portal
  * [Service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token) for autonomous agents and machine-to-machine access
  * [Logpush support](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) for exporting portal activity to external storage or a security information and event management (SIEM) system



To create a portal and connect an MCP client, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

Sep 23, 2026

## [Traffic Destination selector in Gateway policies](https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Destination** selector that identifies how traffic exits Cloudflare. This allows administrators to write policies that target specific off-ramp methods - for example, applying different rules to traffic destined for the public Internet compared to traffic routed through Cloudflare Tunnel or Cloudflare WAN.

#### Available traffic destination values

UI name | API value | Description  
---|---|---  
Internet | `internet` | Traffic to the public Internet  
Cloudflare WAN | `cloudflare_wan` | Traffic through a [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/) connection  
Cloudflare Tunnel | `cloudflare_tunnel` | Traffic to a private origin through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)  
Cloudflare One Client | `device_client` | Traffic to another device running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)  
Mesh | `mesh` | Traffic through a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node  
  
The selector uses the `net.offramp.type` API field in both HTTP and Network policies.

UI name | API example  
---|---  
Traffic Destination | `net.offramp.type == "internet"`  
  
For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

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

Sep 22, 2026

## [Private MCP server support for MCP server portals](https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to MCP servers available only on your private network. The portal uses [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) to reach [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and IP addresses without exposing the MCP server to the public Internet.

Connect the server network to Cloudflare with [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/), or another [Cloudflare One connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/). Configure a private hostname or CIDR route, then turn on **Route traffic through Cloudflare Gateway** when you add the server. OAuth authorization server endpoints, such as the authorization and token endpoints, must be accessible on the public Internet. If Cloudflare automatically registers the OAuth client through Dynamic Client Registration (DCR), the registration endpoint must also be accessible on the public Internet.

For setup instructions, refer to [Connect a private MCP server](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-a-private-mcp-server).

Sep 18, 2026

## [Unified Routing generally available](https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Unified Routing is generally available for Cloudflare WAN and Magic Transit.

Unified Routing improves the integration between Cloudflare One and the standard connectivity onramps supported by Cloudflare WAN. It is capable of many new features including Automatic Return Routing, BGP and custom client subnets.

We recommend Unified Routing for all new accounts.

For details, refer to [Cloudflare WAN traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) and [Magic Transit traffic steering](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/#unified-routing).

Sep 15, 2026

## [Access for Infrastructure now supports tagged targets and tag-based target criteria](https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now integrates with [Resource Tagging](https://developers.cloudflare.com/resource-tagging/). You can attach key-value tags to [infrastructure targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target) and use them in access policies.

You can manage tags on targets inline when you create or edit a target or through the central [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/). Cloudflare keeps tags in sync across both methods.

Infrastructure applications also support a target criteria model with `include`, `require`, and `exclude` operators. Each operator can match targets by hostname, tag, or both.

  * **Include** matches targets that have any of the specified values.
  * **Require** matches targets that have all of the specified values.
  * **Exclude** rejects targets that have any of the specified values.

![Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2372,height=1616,format=webp/_astro/tags-in-infra-app.ja2Tp-Gq.png)

For more information, refer to [Add an infrastructure application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/).

Sep 9, 2026

## [Improved iOS tap-to-type experience for Browser Isolation](https://developers.cloudflare.com/changelog/post/2026-09-09-ios-tap-to-type/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) has improved the tap-to-type experience for users on iOS devices.

Previously, Browser Isolation displayed a full-screen overlay with the message `tap to type` when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.

If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.

![Inline tap-to-type prompt over a focused text field in Browser Isolation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1320,height=605,format=webp/_astro/tap-to-type.UmUg_KNp.jpg)

iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.

For more information on why this interaction is required, refer to [iOS limitations](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/known-limitations/#ios).

Sep 2, 2026

## [Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now define [custom applications](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application) for [breakout](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [prioritized](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/) traffic on the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard, without calling the API.

![Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-custom-application-traffic-steering.D25Ga9-d.gif)

  * In **Traffic Steering** > **Breakout traffic** or **Prioritized traffic** , select **Assign application traffic** > **Add** to create a custom application matched by **Hostnames** , **IP subnets** , and/or the new **Source subnets** field, alongside Cloudflare-managed applications.
  * Edit or delete an existing custom application from the same panel, no API round-trip required.
  * **Source subnets** lets you match traffic by its source IP range, complementing the existing [source LAN interface breakout criteria](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source).



This complements the existing API and Terraform workflow for managing applications.

For details, refer to [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) and [Prioritized traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/).

Sep 2, 2026

## [Configure DHCP options from the dashboard on Cloudflare One Appliance](https://developers.cloudflare.com/changelog/post/2026-09-02-appliance-dhcp-options-ui/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now configure [custom DHCP options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/) directly from the dashboard when the [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) is acting as the DHCP server for a LAN.

![Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-appliance-dhcp-options-ui.B5OEZmib.gif)

  * In **LAN configuration** , under **DHCP server options** , select **Add DHCP option** to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select **Add custom option** to enter your own option code, type, and value.
  * This complements the existing [API and Terraform workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options) for configuring DHCP options.



For details, refer to [DHCP server options](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/).

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

Aug 25, 2026

## [MCP server portals support MCP 2026-07-28 specification](https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support the stateless MCP `2026-07-28` specification for client and upstream server connections.

The portal's `/mcp` endpoint automatically accepts stateless MCP `2026-07-28` requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP `2026-07-28` support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.

SSE connections continue to use the legacy protocol. For details, refer to [MCP server portal transport and protocol compatibility](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport).

Aug 24, 2026

## [Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-24-virtual-appliance-self-serve-download/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

When you register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/), you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.

![Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2813,height=1241,format=webp/_astro/2026-08-24-virtual-appliance-self-serve-download.Ca2YGpCA.png)

  * On the **Connectors** page, select **Add an appliance** , choose **Virtual appliance** , then select your hypervisor: **VMware ESXi** , **Proxmox** , or **libvirt/KVM**.
  * Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.
  * Use **View setup guide** to open deployment instructions for your platform.



This complements the existing self-serve [registration and license key generation](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) in the dashboard.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine).

Aug 12, 2026

## [Independent MFA supports FIDO2 for infrastructure applications](https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow `ssh_fido2_key`, `piv_key`, or both in application-level and policy-level MFA settings.

Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.

For setup instructions, refer to [Enroll a FIDO2 key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps) and [Configure MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

Aug 12, 2026

## [MCP protocol detection and AI Security dashboard](https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare Gateway now automatically detects [Model Context Protocol (MCP) ↗︎](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.

#### MCP policy selector

A new **Is MCP** selector (`experimental.is_mcp`) is available in [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#is-mcp). Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.

This selector is currently in beta and may change before general availability.

For example, the following policy blocks MCP traffic that does not arrive through an approved [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/):

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
Is MCP | is | _True_ | And | Block  
Traffic Source | is not | _MCP portal_ |  |   
  
![Example Gateway policy that blocks MCP traffic not arriving through an MCP portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1104,height=664,format=webp/_astro/gateway-block-unknown-mcp.B2Ainj8x.png)

#### AI security report

A new **AI security report** dashboard under **Insights & Logs > Dashboards** provides visibility into MCP usage across your organization. The dashboard includes:

  * Total MCP request volume, unique users, and unique MCP servers
  * A timeseries chart of unique MCP servers observed over time
  * A summary of Gateway policies that target MCP traffic

![AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2406,height=928,format=webp/_astro/gateway-mcp-dashboard.C9jPahkp.png)

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/).

Aug 12, 2026

## [Traffic Source selector in Gateway policies](https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Source** selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint.

#### Available traffic source values

UI name | API value | Description  
---|---|---  
Device client | `device_client` | Traffic from the [Cloudflare One Client (WARP)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)  
Mesh | `mesh` | Traffic from a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) connector  
Cloudflare WAN | `cloudflare_wan` | Traffic from [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/) (Magic WAN)  
Clientless RDP | `clientless_rdp` | Traffic from a clientless RDP session  
Proxy endpoint | `proxy_endpoint` | Traffic from a [proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) (PAC file)  
Clientless Browser Isolation | `agentless_biso` | Traffic from [clientless Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)  
MCP portal | `mcp_portal` | Traffic from an [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)  
  
The selector uses the `net.onramp.type` API field in both HTTP and Network policies.

UI name | API example  
---|---  
Traffic Source | `net.onramp.type == "device_client"`  
  
#### Browser Isolation selector

A **Browser Isolation** selector is also available in Network and HTTP policies. This selector identifies whether the current session is running inside [Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/), allowing administrators to apply different policy behavior to isolated traffic.

UI name | API example  
---|---  
Browser Isolation | `net.is_isolated == true`  
  
For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

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

Jul 28, 2026

## [Control Cloudflare Gateway DNS caching with a maximum TTL setting](https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.

![The maximum DNS TTL setting in Traffic policies > Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2170,height=294,format=webp/_astro/gateway-max-ttl-traffic-settings.BRF3NUMp.png)

The setting is available at two levels:

  * **Account level** \- In **Traffic Policies** > **Traffic Settings** , under **Proxy and inspection**. This sets the default cap for all DNS locations.
  * **Per-location** \- Each [DNS location](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-proxies/) can inherit the account setting, disable the cap, or override it with a custom value.



Two new fields are also available in DNS logs: `upstream_record_ttls` (the original TTL from the upstream response) and `applied_max_ttl` (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.

For more information, refer to [Maximum DNS TTL](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/).

Jul 17, 2026

## [Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard](https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/)

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

You can now restart, reboot, or shut down a [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard or via API.

![Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-07-17-appliance-restart-reboot-shutdown.DKqTLOh6.gif)

  * **Restart** — Restart managed services. Purges temporary and (optionally) persistent state.
  * **Reboot** — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.
  * **Shutdown** — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.



In the dashboard, go to **Networking** > **Connectors** > **Appliances** , select an appliance, then **Edit** > **Operations** to send an operation. Via API, `POST` to the `/accounts/{account_id}/magic/connectors/{connector_id}/interrupts` endpoint.

For details, refer to [Appliance operations](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product/cloudflare-one/2/)…[4](https://developers.cloudflare.com/changelog/product/cloudflare-one/4/)

[Next →](https://developers.cloudflare.com/changelog/product/cloudflare-one/2/)

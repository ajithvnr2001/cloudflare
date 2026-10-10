---
url: https://developers.cloudflare.com/changelog/product-group/network-security/
title: Network security Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:15.802185+00:00
---

# Network security Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/network-security/

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

Oct 9, 2026

## [Failed detections field available in Rules](https://developers.cloudflare.com/changelog/post/2026-10-09-failed-detections/)

[WAF](https://developers.cloudflare.com/waf/)[Rules](https://developers.cloudflare.com/rules/)

You can now use `cf.appsec.request.failed_detections` to control how your rules handle requests when a security detection reports a failure.

The field is an `Array<String>` of detection IDs that reports failures from content scanning, WAF attack score, attack signature detection, leaked credentials detection, and AI prompt detections for personally identifiable information (PII), prompt injection, custom topics, and unsafe topics.

The field does not alter the existing behavior of detections. Use it in rules to choose how to handle requests with reported failures.

When no failures are reported, the field returns `[]`. You can use it on all plans, but your plan must still include the detections and rule features you want to use.

Supported rules:

  * Custom rules at the zone and account levels
  * Rate limiting rules at the zone and account levels
  * Request Header Transform Rules at the zone level



Match any reported failure:
    
    
    len(cf.appsec.request.failed_detections) gt 0

Match a reported leaked credentials detection failure:
    
    
    any(cf.appsec.request.failed_detections[*] eq "waf_credential_check")

For more information, refer to the [Failed detections field reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.appsec.request.failed_detections/).

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

## [hash_in_range() is globally available for HTTP products](https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/)

[Rules](https://developers.cloudflare.com/rules/)

`hash_in_range()` is globally available for HTTP products on all plans. It hashes fields into an integer within a specified range. Use this result to select a portion of requests.

Use `cf.random_seed` to select approximately 10% of requests at random:
    
    
    hash_in_range(0, 100, cf.random_seed) < 10

With Cloudflare for SaaS, use [custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/) to control rollout progression. Define `rollout_pct` as a custom key for each hostname. Set its value to an integer from 0 to 100. The expression selects approximately that percentage of requests:
    
    
    hash_in_range(0, 100, cf.random_seed) < coalesce(lookup_json_integer(cf.hostname.metadata, "rollout_pct"), 0)

If `rollout_pct` is missing, `coalesce()` supplies `0`. The rule then matches no requests.

For details, refer to the [`hash_in_range()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hash_in_range).

Oct 2, 2026

## [Protect Quick Tunnels with email authentication](https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)

You can now restrict who can access a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/). Use the new `--allowed-mail` flag in `cloudflared` to require visitors to authenticate with a one-time PIN sent to their email before they reach your local service.
    
    
    cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com

![Protected Quick Tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=854,format=webp/_astro/protected-quick-tunnels.DlA306r_.gif)

Previously, anyone with a `trycloudflare.com` URL could access the service behind it. Protected Quick Tunnels let you share a local development server, webhook receiver, or demo with specific people without creating a Cloudflare account or configuring a domain.

You can allow:

  * A single email address: `--allowed-mail alice@example.com`
  * Multiple email addresses, by repeating the flag or using a comma-separated list: `--allowed-mail 'alice@example.com,bob@example.com'`
  * Every address on a domain: `--allowed-mail '*@example.com'`



Visitors do not need a Cloudflare account. Access ends for everyone when you stop the `cloudflared` process.

To get started, [update `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/) to the latest version and refer to [Restrict access by email](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/#restrict-access-by-email).

Oct 1, 2026

## [Handle missing values with coalesce()](https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/)

[Rules](https://developers.cloudflare.com/rules/)

The `coalesce()` function returns the first argument that is not nil. Use it to provide a fallback in rule expressions:
    
    
    http.request.uri.path eq coalesce(http.request.uri.args["expected_path"][0], "/")

For details, refer to the [`coalesce()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#coalesce).

Oct 1, 2026

## [Compare dynamic values in Rules expressions](https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules expressions now support dynamic values on both sides of equality and ordering comparisons. You can compare request fields or function results with one another.

For example, compare the current request path with its original value:
    
    
    http.request.uri.path ne raw.http.request.uri.path

For supported operators and examples, refer to [Compare dynamic values](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#compare-dynamic-values).

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

Sep 25, 2026

## [Managed Rulesets supported in Unified Routing](https://developers.cloudflare.com/changelog/post/2026-09-25-unified-routing-managed-rulesets/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Managed Rulesets are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode.

For the full list of feature availability, refer to [Check feature availability before upgrading](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

Sep 24, 2026

## [RFC 8509 root key trust anchor sentinel support](https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/)

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

1.1.1.1 now supports [RFC 8509 ↗︎](https://datatracker.ietf.org/doc/html/rfc8509) root key trust anchor sentinels. They let you check whether the responding resolver trusts a DNSSEC root key ahead of a key rollover.

To check for KSK-2024 (key tag 38696), query DNSSEC-signed names in `dnstest.dev`:
    
    
    # On a sentinel-aware resolver that trusts KSK-2024:
    
    # Returns NOERROR with an A answer.
    dig @1.1.1.1 root-key-sentinel-is-ta-38696.dnstest.dev. A +noall +comments +answer
    
    # Returns SERVFAIL without an answer.
    dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +noall +comments +answer
    
    # CD bypasses sentinel processing and returns the original A answer.
    dig @1.1.1.1 root-key-sentinel-not-ta-38696.dnstest.dev. A +cdflag +noall +comments +answer

For background on DNSSEC validation, refer to [DNSKEY](https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/).

Sep 22, 2026

## [concat() now supports up to 32 arguments](https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/)

[Rules](https://developers.cloudflare.com/rules/)

The `concat()` function in Cloudflare Rules now accepts up to 32 arguments, increased from 16. This allows you to build richer dynamic values directly in Rules expressions and simplify configurations that combine request data.

A common use case is adding a request header that sends context to your origin. The following Rulesets API request adds a Request Header Transform Rule to an existing `http_request_late_transform` phase ruleset. Its 18-argument expression combines request and network information into one header value:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "ref": "add_request_context_header",
        "description": "Add request context for the origin",
        "expression": "true",
        "action": "rewrite",
        "action_parameters": {
          "headers": {
            "X-Request-Context": {
              "operation": "set",
              "expression": "concat(\"ip=\", to_string(ip.src), \";country=\", ip.src.country, \";host=\", http.host, \";method=\", http.request.method, \";path=\", http.request.uri.path, \";query=\", http.request.uri.query, \";ray-id=\", cf.ray_id, \";asn=\", to_string(ip.src.asnum), \";user-agent=\", http.user_agent)"
            }
          }
        }
      }'

For more information, refer to the [`concat()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#concat) and [HTTP request header modification](https://developers.cloudflare.com/rules/transform/request-header-modification/).

Sep 18, 2026

## [Unified Routing generally available](https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Unified Routing is generally available for Cloudflare WAN and Magic Transit.

Unified Routing improves the integration between Cloudflare One and the standard connectivity onramps supported by Cloudflare WAN. It is capable of many new features including Automatic Return Routing, BGP and custom client subnets.

We recommend Unified Routing for all new accounts.

For details, refer to [Cloudflare WAN traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) and [Magic Transit traffic steering](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/#unified-routing).

Sep 18, 2026

## [cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027](https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of `cloudflared`. After the deprecation takes effect, Cloudflare will no longer publish new `cloudflared` releases for either architecture.

Windows 10, the last Windows release to support 32-bit systems, reached end of support in October 2025. Apple has also deprecated Intel-based Mac computers. macOS 26 Tahoe, released in September 2025, was the final macOS release to support Intel-based Macs. macOS 27, released in September 2026, no longer supports them.

Focusing development on currently supported architectures allows `cloudflared` to align with operating system support and continue receiving updates on supported platforms. For available downloads and supported platforms, refer to the [Cloudflare Tunnel downloads](https://developers.cloudflare.com/tunnel/downloads/) documentation.

Sep 17, 2026

## [Validate Rulesets changes before deployment](https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules now validates ruleset changes before deployment, helping you catch invalid expressions, action parameters, permission issues, unavailable features, and quota limits without publishing the configuration.

The Cloudflare dashboard performs this validation automatically when you create or update rules from **Security** > **Security rules** or **Rules** > **Overview**.

Supported Rulesets API mutation endpoints now also accept the `dry_run=true` query parameter. A dry run performs the same authorization and server-side validation checks as the requested change, but does not persist or publish it. Successful operations that normally return a `200` response return `result: null`. Operations that normally return `204` continue to do so.

#### API example

Add `dry_run=true` to a Rulesets API request to validate it without creating the ruleset:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets?dry_run=true" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Custom firewall rules",
        "kind": "zone",
        "phase": "http_request_firewall_custom",
        "rules": [
          {
            "action": "block",
            "expression": "ip.src.country eq \"GB\"",
            "description": "Block requests from the United Kingdom",
            "enabled": true
          }
        ]
      }'

For more information, refer to [Validate rule changes before deployment](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/).

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

Aug 19, 2026

## [Threat Intel Lists supported in Unified Routing](https://developers.cloudflare.com/changelog/post/2026-08-19-unified-routing-threat-lists/)

[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

[Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) Threat Intel Lists are now supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. This feature requires a Cloudflare Advanced Network Firewall subscription.

Support for additional features - Rate Limiting and Managed Rulesets - is planned.

For the full list of current beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

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

Aug 13, 2026

## [Oracle Cloud Infrastructure Object Storage support in Cloud Connector](https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/)

[Rules](https://developers.cloudflare.com/rules/)

Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.

OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional `oraclecloud.com` and dedicated `customer-oci.com` path-style endpoints.

Public buckets only

Cloud Connector does not sign requests or provide OCI credentials. Your bucket must allow anonymous object reads. Private buckets and pre-authenticated request URLs are not supported.

#### API example

Set `provider` to `oci_storage` and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:
    
    
    {
    	"expression": "http.request.uri.path wildcard \"/assets/*\"",
    	"provider": "oci_storage",
    	"description": "Route assets to OCI Object Storage",
    	"enabled": true,
    	"parameters": {
    		"host": "<BUCKET_NAME>.vhcompat.objectstorage.<REGION>.oci.customer-oci.com"
    	}
    }

For endpoint formats and bucket requirements, refer to [Supported cloud providers in Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage).

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

Jul 28, 2026

## [Improved DoH JSON formatting for additional record types](https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/)

[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)

Cloudflare is rolling out updated formatting for the `data` field in the 1.1.1.1 [DoH JSON API](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/) (`application/dns-json`). During the roll out responses may use either the old or new format.

Note

These are breaking changes. The DoH JSON format has no formal RFC and its schema is not guaranteed to be stable. If you need a stable format, use the [DoH wireformat](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-wireformat/) instead.

#### Human-readable display for additional record types

Several record types previously returned their `data` field in [RFC 3597 ↗︎](https://datatracker.ietf.org/doc/html/rfc3597) generic hex encoding (`\# <length> <hex>`). These now use standard presentation format:
    
    
    CAA:        0 issue "letsencrypt.org"
    NAPTR:      100 10 "s" "SIP+D2U" "" _sip._udp.example.com.
    RP:         admin.example.com. txt.example.com.
    IPSECKEY:   10 1 2 192.0.2.1 AwEA...
    SVCB:       1 target.example.com. alpn=h2
    HTTPS:      1 . alpn=h3,h2 ipv4hint=192.0.2.1
    TLSA:       3 1 1 aabbccdd...
    SSHFP:      1 2 aabbccdd...
    OPENPGPKEY: AwEA...

#### Numeric DNSSEC algorithm identifiers

DNSSEC-related records now use numeric algorithm identifiers as defined in [RFC 4034 ↗︎](https://datatracker.ietf.org/doc/html/rfc4034) instead of mnemonic names. This affects `RRSIG`, `DS`, `CDS`, `DNSKEY`, and `CDNSKEY` records. For example, `RSASHA256` becomes `8`, `ECDSAP256SHA256` becomes `13`, and `ED25519` becomes `15`. DS digest types also change from mnemonic to numeric: `SHA-256` becomes `2`.

Beforetxt
    
    
    RRSIG:  A RSASHA256 2 300 ...
    DS:     12345 RSASHA256 SHA-256 aabb...
    DNSKEY: 257 3 RSASHA256 AwEA...

Aftertxt
    
    
    RRSIG:  A 8 2 300 ...
    DS:     12345 8 2 aabb...
    DNSKEY: 257 3 8 AwEA...

#### Other formatting changes

`HINFO` character-strings are now individually quoted to remove ambiguity when values contain spaces:

Beforetxt
    
    
    "data": "Intel Xeon Linux"

Aftertxt
    
    
    "data": "\"Intel Xeon\" \"Linux\""

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

Jul 16, 2026

## [Bot management fields and ASN support in Cache Rules](https://developers.cloudflare.com/changelog/post/2026-07-16-cache-rules-bot-fields-asn/)

[Rules](https://developers.cloudflare.com/rules/)

#### Bot management fields and ASN support in Cache Rules

Cache Rules now supports bot management fields and the `ip.src.asnum` field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).

This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.

#### New fields

The following fields are now available in Cache Rules expressions:

Field | Type | Description  
---|---|---  
`cf.bot_management.score` | Number | Bot score from `1` to `99`, where a lower value indicates a higher likelihood that the request originates from a bot.  
`cf.bot_management.ja3_hash` | String | JA3 fingerprint of the request, which helps identify the client making the connection.  
`cf.bot_management.ja4` | String | JA4 fingerprint of the request, which provides a more detailed client identification than JA3.  
`cf.bot_management.verified_bot` | Boolean | Whether the request originates from a verified bot, such as a search engine crawler.  
`cf.bot_management.static_resource` | Boolean | Whether the request is for a static resource and therefore exempt from bot detection.  
`cf.bot_management.js_detection.passed` | Boolean | Whether the browser passed JavaScript detection when the feature is enabled.  
`cf.bot_management.detection_ids` | Array<Number> | List of IDs that correspond to Bot Management heuristic detections made on the request.  
`cf.bot_management.tags` | Array<String> | List of tags associated with the bot traffic, such as `API`, `GOOGLE`, or `BING`. Match a tag with an expression such as `any(cf.bot_management.tags[*] eq "API")`.  
`cf.bot_management.signed_agent` | Boolean | Whether the request originates from a known agent that identifies itself with Web Bot Auth.  
`cf.bot_management.corporate_proxy` | Boolean | Whether the request originates from a known corporate proxy.  
`ip.src.asnum` | Number | The autonomous system number (ASN) of the incoming request's IP address.  
  
Note

Bot management fields require a Bot Management subscription. `ip.src.asnum` is available on all plans.

#### Example

Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:
    
    
    (http.request.uri.path contains "/api/" and cf.bot_management.score lt 30)
    or
    (http.request.uri.path contains "/api/" and not ip.src.asnum in {12345 67890})

To learn more, refer to the [Cache Rules documentation](https://developers.cloudflare.com/cache/how-to/cache-rules/) and the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/network-security/2/)…[4](https://developers.cloudflare.com/changelog/product-group/network-security/4/)

[Next →](https://developers.cloudflare.com/changelog/product-group/network-security/2/)

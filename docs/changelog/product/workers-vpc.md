---
url: https://developers.cloudflare.com/changelog/product/workers-vpc/
title: Workers VPC Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:01.534121+00:00
---

# Workers VPC Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/workers-vpc/

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

Jun 16, 2026

## [TCP connections via connect() over VPC Networks](https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

[VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings now support the [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via `fetch()`.

This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "vpc_networks": [
        {
          "binding": "PRIVATE_NETWORK",
          "network_id": "cf1:network",
          "remote": true
        }
      ]
    }
    
    
    [[vpc_networks]]
    binding = "PRIVATE_NETWORK"
    network_id = "cf1:network"
    remote = true

At runtime, use `connect()` on the binding to open a TCP socket to a private destination:
    
    
    export default {
    	async fetch(request: Request, env: Env) {
    		// Open a TCP connection to a private Redis instance
    		const socket = await env.PRIVATE_NETWORK.connect("10.0.1.50:6379");
    
    		// Write a Redis PING command
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("PING\r\n"));
    		await writer.close();
    
    		return new Response(socket.readable);
    	},
    };

Note

`connect()` over VPC Networks currently supports plaintext TCP only.

For more details, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) and the [Workers Binding API](https://developers.cloudflare.com/workers-vpc/api/).

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

May 21, 2026

## [Reach Cloudflare WAN destinations from Workers VPC](https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

You can now use [VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings with `network_id: "cf1:network"` to reach your full private network from Workers, including:

  * [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes and client devices
  * Subnet routes and hostname routes announced through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) or Cloudflare Mesh
  * Destinations connected through [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) on-ramps — GRE, IPsec, and CNI



This means a single VPC Network binding can route Worker requests to private services regardless of how those services are connected to Cloudflare: through a Cloudflare Tunnel from a cloud VPC, a Mesh node on a private subnet, or a Cloudflare WAN on-ramp from your data center or branch site.
    
    
    {
    	"vpc_networks": [
    		{
    			"binding": "PRIVATE_NETWORK",
    			"network_id": "cf1:network",
    			"remote": true,
    		},
    	],
    }
    
    
    [[vpc_networks]]
    binding = "PRIVATE_NETWORK"
    network_id = "cf1:network"
    remote = true

At runtime, the URL you pass to `fetch()` determines the destination:
    
    
    // Reach a service behind a Cloudflare WAN IPsec on-ramp
    const response = await env.PRIVATE_NETWORK.fetch("http://10.50.0.100:8080/api");

Note

For destinations behind Cloudflare WAN on-ramps (GRE, IPsec, or CNI), your network must route the [Cloudflare source IP range](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/) back through the on-ramp so reply traffic returns to Cloudflare. Without this route, stateful flows will fail. This is part of standard Cloudflare WAN onboarding.

For configuration options, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/).

Apr 14, 2026

## [VPC Networks and Cloudflare Mesh support now in public beta](https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

[VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings now give your Workers access to any service in your private network without pre-registering individual hosts or ports. This complements existing [VPC Service](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/) bindings, which scope each binding to a specific host and port.

You can bind to a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) by `tunnel_id` to reach any service on the network where that tunnel is running, or bind to your [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) network using `cf1:network` to reach any Mesh node, client device, or subnet route in your account:
    
    
    {
      "vpc_networks": [
        {
          "binding": "MESH",
          "network_id": "cf1:network",
          "remote": true
        }
      ]
    }
    
    
    [[vpc_networks]]
    binding = "MESH"
    network_id = "cf1:network"
    remote = true

At runtime, `fetch()` routes through the network to reach the service at the IP and port you specify:
    
    
    const response = await env.MESH.fetch("http://10.0.1.50:8080/api/data");

For configuration options and examples, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) and [Connect Workers to Cloudflare Mesh](https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/).

Mar 20, 2026

## [Observability for Workers VPC Services](https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Each VPC Service now has a **Metrics** tab so you can monitor connection health and debug failures without leaving the dashboard.

![Workers VPC Metrics dashboard showing connections, latency, and errors charts](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3336,height=3204,format=webp/_astro/2026-03-20-metrics-dashboard.6kfnbqQd.png)

  * **Connections** — See successful and failed connections over time, broken down by what is responsible: your origin (Bad Upstream), your configuration (Client), or Cloudflare (Internal).
  * **Latency** — Track connection and DNS resolution latency trends.
  * **Errors** — Drill into specific error codes grouped by category, with filters to isolate upstream, client, or internal failures.



You can also view and edit your VPC Service configuration, host details, and port assignments from the **Settings** tab.

For a full list of error codes and what they mean, refer to [Troubleshooting](https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/).

Feb 13, 2026

## [Origin CA certificate support for Workers VPC](https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Workers VPC now supports [Cloudflare Origin CA certificates](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/) when connecting to your private services over HTTPS. Previously, Workers VPC only trusted certificates issued by publicly trusted certificate authorities (for example, Let's Encrypt, DigiCert).

With this change, you can use free Cloudflare Origin CA certificates on your origin servers within private networks and connect to them from Workers VPC using the `https` scheme. This is useful for encrypting traffic between the tunnel and your service without needing to provision certificates from a public CA.

For more information, refer to [Supported TLS certificates](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/#supported-tls-certificates).

Nov 5, 2025

## [Announcing Workers VPC Services (Beta)](https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

**Workers VPC Services** is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.

#### What's new

  * **VPC Services** : Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax
  * **Multi-cloud Support** : Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels


    
    
    export default {
    	async fetch(request, env, ctx) {
    		// Perform application logic in Workers here
    
    		// Sample call to an internal API running on ECS in AWS using the binding
    		const response = await env.AWS_VPC_ECS_API.fetch("https://internal-host.example.com");
    
    		// Additional application logic in Workers
    		return new Response();
    	},
    };

#### Getting started

Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. [Refer to the documentation](https://developers.cloudflare.com/workers-vpc/) to get started.

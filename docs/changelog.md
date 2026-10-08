---
url: https://developers.cloudflare.com/changelog/
title: Changelogs | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:48.486569+00:00
---

# Changelogs | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/

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

## [Cloudflare One Client for macOS (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster connects and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Oct 7, 2026

## [Cloudflare One Client for Windows (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across tunnel reconnections.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved connection reliability on devices with very large hosts files. The client now detects a large hosts file, allows more time for its initial DNS check, and shows a banner letting the user know that connecting may take longer.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * A service recovery mechanism, backed by a Windows scheduled task, now starts the client service on system unlock if it is not already running. This is enabled by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client service failing to restart after an unexpected termination.
  * Fixed the client UI getting stuck in a connecting state after sleep and wake even though the tunnel was connected.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * A Windows DNS client regression may cause connectivity check failures on systems containing large hosts files. While this release includes a fix to mitigate this issue, users may still experience reduced DNS performance and connectivity check failures.



Oct 7, 2026

## [Cloudflare One Client for Linux (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client window not appearing on first launch after a fresh install on RHEL 10.
  * Fixed duplicate WARP routing policy rules accumulating on reconnect.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.



Oct 7, 2026

## [Query Log Explorer datasets from Observability Logs](https://developers.cloudflare.com/changelog/post/2026-10-07-log-search-in-observability-logs/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer datasets are now queried from the [Logs](https://developers.cloudflare.com/observability/logs/) page under **Observability** in the Cloudflare dashboard. The Logs page brings Log Explorer and Workers Observability datasets together with a shared filter builder, SQL editor, and visualizations.

As part of this change, the **Log Explorer** menu is no longer shown in the dashboard navigation.

  * Your enabled datasets, saved queries, and SQL queries continue to work on the Logs page.
  * To manage datasets, open the dataset selector on the Logs page and select **Configure** next to the Log Explorer datasets.
  * The previous Log Search page remains available at its direct URL.



For more information, refer to [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) and the [Logs overview](https://developers.cloudflare.com/observability/logs/).

Oct 7, 2026

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 6, 2026

## [Standardize provider credential error responses in AI Gateway](https://developers.cloudflare.com/changelog/post/2026-10-05-provider-credential-errors/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway's REST API now returns consistent responses when an AI provider rejects credentials. The change applies to [`POST /ai/run` ↗︎](https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT_ID%7D/ai/run).

Scenario | Previous AI Gateway response | New AI Gateway response  
---|---|---  
ElevenLabs | Provider-specific `UserCredentialsError` with HTTP `403` | HTTP `401` with error code `2009`  
Google Vertex | HTTP `500` for rejected credentials, with upstream retries | HTTP `401` with error code `2009`; the request fails without retrying the provider  
All other providers | HTTP `402` or another provider-specific status for rejected credentials | HTTP `401` with error code `2009`  
When using [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), the provider rejects the credentials | Provider-specific authentication error | HTTP `503`  
  
Update applications that handle AI Gateway REST API errors to treat HTTP `401` as an invalid or rejected provider credential.

For details about providing provider credentials, refer to [Bring your own provider keys](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-key/).

Oct 6, 2026

## [Warnings when approaching your DNS records quota](https://developers.cloudflare.com/changelog/post/2026-10-06-dns-records-quota-warning/)

[DNS](https://developers.cloudflare.com/dns/)

The DNS records page in the Cloudflare dashboard now shows a warning once you have used 85% of your [DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#dns-records-quota).

The warning reflects the quota that applies to you. If your zone has its own quota, the warning shows that zone's usage. If your account uses an [account-level DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#per-account-quota), the warning shows your usage across all zones in the account.

![Warning on the DNS records page showing that a domain has used 86% of its DNS record limit](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1520,height=226,format=webp/_astro/dns-records-quota-warning.iH_msM4_.png)

Oct 6, 2026

## [WAF Release - 2026-10-06](https://developers.cloudflare.com/changelog/post/2026-10-06-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces a new detection to mitigate a heap-based buffer overflow vulnerability in F5 BIG-IP, and enhances existing command injection protections by incorporating tested beta logic into the baseline rule.

**Key Findings**

  * CVE-2026-94127: A heap-based buffer overflow vulnerability in F5 BIG-IP. Attackers can exploit this flaw to execute arbitrary code on the affected system.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...a056caff| N/A| Command Injection - Generic 8 - uri - Beta| Log| Block| This rule is merged into the original rule "Command Injection - Generic 8 - uri" (ID: ...ee159e2e).  
Cloudflare Managed Ruleset| ...7206c737| N/A| F5 BIG-IP - UnAuth Heap-Overflow - CVE:CVE-2026-94127| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...549f7356| N/A| Next.js - Cache Poisoning - CVE:CVE-2026-94543| Block| Block| Rule metadata description refined. Detection unchanged.  
  
Oct 6, 2026

## [WAF Release - Scheduled changes for 2026-10-12](https://developers.cloudflare.com/changelog/post/scheduled-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

Announcement Date| Release Date| Release Behavior| Legacy Rule ID| Rule ID| Description| Comments  
---|---|---|---|---|---|---  
2026-10-06| 2026-10-12| Disable| N/A| ...02751ef3| Generic Rules - Template Injection - 2 - Beta| This rule will be merged into the original rule "Generic Rules - Template Injection - 2" (ID: ...d3ed0123).  
  
Oct 5, 2026

## [Detect organization-specific risks with CASB custom finding types](https://developers.cloudflare.com/changelog/post/2026-10-05-casb-custom-findings/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) now supports [**custom finding types**](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/), giving security teams full control over the security conditions CASB detects across their SaaS and cloud integrations.

In addition to CASB's library of standard finding types, you can now write your own detection logic using [Rego ↗︎](https://www.openpolicyagent.org/docs/policy-language), the open-source policy language from Open Policy Agent (OPA). Use custom finding types to match your organization's own thresholds and exceptions, such as flagging admin accounts without two-factor authentication, and get higher-confidence findings to act on.

![Create a custom finding type with a name, severity, scope, and Rego detection logic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1194,height=1194,format=webp/_astro/create-custom-finding-type.CF3GXoPZ.png)

#### Key capabilities

  * **Write your own detection logic** — Define exactly what CASB flags using Rego expressions evaluated against asset data from your connected integrations.
  * **Target any supported provider and asset class** — Scope a custom finding type to a provider (such as Google Workspace or Microsoft 365) and asset class (such as users, files, or groups), and apply it to all integrations for that provider or a selected subset.
  * **Built-in validation** — Select **Validate** to check your expression for syntax errors and schema issues before you create the finding type.
  * **Inspect and duplicate standard finding types** — Open any standard finding type to view its detection logic, then duplicate it as the starting point for a custom finding type.
  * **Works with CASB policies** — Use custom finding types in [CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) to send matching findings to Slack, ServiceNow, or any other webhook destination.



#### Get started

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Findings library**.
  2. Select **Create finding**.
  3. Enter a name, description, and severity.
  4. Select a provider and asset class, then set the integration scope.
  5. Write your Rego expression and select **Validate**.
  6. Select **Create finding**.



CASB evaluates the custom finding type against assets as they are created or updated within the selected scope. Matching assets appear as posture finding instances under **Posture Findings**.

#### Learn more

  * Learn how to [create and manage custom finding types](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/) in Cloudflare One.
  * Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare One.
  * Learn how to [create and manage CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) in Cloudflare One.



CASB custom finding types are now available in Cloudflare One.

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

## [Introducing Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Web Search API](https://developers.cloudflare.com/web-search/)

[Web Search API](https://developers.cloudflare.com/web-search/) is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers: [Ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/). All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) crawling standards.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "What are some fun things to do in Salt Lake City as fall approaches?",
        "provider": "ceramic",
        "limit": 5,
        "options": { "gateway": { "id": "default" } }
      }'

Or from a Worker with the AI binding:
    
    
    const response = await env.AI.websearch({
    	gatewayId: "default",
    	query: "What are some fun things to do in Salt Lake City as fall approaches?",
    	provider: "exa",
    	limit: 5,
    });
    
    const results = await response.json();

To get started, refer to [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/).

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

Oct 2, 2026

## [Run the Pi Durable harness on Cloudflare with the Agents SDK](https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The [Agents SDK](https://developers.cloudflare.com/agents/) now provides first-class support for building agents using the Pi harness. You can build long-running agents using the combination of [Pi 1.0 ↗︎](https://earendil.com/posts/pi-1-0/), [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/), and the new `PiHarness` class that the Cloudflare Agents SDK provides, ensuring your agent's work is durably persisted, even if interrupted mid-turn.

Built with [Earendil ↗︎](https://earendil.com/), this integration is our first step toward first-class support for third-party agent harnesses on Cloudflare.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi)

Beta

`PiHarness` is in beta. [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/) is a new, experimental package, and the `PiHarness` API will likely change as Pi Durable matures.

`PiHarness` is a new "Lifecycle capability" provided by the Cloudflare Agents SDK. Pi Durable provides the agent harness and the Lifecycle is responsible for keeping the agent running in the Durable Object. The Lifecycle is a core concept in the Agents SDK ensuring that long-running work can run in a Durable Object, surviving restarts, crashes, and network issues. We will share more on Lifecycle capabilities in the near future.

#### Install

npmyarnpnpmbun
    
    
    npm i agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    yarn add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    pnpm add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    bun add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai

Both Pi packages are optional peer dependencies of `agents`, so you only install them if you use the harness.

#### Use it in an Agent

Creating a Pi agent requires configuring the Pi `Harness` with a model, skills, and tools, then registering the `PiHarness` with the `Agent` class.
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent<Env> {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt: string) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }

The `agents/models/pi-ai` entry point supports AI Gateway and Workers AI models, so you can get started with Cloudflare models right away or use your existing Pi AI provider.

#### Add tools with extensions

Both tools and system prompt sections are provided to the Pi `Harness` via extensions.
    
    
    import { Type } from "@earendil-works/pi-ai";
    
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));
    
    
    import { Type } from "@earendil-works/pi-ai";
    import type { ToolRegistration } from "@earendil-works/pi-durable";
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount: ToolRegistration<typeof WordCount> = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));

For more information on creating and configuring extensions, refer to [Extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/).

#### Learn more

  * [Pi harness documentation](https://developers.cloudflare.com/agents/harnesses/pi/)
  * [Pi harness extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/)
  * [pi-ai model provider](https://developers.cloudflare.com/agents/models/pi-ai/)
  * [Pi harness example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi), with WebSockets, a browser UI, and a `@cloudflare/computer` Workspace for the model's tools
  * [Lifecycle ↗︎](https://github.com/cloudflare/agents/blob/main/docs/agents/lifecycle.md)
  * [Pi Durable announcement ↗︎](https://earendil.com/posts/pi-durable/) from Earendil



Oct 2, 2026

## [30 days of analytics data on every plan](https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/)

[Analytics](https://developers.cloudflare.com/analytics/)

Every plan now gets at least 30 days of analytics data. Adaptive analytics datasets, such as HTTP requests, security events, and DNS analytics, retain at least 31 days of data for Free and Pro domains, and you can query up to 30 days in a single request. Previously, Free and Pro domains could see between 24 hours and 8 days of history depending on the dataset.

A full month of history lets you investigate an issue after it happens, compare today with the same day in previous weeks, and tell a one-time spike from a longer trend. The change applies in the Cloudflare dashboard, in [Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/), and through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

Domain analytics also now live in one place. In the Cloudflare dashboard, select a domain and go to **Analytics** to see Traffic, Performance, Security, Cache, Origin, DNS, and Visitors as tabs that share one time range and one set of filters. Account-level analytics are under **Observability** > **Analytics**.

This change does not alter which datasets or fields your plan can access. Aggregated datasets, such as `httpRequests1hGroups`, keep their existing per-plan limits. To check the exact retention and query window for a zone or account, query the [settings](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/) for each dataset.

For plan-specific limits, refer to [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/#availability), [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/#availability), and [GraphQL Analytics API limits](https://developers.cloudflare.com/analytics/graphql-api/limits/#node-limits-and-availability).

Oct 2, 2026

## [Workers Observability logs and traces in Custom Dashboards](https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/)

[Analytics](https://developers.cloudflare.com/analytics/)

You can now build Custom Dashboards charts from Workers Observability data. Two new datasets, **Workers Observability — Logs** and **Workers Observability — Traces (OTel)** , let you chart Worker invocations, log levels, errors, CPU and wall time, span counts, and durations next to HTTP traffic, security events, and other analytics datasets.

This gives you one dashboard for an application that spans Cloudflare's network and your Workers. For example, you can put request volume, WAF blocks, and Worker error rates on the same view, filter all three by time range, and spot whether a spike in errors lines up with a change in traffic.

The datasets are available for every Worker in your account that has [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/) turned on. Custom Dashboards also now allow up to 100 dashboards for every account.

To get started, refer to [Workers Observability data in Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/#workers-observability-data).

Oct 2, 2026

## [United States jurisdiction](https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/)

[D1](https://developers.cloudflare.com/d1/)

You can create D1 databases with the `us` jurisdiction. These databases run and persist data within the United States.

Use this option for regional data residency requirements.

To create a database with the `us` jurisdiction, run:
    
    
    npx wrangler@latest d1 create db-with-us-jurisdiction --jurisdiction=us

For more information, refer to [D1 data location](https://developers.cloudflare.com/d1/configuration/data-location/).

Oct 2, 2026

## [Organizations support increased account and zone limits](https://developers.cloudflare.com/changelog/post/2026-10-02-organization-account-zone-limits/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations now support up to **20,000 accounts** and **200,000 zones**. For MSSP/Distributors using sub-organizations, these limits are applied at the root Organization.

If you require a higher limit, reach out to your account team. The new limits apply to enterprise and MSSP/Distributor Organizations. Legacy reseller partner and brand partner tenants retain their existing quota behavior.

For more information, refer to [Account and zone limits](https://developers.cloudflare.com/fundamentals/organizations/limitations/#account-and-zone-limits).

Oct 2, 2026

## [Workers KV namespace jurisdictions are now generally available](https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/)

[KV](https://developers.cloudflare.com/kv/)

Jurisdictions for [Workers KV](https://developers.cloudflare.com/kv/) namespaces are now generally available. When you create a namespace, you can set a [jurisdiction](https://developers.cloudflare.com/kv/reference/data-location/) to make sure the namespace's data is only durably stored within that region. Jurisdictions can help you comply with data localization regulations such as GDPR or FedRAMP. Supported jurisdictions are `eu`, `us`, and `fedramp`.

A jurisdiction can only be set when a namespace is created, using the Cloudflare dashboard, Wrangler, the `cf` CLI, or the REST API, and cannot be added or changed afterwards.
    
    
    npx wrangler@latest kv namespace create <NAMESPACE_NAME> --jurisdiction=eu
    
    
    cf kv namespaces create --title <NAMESPACE_NAME> --jurisdiction eu
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/storage/kv/namespaces" \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "title": "<NAMESPACE_NAME>",
        "jurisdiction": "eu"
      }'

Workers can still access a namespace restricted to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction on Cloudflare's network. The jurisdiction only controls where the namespace's data is durably stored.

To learn more, refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/).

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

## [Introducing Clef: Cloudflare's first open-source decision models, now on Workers AI](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Meet [`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) and [`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/), the first models trained by the Cloudflare Workers AI team, available on Workers AI today.

Clef is a decision model, in the same family as [Typesafe's Jev ↗︎](https://typesafe.ai/blog/introducing-system-one-models-and-jev). Instead of generating text, it reads an input state and a set of typed questions, then returns a probability for every allowed answer. Your agent gets a structured decision it can act on immediately, for example: route the ticket, block the request, or escalate to a human. There is no free-form output to parse and no reasoning tokens to wait for.

Both models are hosted on Workers AI as [Clef](https://developers.cloudflare.com/workers-ai/models/clef/) and [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/). We are also open-sourcing the weights under the Apache 2.0 license on Hugging Face: [Clef ↗︎](https://huggingface.co/Cloudflare/clef) and [Clef-flash ↗︎](https://huggingface.co/Cloudflare/clef-flash). Read the [launch blog post ↗︎](https://blog.cloudflare.com/clef-decision-models/) for the full story, including how we trained them.

We are also launching a reinforcement learning (RL) fine-tuning service to help you tune Clef for your own workloads. [Sign up to work with us as a design partner ↗︎](https://www.cloudflare.com/resource/clef-rl-interest).

#### Built for the hot path

Clef is designed to be fast so decisions come back in milliseconds. Across our 43 benchmark runs, we achieved speeds where Clef is 2.5x faster than Jev at the median, and Clef-flash 13x faster.

Latency | Clef | Clef-flash | Jev  
---|---|---|---  
Median | 209.3 ms | **38.8 ms** | 524.1 ms  
p95 | 238.6 ms | **122.4 ms** | 536.0 ms  
  
Hosting on Workers AI adds to that speed. Requests run on GPUs across Cloudflare's network, running close to your users, so the network round trip stays short. You can put Clef directly in the request path of your agent, then hand off to an LLM on Workers AI to take action.

#### Leading the benchmarks

Across 10 decision benchmarks, a Clef model scores highest on 7, ahead of Jev and other open decision models. A few highlights:

Benchmark | Clef | Clef-flash | Jev  
---|---|---|---  
BFCL (case exact) | 98.47 | **98.76** | 95.75  
BANKING77 (macro-F1) | **94.20** | 90.93 | 79.74  
CLINC150+OOS (macro-F1) | **97.43** | 66.77 | 89.27  
Home appliances (case exact) | 82.95 | **97.73** | 52.27  
  
On Typesafe's own workflow evals, Clef beats Jev in 3 of 4 areas: invoice processing, customer service, and security incidents. The full results are on the [Hugging Face model card ↗︎](https://huggingface.co/Cloudflare/clef).

#### Drop-in compatible with Jev

Model | Size | Best for | Context window  
---|---|---|---  
[`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) | 27B | Highest-precision decisions | 64K tokens  
[`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/) | 9B | Latency-critical, hot-path decisions | 64K tokens  
  
Clef follows the System One API, so you can switch an existing Jev integration to Clef by changing the endpoint and model. Ask up to 64 questions per request, in three types:

  * **`noul`** : A yes/no question. Returns the probability that the answer is yes.
  * **`choice`** : Pick one option from a set you define. Returns the chosen option, a probability per option, and a confidence value.
  * **`score`** : Rate against an ordered rubric. Returns a probability-weighted score and a probability per level.


    
    
    const response = await env.AI.run("@cf/cloudflare/clef", {
    	model: "clef",
    	state: "Checkout has been failing for every customer for the last hour.",
    	questions: {
    		urgent: {
    			type: "noul",
    			instructions: "Is this support request urgent?",
    		},
    		team: {
    			type: "choice",
    			instructions: "Which team should handle this request?",
    			criteria: {
    				billing: "Payments, invoices, and refunds",
    				technical: "Outages, errors, and configuration",
    				sales: "Plans and upgrades",
    			},
    		},
    	},
    });
    
    // response.answers.urgent.noul -> probability the request is urgent
    // response.answers.team.choice -> highest-probability team
    
    
    const response = await env.AI.run("@cf/cloudflare/clef", {
    	model: "clef",
    	state: "Checkout has been failing for every customer for the last hour.",
    	questions: {
    		urgent: {
    			type: "noul",
    			instructions: "Is this support request urgent?",
    		},
    		team: {
    			type: "choice",
    			instructions: "Which team should handle this request?",
    			criteria: {
    				billing: "Payments, invoices, and refunds",
    				technical: "Outages, errors, and configuration",
    				sales: "Plans and upgrades",
    			},
    		},
    	},
    });
    
    // response.answers.urgent.noul -> probability the request is urgent
    // response.answers.team.choice -> highest-probability team

#### What you can build with decision models

  * **Support triage** : Decide whether a ticket is urgent and which team owns it, then route it without a human in the loop.
  * **Threat intelligence** : Classify a website by category. Paired with [Browser Run](https://developers.cloudflare.com/browser-run/), Clef fetched, rendered, and classified a domain in 2.2 seconds, compared to 4.7 seconds for `gpt-oss-120b` in the same workflow.
  * **Trust and safety** : Score user submissions against your own policy rubric and act on the probability.
  * **Agent guardrails** : Let an agent check "should I take this action?" in tens of milliseconds before calling a tool.
  * **Visual classification** : Pass up to four images alongside the state. Unlike text-only decision models, Clef has a vision encoder.



#### Get started

Use Clef through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the REST API at `/ai/run`. You can also use [AI Gateway](https://developers.cloudflare.com/ai-gateway/) with these endpoints.

For more information, refer to the [Clef model page](https://developers.cloudflare.com/workers-ai/models/clef/), the [Clef-flash model page](https://developers.cloudflare.com/workers-ai/models/clef-flash/), and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Oct 1, 2026

## [The best way to do MCP auth just got better: Workers OAuth Provider goes v1, with a new split API and full support for MCP 2026-07-28](https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

[`@cloudflare/workers-oauth-provider` ↗︎](https://github.com/cloudflare/workers-oauth-provider) is now v1, with a new split API. One Worker acts as the authorization server: it signs users in and issues tokens. Your MCP server acts as the resource server, and can run in another Worker. It validates each token with the authorization server over a [Service Binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/), without crossing the public Internet.

  * It supports the [MCP 2026-07-28 authorization specification ↗︎](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), including [Client ID Metadata Documents ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#client-id-metadata-documents) and [issuer identification ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#authorization-response-issuer). It still works with older clients, including those using [Dynamic Client Registration ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#dynamic-client-registration).
  * `insufficientScope()` gives you [step-up authorization ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#scopes-and-step-up-authorization) in one line.
  * The authorization server and the resource server can run in [different Workers ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/resource-servers.md#separate-workers) with different [WAF](https://developers.cloudflare.com/waf/) and [rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) rules.
  * One authorization server can issue tokens for [many MCP servers ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#resources-and-token-audiences).
  * A [migration skill ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/skills/migrate-to-1.0/SKILL.md) ships in the npm package so a coding agent can perform the upgrade.



#### The split API
    
    
    import {
    	OAuthAuthorizationServer,
    	OAuthResourceServer,
    	insufficientScope,
    } from "@cloudflare/workers-oauth-provider";
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    // auth-server Worker: signs users in and issues tokens for both MCP servers.
    const authorizationServer = new OAuthAuthorizationServer({
    	issuer: "https://auth.example.com",
    	resources: [
    		"https://calendar.example.com/mcp",
    		"https://drive.example.com/mcp",
    	],
    	scopesSupported: ["calendar:read", "calendar:write", "offline_access"],
    	clientIdMetadataDocumentEnabled: true,
    });
    
    export class AuthServer extends WorkerEntrypoint {
    	fetch(request) {
    		if (new URL(request.url).pathname === "/authorize") {
    			return showConsent(request, this.env);
    		}
    		return authorizationServer.fetch(request, this.env, this.ctx);
    	}
    
    	validateToken(resource, token) {
    		return authorizationServer.validateToken(resource, token, this.env);
    	}
    }
    
    // calendar MCP Worker: checks tokens with AuthServer over a Service Binding.
    export const calendar = new OAuthResourceServer({
    	resourceMetadata: {
    		resource: "https://calendar.example.com/mcp",
    		authorization_servers: ["https://auth.example.com"],
    	},
    	requiredScopes: ["calendar:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			if (
    				request.method === "POST" &&
    				!ctx.auth.scope.includes("calendar:write")
    			) {
    				return insufficientScope(ctx.auth, ["calendar:read", "calendar:write"]);
    			}
    			return handleMcp(request, ctx.props);
    		},
    	},
    });
    
    
    import {
    	OAuthAuthorizationServer,
    	OAuthResourceServer,
    	insufficientScope,
    } from "@cloudflare/workers-oauth-provider";
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    // auth-server Worker: signs users in and issues tokens for both MCP servers.
    const authorizationServer = new OAuthAuthorizationServer<Env>({
    	issuer: "https://auth.example.com",
    	resources: [
    		"https://calendar.example.com/mcp",
    		"https://drive.example.com/mcp",
    	],
    	scopesSupported: ["calendar:read", "calendar:write", "offline_access"],
    	clientIdMetadataDocumentEnabled: true,
    });
    
    export class AuthServer extends WorkerEntrypoint<Env> {
    	fetch(request: Request) {
    		if (new URL(request.url).pathname === "/authorize") {
    			return showConsent(request, this.env);
    		}
    		return authorizationServer.fetch(request, this.env, this.ctx);
    	}
    
    	validateToken(resource: string, token: string) {
    		return authorizationServer.validateToken(resource, token, this.env);
    	}
    }
    
    // calendar MCP Worker: checks tokens with AuthServer over a Service Binding.
    export const calendar = new OAuthResourceServer<Env, AuthProps>({
    	resourceMetadata: {
    		resource: "https://calendar.example.com/mcp",
    		authorization_servers: ["https://auth.example.com"],
    	},
    	requiredScopes: ["calendar:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			if (
    				request.method === "POST" &&
    				!ctx.auth.scope.includes("calendar:write")
    			) {
    				return insufficientScope(ctx.auth, ["calendar:read", "calendar:write"]);
    			}
    			return handleMcp(request, ctx.props);
    		},
    	},
    });

In the example, `env.AUTH_SERVER.validateToken` is that Service Binding call. The calendar Worker needs no KV namespace of its own.
    
    
    {
    	"name": "calendar-mcp",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"services": [
    		{
    			"binding": "AUTH_SERVER",
    			"service": "auth-server",
    			"entrypoint": "AuthServer",
    		},
    	],
    }
    
    
    name = "calendar-mcp"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[services]]
    binding = "AUTH_SERVER"
    service = "auth-server"
    entrypoint = "AuthServer"

`OAuthResourceServer` publishes the [RFC 9728 ↗︎](https://datatracker.ietf.org/doc/html/rfc9728) protected resource metadata that MCP clients use to find your authorization server. It answers requests without a token with a `401` challenge that points to that metadata. It also rejects tokens issued for any other resource.

You can still use `OAuthProvider` as both the authorization server and the MCP server. For most 0.x deployments, the only required change is to add `resourceMetadata: { resource }`.

#### Other updates and helpers

  * [Consent page ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/consent-page.md) and [upstream sign-in ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/upstream-sign-in.md) helpers implement the MCP confused deputy protections.
  * [Sliding refresh token expiry ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#sliding-expiry) with `refreshTokenIdleTTL`.
  * [Resumable KV cleanup ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#kv-cleanup) with `purgeExpiredData()`.
  * An [internal reason ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#the-internal-reason) on every error passed to `onError`.



#### Upgrade with the migration skill

npmyarnpnpmbun
    
    
    npm i @cloudflare/workers-oauth-provider@latest
    
    
    yarn add @cloudflare/workers-oauth-provider@latest
    
    
    pnpm add @cloudflare/workers-oauth-provider@latest
    
    
    bun add @cloudflare/workers-oauth-provider@latest

Point your coding agent at `node_modules/@cloudflare/workers-oauth-provider/skills/migrate-to-1.0/SKILL.md`, or follow the [migration guide ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/migration-1.0.md).

For both Workers in full, refer to the [split Workers example ↗︎](https://github.com/cloudflare/workers-oauth-provider/tree/main/examples/split-workers).

Oct 1, 2026

## [AI Search is generally available](https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/)

[AI Search](https://developers.cloudflare.com/ai-search/)

AI Search is now generally available. Usage-based billing begins on November 1, 2026, with included monthly ingestion, storage, semantic query, and full-text query usage. Cloudflare will send a reminder email the week before billing begins.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for rates and included usage.

#### Hybrid search is on by default

New AI Search instances use hybrid search by default. Hybrid search combines semantic vector retrieval with full-text matching. You can choose a different index method when you create an instance.

Refer to [Hybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/) for details.

#### Workers AI embeddings and reranking are included

Workers AI embedding and reranking calls made by AI Search are included in AI Search pricing. These calls no longer appear on your Workers AI bill or in your AI Gateway logs. Generation, query rewriting, and external providers continue to use your account and gateway.

Refer to [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for details.

#### Multimodal model and image support

AI Search supports the `@cf/qwen/qwen3-vl-embedding-2b` and `google-ai-studio/gemini-embedding-2` multimodal embedding models. Search and chat requests can include images through the REST API and public endpoint.

Refer to [Supported models](https://developers.cloudflare.com/ai-search/configuration/models/supported-models/) for the full list of embedding models.

#### OCR availability and increased file limits

Optical character recognition (OCR) is available on every account for scanned PDFs. Plain-text or code files and PDFs with OCR enabled can be up to 10 MiB. PDFs without OCR and other supported formats remain limited to 4 MiB.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/#file-limits) for file limits and [Limits & pricing](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) for OCR pricing.

#### Source type inference

When you create an AI Search instance, the `type` field is optional. AI Search infers a website source from an HTTP or HTTPS URL, or an R2 source from an existing bucket name.

Refer to [Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) for details.

Oct 1, 2026

## [Artifacts is now in open beta](https://developers.cloudflare.com/changelog/post/2026-10-01-artifacts-open-beta/)

[Artifacts](https://developers.cloudflare.com/artifacts/)[Workers](https://developers.cloudflare.com/workers/)

[Artifacts](https://developers.cloudflare.com/artifacts/), Cloudflare's versioned file system that speaks Git, is now in open beta. Artifacts is built for scale, so you can create a repository per project, user, session, or task.

With Artifacts, you can:

  * **Deploy repositories to Workers** — Connect an Artifacts repository through [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/). Pushes to the production branch deploy the updated Worker, while other branches create or update [Worker Previews](https://developers.cloudflare.com/workers/previews/).
  * **Programmatically manage repositories** — Use an [Artifacts binding](https://developers.cloudflare.com/artifacts/api/workers-binding/) from a Worker to create or fork repos, inspect files and commits, read files by path, and issue repo-scoped Git tokens.
  * **React to repository changes** — [Subscribe to events](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/) when a repository is created, imported, forked, deleted, pushed to, cloned, or fetched.
  * **Control where repository data is stored** — Choose to [store and process](https://developers.cloudflare.com/artifacts/guides/data-localization/) your data in the US or EU.
  * **Monitor repository usage** — View total operations, pulls, pushes, errors, and error rates in the Cloudflare dashboard or [via API for analytics](https://developers.cloudflare.com/artifacts/observability/metrics/).



Artifacts is available for customers on the Workers Paid plan. Cloudflare will begin [billing](https://developers.cloudflare.com/artifacts/platform/pricing/) for Artifacts on October 14, 2026.

#### Build the next GitHub on Cloudflare

We are hosting a competition to see who can build the next GitHub on Cloudflare using Workers and Artifacts.

[Apply today ↗︎](https://www.cloudflare.com/git-competition/) — submissions are open until October 14, 2026.

The first-place team will receive $25,000 in Cloudflare credits. The top three teams will be flown to San Francisco to present what they built at Cloudflare Connect.

Get started with the [Artifacts documentation](https://developers.cloudflare.com/artifacts/).

← Prev

1[2](https://developers.cloudflare.com/changelog/2/)…[53](https://developers.cloudflare.com/changelog/53/)

[Next →](https://developers.cloudflare.com/changelog/2/)

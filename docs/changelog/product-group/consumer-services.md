---
url: https://developers.cloudflare.com/changelog/product-group/consumer-services/
title: Consumer services Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:23.147176+00:00
---

# Consumer services Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/consumer-services/

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

Sep 8, 2026

## [Radar search now includes Internet events](https://developers.cloudflare.com/changelog/post/2026-09-08-radar-search-events/)

[Radar](https://developers.cloudflare.com/radar/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) search now includes Internet events and outages alongside existing results. Search event descriptions or related entities, such as locations, ASes, bots, and top-level domains, to find relevant events and open the most relevant Radar view.

![Radar search results showing Internet outage events associated with locations and autonomous systems](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2512,height=1130,format=webp/_astro/radar-search-events.DpZAk59G.png)

Event links preserve the event date range, making it easier to investigate what changed before, during, and after an event. These results are also available to browser-based AI agents through [WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/).

Aug 26, 2026

## [Radar Researcher adds richer sources and URL Scanner explanations](https://developers.cloudflare.com/changelog/post/2026-08-26-radar-researcher-improvements/)

[Radar](https://developers.cloudflare.com/radar/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) expands the [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=) beta with richer sources and new ways to investigate Internet data.

#### Connected insights

Radar Researcher responses can now link to relevant Radar pages, reports, and Cloudflare Blog posts.

![Radar Researcher response linking to the IP Address Information and Network Quality Test pages](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=798,height=668,format=webp/_astro/radar-researcher-page-links.D74GzYoL.png)

#### URL Scanner report explanations

Select **Explain with AI** on a [URL Scanner report ↗︎](https://radar.cloudflare.com/scan) to have Radar Researcher explain its findings and answer follow-up questions about the scanned site.

![Radar Researcher explaining findings from an example.com URL Scanner report](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=696,height=1250,format=webp/_astro/radar-researcher-url-scanner-explanation.BBCehcJx.png)

#### Improved shared sessions

Shared conversations now open in fullscreen, while the share URL remains available until you close the panel or start a new conversation.

Open [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=) to explore these improvements.

Aug 24, 2026

## [RPKI ASPA path validation on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-08-24-radar-aspa-validation/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) adds an [ASPA validation tool ↗︎](https://radar.cloudflare.com/routing/aspa-validation) to its [Routing section ↗︎](https://radar.cloudflare.com/routing). Enter a BGP `AS_PATH` and the tool checks it against the [Autonomous System Provider Authorization (ASPA) ↗︎](https://blog.cloudflare.com/aspa-secure-internet/) records currently published in the RPKI, returning a verdict of `Valid`, `Invalid`, or `Unknown`. An `Invalid` verdict means no chain of provider authorizations covers the whole path, which is the signature of a route leak.

Validation follows [draft-ietf-sidrops-aspa-verification ↗︎](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/), so verdicts match those produced by validators implementing the same draft. The draft is still a work in progress and not yet an RFC.

#### Enter a path

Paths are read in BGP wire order: the rightmost AS is the origin, and the leftmost AS is the one closest to the collector or router that observed the route. AS numbers can be separated by spaces, commas, or hyphens, with or without an `AS` prefix. The full ASPA snapshot is loaded into the browser once, so the verdict, graph, and trace update as the path is edited, with no further requests. A set of example paths covers the interesting cases, including a route leak with an AS0 ASPA, where an AS declares that it has no providers at all.

#### Choose an algorithm

The draft defines two verification algorithms that differ only in whether a down-ramp is permitted:

  * **Upstream** ([section 5.4 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.4)) — for routes received from a customer, peer, route server client, or route server. Only an up-ramp is permitted.
  * **Downstream** ([section 5.5 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.5)) — for routes received from a provider. Both an up-ramp and a down-ramp are permitted.



An **up-ramp** is the run of consecutive customer-to-provider hops from the origin to the apex of the path, and a **down-ramp** is the equivalent run from the announcing neighbor back to that apex. The tool evaluates both algorithms at once and labels each with its verdict, so a path that is legitimate when received from one session type and a leak when received from another is visible without switching modes. Selecting an algorithm drives the graph and the trace.

#### Read the result

The **ASPA validation graph** draws the path hop by hop, labeling each AS with its role, whether it publishes an ASPA, and how many providers that ASPA authorizes. Every hop is marked `Provider+`, `Not Provider+`, or `No attestation`, and the maximum and minimum bounds of each ramp are drawn against the length of the path. Hops that no ramp reaches are highlighted, because a path the ramps cannot cover end to end is `Invalid`. The accompanying **ASPA records** table lists every AS in the path with its ASPA status and its authorized providers, each linked to its Radar AS page.

![ASPA validation graph for the path 1003 6939 1299 553, showing a Valid verdict under the downstream algorithm, the Provider+, Not Provider+, and No attestation outcome on each hop, and the up-ramp and down-ramp bounds that together cover the path](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1222,format=webp/_astro/aspa-validation-graph.DQUq8KCm.png)

#### Follow the algorithm

The **Algorithm step by step** section shows the derivation rather than just the answer. Two columns run the same scans under different stopping rules: the upper bounds, which test for `Invalid` and stop only on `Not Provider+`, and the lower bounds, which test for `Unknown` and also stop on `No Attestation`. A hop is `Not Provider+` when the AS publishes an ASPA that does not list the next AS as a provider, and `No Attestation` when the AS publishes no ASPA at all. Each column lists the outcome for every hop scanned, marks where the scan stopped, gives the resulting ramp length, and then evaluates the verdict rule with the numbers filled in.

![Step-by-step trace for the same path, with the upper-bound and lower-bound columns each listing the up-ramp and down-ramp scans, the ramp lengths they produce, and the verdict rule that neither Invalid nor Unknown satisfies, leaving a Valid verdict](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1392,height=586,format=webp/_astro/aspa-validation-algorithm-trace.Bb8SM4wT.png)

#### Share a validation

The path and the selected algorithm are kept in the URL, so a link reproduces a result exactly — for example, this [route leak with an AS0 ASPA ↗︎](https://radar.cloudflare.com/routing/aspa-validation?path=22652-1299-9498-149765-14789). Appending `&mode=upstream` pins the link to the upstream algorithm. The graph is a standard Radar widget, so it can also be embedded or shared as an image.

The records behind the tool are the same ones served by the [`/bgp/rpki/aspa/snapshot`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/) endpoint of the [`ASPA`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/) API, and the number of records loaded and the snapshot timestamp are shown alongside the input.

Try the [ASPA validation tool ↗︎](https://radar.cloudflare.com/routing/aspa-validation) with a path of your own.

Aug 7, 2026

## [AS-level connectivity and upstream providers on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-08-07-radar-as-connectivity-upstreams/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) expands its [Routing section ↗︎](https://radar.cloudflare.com/routing) with two widgets on AS pages, such as [AS13335 ↗︎](https://radar.cloudflare.com/routing/as13335), that describe how a network reaches the rest of the Internet: the paths it takes toward the [Tier-1 ↗︎](https://en.wikipedia.org/wiki/Tier_1_network) networks, and the mix of direct upstreams carrying its routes. Both are derived from [RouteViews ↗︎](https://www.routeviews.org/) RIB snapshots, unioned across selected collectors.

#### AS-level connectivity

The **AS-level connectivity** graph aggregates the BGP paths an AS uses to reach the Tier-1 networks, unioned across all the prefixes it announces, as observed by selected RouteViews collectors. It reads from left to right, starting at the queried AS and ending at the Tier-1 networks, and each node is labeled with its AS number, country, and organization name. Tier-1 nodes are marked so they stand apart from the intermediate networks that lead to them.

By default, the graph shows the network's direct connections to Tier-1 networks plus the indirect paths, which keeps the view readable. A **Show full paths** toggle expands it to every observed path, including transit through Tier-1 networks the AS already connects to. An IP version selector switches between IPv4 and IPv6, because the paths reaching Tier-1 networks may differ between the two address families.

![AS-level connectivity graph for AS13335, showing Tier-1 networks it reaches directly alongside paths that reach others through intermediate networks](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1526,format=webp/_astro/as-level-connectivity-graph.DGv8lrUx.png)

This is the AS-level counterpart to the **Real-time connectivity** graph on prefix pages, such as the one for [1.1.1.0/24 ↗︎](https://radar.cloudflare.com/routing/prefix/1.1.1.0/24). Instead of covering a single prefix, it covers the union of paths for all prefixes an AS announces, which makes it a fast way to read a network's transit hierarchy: which providers it depends on, how many hops separate it from the core, and whether its paths to the core are diverse or concentrated. For more information on the prefix-level graph, refer to [BGP real-time routes](https://developers.cloudflare.com/radar/glossary/#bgp-real-time-routes).

#### Upstream providers

The **Upstream providers** widget tracks the share of an AS's observed paths carried by each of its direct upstream networks over time, drawn as a stacked area chart. Up to 10 upstreams appear as their own series and the remaining ones are grouped into **Other**. Transit changes such as adding a provider, dropping one, or moving traffic between them appear as movement between bands rather than as a single aggregate number. As with the connectivity graph, an IP version selector switches between IPv4 and IPv6.

![Stacked area chart of the share of AS13335's observed paths carried by each of its top 10 direct upstreams, with the remainder grouped into Other](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=976,format=webp/_astro/as-upstream-providers-timeseries.BUc6CJaT.png)

#### API endpoints

The data behind both widgets is also available through two new endpoints on the [`BGP`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/) API:

  * [`/bgp/routes/paths/{asn}`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list/) — Returns the ordered AS path segments an AS uses to reach the Tier-1 networks, each with its observed path count, peer count, and contributing collectors, alongside the name and country of every ASN in the response. Pass `collector` to scope the result to a single RouteViews collector.
  * [`/bgp/routes/upstreams/{asn}/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries/) — Returns the share of an AS's observed paths carried by each direct upstream over time. Use `limit` to control how many upstreams come back as separate series before the rest are grouped into an `OTHER` series, and `ipVersion` to select the address family.



Visit the [AS13335 routing page ↗︎](https://radar.cloudflare.com/routing/as13335) to explore both widgets, or swap in any other AS number.

Aug 7, 2026

## [Radar Researcher beta and WebMCP support now available](https://developers.cloudflare.com/changelog/post/2026-08-07-radar-researcher-and-webmcp/)

[Radar](https://developers.cloudflare.com/radar/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) now includes [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=), a beta AI-powered assistant for exploring Internet trends and traffic data in plain language. Open Researcher from the header on any Radar page to ask questions by voice or text, receive explanations, and view interactive charts based on Radar API data.

![Screenshot of the Radar Researcher panel alongside the Radar overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1430,height=780,format=webp/_astro/radar-researcher-panel.B7QqJlGo.webp)

To ask about a specific chart, select **Explain with AI** to start a conversation with its underlying data and context.

![Screenshot of the Explain with AI option in a Radar chart menu](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=434,height=302,format=webp/_astro/radar-explain-with-ai.Dgw4ghVh.webp)

You can explore further with suggested follow-up questions, find earlier conversations through searchable history, and share conversations through shareable links.

Alongside the user-facing Researcher experience, Radar now supports [WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/), allowing browser-based AI agents to navigate Radar, search data, and use tools such as URL scanning and domain lookup.

To get started, visit [Cloudflare Radar ↗︎](https://radar.cloudflare.com/).

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

Jun 24, 2026

## [Precise IP location and richer AS details on the Cloudflare Radar IP page](https://developers.cloudflare.com/changelog/post/2026-06-24-radar-ip-page-improvements/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now plots your IPv4 and IPv6 locations on the [IP page ↗︎](https://radar.cloudflare.com/ip), shows the Cloudflare data centers serving your connection, and includes more detail about the autonomous system (AS) your primary IP belongs to.

#### Your IP location on the map

The map of your connection now shows:

  * **IP location markers** — The primary IP will show as a red marker. When both IP addresses do not geolocate to the same place, a second marker will appear in blue with a note explaining why IPv4 and IPv6 can resolve to different locations.
  * **Cloudflare data center markers** — Cloudflare data centers now show as orange dots on the map and the one you are connected to is highlighted.
  * **Data center connectors** — Each line connects your IP markers to their respective data centers.

![Map showing Cloudflare data centers and a marker representing the IP location with a line connected to a data center](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3136,height=1305,format=webp/_astro/ip-page-geolocation.BJ53oUtj.png)

Due to the data policies of our geolocation provider, this detailed location is only available for your own IP. Other IP addresses keep the current country-level view.

#### Extended AS information

The AS card on the IP page now shows additional detail about the network an IP belongs to — including alternate names, the operator website, and an estimate of the AS user population — alongside the AS number and country.

Visit the [Cloudflare Radar IP page ↗︎](https://radar.cloudflare.com/ip) to explore more details about your IP.

Jun 18, 2026

## [Updated Workers AI popularity metric in Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-06-18-radar-workers-ai-inference-metric/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) has changed how it measures [Workers AI](https://developers.cloudflare.com/workers-ai/) model and task popularity.

Previously, popularity was based on the number of unique accounts running inferences against each model or task. It is now based on the **number of inferences** , giving a more representative view of actual usage volume. This change will affect all new measurements as well as historical data. As a result, the model and task distributions shown on Radar may differ from what you saw previously, and historical trends may shift accordingly.

The [Workers AI model popularity ↗︎](https://radar.cloudflare.com/ai-insights#workers-ai-model-popularity) chart shows the distribution of inferences across models.

![Screenshot of the Workers AI model popularity chart on the AI Insights page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=938,format=webp/_astro/workers-ai-model-popularity.CMw_WVXg.png)

The [Workers AI task popularity ↗︎](https://radar.cloudflare.com/ai-insights#workers-ai-task-popularity) chart shows the distribution of inferences across tasks.

![Screenshot of the Workers AI task popularity chart on the AI Insights page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=938,format=webp/_astro/workers-ai-task-popularity.ZoA-NO8k.png)

The same data is available via the following API endpoints:

  * [`/ai/inference/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2/)
  * [`/ai/inference/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2/)



Explore the data on the [AI Insights page ↗︎](https://radar.cloudflare.com/ai-insights).

Jun 5, 2026

## [Finer-grained chart granularity on Cloudflare Radar for longer time ranges](https://developers.cloudflare.com/changelog/post/2026-06-05-radar-traffic-chart-granularity/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now provides finer-grained traffic charts for longer time ranges. Previously, selecting a 1-3 month view on HTTP and NetFlows charts defaulted to weekly aggregation, which was too coarse to surface meaningful trends. Views longer than 3 months defaulted to monthly aggregation, returning as few as 7 data points for a 6-month range.

The new defaults are:

  * **1-3 months** : daily granularity (7x more data points)
  * **Longer than 3 months** (HTTP and NetFlows): weekly granularity (4x more data points)



For example, a 12-week traffic view previously showed weekly data:

![Traffic trends chart with weekly granularity for a 12-week view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/traffic-granularity-12w-before.OlJmS6Ts.png)

The same view now shows daily data:

![Traffic trends chart with daily granularity for a 12-week view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/traffic-granularity-12w-after.DL8mxwQ3.png)

Similarly, a 1-year HTTP traffic view that previously showed just 12 monthly data points now provides 52 weekly data points.

Visit [Cloudflare Radar ↗︎](https://radar.cloudflare.com/?dateRange=12w#traffic-trends) to explore the new granular views.

May 29, 2026

## [TLS bug detection in the Cloudflare Radar post-quantum checker](https://developers.cloudflare.com/changelog/post/2026-05-29-radar-pq-tls-bug-detection/)

[Radar](https://developers.cloudflare.com/radar/)

The [**Radar**](https://developers.cloudflare.com/radar/) [post-quantum TLS support checker ↗︎](https://radar.cloudflare.com/post-quantum#website-support) now also reports TLS bugs detected during the handshake test. When a scanned host exhibits compatibility issues, the results include details on the specific bugs detected, along with guidance on how to investigate and remediate each issue. The bugs section only appears for hosts where issues are found.

The following TLS bugs are detected:

  * **Split ClientHello** — The connection fails with a fragmented post-quantum `ClientHello` but succeeds with classical handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS messages.
  * **HRR Failure** — The server sends a `HelloRetryRequest` but fails to complete the handshake afterward.
  * **Unknown Keyshare** — The server cannot handle unknown key exchange algorithms and fails instead of responding with a `HelloRetryRequest` as required by the TLS 1.3 specification.

![TLS bug detection results in the Radar post-quantum checker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2260,height=1244,format=webp/_astro/pq-tls-bug-detection.BrmsVMno.png)

Bug detection data is available through the existing [`/post_quantum/tls/support`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/) endpoint.

Visit the [Post-Quantum Encryption ↗︎](https://radar.cloudflare.com/post-quantum#website-support) page to test a host.

May 20, 2026

## [Content type distribution and API traffic share on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-05-20-radar-content-type-and-api-traffic/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes two new charts on the [traffic page ↗︎](https://radar.cloudflare.com/traffic) that provide deeper insights into the composition of HTTP traffic: a content type distribution chart and an API traffic share chart.

#### Content type distribution

The new [**Content type** ↗︎](https://radar.cloudflare.com/traffic#content-type) chart displays the distribution of HTTP response content types, grouped into high-level categories. A traffic type selector allows filtering by human, bot, or all traffic. The existing [**Bot vs. Human** ↗︎](https://radar.cloudflare.com/traffic#bot-vs-human) chart also gained a content type category filter, allowing users to see the bot/human split for specific content categories.

![Screenshot of the content type distribution chart on the Radar traffic page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/content-type-distribution.Dz2q1n6W.png)

Content type categories:

  * **HTML** — Web pages (`text/html`)
  * **Images** — All image formats (`image/*`)
  * **JSON** — JSON data and API responses (`application/json`, `*+json`)
  * **JavaScript** — Scripts (`application/javascript`, `text/javascript`)
  * **CSS** — Stylesheets (`text/css`)
  * **Plain Text** — Unformatted text (`text/plain`)
  * **Fonts** — Web fonts (`font/*`, `application/font-*`)
  * **XML** — XML documents and feeds (`text/xml`, `application/xml`, `application/rss+xml`, `application/atom+xml`)
  * **YAML** — Configuration files (`text/yaml`, `application/yaml`)
  * **Video** — Video content and streaming (`video/*`, `application/ogg`, `*mpegurl`)
  * **Audio** — Audio content (`audio/*`)
  * **Markdown** — Markdown documents (`text/markdown`)
  * **Documents** — PDFs, Office documents, ePub, CSV (`application/pdf`, `application/msword`, `text/csv`)
  * **Binary** — Executables, archives, WebAssembly (`application/octet-stream`, `application/zip`, `application/wasm`)
  * **Serialization** — Binary API formats (`application/protobuf`, `application/grpc`, `application/msgpack`)
  * **Other** — All other content types



The `CONTENT_TYPE` dimension and `contentType` filter are available on the HTTP [summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/summary_v2/), [timeseries groups](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries_groups_v2/), and [timeseries](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries/) endpoints.

#### API traffic share

The new [**API traffic** ↗︎](https://radar.cloudflare.com/traffic#api-traffic) chart shows the percentage of dynamic (non-cacheable) HTTP request traffic that is API-related. API traffic is identified by JSON or XML response content types (`application/json`, `application/xml`, `text/xml`) on HTTP requests that returned a 200 status code. A traffic type selector allows switching between human traffic, bot traffic, or all traffic.

![Screenshot of the API traffic share chart on the Radar traffic page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1006,format=webp/_astro/api-traffic-share._xl0TThn.png)

The `API_TRAFFIC` dimension is available on the existing HTTP [summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/summary_v2/) and [timeseries groups](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries_groups_v2/) endpoints. An `apiTraffic` filter (`API` or `NON_API`) can also be applied to [HTTP timeseries](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries/) requests to retrieve raw request counts for API-only or non-API traffic.

Visit the [Radar traffic page ↗︎](https://radar.cloudflare.com/traffic) to explore these new charts.

May 19, 2026

## [MRT Explorer on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes an [MRT Explorer ↗︎](https://radar.cloudflare.com/routing/mrt-explorer) tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.

#### Loading a file

Paste a URL to fetch an MRT file remotely, drag and drop one onto the page, or browse for a local file. Gzip and bzip2 compressed files are supported. A sample file is also available to get started right away.

![Screenshot of the MRT Explorer file input form](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2428,height=898,format=webp/_astro/mrt-explorer-form.DKnzUqMC.png)

#### Inspecting events

Once parsed, the tool lists every BGP event with its timestamp, prefix, AS path, OTC (Only to Customer), and community attributes.

![Screenshot of the MRT Explorer event list](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2410,height=1536,format=webp/_astro/mrt-explorer-list.8fq2u5Kc.png)

#### Event details

Clicking on the "View details" action opens a modal with additional properties and the full event JSON.

![Screenshot of the MRT Explorer event details modal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1694,height=1890,format=webp/_astro/mrt-explorer-details.EMcHevWw.png)

#### Shareable URLs

When loading a file by URL, the query string captures the source so the link can be shared directly — the recipient's browser immediately fetches and parses the same file.

Try the [MRT Explorer on Cloudflare Radar ↗︎](https://radar.cloudflare.com/routing/mrt-explorer).

May 6, 2026

## [TLD Nameserver Performance in Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-05-06-radar-tld-nameserver-performance/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now provides TLD authoritative nameserver performance insights, measuring response time (latency) as observed from Cloudflare's [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/) resolver infrastructure when forwarding queries upstream to TLD nameservers.

New widgets on [TLD detail pages ↗︎](https://radar.cloudflare.com/tlds/com):

  * [**Aggregate nameserver latency** ↗︎](https://radar.cloudflare.com/tlds/com#tld-ns-latency): Response time percentiles (p25/p50/p75) for all authoritative nameservers of the selected TLD.
  * [**Latency per nameserver** ↗︎](https://radar.cloudflare.com/tlds/com#tld-ns-latency-by-ns): Median response time (p50) broken down by each authoritative nameserver over time.

![Latency per nameserver chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1268,format=webp/_astro/tld-nameserver-latency-by-ns.CZGT23Vk.png)

  * [**Median latency geographic distribution** ↗︎](https://radar.cloudflare.com/tlds/com#geographical-distribution): p50 response time by Cloudflare data center country, displayed on a choropleth map.
  * [**TLD ranking over time** ↗︎](https://radar.cloudflare.com/tlds/com#tld-ranking): Daily DNS magnitude rank and magnitude value with a Rank/Magnitude toggle.
  * [**Rank change deltas** ↗︎](https://radar.cloudflare.com/tlds): 1 week, 4 weeks, and 3 months rank changes added to the TLD magnitude table and the TLD detail info panel.

![TLD Rankings by DNS Magnitude table with rank change deltas](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2642,height=1446,format=webp/_astro/tld-magnitude-rank-deltas.BaT-jII_.webp)

The new [`TLD Performance`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/) API provides the following endpoints:

  * [`/tlds/performance/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/summary/) — TLD nameserver performance summarized by dimension.
  * [`/tlds/performance/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/timeseries_groups/) — TLD nameserver performance over time grouped by dimension.



Available dimensions: `LATENCY` (aggregate p25/p50/p75), `NAMESERVER_LATENCY` (per-nameserver p50), `LOCATION_LATENCY` (per-data-center-country p50).

TLD Performance is also available as a dataset in the [Data Explorer ↗︎](https://radar.cloudflare.com/explorer?dataSet=tlds.performance).

Check out the updated [TLD detail page ↗︎](https://radar.cloudflare.com/tlds/com).

May 4, 2026

## [New routing widgets on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-05-04-radar-routing-widgets/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) is expanding its [Routing section ↗︎](https://radar.cloudflare.com/routing) with two new widgets that give a deeper view into how networks announce address space and how RPKI ROA coverage evolves over time.

#### Top ASes by announced IP space on country pages

Country routing pages now include a **Top ASes by announced IP space** chart, breaking down the IPv4 and IPv6 address space announced from a country across the autonomous systems that originate it. The chart stacks the IPv4 and IPv6 views vertically, with the top contributing ASes called out by color and the remaining networks aggregated as **Other**.

![Screenshot of the top ASes by announced IP space chart on a country routing page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1322,format=webp/_astro/country-top-ases-ip-space.CoGqJB6W.png)

#### RPKI ROA deployment timeseries

The [RPKI sub-page ↗︎](https://radar.cloudflare.com/routing/rpki) adds an **RPKI ROA deployment** timeseries widget that tracks the share of announced BGP space covered by a valid Route Origin Authorization (ROA) over time, with separate IPv4 and IPv6 lines. A toggle switches the view between the share of covered **prefixes** and the share of covered **IP address space**. The widget is available on global, country, and AS views, so operators can monitor RPKI adoption progress and compare deployment trends across different scopes.

![Screenshot of the RPKI ROA deployment timeseries widget](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=874,format=webp/_astro/rpki-roa-deployment-timeseries.DTsP_V93.png)

#### API endpoints

The data behind these widgets is also available through two new endpoints on the [`BGP`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/) API:

  * [`/bgp/ips/top/ases`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/) \- Returns the top autonomous systems by announced IP space (IPv4 `/24`s or IPv6 `/48`s), globally or filtered by country, snapped to the nearest 8-hour RIB boundary.
  * [`/bgp/rpki/roas/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/) \- Returns RPKI ROA validation coverage over time, by share of prefixes or share of IP address space, split by IP version, with optional ASN or location filters.



Visit the [Radar routing section ↗︎](https://radar.cloudflare.com/routing) to explore both widgets.

Apr 30, 2026

## [Cloud Observatory connection metrics improvements](https://developers.cloudflare.com/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/)

[Radar](https://developers.cloudflare.com/radar/)

The [Cloud Observatory ↗︎](https://radar.cloudflare.com/cloud-observatory) on [**Radar**](https://developers.cloudflare.com/radar/) now provides improved connection metric insights, offering new ways to explore TCP round-trip time, TCP handshake duration, TLS handshake duration, and response header receive duration across cloud provider origin servers.

The [Cloud Observatory overview ↗︎](https://radar.cloudflare.com/cloud-observatory#connection-metrics) now shows connection metrics broken down by cloud provider, making it easy to compare connection performance across Amazon Web Services, Google Cloud, Microsoft Azure, and Oracle Cloud.

![Screenshot of Cloud Observatory connection metrics broken down by cloud provider](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2338,height=1408,format=webp/_astro/cloud-observatory-connection-metrics-by-provider.Bk9nSitV.png)

Each [provider page ↗︎](https://radar.cloudflare.com/cloud-observatory/amazon#connection-metrics) now shows connection metrics for the top five regions, with a selector to rank by lowest or highest values.

![Screenshot of Cloud Observatory connection metrics broken down by region for a provider](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2338,height=1414,format=webp/_astro/cloud-observatory-connection-metrics-by-region.CbHAKXoc.png)

Each [region page ↗︎](https://radar.cloudflare.com/cloud-observatory/amazon/us-east-1#connection-metrics) now displays connection metrics as percentile distributions (25th percentile, median, and 75th percentile), providing insight into the range and variability of connection times.

![Screenshot of Cloud Observatory connection metrics with percentile distribution for a region](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2340,height=1288,format=webp/_astro/cloud-observatory-connection-metrics-percentiles.DJ9eAE0-.png)

These views are also available through the [`Origins` API](https://developers.cloudflare.com/api/resources/radar/subresources/origins/), using the `timeseries_groups` endpoint with the `ORIGIN`, `REGION`, or `PERCENTILE` dimension.

Apr 30, 2026

## [Dark mode support on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-04-30-radar-dark-mode/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now supports **dark mode**. A theme selector in the upper right corner of the page lets users explicitly choose between three display options:

  * **Light** — standard light theme
  * **Dark** — full dark theme
  * **System** — follows the operating system preference

![Screenshot of the theme selector showing Light, Dark, and System options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=404,height=296,format=webp/_astro/dark-mode-theme-selector.D5ih8e4q.png)

The selected theme applies consistently across all Radar pages and widgets.

![Screenshot of the Cloudflare Radar overview page in dark mode](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3818,height=1682,format=webp/_astro/dark-mode-overview.D-39RJlY.png)

The theme choice also applies to shared and embedded graphs.

Try it out at [Cloudflare Radar ↗︎](https://radar.cloudflare.com).

Apr 17, 2026

## [AI Insights updates on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) adds three new features to the [AI Insights ↗︎](https://radar.cloudflare.com/ai-insights) page, expanding visibility into how AI bots, crawlers, and agents interact with the web.

#### Adoption of AI agent standards

The AI Insights page now includes an [adoption of AI agent standards ↗︎](https://radar.cloudflare.com/ai-insights#adoption-of-ai-agent-standards) widget that tracks how websites adopt agent-facing standards. The data is filterable by domain category and updated weekly on Mondays. This data is also available through the [Agent Readiness API reference](https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness/methods/summary/).

![Screenshot of the adoption of AI agent standards chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1332,format=webp/_astro/agent-readiness-adoption-chart.B3ATN59P.png)

[URL Scanner ↗︎](https://radar.cloudflare.com/scan) reports now include an **Agent readiness** tab that evaluates a scanned URL against the criteria used by the [Agent Readiness score tool ↗︎](https://isitagentready.com/).

![Screenshot of the URL Scanner agent readiness tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1145,format=webp/_astro/agent-readiness-url-scanner.DRVuuaUi.png)

For more details, refer to the [Agent Readiness blog post ↗︎](https://blog.cloudflare.com/agent-readiness/).

#### Markdown for Agents savings

A new [savings gauge ↗︎](https://radar.cloudflare.com/ai-insights#markdown-for-agents-savings) shows the median response-size reduction when serving Markdown instead of HTML to AI bots and crawlers. This highlights the bandwidth and token savings that [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) provides.

![Screenshot of the Markdown for Agents savings gauge](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=614,height=652,format=webp/_astro/markdown-for-agents-savings.Di1GjNON.png)

For more details, refer to the [Markdown for Agents API reference](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary).

#### Response status

The new [response status widget ↗︎](https://radar.cloudflare.com/ai-insights#response-status) displays the distribution of HTTP response status codes returned to AI bots and crawlers. Results are groupable by individual status code (200, 403, 404) or by category (2xx, 3xx, 4xx, 5xx).

The same widget is available on each verified bot's detail page (only available for AI bots), for example [Google ↗︎](https://radar.cloudflare.com/bots/directory/google#response-status).

![Screenshot of the response status distribution widget](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=878,format=webp/_astro/ai-response-status.BwSMF23Z.png)

Explore all three features on the [Cloudflare Radar AI Insights ↗︎](https://radar.cloudflare.com/ai-insights) page.

Apr 14, 2026

## [Generate citations on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-04-14-radar-citations/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) shareable widgets now include a **generate citation** action, making it easier to reference [Cloudflare Radar ↗︎](https://radar.cloudflare.com) data in research papers and other publications.

![Screenshot of the generate citation icon in the widget action bar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=548,height=308,format=webp/_astro/citation-action-icon.B2QPGPhA.png)

Select the citation icon to open a modal with five supported citation styles:

  * **BibTeX**
  * **APA**
  * **MLA**
  * **Chicago**
  * **RIS**

![Screenshot of the citation modal with format options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1432,height=800,format=webp/_astro/citation-modal.Bf5eDHwO.png)

Explore the feature on any shareable widget at [Cloudflare Radar ↗︎](https://radar.cloudflare.com).

Apr 1, 2026

## [Routing Section Expansion on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-04-01-radar-routing-section/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now features an expanded [Routing section ↗︎](https://radar.cloudflare.com/routing) with dedicated sub-pages, providing a more organized and in-depth view of the global routing ecosystem. This restructuring lays the groundwork for additional routing features and widgets coming in the near future.

#### Dedicated sub-pages

The single Routing page has been split into three focused sub-pages:

  * [**Overview** ↗︎](https://radar.cloudflare.com/routing) — Routing statistics, IP address space trends, BGP announcements, and the new Top 100 ASes ranking.
  * [**RPKI** ↗︎](https://radar.cloudflare.com/routing/rpki) — RPKI validation status, ASPA deployment trends, and per-ASN ASPA provider details.
  * [**Anomalies** ↗︎](https://radar.cloudflare.com/routing/anomalies) — BGP route leaks, origin hijacks, and Multi-Origin AS (MOAS) conflicts.

![Screenshot of the routing section menu](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=574,height=342,format=webp/_astro/routing-section-menu.CEq17il_.png)

#### New widgets

The routing overview now includes a **Top 100 ASes** table ranking autonomous systems by customer cone size, IPv4 address space, or IPv6 address space. Users can switch between rankings using a segmented control.

![Screenshot of the top-100 ASes table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1426,format=webp/_astro/top-100-ases-table.ZBSReN_5.png)

The RPKI sub-page introduces a **RPKI validation** view for per-ASN pages, showing prefixes grouped by RPKI validation status (Valid, Invalid, Unknown) with visibility scores.

![Screenshot of the RPKI validation view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=978,format=webp/_astro/rpki-validation-view.D3eQih4x.png)

#### Improved IP address space chart

The [IP address space ↗︎](https://radar.cloudflare.com/routing) chart now displays both IPv4 and IPv6 trends stacked vertically and is available on global, country, and AS views.

![Screenshot of the IPv4 and IPv6 combined IP space chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1310,format=webp/_astro/combined-ipv4-ipv6-space.DQ5qc8la.png)

Check out the [Radar routing section ↗︎](https://radar.cloudflare.com/routing) to explore the data, and stay tuned for more routing insights coming soon.

Mar 26, 2026

## [URL Scanner improvements on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-03-26-url-scanner-improvements/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) ships several improvements to the [URL Scanner ↗︎](https://radar.cloudflare.com/scan) that make scan reports more informative and easier to share:

  * **Live screenshots** — the summary card now includes an option to capture a live screenshot of the scanned URL on demand using the [Browser Rendering](https://developers.cloudflare.com/browser-run/) API.
  * **Save as PDF** — a new button generates a print-optimized document aggregating all tab contents (Summary, Security, Network, Behavior, and Indicators) into a single file.
  * **Download as JSON** — raw scan data is available as a JSON download for programmatic use.
  * **Redesigned summary layout** — page information and security details are now displayed side by side with the screenshot, with a layout that adapts to narrower viewports.
  * **File downloads** — downloads are separated into a dedicated card with expandable rows showing each file's source URL and SHA256 hash.
  * **Detailed IP address data** — the Network tab now includes additional detail per IP address observed during the scan.

![Screenshot of the redesigned URL Scanner summary on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2424,height=2658,format=webp/_astro/url-scanner-summary-redesign.DO4wDjQ3.png)

Explore these improvements on the [Cloudflare Radar URL Scanner ↗︎](https://radar.cloudflare.com/scan).

Mar 6, 2026

## [Region Filtering, AS Traffic Volume, and Navigation Improvements on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) ships several new features that improve the flexibility and usability of the platform, as well as visibility into what is happening on the Internet.

#### Region filtering

All location-aware pages now support filtering by region, including continents, geographic subregions ([Middle East ↗︎](https://radar.cloudflare.com/middle-east), [Eastern Asia ↗︎](https://radar.cloudflare.com/eastern-asia), etc.), political regions ([EU ↗︎](https://radar.cloudflare.com/european-union), [African Union ↗︎](https://radar.cloudflare.com/african-union)), and US Census regions/divisions (for example, [New England ↗︎](https://radar.cloudflare.com/traffic/us-new-england), [US Northeast ↗︎](https://radar.cloudflare.com/traffic/us-northeast)).

![Screenshot of region filtering on Radar - Middle east](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1108,format=webp/_astro/region-filtering-middle-east.D__dYNBw.png)

#### Traffic volume by top autonomous systems and locations

A new traffic volume view shows the top autonomous systems and countries/territories for a given location. This is useful for quickly determining which network providers in a location may be experiencing connectivity issues, or how traffic is distributed across a region.

![Screenshot of traffic volume by top autonomous systems in US](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=928,format=webp/_astro/traffic-volume-top-as-us.DhnbB8gy.png)

The new AS and location dimensions have also been added to the [Data Explorer ↗︎](https://radar.cloudflare.com/explorer) for the HTTP, DNS, and NetFlows datasets. Combined with other available filters, this provides a powerful tool for generating unique insights.

![Screenshot of AS and location dimensions in Data Explorer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1486,format=webp/_astro/data-explorer-top-as-pt.DAWOCd_b.png)

Finally, breadcrumb navigation is now available on most pages, allowing easier navigation between parent and related pages.

Check out these features on [Cloudflare Radar ↗︎](https://radar.cloudflare.com).

Mar 3, 2026

## [Network Quality Test on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-03-03-radar-network-quality-test/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes a [Network Quality Test ↗︎](https://radar.cloudflare.com/speedtest) page. The tool measures Internet connection quality and performance, showing connection details such as IP address, server location, network (ASN), and IP version. For more detailed speed test results, the page links to [speed.cloudflare.com ↗︎](https://speed.cloudflare.com/).

![Screenshot of the Network Quality Test page on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2294,height=1526,format=webp/_astro/network-quality-test.BwQ-CoTH.png)

Feb 27, 2026

## [Post-Quantum Encryption and Key Transparency on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-02-27-radar-pq-key-transparency/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now tracks post-quantum encryption support on origin servers, provides a tool to test any host for post-quantum compatibility, and introduces a Key Transparency dashboard for monitoring end-to-end encrypted messaging audit logs.

#### Post-quantum origin support

The new [`Post-Quantum`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/) API provides the following endpoints:

  * [`/post_quantum/tls/support`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/) \- Tests whether a host supports post-quantum TLS key exchange.
  * [`/post_quantum/origin/summary/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/methods/summary/) \- Returns origin post-quantum data summarized by key agreement algorithm.
  * [`/post_quantum/origin/timeseries_groups/{dimension}`](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/methods/timeseries_groups/) \- Returns origin post-quantum timeseries data grouped by key agreement algorithm.



The new [Post-Quantum Encryption ↗︎](https://radar.cloudflare.com/post-quantum) page shows the share of customer origins supporting [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-support/#x25519mlkem768), derived from daily automated TLS scans of TLS 1.3-compatible origins. The scanner tests for algorithm support rather than the origin server's configured preference.

![Screenshot of the origin post-quantum support graph on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1040,format=webp/_astro/pq-origin-support.Bn5Dw_It.png)

A host test tool allows checking any publicly accessible website for post-quantum encryption compatibility. Enter a hostname and optional port to see whether the server negotiates a post-quantum key exchange algorithm.

![Screenshot of the post-quantum host test tool on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2372,height=566,format=webp/_astro/pq-host-test.dRqwoOvo.png)

#### Key Transparency

A new [Key Transparency ↗︎](https://radar.cloudflare.com/key-transparency) section displays the audit status of Key Transparency logs for end-to-end encrypted messaging services. The page launches with two monitored logs: WhatsApp and Facebook Messenger Transport.

Each log card shows the current status, last signed epoch, last verified epoch, and the root hash of the Auditable Key Directory tree. The data is also available through the [Key Transparency Auditor API](https://developers.cloudflare.com/key-transparency/api/).

![Screenshot of the Key Transparency dashboard on Radar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2454,height=1062,format=webp/_astro/key-transparency-dashboard.DNQgLsb0.png)

Learn more about these features in our [blog post ↗︎](https://blog.cloudflare.com/radar-origin-pq-key-transparency-aspa) and check out the [Post-Quantum Encryption ↗︎](https://radar.cloudflare.com/post-quantum) and [Key Transparency ↗︎](https://radar.cloudflare.com/key-transparency) pages to explore the data.

Feb 25, 2026

## [RPKI ASPA Deployment Insights on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-02-25-radar-aspa-insights/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes [Autonomous System Provider Authorization (ASPA) ↗︎](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/) deployment insights, providing visibility into the adoption and verification of ASPA objects across the global routing ecosystem.

#### New API endpoints

The new [`ASPA`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/) API provides the following endpoints:

  * [`/bgp/rpki/aspa/snapshot`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/) \- Retrieves current or historical ASPA objects.
  * [`/bgp/rpki/aspa/changes`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes/) \- Retrieves changes to ASPA objects over time.
  * [`/bgp/rpki/aspa/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries/) \- Retrieves ASPA object counts over time as a timeseries.



#### New Radar widgets

The [global routing page ↗︎](https://radar.cloudflare.com/routing) now shows the ASPA deployment trend over time by counting daily ASPA objects.

![Screenshot of the ASPA deployment trend chart](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=876,format=webp/_astro/aspa-global-trend.CXGWGFL4.png)

The global routing page also displays the most recent ASPA objects, searchable by ASN or AS name.

![Screenshot of the ASPA objects table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1852,format=webp/_astro/aspa-global-table.vHUyNoTh.png)

On country and region routing pages, a new widget shows the ASPA deployment rate for ASNs registered in the selected country or region.

![Screenshot of the ASPA deployment trent chart for Germany](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=876,format=webp/_astro/aspa-germany-trend.DIH6CESC.png)

On AS routing pages, the connectivity table now includes checkmarks for ASPA-verified upstreams. All ASPA upstreams are listed in a dedicated table, and a timeline shows ASPA changes at daily granularity.

![Screenshot of the ASPA changes timeline on an AS routing page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2198,height=1212,format=webp/_astro/aspa-asn-timeline.Bnl6upJs.png)

Check out the [Radar routing page ↗︎](https://radar.cloudflare.com/routing) to explore the data.

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/consumer-services/2/)

[Next →](https://developers.cloudflare.com/changelog/product-group/consumer-services/2/)

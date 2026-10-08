---
url: https://developers.cloudflare.com/dns/internal-dns/
title: Internal DNS \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:57.712669+00:00
---

# Internal DNS · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/internal-dns/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /Internal DNS



# Internal DNS

Last updated Jul 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/internal-dns/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArchitecture overviewResourcesRelated products

Simplify private network management with Cloudflare DNS for your internal resources.

Enterprise-only

Manage DNS records that should only be accessible within your private network. Internal DNS [zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/) and [views](https://developers.cloudflare.com/dns/internal-dns/dns-views/) pair up with [Gateway resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) so that you can control how a DNS query should be responded to according to query context, such as query source IP.

Internal DNS is included with [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) for Enterprise customers. There is no additional SKU or separate subscription required.

## Architecture overview

You can use different [connectivity options](https://developers.cloudflare.com/dns/internal-dns/connectivity/) to on-ramp your traffic to Cloudflare. Then, Cloudflare Gateway resolver acts as an interface between the DNS client and internal DNS zones.

Internal DNS zones do not get assigned Cloudflare nameservers and can only be queried via Cloudflare Gateway resolver.
    
    
    flowchart LR
            accTitle: Internal DNS query overview
            accDescr: Diagram comparing internal DNS query with public DNS
            A[Client]
            subgraph Cloudflare account
            subgraph Gateway
    				B[Default 1.1.1.1 resolver]
            X[Resolver policy selecting an internal DNS view]
            end
            subgraph Authoritative DNS
            Y[(Public DNS)]
    				Z[(Internal DNS)]
            end
            end
    
    			  C[Public resolver]
    
            B --Query--> Y
            X --Query + View ID--> Z
            A --Query--> B
    				A --Query--> X
    				C --Query--> Y
    

Internal DNS zones are grouped into DNS views, which are selected by the resolver policy you define. Views are usually logical groupings relevant to your organization, such as different geographical locations.
    
    
    flowchart LR
            accTitle: Internal DNS views and zones
            accDescr: Diagram exemplifying Internal DNS views and zones relationship
            subgraph Internal DNS
            subgraph View 111 - London
            Y[Zone 600 <br /> example.local]
    				Z[Zone 601 <br /> local]
            end
            subgraph View 110 - San Francisco
            X[Zone 101 <br /> example.com]
    				B[Zone 100 <br /> example.local]
    				S[Zone 102 <br /> com]
            end
    				W[Zone 701 <br /> net]
    				end
    

Internal DNS zones contain the [DNS records](https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/) that should be used to resolve an internal DNS query. Also, if no internal record is found within a matching internal zone, Cloudflare will check if the matching internal zone is [referencing another internal zone](https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/).
    
    
    flowchart LR
            accTitle: Internal DNS zones and internal records
            accDescr: Diagram exemplifying Internal DNS zones and records relationship
            subgraph View 111 - London
    				subgraph Zone 601 - local
    				S["@ A 192.0.2.10"]
    				T["ghi.example A 192.0.2.15"]
    				end
            subgraph Zone 600 - example.local
    				X["@ A 192.0.2.1"]
    				Y["abc A 192.0.2.6"]
    				Z["def A 192.0.2.9"]
    				end
    				end
    

In this example, a query for `ghi.example.local` routed to view ID 111 would go to zone 600, which presents the longest matching zone name (`example.local`). Zone 600 does not contain a record for `ghi` but, if it is referencing zone 601, Cloudflare will then look for the queried record within the reference zone.

## Resources

  * [Get started](https://developers.cloudflare.com/dns/internal-dns/get-started/)
  * [Internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/)
  * [Manage DNS views](https://developers.cloudflare.com/dns/internal-dns/dns-views/)
  * [Connect to Gateway resolver](https://developers.cloudflare.com/dns/internal-dns/connectivity/)
  * [Analytics and logs](https://developers.cloudflare.com/dns/internal-dns/analytics/)



## Related products

[Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Set up policies to inspect DNS, Network, HTTP, and Egress traffic.

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Improve security and performance for your entire corporate networking, reducing cost and operation complexity.

[PreviousTroubleshooting](https://developers.cloudflare.com/dns/private-origins/troubleshooting/)[NextGet started](https://developers.cloudflare.com/dns/internal-dns/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/internal-dns/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

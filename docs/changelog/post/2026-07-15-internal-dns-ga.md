---
url: https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/
title: Internal DNS is now generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.277687+00:00
---

# Internal DNS is now generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 15, 2026

## Internal DNS is now generally available

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-15-internal-dns-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/) is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.

#### Why it matters

  * **Consolidate DNS operations.** Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.
  * **Simplify split-horizon DNS.** Internal and external resolution are defined as separate [views](https://developers.cloudflare.com/dns/internal-dns/dns-views/) over shared zones, managed from a single control plane — so there is no drift to chase down.
  * **Extend Zero Trust to DNS.** Resolver policies decide which users and devices resolve against which view, enforced by the same [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) that already governs the rest of your traffic.



Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.
    
    
    POST /zones
    {
      "account": {
        "id": "<ACCOUNT_ID>"
      },
      "name": "corp.internal",
      "type": "internal"
    }

Internal DNS is included with [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) for Enterprise customers. To get started, refer to the [Internal DNS documentation](https://developers.cloudflare.com/dns/internal-dns/).

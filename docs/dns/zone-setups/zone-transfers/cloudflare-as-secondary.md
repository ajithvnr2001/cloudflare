---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/
title: Cloudflare as Secondary \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.864560+00:00
---

# Cloudflare as Secondary · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)
  5. /Cloudflare as Secondary



# Cloudflare as Secondary

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow toAvailability

With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider.

When you make edits in your primary DNS provider, those DNS records will be transferred from your primary DNS provider to Cloudflare via zone transfer using [AXFR ↗︎](https://datatracker.ietf.org/doc/html/rfc5936) or [IXFR ↗︎](https://datatracker.ietf.org/doc/html/rfc1995).
    
    
    flowchart LR
    accTitle: Cloudflare as Secondary DNS
    A((Zone Admin)) --DNS record <br /> management--> B[Primary DNS <br /> provider]
    B --Zone transfer--> C[Cloudflare <br /> DNS]
    B & C <--DNS lookups--> D[Resolver] <--DNS lookups--> E((User))
    

## How to

  * [Set up incoming zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/)
  * Proxy traffic through Cloudflare with [Secondary DNS Override](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/)



## Availability

Secondary DNS is only available to Enterprise customers. For more details on activation and pricing, contact your account team.

[PreviousRecords transfer](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/)[NextSetup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/cloudflare-as-secondary/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

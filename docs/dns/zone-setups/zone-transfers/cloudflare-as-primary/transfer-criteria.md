---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/
title: Records transfer \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.822516+00:00
---

# Records transfer · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)

  4. /[Cloudflare as Primary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/)
  5. /Records transfer



# Records transfer

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProxied recordsDNS-only CNAME recordsRecords that are not transferred

Consider the sections below to understand the expected behaviors, depending on DNS record type and proxied status.

## Proxied records

For each [proxied DNS record](https://developers.cloudflare.com/dns/proxy-status/) in your zone, Cloudflare will transfer out two `A` and two `AAAA` records.

These records correspond to the [Cloudflare IP addresses ↗︎](https://www.cloudflare.com/ips) used for proxying traffic.

## DNS-only CNAME records

As explained in [DNS record types](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#cname), Cloudflare uses a process called [CNAME flattening](https://developers.cloudflare.com/dns/cname-flattening/) to return the final IP address instead of the CNAME target. CNAME flattening improves performance and is also what allows you to set a CNAME record on the zone apex.

Depending on the [settings](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/) you have, when you use DNS-only CNAME records with outgoing zone transfers, you can expect the following:

  * For DNS-only CNAME records on the zone apex, Cloudflare will always transfer out the flattened IP addresses.
  * For DNS-only CNAME records on subdomains, Cloudflare will only transfer out flattened IP addresses if the setting [**CNAME flattening for all CNAME records**](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records) is enabled.



Per-record CNAME flattening

For records using [per-record CNAME flattening](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/#per-record) (meaning **CNAME flattening for all CNAME records** is disabled), Cloudflare will transfer out the CNAME, not the flattened IP address.

## Records that are not transferred

The following records are not transferred out when you use Cloudflare as primary:

  * [CAA records](https://developers.cloudflare.com/ssl/edge-certificates/caa-records/)
  * TXT records used for TLS certificate validation
  * DNS-only [Load Balancing](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/) records



Note

Proxied Load Balancing records are transferred as explained in Proxied records.

[PreviousDNSSEC options](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/)[NextAbout](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

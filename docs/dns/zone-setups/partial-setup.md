---
url: https://developers.cloudflare.com/dns/zone-setups/partial-setup/
title: CNAME setup (Partial) \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:02.930152+00:00
---

# CNAME setup (Partial) · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/partial-setup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)
  4. /CNAME setup (Partial)



# CNAME setup (Partial)

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/partial-setup/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow toAvailabilityReference DNS resolution CNAME flattening DDoS protection Domain ownership

A CNAME setup (also known as partial setup) allows you to use [Cloudflare's reverse proxy](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/) while maintaining your primary and authoritative DNS provider.

Use this option to proxy only individual subdomains through Cloudflare when you cannot change your authoritative DNS provider. You will be able to create A, AAAA, and CNAME records, which are the DNS record types that can be [proxied](https://developers.cloudflare.com/dns/proxy-status/).

Availability

A CNAME setup (partial) is only available to customers on a Business or Enterprise plan. Partial setups are not supported on Cloudflare Registrar domains.

Once you are on a CNAME setup (partial), the actual resolution of your records to Cloudflare depends on CNAME records [added at your authoritative DNS provider](https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/#3-add-dns-records). Check your authoritative DNS provider to know which records are pointing to `{your-hostname}.cdn.cloudflare.net`.

## How to

  * [Set up a partial zone (CNAME setup)](https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/)
  * [Convert a CNAME setup (partial) to a primary setup (full)](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/)
  * [Convert a CNAME setup (partial) to a secondary setup](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-secondary/)
  * [Create DNS records of other types](https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/#other-record-types)



## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | No | Yes | Yes  
  
## Reference

### DNS resolution

When you have a partial zone ([CNAME setup](https://developers.cloudflare.com/dns/zone-setups/partial-setup/)), Cloudflare resolves [DNS records differently](https://developers.cloudflare.com/dns/zone-setups/partial-setup/dns-resolution/) than for primary zones (full setup).

### CNAME flattening

A CNAME setup (partial) requires the proxied hostname to be pointed to Cloudflare via a CNAME record. Since [CNAME records are not allowed on the zone apex ↗︎](https://datatracker.ietf.org/doc/html/rfc1912#section-2.4) (`example.com`), you can only proxy your zone apex to Cloudflare if your authoritative DNS provider supports [CNAME Flattening ↗︎](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/).

If your authoritative DNS provider does not support CNAME Flattening, redirect its traffic — for example, with an `.htaccess` file — to a subdomain proxied to Cloudflare. Alternatively, you can use [static IPs or BYOIPs](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses).

### DDoS protection

[DDoS protection](https://developers.cloudflare.com/ddos-protection/) for attacks against DNS infrastructure is only available for domains on [primary setup (full)](https://developers.cloudflare.com/dns/zone-setups/full-setup/). Domains on the CNAME setup (partial) are not using Cloudflare authoritative nameservers.

### Domain ownership

Enterprise customers can use [zone holds](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/) to prevent other teams in the organization from adding zones that are already active in another Cloudflare account. For CNAME setups (partial), if the same zone is added to different accounts, the last account to complete the setup will gain ownership.

[PreviousTroubleshooting](https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/)[NextSetup](https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/partial-setup/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

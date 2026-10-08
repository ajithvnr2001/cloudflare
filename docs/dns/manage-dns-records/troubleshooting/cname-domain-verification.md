---
url: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/
title: Cannot verify a domain with CNAME \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:59.689497+00:00
---

# Cannot verify a domain with CNAME · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)

  4. /Troubleshooting
  5. /Verify a domain with CNAME



# Verify a domain with CNAME

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCausesSolution

When configuring services from external providers - such as email services, for example - it is possible that they require you to verify your domain by placing a CNAME record at your zone, similar to the following:
    
    
    <value>._domainkey.example.com CNAME <hostname>.<service provider domain>

Consider the sections below if this is not working correctly for you.

## Causes

You may find issues if you have one of the following:

  * The CNAME record you created for domain verification is set to [**Proxied**](https://developers.cloudflare.com/dns/proxy-status/).
  * The CNAME record is correctly set to DNS only (not proxied) but, in your [zone settings ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/settings), [**CNAME flattening for all CNAME records**](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records) is on.
  * The CNAME record is correctly set to DNS only (not proxied) but CNAME flattening is set [for that record specifically](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/#per-record).
  * An [NS record ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/) exists, causing a different DNS provider to be authoritative for the subdomain.



## Solution

Make sure that:

  * In your zone DNS settings: [**CNAME flattening for all CNAME records**](https://developers.cloudflare.com/dns/cname-flattening/) is turned off.
  * On the DNS records table: you have filled in the CNAME record fields correctly, proxy status is set to **DNS only** , and **Flatten** is turned off.
  * You have the correct NS configuration, and either: 
    * Make sure that the CNAME record is set as expected with the DNS provider that the NS record points to.
    * Review your configuration for other DNS records that may be affected by the NS record. Once you are aware of any consequences or have made any necessary adjustments, remove the NS record so that the CNAME is resolved to the target you configured on Cloudflare.



[PreviousExposed IP addresses](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/)[NextNS records already exist](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/manage-dns-records/troubleshooting/cname-domain-verification.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

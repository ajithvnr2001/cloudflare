---
url: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/
title: Existing NS records block new record creation \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:59.841284+00:00
---

# Existing NS records block new record creation · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)

  4. /Troubleshooting
  5. /NS records already exist



# NS records already exist

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCausesSolution

As you try to create a new DNS record, Cloudflare displays the following error:
    
    
    NS records with that host already exist. (Code:81056)

## Causes

When a child domain (`blog.example.com`) of your domain (`example.com`) has been set up as a separate [subdomain zone](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/), corresponding `NS` records must have been placed within the parent zone.

When you are managing DNS records for the parent zone (in this example, `example.com`), you cannot create IP address resolution records (`A`, `AAAA`, or `CNAME`) with a name that specifies the same subdomain that already exists as a separate subdomain zone.

Type | Name | Content | TTL  
---|---|---|---  
`A` | `blog` | `192.0.2.0` | `Auto`  
  
## Solution

Before creating such records, remove any `NS` records with the same name.

Important

This action might be reverting an existing subdomain setup and may incur in downtime. Refer to [Rollback subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/) for more guidance.

[PreviousVerify a domain with CNAME](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/)[NextStale response](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/manage-dns-records/troubleshooting/existing-ns-record.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/
title: Enable DNSSEC - subdomain setup \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:03.641840+00:00
---

# Enable DNSSEC - subdomain setup · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[Subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/)
  5. /Enable DNSSEC



# Enable DNSSEC

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequirementsSetup

As opposed to the [normal process](https://developers.cloudflare.com/dns/dnssec/) for enabling DNSSEC, DNSSEC with a subdomain setup requires a few additional steps.

## Requirements

To use DNSSEC for a subdomain setup, DNSSEC must be enabled on the parent zone. After enabling DNSSEC on the parent zone, you should wait the minimum TTL value (specified in the [SOA record ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/) of the parent zone) to ensure DNS resolvers provide the same DNS query responses.

## Setup

  1. [Create](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/#how-to) the child zone.

  2. Make sure the child zone is [active](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) on Cloudflare and that DNS resolution is working properly for your subdomain.

  3. [Enable DNSSEC](https://developers.cloudflare.com/dns/dnssec/) for the child zone and save the information provided within the DS record output.

  4. On the [**DNS Records** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/records) page of the parent zone, [add the DS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) from the previous step.

![Screenshot showing how to add a DS record within Cloudflare](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2066,height=1040,format=webp/_astro/ds-record-example.eCudbis6.png)
  5. Add an A record to the child zone to validate DNS resolution.

  6. Wait two to six hours. Then, [test the A record](https://developers.cloudflare.com/dns/dnssec/troubleshooting/#test-dnssec-with-dig) added in the previous step using multiple DNS resolvers with DNSSEC validation (`1.1.1.1`, `8.8.8.8`, and `9.9.9.9`). For example, if the A record is for `test.child.example.com`: `dig test.child.example.com +dnssec @1.1.1.1`.




[PreviousParent zone on partial setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-partial/)[NextMigrate to new account](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/move-to-new-account/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/subdomain-setup/dnssec.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

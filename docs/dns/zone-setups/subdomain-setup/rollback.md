---
url: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/
title: Rollback subdomain setup \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:03.687000+00:00
---

# Rollback subdomain setup · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[Subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/)
  5. /Rollback



# Rollback

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginSteps

Refer to the following process to understand how you can rollback a [subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/) and recreate the corresponding subdomain DNS records in an existing parent zone within Cloudflare.

## Before you begin

  * This guide assumes both your child domain (`blog.example.com`) and its parent domain (`example.com`) are in Cloudflare.
  * In the child zone, review and [export](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/#export-records) the DNS records.



Important

This process may incur in downtime, as it is not possible to add address records (A/AAAA) while still having [corresponding NS records at the same name](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/) within the parent zone.

## Steps

  1. (Optional) In the parent zone, migrate over any settings - [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/), [Rules](https://developers.cloudflare.com/rules/), [Workers](https://developers.cloudflare.com/workers/), and more - that might be needed for the child domain.
  2. (Optional) If necessary, [order an advanced SSL certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) that covers the child domain and any deeper subdomains.
  3. In the parent zone, go to the [**DNS Records** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/dns/records) page.
  4. Delete one of the `NS` records defined for the child domain.
  5. Edit the remaining `NS` record to create the subdomain address record.
  6. [Import](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/#import-records) the records you had obtained before you began.



[PreviousMigrate to new account](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/move-to-new-account/)[NextRecords quick scan](https://developers.cloudflare.com/dns/zone-setups/reference/dns-quick-scan/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/subdomain-setup/rollback.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/
title: Dynamically update DNS records \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:58.886213+00:00
---

# Dynamically update DNS records · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)

  4. /How to
  5. /Dynamically update DNS records



# Dynamically update DNS records

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCloudflare APIddclient

Most Internet service providers and some hosting providers dynamically update their customer's IP addresses. If this situation applies to you, you need an automated solution to dynamically update your DNS records in Cloudflare.

## Cloudflare API

Create a script to monitor IP address changes and then have that script push changes to the [Cloudflare API](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/update/).

## ddclient

[ddclient ↗︎](https://github.com/ddclient/ddclient) is a third-party Perl client used to update dynamic DNS entries for accounts on various DNS providers.

[PreviousBatch record changes](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/)[NextRound-robin DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

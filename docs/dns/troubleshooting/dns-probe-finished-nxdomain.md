---
url: https://developers.cloudflare.com/dns/troubleshooting/dns-probe-finished-nxdomain/
title: Fix DNS_PROBE_FINISHED_NXDOMAIN \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:01.950083+00:00
---

# Fix DNS_PROBE_FINISHED_NXDOMAIN · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/troubleshooting/dns-probe-finished-nxdomain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Troubleshooting](https://developers.cloudflare.com/dns/troubleshooting/)
  4. /DNS_PROBE_FINISHED_NXDOMAIN



# DNS_PROBE_FINISHED_NXDOMAIN

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/troubleshooting/dns-probe-finished-nxdomain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundPotential solutions

If you or your visitors experience `DNS_PROBE_FINISHED_NXDOMAIN` errors after you [activate your domain on Cloudflare](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/), review your DNS records in Cloudflare.

Note

If your domain is added to Cloudflare by a hosting partner, manage your DNS records via the hosting partner.

## Background

`DNS_PROBE_FINISHED_NXDOMAIN` indicates that the DNS lookup completed and the result was that the domain does not exist. `DNS_PROBE_FINISHED` means that the DNS probe ran to completion and `NXDOMAIN` stands for non-existent domain. Together, these messages mean that the DNS resolver determined the requested domain has no associated [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/).

Though visitors sometimes encounter this error — or similarly worded messages from Safari, Edge, or Firefox — because of network or local DNS issues, it might point to an issue with your DNS records in Cloudflare.

## Potential solutions

If you experience `DNS_PROBE_FINISHED_NXDOMAIN` errors with a newly activated domain, review your DNS settings in the Cloudflare dashboard.

Check your expected apex domain (`example.com`) and any active subdomains (`www.example.com` or `blog.example.com`). If they do not resolve correctly, you may need to [add a record on the zone apex](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-zone-apex/) or a [subdomain record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-subdomain/) in Cloudflare DNS.

If you have the correct records set up, make sure those records are also pointing to the correct origin IP address.

After making changes to your DNS records, you may need to wait a few minutes for those changes to take effect.

Note

For additional troubleshooting help, refer to the [Community troubleshooting guide ↗︎](https://community.cloudflare.com/t/community-tip-fixing-the-dns-probe-finished-nxdomain-error/42818).

[PreviousGeneral DNS issues](https://developers.cloudflare.com/dns/troubleshooting/dns-issues/)[NextDNS_PROBE_POSSIBLE](https://developers.cloudflare.com/dns/troubleshooting/dns-probe-possible/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/troubleshooting/dns-probe-finished-nxdomain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

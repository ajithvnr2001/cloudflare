---
url: https://developers.cloudflare.com/dns/troubleshooting/dns-probe-possible/
title: Fix DNS_PROBE_POSSIBLE error \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:01.988106+00:00
---

# Fix DNS_PROBE_POSSIBLE error · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/troubleshooting/dns-probe-possible/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Troubleshooting](https://developers.cloudflare.com/dns/troubleshooting/)
  4. /DNS_PROBE_POSSIBLE



# DNS_PROBE_POSSIBLE

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/troubleshooting/dns-probe-possible/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundPotential solutions

If you or your visitors experience `DNS_PROBE_POSSIBLE` errors after you [activate your domain on Cloudflare](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/), review your DNS records in Cloudflare.

Note

If your domain is added to Cloudflare by a hosting partner, manage your DNS records via the hosting partner.

## Background

`DNS_PROBE_POSSIBLE` means that the resolver could not find [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/) for the requested hostname.

Though visitors sometimes encounter this error — or similarly worded messages from Safari, Edge, or Firefox — because of network or local DNS issues, it might point to an issue with your DNS records in Cloudflare.

## Potential solutions

If you experience `DNS_PROBE_POSSIBLE` errors with a newly activated domain, review your DNS settings in the Cloudflare dashboard.

Check your expected apex domain (`example.com`) and any active subdomains (`www.example.com` or `blog.example.com`). If they do not resolve correctly, you may need to [add a record on the zone apex](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-zone-apex/) or a [subdomain record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-subdomain/) in Cloudflare DNS.

If you have the correct records set up, make sure those records are also pointing to the correct origin IP address.

After making changes to your DNS records, you may need to wait a few minutes for those changes to take effect.

[PreviousDNS_PROBE_FINISHED_NXDOMAIN](https://developers.cloudflare.com/dns/troubleshooting/dns-probe-finished-nxdomain/)[NextEmail issues](https://developers.cloudflare.com/dns/troubleshooting/email-issues/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/troubleshooting/dns-probe-possible.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

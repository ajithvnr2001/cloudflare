---
url: https://developers.cloudflare.com/dns/troubleshooting/dns-debug-endpoints/
title: Available debug endpoints \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:01.678464+00:00
---

# Available debug endpoints · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/troubleshooting/dns-debug-endpoints/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Troubleshooting](https://developers.cloudflare.com/dns/troubleshooting/)
  4. /Debug endpoints



# Available debug endpoints

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/troubleshooting/dns-debug-endpoints/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet your public IP addressFind your connected data centerCheck the DNS software versionGet your IP, ASN, and country code

The following debug endpoints are available via `dig` or other DNS query tools.

Note

For all commands, replace `alex.ns.cloudflare.com` with your Cloudflare-assigned nameservers.

## Get your public IP address
    
    
    dig @alex.ns.cloudflare.com chaos txt myip.cloudflare +short

This command returns your public IP address, meaning the IP address that Cloudflare receives the DNS query from. This is useful for debugging when you need to know your own IP.

## Find your connected data center
    
    
    dig @alex.ns.cloudflare.com chaos txt id.server +short

This command returns the Cloudflare data center you are connecting to, for DNS queries sent from where you execute this command.

## Check the DNS software version
    
    
    dig @alex.ns.cloudflare.com chaos txt version.bind +short

This command returns the version of Cloudflare's authoritative DNS software that is running on the data center you are connected to. Usually, the same version is present on all Cloudflare data centers. However, since Cloudflare performs staged releases, different versions can exist on different data centers.

## Get your IP, ASN, and country code
    
    
    dig @alex.ns.cloudflare.com txt whoami.cloudflare.net +short

This command returns your public IP (same as the first command), your ASN, and the associated country code, all indicating where you are sending the query from.

[PreviousEmail issues](https://developers.cloudflare.com/dns/troubleshooting/email-issues/)[NextFAQ](https://developers.cloudflare.com/dns/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/troubleshooting/dns-debug-endpoints.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

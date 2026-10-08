---
url: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/protect-origin-ip/
title: Protect origin IP address \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:51.497192+00:00
---

# Protect origin IP address · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/protect-origin-ip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Prevent Ddos Attacks

  4. /[Advanced DDoS protection](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/)
  5. /Protect origin IP address



# Protect origin IP address

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/protect-origin-ip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRotate IP addressesReview unproxied DNS recordsConceal unproxied DNS recordsEvaluate mail infrastructure

Though Cloudflare automatically hides your origin server IP address when you [proxy your DNS records](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/), there are other ways to discover an IP address.

To prevent attackers from discovering your origin's IP address, review the following suggestions.

## Rotate IP addresses

DNS records are in the public domain, meaning that - even though your IP addresses are hidden once you proxy your DNS records - someone could uncover historical records of your addresses.

For additional security, you could rotate the IP addresses of your origin server, which would also require [updating your DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records) within Cloudflare.

## Review unproxied DNS records

Unproxied DNS records - also known as **DNS-only** records - can sometimes contain origin IP information, especially those used for FTP or SSH.

Review these records to make sure they do not contain origin IP information or use [Cloudflare Spectrum](https://developers.cloudflare.com/spectrum/) to proxy these records.

## Conceal unproxied DNS records

If you need to have **DNS-only** records that contain origin IP information, use non-standard names for these records. This action makes dictionary scans of your DNS less likely to expose your origin IP address.

For example, instead of `ftp.example.com`, you could use `827450184590183489.example.com` or `cloudflare-docs-are-great.example.com`.

## Evaluate mail infrastructure

If possible, do not host a mail service on the same server as the web resource you want to protect, since emails sent to non-existent addresses get bounced back to the attacker and reveal the mail server IP address.

Cloudflare recommends using non-contiguous IPs from different IP ranges.

[PreviousOverview](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/)[NextOptimize caching](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/optimize-caching/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/prevent-ddos-attacks/advanced/protect-origin-ip.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

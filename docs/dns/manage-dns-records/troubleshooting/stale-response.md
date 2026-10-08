---
url: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/
title: Stale response for upstream DNS resolution \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:00.057982+00:00
---

# Stale response for upstream DNS resolution · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)

  4. /Troubleshooting
  5. /Stale response



# Stale response for upstream DNS resolution

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCauseSolutions

In one of the scenarios below, you notice that stale DNS responses are used. Depending on the scenario and other aspects of your configuration, this can cause wrong content or no content to be returned.

  * A proxied CNAME record ([flattened by default](https://developers.cloudflare.com/dns/cname-flattening/)).
  * A DNS-only CNAME record that has flattening turned on. This can happen either via the specific record configuration or as a consequence of the [zone settings](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/).
  * A [Workers](https://developers.cloudflare.com/workers/) script making a subrequest to an external hostname1.



## Cause

In the event that an upstream DNS server takes too long to respond, or the upstream returns a SERVFAIL, Cloudflare will use the expired DNS response from the cache and then attempt to update that cache asynchronously.

## Solutions

  * If possible, temporarily replace the proxied CNAME with a proxied A record. This may not always be possible, especially if the upstream target is a load balancer or if it returns dynamic responses.

  * Report the issues to the zone owner or DNS provider for the upstream target that is unresponsive.

  * You can also raise the issue through the DNS Operations Analysis and Research Center (DNS OARC). Consider its [chat platform ↗︎](https://www.dns-oarc.net/oarc/services/chat) or [email lists ↗︎](https://www.dns-oarc.net/oarc/lists).




## Footnotes

  1. A hostname that is not using Cloudflare as its [authoritative DNS provider](https://developers.cloudflare.com/dns/concepts/#authoritative-dns). ↩




[PreviousNS records already exist](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/)[NextOverview](https://developers.cloudflare.com/dns/proxy-status/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/manage-dns-records/troubleshooting/stale-response.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

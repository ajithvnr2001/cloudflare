---
url: https://developers.cloudflare.com/dns/internal-dns/internal-zones/
title: Internal zones \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:58.134691+00:00
---

# Internal zones · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/internal-dns/internal-zones/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[Internal DNS](https://developers.cloudflare.com/dns/internal-dns/)
  4. /Internal zones



# Internal zones

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/internal-dns/internal-zones/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewResources

Internal DNS zones are groupings of internal DNS records. While [public DNS records](https://developers.cloudflare.com/dns/manage-dns-records/) contain information about resources that you want to make available to the public Internet, [internal DNS records](https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/) allow you to manage resources that should only be available within your private network.

Refer to [Manage internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/) for a full list of configuration conditions and step-by-step instructions.

Internal DNS zones do not get assigned Cloudflare nameservers and can only be queried via [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) when linked to a [DNS view](https://developers.cloudflare.com/dns/internal-dns/dns-views/). The Gateway configuration must exist within the same Cloudflare account where the internal zone exists.

## Resources

  * [Manage internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/)
  * [Manage internal DNS records](https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/)
  * [Reference zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/)



[PreviousGet started](https://developers.cloudflare.com/dns/internal-dns/get-started/)[NextManage internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/internal-dns/internal-zones/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

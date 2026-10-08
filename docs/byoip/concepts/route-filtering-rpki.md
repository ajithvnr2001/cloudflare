---
url: https://developers.cloudflare.com/byoip/concepts/route-filtering-rpki/
title: Route filtering and RPKI \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.930484+00:00
---

# Route filtering and RPKI · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/concepts/route-filtering-rpki/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Concepts
  4. /Route filtering and RPKI



# Route filtering and RPKI

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/concepts/route-filtering-rpki/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Network operators rely on [IRR records](https://developers.cloudflare.com/byoip/concepts/irr-entries/) to determine which autonomous systems (ASNs) are authorized to announce specific IP prefixes. Based on these records, operators configure filtering policies on their routers to block unauthorized announcements — a practice known as route filtering.

However, IRR records alone are not cryptographically verified, which means they can be inaccurate or outdated. Resource Public Key Infrastructure (RPKI) addresses this gap by adding cryptographic validation. With RPKI, the association between an IP prefix and its authorized ASN is signed and verifiable, allowing network operators to confirm that a route announcement is legitimate before accepting it.

When you register your prefix with one of the five Regional Internet Registries (RIRs)1, you can create a Route Origin Authorization (ROA) — a cryptographically signed object that declares which ASN is authorized to originate your prefix. ROAs are publicly verifiable, and you can check your prefixes using [Cloudflare's RPKI Portal ↗︎](https://rpki.cloudflare.com/?view=validator) or other sources such as [Routinator ↗︎](https://rpki-validator.ripe.net/ui/).

## Footnotes

  1. AFRINIC, APNIC, ARIN, LACNIC, and RIPE. ↩




[PreviousManage IRR entries](https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/)[NextLetter of Agency](https://developers.cloudflare.com/byoip/concepts/loa/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/concepts/route-filtering-rpki.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

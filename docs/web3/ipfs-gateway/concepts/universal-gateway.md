---
url: https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/
title: Universal Path gateway \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:55.661920+00:00
---

# Universal Path gateway · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /…

[IPFS Gateway](https://developers.cloudflare.com/web3/ipfs-gateway/)

  4. /[Concepts](https://developers.cloudflare.com/web3/ipfs-gateway/concepts/)
  5. /Universal Path gateway



# Universal Path gateway

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/ipfs-gateway/concepts/universal-gateway/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow is it used with Cloudflare?

A Universal Path gateway is a gateway without a DNSLink record. It allows users to access any content hosted on the IPFS network by specifying a CID or IPNS path in the URL.

This differs from a [restricted gateway](https://developers.cloudflare.com/web3/ipfs-gateway/concepts/dnslink/), which limits the gateway to a single piece of content (a specific CID or IPNS hostname).

## How is it used with Cloudflare?

You can set up a Universal Path gateway the same way you [create any gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/).

Because a Universal Path gateway is open by default, you may want to use the [gateway blocklist](https://developers.cloudflare.com/web3/how-to/manage-gateways/#update-blocklist) to prevent access to specific content. You can block one or more:

  * CIDs (`QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB`)
  * IPFS content paths (`/ipfs/QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme`)
  * IPNS content paths (`/ipns/example.com`)



Note

This feature is limited to specific plans. For more detail, refer to [Limits](https://developers.cloudflare.com/web3/reference/limits/).

[PreviousDNSLink gateways](https://developers.cloudflare.com/web3/ipfs-gateway/concepts/dnslink/)[NextOverview](https://developers.cloudflare.com/web3/ipfs-gateway/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/ipfs-gateway/concepts/universal-gateway.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

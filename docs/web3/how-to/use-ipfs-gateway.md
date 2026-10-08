---
url: https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/
title: Use IPFS gateway \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:55.373203+00:00
---

# Use IPFS gateway · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /[How to](https://developers.cloudflare.com/web3/how-to/)
  4. /Use IPFS gateway



# Use IPFS gateway

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRead from the network Gateway hostname Request pathWrite to the network

Once you have an IPFS gateway — meaning that you [create a new gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway) with a `target` of **IPFS** — you can get data from the IPFS network by using a URL.

## Read from the network

Every time you access a piece of content through Cloudflare's IPFS Gateway, you need a URL with two parts: the gateway hostname and the request path.

### Gateway hostname

Your gateway hostname will be the **Hostname** value you supplied when you [created the gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway).

### Request path

The request path will vary based on the type of content you are serving.

If a request path is `/ipfs/<CID_HASH>`, that tells the gateway that you want the content with the Content Identifier (CID) that immediately follows. Because the content is addressed by CID, the gateway's response is immutable and will never change. An example would be `https://cloudflare-ipfs.com/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/`, which is a mirror of Wikipedia and an immutable `/ipfs/` link.

If a request path is `/ipns/<DOMAIN>`, that tells the gateway that you want it to lookup the CID associated with a given domain in DNS and then serve whatever content corresponds to the CID it happens to find. Because DNS can change over time, so will the gateway's response. An example would be `https://cloudflare-ipfs.com/ipns/ipfs.tech/`, which is IPFS's marketing site and can be changed at any time by modifying the [DNSLink record](https://developers.cloudflare.com/web3/ipfs-gateway/concepts/dnslink/) associated with the `ipfs.tech` domain.

## Write to the network

Cloudflare's IPFS Gateway is currently limited to read-only access.

[PreviousUse Ethereum gateway](https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/)[NextCustomize Cloudflare settings](https://developers.cloudflare.com/web3/how-to/customize-cloudflare-settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/how-to/use-ipfs-gateway.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

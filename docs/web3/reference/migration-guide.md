---
url: https://developers.cloudflare.com/web3/reference/migration-guide/
title: Legacy gateway migration \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:56.389281+00:00
---

# Legacy gateway migration · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/reference/migration-guide/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /[Reference](https://developers.cloudflare.com/web3/reference/)
  4. /Legacy gateway migration



# Legacy gateway migration

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/reference/migration-guide/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMigration guide

As announced in [our blog post ↗︎](https://blog.cloudflare.com/ea-web3-gateways/), Cloudflare is deprecating legacy hostnames that point to our public gateway endpoints at `cloudflare-eth.com` and `cloudflare-ipfs.com`.

If you created a hostname pointing to these gateways during the [private beta ↗︎](https://blog.cloudflare.com/announcing-web3-gateways/), you should migrate to use our new Web3 gateways to avoid a disruption in service.

* * *

## Migration guide

The migration is a simple process.

First, create a [Cloudflare account](https://developers.cloudflare.com/fundamentals/account/create-account/).

Then create a new [Web3 custom gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway) with your existing hostname.

Alternatively, you could also create a [Web3 custom gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway) for a new hostname and then modify your application to use your newly created hostname ([IPFS](https://developers.cloudflare.com/web3/how-to/use-ipfs-gateway/) or [Ethereum](https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/)).

[PreviousGateway status](https://developers.cloudflare.com/web3/reference/gateway-status/)[NextLimits](https://developers.cloudflare.com/web3/reference/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/reference/migration-guide.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

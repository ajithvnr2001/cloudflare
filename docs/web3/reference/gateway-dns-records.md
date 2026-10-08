---
url: https://developers.cloudflare.com/web3/reference/gateway-dns-records/
title: Gateway DNS records \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:56.222194+00:00
---

# Gateway DNS records · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/reference/gateway-dns-records/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /[Reference](https://developers.cloudflare.com/web3/reference/)
  4. /Gateway DNS records



# Gateway DNS records

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/reference/gateway-dns-records/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExisting DNS records

Once you [create a gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway), Cloudflare automatically creates and adds records to your Cloudflare DNS so your gateway can receive and route traffic appropriately:

  * **Ethereum gateways** : Creates a [proxied](https://developers.cloudflare.com/dns/proxy-status/) `CNAME` record pointing your hostname to `ethereum.cloudflare.com`.
  * **IPFS gateways** : Creates a [proxied](https://developers.cloudflare.com/dns/proxy-status/) `CNAME` record pointing your hostname to `ipfs.cloudflare.com` and a `TXT` record with the value specified for its [DNSLink](https://developers.cloudflare.com/web3/ipfs-gateway/concepts/dnslink/#how-is-it-used-with-cloudflare).



These records cannot be edited within Cloudflare DNS. To make edits, you will have to [edit the gateway configuration](https://developers.cloudflare.com/web3/how-to/manage-gateways/#edit-a-gateway) itself.

## Existing DNS records

When you [create a gateway](https://developers.cloudflare.com/web3/how-to/manage-gateways/#create-a-gateway) using a hostname with pre-existing DNS records, Cloudflare automatically overwrites your existing records to make them apply to your Web3 gateway.

[PreviousOverview](https://developers.cloudflare.com/web3/reference/)[NextGateway status](https://developers.cloudflare.com/web3/reference/gateway-status/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/reference/gateway-dns-records.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

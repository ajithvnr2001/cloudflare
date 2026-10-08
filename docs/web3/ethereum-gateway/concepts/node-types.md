---
url: https://developers.cloudflare.com/web3/ethereum-gateway/concepts/node-types/
title: Node types \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:54.345389+00:00
---

# Node types · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/ethereum-gateway/concepts/node-types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /…

[Ethereum Gateway](https://developers.cloudflare.com/web3/ethereum-gateway/)

  4. /[Concepts](https://developers.cloudflare.com/web3/ethereum-gateway/concepts/)
  5. /Node types



# Node types

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/ethereum-gateway/concepts/node-types/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFull nodesLight nodesArchive nodesNodes at Cloudflare

Ethereum nodes are the computers that store blockchain data and process queries. There are three types, each with different trade-offs between storage requirements and query capabilities.

## Full nodes

Full nodes store the current state of the blockchain and validate new blocks as they are produced. Once fully synced with the network, a full node can answer queries about any current blockchain data. Full nodes do not retain every historical state — they can recalculate past states when needed, but this requires additional computation.

## Light nodes

Light nodes store only block headers (summaries of each block) rather than the full blockchain state. They can query the Ethereum network but rely on full nodes to provide and verify the underlying data. This makes them much smaller and faster to set up, but less self-sufficient.

## Archive nodes

Archive nodes are full nodes that also store every historical state of the blockchain. Because they keep this data readily available in local storage, they can answer queries about past states (such as "what was this account's balance at block 5,000,000?") much faster than a full node, which would need to recalculate that state.

## Nodes at Cloudflare

Cloudflare's Ethereum Gateway provides access to full and archive nodes.

The archive nodes serve requests for the following [RPC state methods ↗︎](https://ethereum.org/en/developers/docs/apis/json-rpc/#state_methods) when the block number parameter is before the most recent 128 blocks or the default block parameter is set to `earliest`:

  * [eth_getBalance ↗︎](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getbalance)
  * [eth_getCode ↗︎](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getcode)
  * [eth_getTransactionCount ↗︎](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactioncount)
  * [eth_getStorageAt ↗︎](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getstorageat)
  * [eth_call ↗︎](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_call)



[PreviousEthereum network](https://developers.cloudflare.com/web3/ethereum-gateway/concepts/ethereum/)[NextOverview](https://developers.cloudflare.com/web3/ethereum-gateway/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/ethereum-gateway/concepts/node-types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

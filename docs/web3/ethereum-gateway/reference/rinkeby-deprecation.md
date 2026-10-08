---
url: https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/
title: Rinkeby deprecation \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:54.677799+00:00
---

# Rinkeby deprecation · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /…

[Ethereum Gateway](https://developers.cloudflare.com/web3/ethereum-gateway/)

  4. /[Reference](https://developers.cloudflare.com/web3/ethereum-gateway/reference/)
  5. /Rinkeby deprecation



# Rinkeby deprecation

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMigration

Though Cloudflare's Ethereum Gateway launched with support for the Rinkeby testnet, Rinkeby did not run through [The Merge ↗︎](https://ethereum.org/en/upgrades/merge/) and - as a result - will no longer be a reliable staging environment for mainnet.

Cloudflare will be deprecating support for Rinkeby on January 30, 2023.

## Migration

To avoid any issues with your Web3 development or debugging, you should switch over to the [Sepolia testnet](https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/), which is fully supported with your Ethereum Gateway.

To migrate, you should update the endpoints you use when [reading from or writing to](https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/) the Ethereum network.

For example, you might have been using the previous endpoints to interact with your Ethereum Gateway.

Previous curlbash
    
    
    curl https://web3-trial.cloudflare-eth.com/v1/rinkeby \
    --header 'Content-Type: application/json' \
    --data '{
      "jsonrpc": "2.0",
      "method": "eth_getBlockByNumber",
      "params": ["0x2244", true],
      "id": 1
    }'

Previous JS Fetch APIjs
    
    
    await fetch(
      new Request('https://web3-trial.cloudflare-eth.com/v1/rinkeby', {
        method: 'POST',
        body: JSON.stringify({
          jsonrpc: '2.0',
          method: 'eth_getBlockByNumber',
          params: ['0x2244', true],
          id: 1,
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      })
    ).then(resp => {
      return resp.json();
    });

To migrate away from Rinkeby, change the end of your endpoint to use another testnet.

New curlbash
    
    
    curl https://web3-trial.cloudflare-eth.com/v1/sepolia \
    --header 'Content-Type: application/json' \
    --data '{
      "jsonrpc": "2.0",
      "method": "eth_getBlockByNumber",
      "params": ["0x2244", true],
      "id": 1
    }'

New JS Fetch APIjs
    
    
    await fetch(
      new Request('https://web3-trial.cloudflare-eth.com/v1/sepolia', {
        method: 'POST',
        body: JSON.stringify({
          jsonrpc: '2.0',
          method: 'eth_getBlockByNumber',
          params: ['0x2244', true],
          id: 1,
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      })
    ).then(resp => {
      return resp.json();
    });

[PreviousSupported networks](https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/)[NextKill Switches](https://developers.cloudflare.com/web3/ethereum-gateway/reference/kill-switches/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/ethereum-gateway/reference/rinkeby-deprecation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

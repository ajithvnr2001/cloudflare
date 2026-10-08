---
url: https://developers.cloudflare.com/workers/wrangler/commands/
title: Commands - Wrangler \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:06.174006+00:00
---

# Commands - Wrangler · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/commands/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Wrangler](https://developers.cloudflare.com/workers/wrangler/)
  4. /Commands



# Commands

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/commands/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWorkers commandsAll commandsHow to run Wrangler commands

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) offers a number of commands to manage your Cloudflare Workers.

## Workers commands

The core Wrangler commands for creating, developing, and deploying Workers are on the [Workers commands page](https://developers.cloudflare.com/workers/wrangler/commands/workers/). This includes `wrangler dev`, `wrangler deploy`, `wrangler versions`, and more.

## All commands

  * [Workers](https://developers.cloudflare.com/workers/wrangler/commands/workers/)
  * [General commands](https://developers.cloudflare.com/workers/wrangler/commands/general/)
  * [Artifacts](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/)
  * [Basin Pipelines](https://developers.cloudflare.com/workers/wrangler/commands/pipelines/)
  * [Browser](https://developers.cloudflare.com/workers/wrangler/commands/browser/)
  * [Certificates](https://developers.cloudflare.com/workers/wrangler/commands/certificates/)
  * [Containers](https://developers.cloudflare.com/workers/wrangler/commands/containers/)
  * [D1](https://developers.cloudflare.com/workers/wrangler/commands/d1/)
  * [Flagship](https://developers.cloudflare.com/workers/wrangler/commands/flagship/)
  * [Hyperdrive](https://developers.cloudflare.com/workers/wrangler/commands/hyperdrive/)
  * [KV](https://developers.cloudflare.com/workers/wrangler/commands/kv/)
  * [Pages](https://developers.cloudflare.com/workers/wrangler/commands/pages/)
  * [Queues](https://developers.cloudflare.com/workers/wrangler/commands/queues/)
  * [R2](https://developers.cloudflare.com/workers/wrangler/commands/r2/)
  * [Secrets Store](https://developers.cloudflare.com/workers/wrangler/commands/secrets-store/)
  * [Tunnel](https://developers.cloudflare.com/workers/wrangler/commands/tunnel/)
  * [Vectorize](https://developers.cloudflare.com/workers/wrangler/commands/vectorize/)
  * [VPC](https://developers.cloudflare.com/workers/wrangler/commands/vpc/)
  * [Workers for Platforms](https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/)
  * [Workflows](https://developers.cloudflare.com/workers/wrangler/commands/workflows/)



## How to run Wrangler commands
    
    
    wrangler <COMMAND> <SUBCOMMAND> [PARAMETERS] [OPTIONS]

Since Cloudflare recommends [installing Wrangler locally](https://developers.cloudflare.com/workers/wrangler/install-and-update/) in your project (rather than globally), the way to run Wrangler will depend on your specific setup and package manager.

npmyarnpnpm
    
    
    npx wrangler <COMMAND> <SUBCOMMAND> [PARAMETERS] [OPTIONS]
    
    
    yarn wrangler <COMMAND> <SUBCOMMAND> [PARAMETERS] [OPTIONS]
    
    
    pnpm wrangler <COMMAND> <SUBCOMMAND> [PARAMETERS] [OPTIONS]

You can add Wrangler commands that you use often as scripts in your project's `package.json` file:
    
    
    {
      ...
      "scripts": {
        "deploy": "wrangler deploy",
        "dev": "wrangler dev"
      }
      ...
    }

You can then run them using your package manager of choice:

npmyarnpnpm
    
    
    npm run deploy
    
    
    yarn run deploy
    
    
    pnpm run deploy

[PreviousAPI](https://developers.cloudflare.com/workers/wrangler/api/)[NextWorkers](https://developers.cloudflare.com/workers/wrangler/commands/workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/commands/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/
title: Workers for Platforms \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:09.883760+00:00
---

# Workers for Platforms · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Wrangler](https://developers.cloudflare.com/workers/wrangler/)

  4. /[Commands](https://developers.cloudflare.com/workers/wrangler/commands/)
  5. /Workers for Platforms



# Workers for Platforms

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler commands for managing Workers for Platforms [dispatch namespace](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace) using Wrangler.

## `dispatch-namespace list`

List all dispatch namespaces

npmyarnpnpm
    
    
    npx wrangler dispatch-namespace list
    
    
    yarn wrangler dispatch-namespace list
    
    
    pnpm wrangler dispatch-namespace list

Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `dispatch-namespace get`

Get information about a dispatch namespace

npmyarnpnpm
    
    
    npx wrangler dispatch-namespace get <NAME>
    
    
    yarn wrangler dispatch-namespace get <NAME>
    
    
    pnpm wrangler dispatch-namespace get <NAME>

  * `<NAME>``string` required

Name of the dispatch namespace




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `dispatch-namespace create`

Create a dispatch namespace

npmyarnpnpm
    
    
    npx wrangler dispatch-namespace create <NAME>
    
    
    yarn wrangler dispatch-namespace create <NAME>
    
    
    pnpm wrangler dispatch-namespace create <NAME>

  * `<NAME>``string` required

Name of the dispatch namespace




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `dispatch-namespace delete`

Delete a dispatch namespace

npmyarnpnpm
    
    
    npx wrangler dispatch-namespace delete <NAME>
    
    
    yarn wrangler dispatch-namespace delete <NAME>
    
    
    pnpm wrangler dispatch-namespace delete <NAME>

  * `<NAME>``string` required

Name of the dispatch namespace




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




Note

You must delete all user Workers in the dispatch namespace before it can be deleted.

## `dispatch-namespace rename`

Rename a dispatch namespace

npmyarnpnpm
    
    
    npx wrangler dispatch-namespace rename <OLDNAME> <NEWNAME>
    
    
    yarn wrangler dispatch-namespace rename <OLDNAME> <NEWNAME>
    
    
    pnpm wrangler dispatch-namespace rename <OLDNAME> <NEWNAME>

  * `<OLDNAME>``string` required

Name of the dispatch namespace

  * `<NEWNAME>``string` required

New name of the dispatch namespace




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




[PreviousVPC](https://developers.cloudflare.com/workers/wrangler/commands/vpc/)[NextWorkflows](https://developers.cloudflare.com/workers/wrangler/commands/workflows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/commands/workers-for-platforms.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

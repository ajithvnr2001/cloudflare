---
url: https://developers.cloudflare.com/artifacts/api/wrangler/
title: Wrangler commands \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:20.504979+00:00
---

# Wrangler commands · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/api/wrangler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /API
  4. /Wrangler commands



# Wrangler commands

Last updated May 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/api/wrangler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use `wrangler artifacts` commands to manage Artifacts namespaces, repositories, and repo-scoped tokens from the command line.

## `artifacts namespaces list`

List Artifacts namespaces

npmyarnpnpm
    
    
    npx wrangler artifacts namespaces list
    
    
    yarn wrangler artifacts namespaces list
    
    
    pnpm wrangler artifacts namespaces list

  * `--json``boolean` default: false

Return output as JSON




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




## `artifacts namespaces get`

Get an Artifacts namespace

npmyarnpnpm
    
    
    npx wrangler artifacts namespaces get <NAME>
    
    
    yarn wrangler artifacts namespaces get <NAME>
    
    
    pnpm wrangler artifacts namespaces get <NAME>

  * `<NAME>``string` required

The Artifacts namespace name

  * `--json``boolean` default: false

Return output as JSON




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




## `artifacts repos create`

Create an Artifacts repository

npmyarnpnpm
    
    
    npx wrangler artifacts repos create <NAME>
    
    
    yarn wrangler artifacts repos create <NAME>
    
    
    pnpm wrangler artifacts repos create <NAME>

  * `<NAME>``string` required

The Artifacts repository name

  * `--namespace``string` required

The Artifacts namespace name

  * `--description``string`

An optional description for the repository

  * `--default-branch``string`

The default branch for the repository

  * `--read-only``boolean`

Create the repository as read-only

  * `--json``boolean` default: false

Return output as JSON




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




## `artifacts repos list`

List Artifacts repositories in a namespace

npmyarnpnpm
    
    
    npx wrangler artifacts repos list
    
    
    yarn wrangler artifacts repos list
    
    
    pnpm wrangler artifacts repos list

  * `--namespace``string` required

The Artifacts namespace name

  * `--json``boolean` default: false

Return output as JSON




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




## `artifacts repos get`

Get an Artifacts repository

npmyarnpnpm
    
    
    npx wrangler artifacts repos get <NAME>
    
    
    yarn wrangler artifacts repos get <NAME>
    
    
    pnpm wrangler artifacts repos get <NAME>

  * `<NAME>``string` required

The Artifacts repository name

  * `--namespace``string` required

The Artifacts namespace name

  * `--json``boolean` default: false

Return output as JSON




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




## `artifacts repos delete`

Delete an Artifacts repository

npmyarnpnpm
    
    
    npx wrangler artifacts repos delete <NAME>
    
    
    yarn wrangler artifacts repos delete <NAME>
    
    
    pnpm wrangler artifacts repos delete <NAME>

  * `<NAME>``string` required

The Artifacts repository name

  * `--namespace``string` required

The Artifacts namespace name

  * `--force``boolean` alias: --ydefault: false

Skip confirmation

  * `--json``boolean` default: false

Return output as JSON




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




## `artifacts repos issue-token`

Issue a repo-scoped Artifacts token

npmyarnpnpm
    
    
    npx wrangler artifacts repos issue-token <REPO>
    
    
    yarn wrangler artifacts repos issue-token <REPO>
    
    
    pnpm wrangler artifacts repos issue-token <REPO>

  * `<REPO>``string` required

The Artifacts repository name

  * `--namespace``string` required

The Artifacts namespace name

  * `--scope``string`

The token scope

  * `--ttl``number`

The token TTL in seconds

  * `--json``boolean` default: false

Return output as JSON




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




[PreviousGit protocol](https://developers.cloudflare.com/artifacts/api/git-protocol/)[NextErrors](https://developers.cloudflare.com/artifacts/api/errors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/api/wrangler.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

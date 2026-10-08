---
url: https://developers.cloudflare.com/workers/wrangler/commands/workflows/
title: Workflows \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:10.164281+00:00
---

# Workflows · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/commands/workflows/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Wrangler](https://developers.cloudflare.com/workers/wrangler/)

  4. /[Commands](https://developers.cloudflare.com/workers/wrangler/commands/)
  5. /Workflows



# Workflows

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/commands/workflows/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Manage and configure [Workflows](https://developers.cloudflare.com/workflows/) using Wrangler.

Note

The `wrangler workflows` command requires Wrangler version `3.83.0` or greater. Use `npx wrangler@latest` to always use the latest Wrangler version when invoking commands.

`--local` option

All `wrangler workflows` commands support the `--local` flag to target a Workflow running in a local [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) session instead of production. Use `--port` to specify the port of the dev session (defaults to `8787`).

The `--local` flag requires Wrangler version `4.79.0` or greater.

For more information, refer to [Workflows local development](https://developers.cloudflare.com/workflows/build/local-development/).

## `workflows list`

List Workflows associated to account

npmyarnpnpm
    
    
    npx wrangler workflows list
    
    
    yarn wrangler workflows list
    
    
    pnpm wrangler workflows list

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `--page``number` default: 1

Show a sepecific page from the listing, can configure page size using "per-page"

  * `--per-page``number`

Configure the maximum number of workflows to show per page




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




## `workflows describe`

Describe Workflow resource

npmyarnpnpm
    
    
    npx wrangler workflows describe <NAME>
    
    
    yarn wrangler workflows describe <NAME>
    
    
    pnpm wrangler workflows describe <NAME>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow




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




## `workflows delete`

Delete workflow - when deleting a workflow, it will also delete it's own instances

npmyarnpnpm
    
    
    npx wrangler workflows delete <NAME>
    
    
    yarn wrangler workflows delete <NAME>
    
    
    pnpm wrangler workflows delete <NAME>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow




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




## `workflows trigger`

Trigger a workflow, creating a new instance. Can optionally take a JSON string to pass a parameter into the workflow instance

npmyarnpnpm
    
    
    npx wrangler workflows trigger <NAME> [PARAMS]
    
    
    yarn wrangler workflows trigger <NAME> [PARAMS]
    
    
    pnpm wrangler workflows trigger <NAME> [PARAMS]

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `[PARAMS]``string` default: 

Params for the workflow instance, encoded as a JSON string

  * `--id``string`

Custom instance ID, if not provided it will default to a random UUIDv4




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




## `workflows instances list`

Instance related commands (list, describe, terminate, pause, resume)

npmyarnpnpm
    
    
    npx wrangler workflows instances list <NAME>
    
    
    yarn wrangler workflows instances list <NAME>
    
    
    pnpm wrangler workflows instances list <NAME>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `--reverse``boolean` default: false

Reverse order of the instances table

  * `--status``string`

Filters list by instance status (can be one of: queued, running, paused, errored, terminated, complete)

  * `--date-start``string`

Only list instances created at or after this date (ISO 8601, e.g. 2026-01-01 or 2026-01-01T13:00:00Z)

  * `--date-end``string`

Only list instances created at or before this date (ISO 8601). A date without a time covers the whole UTC day, so 2026-01-31 includes everything up to 2026-01-31T23:59:59.999Z

  * `--page``number` default: 1

Show a sepecific page from the listing, can configure page size using "per-page"

  * `--per-page``number`

Configure the maximum number of instances to show per page




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




## `workflows instances describe`

Describe a workflow instance - see its logs, retries and errors

npmyarnpnpm
    
    
    npx wrangler workflows instances describe <NAME> [ID]
    
    
    yarn wrangler workflows instances describe <NAME> [ID]
    
    
    pnpm wrangler workflows instances describe <NAME> [ID]

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `[ID]``string` default: latest

ID of the instance - instead of an UUID you can type 'latest' to get the latest instance and describe it

  * `--step-output``boolean` default: true

Don't output the step output since it might clutter the terminal

  * `--truncate-output-limit``number` default: 5000

Truncate step output after x characters




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




## `workflows instances send-event`

Send an event to a workflow instance

npmyarnpnpm
    
    
    npx wrangler workflows instances send-event <NAME> <ID>
    
    
    yarn wrangler workflows instances send-event <NAME> <ID>
    
    
    pnpm wrangler workflows instances send-event <NAME> <ID>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `<ID>``string` required

ID of the instance - instead of an UUID you can type 'latest' to get the latest instance and send an event to it

  * `--type``string` required

Type of the workflow event

  * `--payload``string` default: {}

JSON string for the workflow event (e.g., '{"key": "value"}')




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




## `workflows instances terminate`

Terminate a workflow instance

npmyarnpnpm
    
    
    npx wrangler workflows instances terminate <NAME> <ID>
    
    
    yarn wrangler workflows instances terminate <NAME> <ID>
    
    
    pnpm wrangler workflows instances terminate <NAME> <ID>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `<ID>``string` required

ID of the instance - instead of an UUID you can type 'latest' to get the latest instance and describe it

  * `--rollback``boolean` default: false

Run registered rollback handlers before terminating




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




## `workflows instances restart`

Restart a workflow instance

npmyarnpnpm
    
    
    npx wrangler workflows instances restart <NAME> <ID>
    
    
    yarn wrangler workflows instances restart <NAME> <ID>
    
    
    pnpm wrangler workflows instances restart <NAME> <ID>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `<ID>``string` required

ID of the instance - instead of an UUID you can type 'latest' to get the latest instance and describe it

  * `--from-step-name``string`

Name of the step to restart from

  * `--from-step-count``number`

1-based occurrence of the step name/type to restart from (defaults to 1)

  * `--from-step-type``string`

Step type to restart from, used when the same name is shared across step types (defaults to do)




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




## `workflows instances pause`

Pause a workflow instance

npmyarnpnpm
    
    
    npx wrangler workflows instances pause <NAME> <ID>
    
    
    yarn wrangler workflows instances pause <NAME> <ID>
    
    
    pnpm wrangler workflows instances pause <NAME> <ID>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `<ID>``string` required

ID of the instance - instead of an UUID you can type 'latest' to get the latest instance and pause it




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




## `workflows instances resume`

Resume a workflow instance

npmyarnpnpm
    
    
    npx wrangler workflows instances resume <NAME> <ID>
    
    
    yarn wrangler workflows instances resume <NAME> <ID>
    
    
    pnpm wrangler workflows instances resume <NAME> <ID>

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `<ID>``string` required

ID of the instance - instead of an UUID you can type 'latest' to get the latest instance and resume it




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




## `workflows instances delete`

Delete workflow instances

npmyarnpnpm
    
    
    npx wrangler workflows instances delete <NAME> [ID]
    
    
    yarn wrangler workflows instances delete <NAME> [ID]
    
    
    pnpm wrangler workflows instances delete <NAME> [ID]

  * `--local``boolean`

Interact with local dev session

  * `--port``number` default: 8787

Port of the local dev session (default: 8787)

  * `--json``boolean` default: false

Output the raw API response as JSON

  * `<NAME>``string` required

Name of the workflow

  * `[ID]``string`

IDs of the instances - you can type 'latest' to get the latest instance and delete it

  * `--filename``string`

Path to a JSON file containing an array of instance IDs




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




[PreviousWorkers for Platforms](https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/)[NextAuthentication profiles](https://developers.cloudflare.com/workers/wrangler/profiles/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/commands/workflows.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/browser-run/reference/wrangler-commands/
title: Wrangler commands \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.211757+00:00
---

# Wrangler commands · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/reference/wrangler-commands/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Reference
  4. /Wrangler commands



# Wrangler commands

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/reference/wrangler-commands/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use `wrangler browser` commands to manage Browser Run sessions from the command line.

## `browser create`

Create a new Browser Run session

npmyarnpnpm
    
    
    npx wrangler browser create
    
    
    yarn wrangler browser create
    
    
    pnpm wrangler browser create

  * `--lab``boolean` default: false

Enable lab browser session with experimental Chrome features (e.g., WebMCP)

  * `--keepAlive``number` alias: --k

Keep-alive duration in seconds (60-600)

  * `--json``boolean` default: false

Return session info as JSON

  * `--open``boolean`

Open DevTools in browser (default: true in interactive mode)




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




## `browser close`

Close a Browser Run session

npmyarnpnpm
    
    
    npx wrangler browser close <SESSIONID>
    
    
    yarn wrangler browser close <SESSIONID>
    
    
    pnpm wrangler browser close <SESSIONID>

  * `<SESSIONID>``string` required

The session ID to close

  * `--json``boolean` default: false

Return result as JSON




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




## `browser list`

List active Browser Run sessions

npmyarnpnpm
    
    
    npx wrangler browser list
    
    
    yarn wrangler browser list
    
    
    pnpm wrangler browser list

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




## `browser view`

View a live browser session

npmyarnpnpm
    
    
    npx wrangler browser view [SESSIONID]
    
    
    yarn wrangler browser view [SESSIONID]
    
    
    pnpm wrangler browser view [SESSIONID]

  * `[SESSIONID]``string`

The session ID to inspect (optional if only one session exists)

  * `--target``string`

Target selector (matches id exactly, or url/title by substring)

  * `--json``boolean` default: false

Return live browser session URL(s) as JSON

  * `--open``boolean`

Open in browser (default: true in interactive mode)




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




[PreviousWrangler](https://developers.cloudflare.com/browser-run/reference/wrangler/)[NextBrowser binding API](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/reference/wrangler-commands.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

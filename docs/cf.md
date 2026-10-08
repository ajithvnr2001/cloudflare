---
url: https://developers.cloudflare.com/cf/
title: Cloudflare CLI \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:46.404194+00:00
---

# Cloudflare CLI · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/

  1. [Home](https://developers.cloudflare.com/)
  2. /Cloudflare CLI



# Cloudflare CLI

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cf/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose your pathWhat cf providescf and Wrangler

The Cloudflare CLI, `cf`, is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers. Coding agents run the same commands you do.

Beta

`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

Install `cf` globally:

npmyarnpnpmbun
    
    
    npm install --global cf
    
    
    yarn global add cf
    
    
    pnpm add --global cf
    
    
    bun add --global cf

To sign in and run your first command, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/).

## Choose your path

### [Deploy a Worker](https://developers.cloudflare.com/cf/get-started/first-worker/)

Create a project with cf init, develop it locally, and deploy it.

### [Manage resources](https://developers.cloudflare.com/cf/get-started/resources/)

Find zones and create, list, and delete DNS records from the command line.

### [Coming from Wrangler](https://developers.cloudflare.com/cf/wrangler/)

Learn what changes, and move a project to cf with cf migrate.

### [Coding agents](https://developers.cloudflare.com/cf/agents/)

Set up coding agents to find and run Cloudflare commands with cf.

### [CI and automation](https://developers.cloudflare.com/cf/ci/)

Authenticate with API tokens and run cf in pipelines.

## What `cf` provides

  * **Commands for the public API.** More than 2,900 commands, most of them generated from the schemas that describe the Cloudflare API.
  * **Typed project configuration.** Workers projects use [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), so editors and agents can autocomplete bindings and triggers.
  * **Project commands.** `cf dev`, `cf build`, and `cf deploy` run your framework's own command, the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), or Wrangler, depending on the project. To learn more, refer to [How cf runs your project](https://developers.cloudflare.com/cf/projects/#how-cf-runs-your-project).
  * **Command search.** `cf cli search` finds commands from a plain-language description of a task.



## `cf` and Wrangler

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) is the CLI for Workers projects configured with `wrangler.jsonc` or `wrangler.toml`. `cf` covers the public Cloudflare API and uses `cloudflare.config.ts` for Workers projects.

You can run `cf` resource commands alongside an existing Wrangler project without changing it. Before you run `cf dev`, `cf build`, or `cf deploy` in a Wrangler project, convert it with `cf migrate`. To compare the two tools and plan a move, refer to [`cf` for Wrangler users](https://developers.cloudflare.com/cf/wrangler/).

[NextInstall and sign in](https://developers.cloudflare.com/cf/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

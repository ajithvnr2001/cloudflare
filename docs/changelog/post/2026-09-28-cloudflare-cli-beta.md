---
url: https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/
title: Cloudflare CLI is now in beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:17.076868+00:00
---

# Cloudflare CLI is now in beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 28, 2026

## Cloudflare CLI is now in beta

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare CLI](https://developers.cloudflare.com/cf/), `cf`, is now in beta. `cf` is one command-line interface for the public Cloudflare API and for Workers projects. Use it to manage zones, DNS, storage, and security settings, and to create, develop, and deploy Workers, without switching between tools.

Install `cf` globally, then sign in:

npmyarnpnpmbun
    
    
    npm install --global cf
    
    
    yarn global add cf
    
    
    pnpm add --global cf
    
    
    bun add --global cf
    
    
    cf auth login

With `cf`, you can:

  * **Manage resources across Cloudflare.** More than 2,900 commands cover the public Cloudflare API, and most print their results as JSON.
  * **Create and deploy Workers.** `cf init` creates a project that uses [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/), a typed configuration file. `cf dev`, `cf build`, and `cf deploy` develop, build, and deploy it.
  * **Move from Wrangler.** `cf migrate` converts a Wrangler configuration file to `cloudflare.config.ts`. You can also run `cf` resource commands in an existing Wrangler project without migrating it.
  * **Work with coding agents.** `cf cli search` finds the command for a task from a plain-language description, so an agent can find and run commands without prior knowledge of `cf`.



`cf` is in beta. Commands, configuration, and Build Output can change before the stable release.

To get started, refer to [Install and sign in](https://developers.cloudflare.com/cf/get-started/). To move an existing project, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

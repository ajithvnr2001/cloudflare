---
url: https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/
title: Manage Flagship from the command line with Wrangler \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.727957+00:00
---

# Manage Flagship from the command line with Wrangler · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 16, 2026

## Manage Flagship from the command line with Wrangler

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**[Wrangler](https://developers.cloudflare.com/workers/wrangler/)** now includes `wrangler flagship`, a command suite for managing [Flagship](https://developers.cloudflare.com/flagship/) apps and feature flags from your terminal.

Create an app and, if you use it from a Worker, add it to your `wrangler.json` or `wrangler.jsonc` file as a binding:
    
    
    wrangler flagship apps create "My Worker App" \
      --binding FLAGS \
      --update-config

Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values:
    
    
    wrangler flagship flags create <APP_ID> new-checkout
    
    wrangler flagship flags create <APP_ID> checkout-flow \
      --variation control=old-checkout \
      --variation treatment=new-checkout \
      --default control \
      --type string

After a flag exists, change its default variation or use enable and disable commands as kill switches. Existing targeting rules continue to apply unless you change or clear them explicitly:
    
    
    wrangler flagship flags update <APP_ID> checkout-flow --default treatment
    wrangler flagship flags disable <APP_ID> checkout-flow
    wrangler flagship flags enable <APP_ID> checkout-flow

For release workflows, use `rollout`, `split`, and `rules` to change exposure without redeploying your Worker:
    
    
    wrangler flagship flags rollout <APP_ID> new-checkout \
      --to on \
      --percentage 25 \
      --by user_id
    
    wrangler flagship flags split <APP_ID> checkout-flow \
      --weight control=80 \
      --weight treatment=20 \
      --by user_id
    
    wrangler flagship flags rules update <APP_ID> checkout-flow \
      --priority 1 \
      --when "country equals US"

These commands can also be used from CI/CD pipelines, scripts, and AI agents to inspect Flagship state, update flag behavior, or roll back changes through Wrangler.

Refer to the [`wrangler flagship` command reference](https://developers.cloudflare.com/flagship/reference/wrangler-commands/) for the full command guide.

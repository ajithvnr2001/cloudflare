---
url: https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/
title: All Wrangler commands for Workflows now support local development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.223452+00:00
---

# All Wrangler commands for Workflows now support local development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-01-wrangler-workflows-local/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 1, 2026

## All Wrangler commands for Workflows now support local development

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

All `wrangler workflows` commands now accept a `--local` flag to target a Workflow running in a local `wrangler dev` session instead of the production API.

You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:
    
    
    npx wrangler workflows list --local
    npx wrangler workflows trigger my-workflow --local
    npx wrangler workflows instances list my-workflow --local
    npx wrangler workflows instances pause my-workflow <INSTANCE_ID> --local
    npx wrangler workflows instances send-event my-workflow <INSTANCE_ID> --type my-event --local

All commands also accept `--port` to target a specific `wrangler dev` session (defaults to `8787`).

For more information, refer to [Workflows local development](https://developers.cloudflare.com/workflows/build/local-development/).

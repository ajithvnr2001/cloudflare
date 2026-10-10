---
url: https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/
title: Declare required secrets in your Wrangler configuration \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.612382+00:00
---

# Declare required secrets in your Wrangler configuration · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-24-secrets-config-property/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 25, 2026

## Declare required secrets in your Wrangler configuration

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The new `secrets` configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.
    
    
    {
    	"secrets": {
    		"required": ["API_KEY", "DB_PASSWORD"],
    	},
    }
    
    
    [secrets]
    required = [ "API_KEY", "DB_PASSWORD" ]

#### Local development

When `secrets` is defined, `wrangler dev` and `vite dev` load only the keys listed in `secrets.required` from `.dev.vars` or `.env`/`process.env`. Additional keys in those files are excluded. If any required secrets are missing, a warning is logged listing the missing names.

#### Type generation

`wrangler types` generates typed bindings from `secrets.required` instead of inferring names from `.dev.vars` or `.env`. This lets you run type generation in CI or other environments where those files are not present. Per-environment secrets are supported — the aggregated `Env` type marks secrets that only appear in some environments as optional.

#### Deploy

`wrangler deploy` and `wrangler versions upload` validate that all secrets in `secrets.required` are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.

For more information, refer to the [`secrets` configuration property](https://developers.cloudflare.com/workers/wrangler/configuration/#secrets-configuration-property) reference.

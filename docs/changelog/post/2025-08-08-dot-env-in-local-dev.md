---
url: https://developers.cloudflare.com/changelog/post/2025-08-08-dot-env-in-local-dev/
title: Wrangler and the Cloudflare Vite plugin support `.env` files in local development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:19.179754+00:00
---

# Wrangler and the Cloudflare Vite plugin support `.env` files in local development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-08-dot-env-in-local-dev/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 8, 2025

## Wrangler and the Cloudflare Vite plugin support `.env` files in local development

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-08-dot-env-in-local-dev/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, you can use `.env` files to provide secrets and override environment variables on the `env` object during local development with Wrangler and the Cloudflare Vite plugin.

Previously in local development, if you wanted to provide secrets or environment variables during local development, you had to use `.dev.vars` files. This is still supported, but you can now also use `.env` files, which are more familiar to many developers.

#### Using `.env` files in local development

You can create a `.env` file in your project root to define environment variables that will be used when running `wrangler dev` or `vite dev`. The `.env` file should be formatted like a `dotenv` file, such as `KEY="VALUE"`:

.envbash
    
    
    TITLE="My Worker"
    API_TOKEN="dev-token"

When you run `wrangler dev` or `vite dev`, the environment variables defined in the `.env` file will be available in your Worker code via the `env` object:
    
    
    export default {
    	async fetch(request, env) {
    		const title = env.TITLE; // "My Worker"
    		const apiToken = env.API_TOKEN; // "dev-token"
    		const response = await fetch(
    			`https://api.example.com/data?token=${apiToken}`,
    		);
    		return new Response(`Title: ${title} - ` + (await response.text()));
    	},
    };

#### Multiple environments with `.env` files

If your Worker defines multiple [environments](https://developers.cloudflare.com/workers/wrangler/environments/), you can set different variables for each environment (ex: production or staging) by creating files named `.env.<environment-name>`.

When you use `wrangler <command> --env <environment-name>` or `CLOUDFLARE_ENV=<environment-name> vite dev`, the corresponding environment-specific file will also be loaded and merged with the `.env` file.

For example, if you want to set different environment variables for the `staging` environment, you can create a file named `.env.staging`:

.env.stagingbash
    
    
    API_TOKEN="staging-token"

When you run `wrangler dev --env staging` or `CLOUDFLARE_ENV=staging vite dev`, the environment variables from `.env.staging` will be merged onto those from `.env`.
    
    
    export default {
    	async fetch(request, env) {
    		const title = env.TITLE; // "My Worker" (from `.env`)
    		const apiToken = env.API_TOKEN; // "staging-token" (from `.env.staging`, overriding the value from `.env`)
    		const response = await fetch(
    			`https://api.example.com/data?token=${apiToken}`,
    		);
    		return new Response(`Title: ${title} - ` + (await response.text()));
    	},
    };

#### Find out more

For more information on how to use `.env` files with Wrangler and the Cloudflare Vite plugin, see the following documentation:

  * [Environment variables and secrets](https://developers.cloudflare.com/workers/local-development/environment-variables)
  * [Wrangler Documentation ↗︎](https://developers.cloudflare.com/workers/wrangler)
  * [Cloudflare Vite Plugin Documentation ↗︎](https://developers.cloudflare.com/workers/wrangler/vite)



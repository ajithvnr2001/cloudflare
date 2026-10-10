---
url: https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/
title: No config? No problem. Just `wrangler deploy` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.224522+00:00
---

# No config? No problem. Just `wrangler deploy` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-25-wrangler-autoconfig-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 25, 2026

## No config? No problem. Just `wrangler deploy`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now deploy any existing project to Cloudflare Workers — even without a Wrangler configuration file — and `wrangler deploy` will _just work_.

Starting with Wrangler **4.68.0** , running [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy) [automatically configures your project](https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/) by detecting your framework, installing required adapters, and deploying it to Cloudflare Workers.

#### Using Wrangler locally
    
    
    npx wrangler deploy

When you run `wrangler deploy` in a project without a configuration file, Wrangler:

  1. Detects your framework from `package.json`
  2. Prompts you to confirm the detected settings
  3. Installs any required adapters
  4. Generates a `wrangler.jsonc` [configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/)
  5. Deploys your project to Cloudflare Workers



You can also use [`wrangler setup`](https://developers.cloudflare.com/workers/wrangler/commands/general/#setup) to configure without deploying, or pass [`--yes`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy) to skip prompts.

#### Using the Cloudflare dashboard

![Automatic configuration pull request created by Workers Builds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1918,height=1348,format=webp/_astro/automatic-pr.CwJG6Bec.png)

When you connect a repository through the [Workers dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/create), a [pull request is generated](https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/) for you with all necessary files, and a [preview deployment](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) to check before merging.

Note

A pull request is only generated when your deploy command is `npx wrangler deploy`. If you use a custom deploy command, automatic configuration still runs but a PR is not created.

#### Background

In December 2025, we [introduced automatic configuration](https://developers.cloudflare.com/changelog/2025-12-16-wrangler-autoconfig/) as an experimental feature. It is now generally available and the default behavior.

If you have questions or run into issues, join the [GitHub discussion ↗︎](https://github.com/cloudflare/workers-sdk/discussions/11667).

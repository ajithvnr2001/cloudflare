---
url: https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/
title: Select Wrangler environments using the CLOUDFLARE_ENV environment variable \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.040669+00:00
---

# Select Wrangler environments using the CLOUDFLARE_ENV environment variable · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-09-cloudflare-env-variable/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2025

## Select Wrangler environments using the CLOUDFLARE_ENV environment variable

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now supports using the `CLOUDFLARE_ENV` [environment variable](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/#supported-environment-variables) to select the active [environment](https://developers.cloudflare.com/workers/wrangler/environments/) for your Worker commands. This provides a more flexible way to manage environments, especially when working with build tools and CI/CD pipelines.

#### What's new

**Environment selection via environment variable:**

  * Set `CLOUDFLARE_ENV` to specify which environment to use for Wrangler commands
  * Works with all Wrangler commands that support the `--env` flag
  * The `--env` command line argument takes precedence over the `CLOUDFLARE_ENV` environment variable



#### Example usage
    
    
    # Deploy to the production environment using CLOUDFLARE_ENV
    CLOUDFLARE_ENV=production wrangler deploy
    
    # Upload a version to the staging environment
    CLOUDFLARE_ENV=staging wrangler versions upload
    
    # The --env flag takes precedence over CLOUDFLARE_ENV
    CLOUDFLARE_ENV=dev wrangler deploy --env production
    # This will deploy to production, not dev

#### Use with build tools

The `CLOUDFLARE_ENV` environment variable is particularly useful when working with build tools like Vite. You can set the environment once during the build process, and it will be used for both building and deploying your Worker:
    
    
    # Set the environment for both build and deploy
    CLOUDFLARE_ENV=production npm run build & wrangler deploy

When using `@cloudflare/vite-plugin`, the build process generates a ["redirected deploy config"](https://developers.cloudflare.com/workers/wrangler/configuration/#generated-wrangler-configuration) that is flattened to only contain the active environment. Wrangler will validate that the environment specified matches the environment used during the build to prevent accidentally deploying a Worker built for one environment to a different environment.

#### Learn more

  * [System environment variables](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/)
  * [Environments](https://developers.cloudflare.com/workers/wrangler/environments/)



---
url: https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/
title: Deploy static sites to Workers without a configuration file \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:22.303598+00:00
---

# Deploy static sites to Workers without a configuration file · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 9, 2025

## Deploy static sites to Workers without a configuration file

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-09-interactive-wrangler-assets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Deploying static site to Workers is now easier. When you run `wrangler deploy [directory]` or `wrangler deploy --assets [directory]` without an existing [configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/), [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) now guides you through the deployment process with interactive prompts.

#### Before and after

**Before:** Required remembering multiple flags and parameters
    
    
    wrangler deploy --assets ./dist --compatibility-date 2025-09-09 --name my-project

**After:** Simple directory deployment with guided setup
    
    
    wrangler deploy dist
    # Interactive prompts handle the rest as shown in the example flow below

#### What's new

**Interactive prompts for missing configuration:**

  * Wrangler detects when you're trying to deploy a directory of static assets
  * Prompts you to confirm the deployment type
  * Asks for a project name (with smart defaults)
  * Automatically sets the compatibility date to today



**Automatic configuration generation:**

  * Creates a `wrangler.jsonc` file with your deployment settings
  * Stores your choices for future deployments
  * Eliminates the need to remember complex command-line flags



#### Example workflow
    
    
    # Deploy your built static site
    wrangler deploy dist
    
    # Wrangler will prompt:
    ✔ It looks like you are trying to deploy a directory of static assets only. Is this correct? … yes
    ✔ What do you want to name your project? … my-astro-site
    
    # Automatically generates a wrangler.jsonc file and adds it to your project:
    {
      "name": "my-astro-site",
      "compatibility_date": "2025-09-09",
      "assets": {
        "directory": "dist"
      }
    }
    
    # Next time you run wrangler deploy, this will use the configuration in your newly generated wrangler.jsonc file
    wrangler deploy

#### Requirements

  * You must use Wrangler version 4.24.4 or later in order to use this feature



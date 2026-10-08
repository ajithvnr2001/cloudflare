---
url: https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/
title: Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:16.070903+00:00
---

# Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 29, 2025

## Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets

[Workers](https://developers.cloudflare.com/workers/)[Secrets Store](https://developers.cloudflare.com/secrets-store/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Any template which uses [Worker environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), or [Secrets Store secrets](https://developers.cloudflare.com/secrets-store/) can now be deployed using a [Deploy to Cloudflare button](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

Define environment variables and secrets store bindings in your Wrangler configuration file as normal:
    
    
    {
      "name": "my-worker",
      "main": "./src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
      "vars": {
        "API_HOST": "https://example.com",
      },
    	"secrets_store_secrets": [
    		{
    			"binding": "API_KEY",
    			"store_id": "demo",
    			"secret_name": "api-key"
    		}
    	]
    }
    
    
    name = "my-worker"
    main = "./src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [vars]
    API_HOST = "https://example.com"
    
    [[secrets_store_secrets]]
    binding = "API_KEY"
    store_id = "demo"
    secret_name = "api-key"

Add secrets to a `.dev.vars.example` or `.env.example` file:

.dev.vars.exampleini
    
    
    COOKIE_SIGNING_KEY=my-secret # comment

And optionally, you can add a description for these bindings in your template's `package.json` to help users understand how to configure each value:

package.jsonjson
    
    
    {
    	"name": "my-worker",
    	"private": true,
    	"cloudflare": {
    		"bindings": {
    			"API_KEY": {
    				"description": "Select your company's API key for connecting to the example service."
    			},
    			"COOKIE_SIGNING_KEY": {
    				"description": "Generate a random string using `openssl rand -hex 32`."
    			}
    		}
    	}
    }

These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in [our documentation](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

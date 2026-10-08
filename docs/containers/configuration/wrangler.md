---
url: https://developers.cloudflare.com/containers/configuration/wrangler/
title: Wrangler configuration \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:34.461853+00:00
---

# Wrangler configuration · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/configuration/wrangler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Configuration
  4. /Wrangler configuration



# Wrangler configuration

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/configuration/wrangler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMinimal configurationContainer settingsNext steps

Define Containers in the Wrangler configuration file for your Worker. Each Container is associated with a Durable Object class, which provides access to the Container at runtime.

## Minimal configuration

A new Container application requires a Container definition, a Durable Object binding, and a Durable Object class export:
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "my-container-worker",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"containers": [
    		{
    			"class_name": "MyContainer",
    			"image": "./Dockerfile",
    			"max_instances": 10,
    		},
    	],
    	"durable_objects": {
    		"bindings": [
    			{
    				"name": "MY_CONTAINER",
    				"class_name": "MyContainer",
    			},
    		],
    	},
    	"exports": {
    		"MyContainer": {
    			"type": "durable-object",
    			"storage": "sqlite",
    		},
    	},
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "my-container-worker"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[containers]]
    class_name = "MyContainer"
    image = "./Dockerfile"
    max_instances = 10
    
    [[durable_objects.bindings]]
    name = "MY_CONTAINER"
    class_name = "MyContainer"
    
    [exports.MyContainer]
    type = "durable-object"
    storage = "sqlite"

The configuration uses three sections:

  1. **`containers`** defines the container image and associates it with a Durable Object class through `class_name`.
  2. **`durable_objects.bindings`** makes the Durable Object namespace available to Worker code. In this example, access it through `env.MY_CONTAINER`.
  3. **`exports`** declares the Durable Object class and provisions it with SQLite storage.



The `class_name` in `containers` and `durable_objects.bindings`, and the key in `exports`, must match the exported Durable Object class in your Worker.

Existing applications

Existing applications that use the legacy `migrations` array can continue to use it. Do not configure `exports` and `migrations` together. To switch an existing application to `exports`, refer to [Migrate from the legacy `migrations` flow](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow).

## Container settings

The `containers` entry can also configure the instance type, maximum number of running instances, image build, placement constraints, rollouts, and SSH access.

For all available fields and values, refer to the [Containers Wrangler configuration reference](https://developers.cloudflare.com/workers/wrangler/configuration/#containers).

## Next steps

  * [Deploy Containers](https://developers.cloudflare.com/containers/guides/deploy/) — Build the image and deploy the Worker.
  * [Scaling and Routing](https://developers.cloudflare.com/containers/configuration/scaling-and-routing/) — Route requests and scale Container instances.
  * [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/) — Control how configuration changes reach running instances.
  * [Image management](https://developers.cloudflare.com/containers/guides/image-management/) — Use local and remote container images.



[PreviousMigrate to the Durable Object scheduling policy](https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-scheduling-policy/)[NextScheduling Policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/configuration/wrangler.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

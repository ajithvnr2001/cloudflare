---
url: https://developers.cloudflare.com/durable-objects/reference/environments/
title: Environments \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:10.324564+00:00
---

# Environments · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/reference/environments/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Reference
  4. /Environments



# Environments

Last updated Jul 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/reference/environments/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWrangler environments Migration environmentsLocal developmentRemote development

Environments provide isolated spaces where your code runs with specific dependencies and configurations. This can be useful for a number of reasons, such as compatibility testing or version management. Using different environments can help with code consistency, testing, and production segregation, which reduces the risk of errors when deploying code.

## Wrangler environments

[Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) allows you to deploy the same Worker application with different configuration for each [environment](https://developers.cloudflare.com/workers/wrangler/environments/).

If you are using Wrangler environments, you must specify any [Durable Object bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) you wish to use on a per-environment basis.

Durable Object bindings are not inherited. For example, you can define an environment named `staging` as below:
    
    
    {
    	"env": {
    		"staging": {
    			"durable_objects": {
    				"bindings": [
    					{
    						"name": "EXAMPLE_CLASS",
    						"class_name": "DurableObjectExample"
    					}
    				]
    			}
    		}
    	}
    }
    
    
    [[env.staging.durable_objects.bindings]]
    name = "EXAMPLE_CLASS"
    class_name = "DurableObjectExample"

Because Wrangler appends the [environment name](https://developers.cloudflare.com/workers/wrangler/environments/) to the top-level name when publishing, for a Worker named `worker-name` the above example is equivalent to:
    
    
    {
    	"env": {
    		"staging": {
    			"durable_objects": {
    				"bindings": [
    					{
    						"name": "EXAMPLE_CLASS",
    						"class_name": "DurableObjectExample",
    						"script_name": "worker-name-staging"
    					}
    				]
    			}
    		}
    	}
    }
    
    
    [[env.staging.durable_objects.bindings]]
    name = "EXAMPLE_CLASS"
    class_name = "DurableObjectExample"
    script_name = "worker-name-staging"

`"EXAMPLE_CLASS"` in the staging environment is bound to a different Worker code name compared to the top-level `"EXAMPLE_CLASS"` binding, and will therefore access different Durable Objects with different persistent storage.

If you want an environment-specific binding that accesses the same Objects as the top-level binding, specify the top-level Worker code name explicitly using `script_name`:
    
    
    {
    	"env": {
    		"another": {
    			"durable_objects": {
    				"bindings": [
    					{
    						"name": "EXAMPLE_CLASS",
    						"class_name": "DurableObjectExample",
    						"script_name": "worker-name"
    					}
    				]
    			}
    		}
    	}
    }
    
    
    [[env.another.durable_objects.bindings]]
    name = "EXAMPLE_CLASS"
    class_name = "DurableObjectExample"
    script_name = "worker-name"

### Migration environments

You can define a Durable Object migration for each environment, as well as at the top level. Migrations at the environment-level override migrations at the top level.

For more information, refer to [Migration Wrangler Configuration](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/#migration-wrangler-configuration).

## Local development

Local development sessions create a standalone, local-only environment that mirrors the production environment, so that you can test your Worker and Durable Objects before you deploy to production.

An existing Durable Object binding of `DB` would be available to your Worker when running locally.

Refer to Workers [Local development](https://developers.cloudflare.com/workers/local-development/bindings-per-env/).

## Remote development

KV-backed Durable Objects support remote development using the dashboard playground. The dashboard playground uses a browser version of Visual Studio Code, allowing you to rapidly iterate on your Worker entirely in your browser.

To start remote development:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select an existing Worker.

  3. Select the **Edit code** icon located on the upper-right of the screen.




Caution

Remote development is only available for KV-backed Durable Objects. SQLite-backed Durable Objects do not support remote development.

[PreviousData location](https://developers.cloudflare.com/durable-objects/reference/data-location/)[NextGradual Deployments ↗︎](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/#gradual-deployments-for-durable-objects)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/reference/environments.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

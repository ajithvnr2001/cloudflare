---
url: https://developers.cloudflare.com/workers/previews/configuration/
title: Configuration \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:39.877305+00:00
---

# Configuration · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/previews/configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Previews](https://developers.cloudflare.com/workers/previews/)
  4. /Configuration



# Configuration

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/previews/configuration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetting your Previews Base configurationSecretsWrangler configuration file What goes in the previews blockDashboard configuration

Previews do not inherit production settings. Define them in the `previews` block of your configuration file. For how bindings share or isolate data and state, refer to [Resources and isolation](https://developers.cloudflare.com/workers/previews/resources/).

## Setting your Previews Base configuration

Define your starting `previews` block on the branch your team branches from, such as `main`. Git carries the configuration file into each new branch.

Change the `previews` block on a branch when its Preview needs different settings. When you run `npx wrangler preview`, Wrangler uses the configuration file from your current branch as the source of truth. For setup instructions, refer to [Get started](https://developers.cloudflare.com/workers/previews/get-started/).

**`previews` on main**

var`APP_ENV = "preview"`

var`API_URL = "api.staging.example.com"`

binding`UPLOADS = preview-r2-bucket`

Previewfeature/loginredesignfix-api

**feature/login**

var`APP_ENV = "preview"`

var`API_URL = "api.staging.example.com"`

binding`UPLOADS = login-test-r2-bucket`

var`DEBUG = "true"`added

**redesign**

var`APP_ENV = "preview"`

var`API_URL = "api.staging.example.com"`

binding`UPLOADS = preview-r2-bucket`

**fix-api**

var`APP_ENV = "preview"`

var`API_URL = "api.dev.example.com"`

binding`UPLOADS`removed

`npx wrangler preview`uses the configuration file on feature/login as the source of truth

## Secrets

Secrets cannot be stored in Wrangler configuration files. To preserve the branching model without applying the same secrets to every Preview manually, set shared secrets once in the Previews Base configuration. Each new Preview receives those secrets when it is created. Set a different value for an individual Preview when needed. Later changes to Base secrets apply only to new Previews, so active Previews remain unchanged.

I want to | Command  
---|---  
Add a secret to the **Base configuration** | [`npx wrangler preview base-config secret put SECRET_NAME`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#preview-base-config-secret-put)  
Add a secret to **one Preview** | [`npx wrangler preview secret put SECRET_NAME --name <preview>`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#preview-secret-put)  
Remove a secret from the **Base configuration** | [`npx wrangler preview base-config secret delete SECRET_NAME`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#preview-base-config-secret-delete)  
Remove a secret from **one Preview** | [`npx wrangler preview secret delete SECRET_NAME --name <preview>`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#preview-secret-delete)  
  
The `--name` flag defaults to the current git branch if omitted.

## Wrangler configuration file

Your Wrangler file has production settings at the top level and Preview settings in a `previews` block. The `previews` block is required, but it can be empty if your Preview does not need separate settings. Point Preview bindings at staging or test resources instead of production resources.
    
    
    {
      // ...
      "vars": {
        "ENVIRONMENT": "production"
      },
      "r2_buckets": [
        {
          "binding": "UPLOADS",
          "bucket_name": "prod-uploads"
        }
      ],
      // ...
      "previews": {
        // ...
        "vars": {
          "ENVIRONMENT": "preview"
        },
        "r2_buckets": [
          {
            "binding": "UPLOADS",
            "bucket_name": "r2-staging"
          }
        ]
        // ...
      }
    }
    
    
    [vars]
    ENVIRONMENT = "production"
    
    [[r2_buckets]]
    binding = "UPLOADS"
    bucket_name = "prod-uploads"
    
    [previews.vars]
    ENVIRONMENT = "preview"
    
    [[previews.r2_buckets]]
    binding = "UPLOADS"
    bucket_name = "r2-staging"

If `npx wrangler preview` creates a Preview URL but warns that bindings are missing, the URL is live but the runtime configuration is incomplete. Copy the missing bindings into the `previews` block, using Preview-safe values and test resources. For resource sharing behavior, refer to [Resources and isolation](https://developers.cloudflare.com/workers/previews/resources/).

### What goes in the `previews` block

Use this table to determine where each setting belongs.

Setting| Behavior  
---|---  
Top level only  
`assets`| Keep at the top level, even with an `ASSETS` binding. `npx wrangler preview` uploads assets from the branch you are previewing.  
`compatibility_date`, `compatibility_flags`| Keep at the top level.  
Top level or `previews` block  
`placement`| Top-level placement applies to Previews. Add `previews.placement` to override it.  
`observability`, `logpush`, `limits`| Add to `previews` only if you want Preview-specific values. For observability settings, refer to [Test and debug](https://developers.cloudflare.com/workers/previews/test-and-debug/).  
Needs a `previews` block  
`vars`| Add `previews.vars` with Preview values.  
[Storage and data bindings](https://developers.cloudflare.com/workers/previews/resources/#resource-bindings)| Add the same binding name, pointed at a Preview-safe resource. Examples: KV, D1, R2, Hyperdrive, Vectorize, Analytics Engine, Pipelines, and Secrets Store.  
[D1 migrations](https://developers.cloudflare.com/workers/previews/resources/#d1-migrations)| Configure a shared staging database on the base branch. To isolate one branch, update both its Preview binding and migration configuration to use a different database. Apply migrations to the database used by the branch before deploying its Preview.  
[Workflows](https://developers.cloudflare.com/workers/previews/resources/#workflows)| Add a binding to an existing Workflow. Previews do not create a Workflow when you change the Workflow name.  
Queue producers| Add `previews.queues.producers`, pointed at a Preview-safe queue.  
`define`| Add `previews.define`. Top-level values are not inherited.  
`tail_consumers`| Add `previews.tail_consumers`. Top-level Tail Worker destinations are not inherited.  
[Durable Objects](https://developers.cloudflare.com/workers/previews/resources/#durable-objects)| Each Preview automatically gets a new Durable Object namespace and storage. Keep classes and migrations at the top level. Add `previews.durable_objects.bindings` only if your code reads the binding from `env`.  
[Containers](https://developers.cloudflare.com/workers/previews/resources/#containers)| Each Preview automatically gets a new container app and container instances. Keep migrations at the top level and add container definitions under `previews.containers`. Keep production container definitions in top-level `containers`. Add the Durable Object binding under `previews` only if your code reads the container binding from `env`.  
API bindings| Add `ai`, `browser`, `images`, `stream`, `media`, `worker_loaders`, or `version_metadata` under `previews` if your code reads the binding from `env`. No staging resource is required.  
  
If your Worker uses only top-level settings, include an empty `previews` block:
    
    
    {
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "assets": {
        "directory": "./public"
      },
      "previews": {}
    }
    
    
    # Set this to today's date
    compatibility_date = "2026-10-08"
    previews = { }
    
    [assets]
    directory = "./public"

Do not add Queue consumers, Cron Triggers, or production routes to `previews`. These do not target Previews. For Preview hostnames, refer to [Custom domains](https://developers.cloudflare.com/workers/previews/custom-domains/).

Service bindings from a Preview call the bound Worker's production deployment. For more limitations, refer to [Limitations](https://developers.cloudflare.com/workers/previews/resources/#limitations).

## Dashboard configuration

You can configure Previews Base settings in the dashboard, but you must copy the generated configuration into your Wrangler file. To avoid this extra step, configure your Preview settings in the Wrangler file directly.

  1. In the Cloudflare dashboard, go to **Workers & Pages**.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Worker.

  3. Go to **Settings**. The **Variables and secrets** , **Bindings** , **Observability** , and **Runtime** sections have toggles for **Production** and **Previews Base**.

![Settings tab showing Production and Previews Base toggles for variables, secrets, and bindings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2610,height=1230,format=webp/_astro/settings-base-configuration.aArpBIxr.png)
  4. Select **Previews Base** in each section to configure what new Previews start from. You can import names and values from production, then edit them. You must re-enter secrets manually.

![Import dialog showing variables and secrets imported from production to Previews](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1220,height=780,format=webp/_astro/import_from_prod.mkZszc4R.png)
  5. Update your Wrangler configuration file with the generated `previews` configuration. This keeps future deployments in sync.

![Dashboard showing generated Wrangler configuration for a Previews Base binding](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1896,height=792,format=webp/_astro/dashboard-wrangler-config.BaNl-i5F.png)



[PreviousGet started](https://developers.cloudflare.com/workers/previews/get-started/)[NextResources and isolation](https://developers.cloudflare.com/workers/previews/resources/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/previews/configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

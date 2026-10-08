---
url: https://developers.cloudflare.com/workers/previews/compare-workflows/
title: Compare workflows \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:39.985367+00:00
---

# Compare workflows · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/previews/compare-workflows/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Previews](https://developers.cloudflare.com/workers/previews/)
  4. /Compare workflows



# Compare workflows

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/previews/compare-workflows/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewQuick comparisonVersion URLs Migrate from aliased Version URLs to PreviewsWrangler environments

Previews are the recommended way to test changes before production.

## Quick comparison

Workflow | Best for | Command  
---|---|---  
**Previews** | Full environments for branches and pull requests under the same Worker. | `npx wrangler preview`  
**[Version URLs](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/)** | An uploaded version of your code that uses production resources. | `wrangler versions upload`  
**[Wrangler environments](https://developers.cloudflare.com/workers/wrangler/environments/)** | Separately deployed Workers. | `wrangler deploy --env <name>`  
  
## Version URLs

Version URLs use production resources

A Version URL runs one uploaded Worker version with the production resources configured for that version. It does not create isolated branch resources.

Do not use Version URLs for branch or pull request testing. Use [Previews](https://developers.cloudflare.com/workers/previews/) instead.

Use Version URLs only when you need to inspect one specific uploaded version before deploying it to production traffic.

Version URLs are created from Worker versions, including versions uploaded with `wrangler versions upload`. They are tied to the [Versions and Deployments](https://developers.cloudflare.com/workers/versions-and-deployments/) workflow.

Version URLs are the right fit for:

  * Inspecting one uploaded version before a production deployment or gradual deployment.
  * Workflows built around `wrangler versions upload` and `wrangler versions deploy`.



### Migrate from aliased Version URLs to Previews

If you are using aliased Version URLs created with `wrangler versions upload --preview-alias` for branch or pull request previews, switch to Previews instead. Aliased Version URLs do not create branch-isolated resources.

What you do today | What to do instead  
---|---  
`wrangler versions upload --preview-alias staging` | `npx wrangler preview --name staging`  
Share an aliased Version URL for PR review | Share a [Preview URL](https://developers.cloudflare.com/workers/previews/) or [custom domain Preview URL](https://developers.cloudflare.com/workers/previews/custom-domains/).  
Set `preview_urls = true` for aliased Version URLs | Use [Preview settings](https://developers.cloudflare.com/workers/previews/configuration/) for branch-specific variables, secrets, and bindings.  
  
Previews give you branch isolation, Preview-specific settings, custom domain support, and automatic resource isolation for Durable Objects and Containers.

## Wrangler environments

Wrangler environments create separately named Workers, such as `my-worker-staging`. Use them when development, staging, or other environments need persistent Workers with different settings, routes, or custom domains.

You can create branch Previews under a Wrangler environment. Define its Preview settings in `env.staging.previews`:
    
    
    {
      "name": "my-worker",
      "env": {
        "dev": {
          "name": "my-worker-dev",
          "vars": {
            "ENVIRONMENT": "development"
          }
        },
        "staging": {
          "name": "my-worker-staging",
          "vars": {
            "ENVIRONMENT": "staging"
          },
          "previews": {
            "vars": {
              "ENVIRONMENT": "staging-preview"
            }
          }
        }
      }
    }
    
    
    name = "my-worker"
    
    [env.dev]
    name = "my-worker-dev"
    
      [env.dev.vars]
      ENVIRONMENT = "development"
    
    [env.staging]
    name = "my-worker-staging"
    
      [env.staging.vars]
      ENVIRONMENT = "staging"
    
    [env.staging.previews.vars]
    ENVIRONMENT = "staging-preview"

In this example, `dev` has no `previews` block and remains a persistent Worker environment. `staging` includes a `previews` block for branch Previews.

Then include the environment when you run the Preview command:
    
    
    npx wrangler preview --env staging

This creates or updates the branch Preview under the staging Worker. The Wrangler environment provides the persistent boundary, and Previews provide branch isolation within it.

Include the environment in every Preview command

Use the same `--env` value when you create, update, manage, or delete a Preview. For example:
    
    
    npx wrangler preview delete --env staging --name <PREVIEW_NAME>

If you omit `--env staging`, Wrangler targets the top-level Worker instead of the staging Worker.

[PreviousTest and debug](https://developers.cloudflare.com/workers/previews/test-and-debug/)[NextExamples](https://developers.cloudflare.com/workers/previews/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/previews/compare-workflows.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

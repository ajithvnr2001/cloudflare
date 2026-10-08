---
url: https://developers.cloudflare.com/workers/previews/
title: Previews \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:39.373842+00:00
---

# Previews · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/previews/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Previews



# Previews

Last updated Sep 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/previews/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it works URLs Settings and isolation Access control LimitsNext steps

**Previews** give each branch an isolated, production-like environment under the same Worker. Each Preview is [configured with its own variables, secrets, and bindings](https://developers.cloudflare.com/workers/previews/configuration/), served on its own [URL](https://developers.cloudflare.com/workers/previews/custom-domains/), and has its own [observability](https://developers.cloudflare.com/workers/previews/test-and-debug/).

Worker Previews requires `Wrangler 4.135.0` or later. Update the project dependency because project commands do not use a newer global installation.

![Worker dashboard showing the Preview dropdown and an overview of bindings, metrics, and deployments](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2386,height=1304,format=webp/_astro/previews-dash-overview.BL1UHZHT.png)

Used [Version URLs](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/) or [Wrangler environments](https://developers.cloudflare.com/workers/wrangler/environments/) before? Refer to [Compare workflows](https://developers.cloudflare.com/workers/previews/compare-workflows/) to understand how they differ from Previews and our recommended practices for branch testing.

## How it works

Running `npx wrangler preview` creates or updates a Preview for your current branch under the same Worker. As you use `npx wrangler deploy` for production, use `npx wrangler preview` to test a branch before merging.

Branch | Command | What happens  
---|---|---  
`main` | `npx wrangler deploy` | Deploys to production with production settings.  
`feature/login` | `npx wrangler preview` | Creates or updates a Preview with its own settings.  
  
### URLs

Each Preview gets two types of URLs. You can serve them on `workers.dev`, a [custom domain](https://developers.cloudflare.com/workers/previews/custom-domains/), or both.

  * **Preview URL** : always serves the latest deployment. Share this with your team so they always see the most up-to-date version of your branch.
  * **Deployment URL** : points to one specific deploy and never changes. Use this to reference or compare exact versions, like linking a specific deploy in a PR review.



Host type | Preview URL | Deployment URL  
---|---|---  
`workers.dev` | `<preview-name>-<worker-name>.<subdomain>.workers.dev` | `<deployment-id>-<worker-name>.<subdomain>.workers.dev`  
Custom domain | `<preview-name>.app.example.com` | `<deployment-id>-<preview-name>.app.example.com`  
  
To prevent search engines from indexing your Preview, use its `workers.dev` URL, which includes an `X-Robots-Tag: noindex` response header. For custom domain Preview URLs, use [Cloudflare Access](https://developers.cloudflare.com/workers/previews/custom-domains/#protect-preview-content).

### Settings and isolation

Previews do not inherit production settings. Define them in the `previews` block of your Wrangler configuration file. When you run `npx wrangler preview` on a branch, Wrangler creates or updates its Preview using that branch's `previews` block. For more information, refer to [Configuration](https://developers.cloudflare.com/workers/previews/configuration/).

Since secrets cannot be stored in the configuration file or version control, use commands to apply [secrets](https://developers.cloudflare.com/workers/previews/configuration/#secrets) to all new Previews or to an individual Preview.

Cloudflare automatically provisions a new [Durable Object namespace](https://developers.cloudflare.com/workers/previews/resources/#durable-objects) and [container instances](https://developers.cloudflare.com/workers/previews/resources/#containers) for each Preview. KV, D1, R2, and other resources are isolated when you bind the Preview to a separate resource. For the full matrix, refer to [Resources and isolation](https://developers.cloudflare.com/workers/previews/resources/).

Workflow bindings use existing Workflows and do not create Preview-specific Workflows. Service bindings from a Preview call the bound Worker's production deployment. Routes and Cron Triggers target production. Queue consumers cannot target a Preview. For details, refer to [Limitations](https://developers.cloudflare.com/workers/previews/resources/#limitations).

### Access control

Preview URLs are public by default. Use [Cloudflare Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/) to require sign-in. You can protect all Previews on an account, one Worker's Previews, or specific hostnames. Details in [Custom domains](https://developers.cloudflare.com/workers/previews/custom-domains/).

### Limits

Limit | Free plan | Paid plans  
---|---|---  
Previews per Worker | 100 | 500  
Deployments per Preview | 100 | 100  
  
When a limit is reached, Cloudflare automatically deletes the oldest to make room:

  * **Preview limit** : the Preview that was deployed to least recently is deleted.
  * **Deployment limit** : the oldest deployment in that Preview is deleted.



You can also delete Previews yourself with `npx wrangler preview delete --name <preview-name>`. For a pull request cleanup example, refer to [Delete closed pull request Previews](https://developers.cloudflare.com/workers/previews/examples/#delete-closed-pull-request-previews).

## Next steps

  * [Get started](https://developers.cloudflare.com/workers/previews/get-started/) \- Set up your first Preview
  * [Configuration](https://developers.cloudflare.com/workers/previews/configuration/) \- Configure variables, secrets, bindings, and Base configuration
  * [Resources and isolation](https://developers.cloudflare.com/workers/previews/resources/) \- Understand which resources are isolated or shared
  * [Limitations](https://developers.cloudflare.com/workers/previews/resources/#limitations) \- Review current support gaps and workarounds



[PreviousSecrets](https://developers.cloudflare.com/workers/configuration/secrets/)[NextGet started](https://developers.cloudflare.com/workers/previews/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/previews/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/
title: Limits & pricing \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:13.063871+00:00
---

# Limits & pricing · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[CI/CD](https://developers.cloudflare.com/workers/ci-cd/)

  4. /[Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  5. /Limits & pricing



# Limits & pricing

Last updated May 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDefinitions

Workers Builds has the following limits.

Metric | Free plan | Paid plans  
---|---|---  
**Build minutes** | 3,000 per month | 6,000 per month (then, +$0.005 per minute)  
**Concurrent builds** | 1 | 6  
**Build timeout** | 20 minutes | 20 minutes  
**Deploy Hooks** | 10/min per Worker, 100/min per account | 10/min per Worker, 100/min per account  
**CPU** | 2 vCPU | 4 vCPU  
**Memory** | 8 GB | 8 GB  
**Disk space** | 20 GB | 20 GB  
**Environment variables** | 64 | 64  
**Size per environment variable** | 5 KB | 5 KB  
  
## Definitions

  * **Build minutes** : The number of minutes that it takes to build a project.
  * **Concurrent builds** : The number of builds that can run in parallel across an account.
  * **Build timeout** : The amount of time that a build can be run before it is terminated.
  * **Deploy Hooks** : The rate limit for builds triggered by [Deploy Hooks](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/).
  * **vCPU** : The number of CPU cores available to your build.
  * **Memory** : The amount of memory available to your build.
  * **Disk space** : The amount of disk space available to your build.
  * **Environment variables** : The number of custom environment variables you can configure per Worker.
  * **Size per environment variable** : The maximum size for each individual environment variable.



[PreviousBuilds API reference](https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/)[NextOverview](https://developers.cloudflare.com/workers/ci-cd/external-cicd/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/builds/limits-and-pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

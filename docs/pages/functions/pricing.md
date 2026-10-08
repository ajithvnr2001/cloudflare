---
url: https://developers.cloudflare.com/pages/functions/pricing/
title: Pricing \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:34.390768+00:00
---

# Pricing · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /[Functions](https://developers.cloudflare.com/pages/functions/)
  4. /Pricing



# Pricing

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/pricing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPaid Plans Static asset requestsFree Plan

Requests to your Functions are billed as Cloudflare Workers requests. Workers plans and pricing can be found [in the Workers documentation](https://developers.cloudflare.com/workers/platform/pricing/).

## Paid Plans

Requests to your Pages functions count towards your quota for Workers Paid plans, including requests from your Function to KV or Durable Object bindings.

Pages supports the [Standard usage model](https://developers.cloudflare.com/workers/platform/pricing/#example-pricing-standard-usage-model).

Note

Workers Enterprise accounts are billed based on the usage model specified in their contract. To switch to the Standard usage model, reach out to your account team. Some Workers Enterprise customers maintain the ability to [change usage models](https://developers.cloudflare.com/workers/platform/pricing/#how-to-switch-usage-models).

### Static asset requests

On both free and paid plans, requests to static assets are free and unlimited. A request is considered static when it does not invoke Functions. Refer to [Functions invocation routes](https://developers.cloudflare.com/pages/functions/routing/#functions-invocation-routes) to learn more about when Functions are invoked.

## Free Plan

Requests to your Pages Functions count towards your quota for the Workers Free plan. For example, you could use 50,000 Functions requests and 50,000 Workers requests to use your full 100,000 daily request usage. The free plan daily request limit resets at midnight UTC.

[PreviousDebugging and logging](https://developers.cloudflare.com/pages/functions/debugging-and-logging/)[NextModule support](https://developers.cloudflare.com/pages/functions/module-support/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

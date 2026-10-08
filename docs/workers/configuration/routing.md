---
url: https://developers.cloudflare.com/workers/configuration/routing/
title: Routes and domains \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:15.594624+00:00
---

# Routes and domains · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/configuration/routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Configuration](https://developers.cloudflare.com/workers/configuration/)
  4. /Routes and domains



# Routes and domains

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/configuration/routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is best for me?

To allow a Worker to receive inbound HTTP requests, you must connect it to an external endpoint such that it can be accessed by the Internet.

There are three types of routes:

  * [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains): Routes to a domain or subdomain (such as `example.com` or `shop.example.com`) within a Cloudflare zone where the Worker is the origin.

  * [Routes](https://developers.cloudflare.com/workers/configuration/routing/routes/): Routes that are set within a Cloudflare zone where your origin server, if you have one, is behind a Worker that the Worker can communicate with.

  * [`workers.dev`](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/): A `workers.dev` subdomain route is automatically created for each Worker to help you getting started quickly. You may choose to [disable](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) your `workers.dev` subdomain.




## What is best for me?

It's recommended to run production Workers on a [Workers route or custom domain](https://developers.cloudflare.com/workers/configuration/routing/), rather than on your `workers.dev` subdomain. Your `workers.dev` subdomain is treated as a [Free website ↗︎](https://www.cloudflare.com/plans/) and is intended for personal or hobby projects that aren't business-critical.

Custom Domains are recommended for use cases where your Worker is your application's origin server. Custom Domains can also be invoked within the same zone via `fetch()`, unlike Routes.

Routes are recommended for use cases where your application's origin server is external to Cloudflare. Note that Routes cannot be the target of a same-zone `fetch()` call.

[PreviousPlacement](https://developers.cloudflare.com/workers/configuration/placement/)[NextCustom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/configuration/routing/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

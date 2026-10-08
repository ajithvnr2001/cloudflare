---
url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/local-development/
title: Local development \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:05.492387+00:00
---

# Local development · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/local-development/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

  4. /Reference
  5. /Local development



# Local development

Last updated Jun 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/local-development/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview How to use remote dispatch namespaces

Test changes to your [dynamic dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker) by running the dynamic dispatch Worker locally but connecting it to user Workers that have been deployed to Cloudflare.

Note

Consider using a staging namespace to test changes safely before deploying to production.

This is helpful when:

  * **Testing routing changes** and validating that updates continue to work with deployed User Workers
  * **Adding new middleware** like authentication, rate limiting, or logging to the dynamic dispatch Worker
  * **Debugging issues** in the dynamic dispatcher that may be impacting deployed User Workers



### How to use remote dispatch namespaces

In the dynamic dispatch Worker's Wrangler file, configure the [dispatch namespace binding](https://developers.cloudflare.com/workers/wrangler/configuration/#dispatch-namespace-bindings-workers-for-platforms) to connect to the remote namespace by setting [`remote = true`](https://developers.cloudflare.com/workers/local-development/#remote-bindings):
    
    
    {
      "dispatch_namespaces": [
        {
          "binding": "DISPATCH_NAMESPACE",
          "namespace": "production",
          "remote": true
    		}
      ]
    }
    
    
    [[dispatch_namespaces]]
    binding = "DISPATCH_NAMESPACE"
    namespace = "production"
    remote = true

This tells your dispatch Worker that's running locally to connect to the remote `production` namespace. When you run `wrangler dev`, your Dispatch Worker will route requests to the User Workers deployed in that namespace.

For more information about remote bindings during local development, refer to [remote bindings documentation](https://developers.cloudflare.com/workers/local-development/#remote-bindings).

[PreviousLimits](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/limits/)[NextPricing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/workers-for-platforms/reference/local-development.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

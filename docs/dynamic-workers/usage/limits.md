---
url: https://developers.cloudflare.com/dynamic-workers/usage/limits/
title: Custom resource limits \u00b7 Cloudflare Dynamic Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:11.751213+00:00
---

# Custom resource limits · Cloudflare Dynamic Workers docs

> Source: https://developers.cloudflare.com/dynamic-workers/usage/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)
  3. /Usage
  4. /Custom resource limits



# Custom resource limits

Last updated Aug 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dynamic-workers/usage/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet custom limits

By default, each Dynamic Worker invocation uses your Workers plan [limits](https://developers.cloudflare.com/workers/platform/limits/#account-plan-limits) for CPU time and subrequests. Custom limits allow you to programmatically enforce lower limits on the Dynamic Worker's resource usage.

You can set limits for the maximum CPU time and number of subrequests per invocation. If a Dynamic Worker hits either of these limits, it will immediately throw an exception.

## Set custom limits

Custom limits can be specified as part of the worker code:
    
    
    const worker = env.LOADER.get("my-worker", async () => {
      return {
        compatibilityDate: "$today",
        mainModule: "index.js",
        modules: { "index.js": code },
        limits: { cpuMs: 10, subRequests: 5 },
      };
    });

They can also be specified as part of the `getEntrypoint()` call:
    
    
    // get the worker's default entrypoint with custom limits
    // if limits were already specified as part of the worker code, the lower of the two limits is used
    const entrypoint = worker.getEntrypoint(null, { limits: { cpuMs: 10, subRequests: 5 } });
    await entrypoint.fetch(...);

[PreviousDurable Object Facets](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/)[NextDynamic Workflows](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dynamic-workers/usage/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/sandbox/sdk/platform/limits/
title: Limits (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:28.173023+00:00
---

# Limits (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Platform](https://developers.cloudflare.com/sandbox/sdk/platform/)
  5. /Limits



# Limits

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewContainer limitsWorkers and Durable Objects limits Subrequest limits Avoid subrequest limits with RPC transportBest practices

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Since the Sandbox SDK is built on top of the [Containers](https://developers.cloudflare.com/containers/) platform, it shares the same underlying platform characteristics. Refer to these pages to understand how pricing and limits work for your sandbox deployments.

Sandbox also inherits current Containers lifecycle, placement, and routing behavior. For more detail, refer to [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/) and [Scaling and Routing](https://developers.cloudflare.com/containers/configuration/scaling-and-routing/).

## Container limits

Refer to [Containers limits](https://developers.cloudflare.com/containers/platform/limits/) for complete details on:

  * Memory, vCPU, and disk limits for concurrent container instances
  * Instance types and their resource allocations
  * Image size and storage limits



## Workers and Durable Objects limits

When using the Sandbox SDK from Workers or Durable Objects, you are subject to [Workers subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests). By default, the SDK uses HTTP transport where each operation (`exec()`, `readFile()`, `writeFile()`, etc.) counts as one subrequest.

### Subrequest limits

  * **Workers Free** : 50 subrequests per request
  * **Workers Paid** : 1,000 subrequests per request



### Avoid subrequest limits with RPC transport

Enable RPC transport to multiplex all SDK calls over a single persistent connection:
    
    
    {
    	"vars": {
    		"SANDBOX_TRANSPORT": "rpc"
    	},
    }
    
    
    [vars]
    SANDBOX_TRANSPORT = "rpc"

With RPC transport enabled:

  * The persistent connection counts as one subrequest
  * All subsequent SDK operations use the existing connection (no additional subrequests)
  * Ideal for workflows with many SDK operations per request



See [Transport modes](https://developers.cloudflare.com/sandbox/sdk/configuration/transport/) for a complete guide.

## Best practices

To work within these limits:

  * **Right-size your instances** \- Choose the appropriate [instance type](https://developers.cloudflare.com/containers/platform/limits/#instance-types) based on your workload requirements
  * **Clean up unused sandboxes** \- Terminate sandbox sessions when they are no longer needed to free up resources
  * **Optimize images** \- Keep your [custom Dockerfiles](https://developers.cloudflare.com/sandbox/sdk/configuration/dockerfile/) lean to reduce image size
  * **Use RPC transport for high-frequency operations** \- Enable `SANDBOX_TRANSPORT=rpc` to avoid subrequest limits when making many SDK calls per request



[PreviousPricing](https://developers.cloudflare.com/sandbox/sdk/platform/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

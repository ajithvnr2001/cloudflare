---
url: https://developers.cloudflare.com/workers/local-development/bindings-per-env/
title: Supported bindings per development mode \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:33.360925+00:00
---

# Supported bindings per development mode · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/local-development/bindings-per-env/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Local development](https://developers.cloudflare.com/workers/local-development/)
  4. /Supported bindings per development mode



# Supported bindings per development mode

Last updated Jun 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/local-development/bindings-per-env/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLocal developmentRemote development

## Local development

**Local simulations** : During local development, your Worker code always executes locally and bindings connect to locally simulated resources [by default](https://developers.cloudflare.com/workers/local-development/#remote-bindings). This is supported in [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

**Remote binding connections:** : Allows you to connect to remote resources on a [per-binding basis](https://developers.cloudflare.com/workers/local-development/#remote-bindings). This is supported in [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

Binding | Local simulations | Remote binding connections  
---|---|---  
**AI** | ❌ | ✅  
**Assets** | ✅ | ❌  
**Analytics Engine** | ✅ | ❌  
**Browser Run** | ✅ | ✅  
**D1** | ✅ | ✅  
**Durable Objects** | ✅ | ❌ 1  
**Containers** | ✅ | ❌  
**Email Bindings** | ✅ | ✅  
**Hyperdrive** | ✅ | ❌  
**Images** | ✅ | ✅  
**KV** | ✅ | ✅  
**Media Transformations** | ❌ | ✅  
**mTLS** | ❌ | ✅  
**Queues** | ✅ | ✅  
**R2** | ✅ | ✅  
**Rate Limiting** | ✅ | ❌  
**Service Bindings (multiple Workers)** | ✅ | ✅  
**Vectorize** | ❌ | ✅  
**Workflows** | ✅ | ❌  
  
## Remote development

During remote development, all of your Worker code is uploaded and executed on Cloudflare's infrastructure, and bindings always connect to remote resources. **We recommend using local development with remote binding connections instead** for faster iteration and debugging.

Supported only in [`wrangler dev --remote`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) \- there is **no Vite plugin equivalent**.

Binding | Remote development  
---|---  
**AI** | ✅  
**Assets** | ✅  
**Analytics Engine** | ✅  
**Browser Run** | ✅  
**D1** | ✅  
**Durable Objects** | ✅  
**Containers** | ❌  
**Email Bindings** | ✅  
**Hyperdrive** | ✅  
**Images** | ✅  
**KV** | ✅  
**Media Transformations** | ✅  
**mTLS** | ✅  
**Queues** | ❌  
**R2** | ✅  
**Rate Limiting** | ✅  
**Service Bindings (multiple Workers)** | ✅  
**Vectorize** | ✅  
**Workflows** | ❌  
  
## Footnotes

  1. Refer to [Using remote resources with Durable Objects and Workflows](https://developers.cloudflare.com/workers/local-development/#using-remote-resources-with-durable-objects-and-workflows) for recommended workarounds. ↩




[PreviousAdding local data](https://developers.cloudflare.com/workers/local-development/local-data/)[NextLocal Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/local-development/bindings-per-env.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

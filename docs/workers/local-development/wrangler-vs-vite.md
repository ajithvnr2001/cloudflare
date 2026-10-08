---
url: https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/
title: Choosing between Wrangler & Vite \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:34.384177+00:00
---

# Choosing between Wrangler & Vite · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Local development](https://developers.cloudflare.com/workers/local-development/)
  4. /Choosing between Wrangler & Vite



# Choosing between Wrangler & Vite

Last updated Jul 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCompare Wrangler and Vite

Wrangler and the Cloudflare Vite plugin both provide local development environments for Workers. Both support backend Workers, local and remote bindings, and multi-Worker applications.

Choose based on the build tools your project uses. You can also use the Vite plugin for development and builds while using Wrangler for deployment and other Workers commands.

## Compare Wrangler and Vite

Capability or workflow | Wrangler | Cloudflare Vite plugin  
---|---|---  
Standalone JavaScript or TypeScript Workers | Supported | Supported  
Full-stack and backend Workers | Supported | Supported  
Local binding simulations via [Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/) | Supported | Supported  
[Remote bindings](https://developers.cloudflare.com/workers/local-development/) | Supported | Supported  
Multi-Worker development | Supported | Supported  
Frontend and server-side rendering frameworks | Use the framework build output | Integrates with Vite-powered frameworks  
Build pipeline | Uses Wrangler's bundler or a custom build | Uses Vite transformations, Hot Module Replacement, and plugins  
Deployment and resource management | Supported | Use Wrangler after `vite build`  
[Rust Workers](https://developers.cloudflare.com/workers/languages/rust/) | Supported | Not supported  
[Python Workers](https://developers.cloudflare.com/workers/languages/python/) | Use [`pywrangler`](https://developers.cloudflare.com/workers/languages/python/) instead of `wrangler` | Not supported  
  
Use the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) when your project already uses Vite or would benefit from its build pipeline. Vite is valid for standalone backend Workers, not only frontend applications.

Use [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) when your project does not use Vite or you want a direct command-line workflow. Wrangler also provides deployment and resource management commands.

For local development that requires deployed resources, both tools support [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings). Your Worker runs locally while selected bindings connect to deployed Cloudflare resources.

For configuration differences when moving an existing project, refer to [Migrating from wrangler dev](https://developers.cloudflare.com/workers/vite-plugin/reference/migrating-from-wrangler-dev/).

[PreviousVite Plugin ↗︎](https://developers.cloudflare.com/workers/vite-plugin/)[NextDeveloping with multiple Workers](https://developers.cloudflare.com/workers/local-development/multi-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/local-development/wrangler-vs-vite.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

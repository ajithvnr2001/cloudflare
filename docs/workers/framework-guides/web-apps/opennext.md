---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/
title: OpenNext adapter \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:28.921801+00:00
---

# OpenNext adapter · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guides

  4. /Web applications
  5. /OpenNext adapter



# OpenNext adapter

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported featuresConfigure OpenNext manually

Recommended path

Cloudflare recommends [vinext](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) instead of OpenNext for new Next.js applications on Cloudflare Workers.

Use this guide to maintain an existing OpenNext application. Migrate to vinext when compatibility allows.

[OpenNext ↗︎](https://opennext.js.org/) adapts the output of `next build` so it can run on different platforms, including Cloudflare Workers.

## Supported features

Most Next.js features are supported by the Cloudflare OpenNext adapter:

Feature | Cloudflare OpenNext adapter | Notes  
---|---|---  
App Router | Supported |   
Pages Router | Supported |   
Route Handlers | Supported |   
React Server Components | Supported |   
Static Site Generation (SSG) | Supported |   
Server-Side Rendering (SSR) | Supported |   
Incremental Static Regeneration (ISR) | Supported |   
Server Actions | Supported |   
Response streaming | Supported |   
Asynchronous work with `next/after` | Supported |   
Middleware | Supported |   
Image optimization | Supported | Supported through [Cloudflare Images](https://developers.cloudflare.com/images/).  
Partial Prerendering (PPR) | Supported | PPR is experimental in Next.js.  
Composable Caching (`"use cache"`) | Supported | Composable Caching is experimental in Next.js.  
Node.js in Middleware | Not yet supported | Node.js middleware introduced in Next.js 15.2 is not yet supported.  
  
For detailed OpenNext documentation, refer to [OpenNext for Cloudflare ↗︎](https://opennext.js.org/cloudflare).

## Configure OpenNext manually

Wrangler automatic configuration uses vinext for Next.js projects. To use OpenNext, configure the adapter manually.

  1. **Install the OpenNext Cloudflare adapter.**

npmyarnpnpmbun
         
         npm i @opennextjs/cloudflare@latest
         
         yarn add @opennextjs/cloudflare@latest
         
         pnpm add @opennextjs/cloudflare@latest
         
         bun add @opennextjs/cloudflare@latest

  2. **Install Wrangler.**

npmyarnpnpmbun
         
         npm i -D wrangler@latest
         
         yarn add -D wrangler@latest
         
         pnpm add -D wrangler@latest
         
         bun add -d wrangler@latest

  3. **Add a Wrangler configuration file.**

In your project root, create a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) with the following content:
         
         {
           "$schema": "./node_modules/wrangler/config-schema.json",
           "name": "my-app",
           "main": ".open-next/worker.js",
           // Set this to today's date
           "compatibility_date": "2026-10-08",
           "compatibility_flags": [
             "nodejs_compat"
           ],
           "assets": {
             "directory": ".open-next/assets",
             "binding": "ASSETS"
           },
           "observability": {
             "enabled": true
           }
         }
         
         name = "my-app"
         main = ".open-next/worker.js"
         # Set this to today's date
         compatibility_date = "2026-10-08"
         compatibility_flags = ["nodejs_compat"]
         
         [assets]
         directory = ".open-next/assets"
         binding = "ASSETS"
         
         [observability]
         enabled = true

Note

You must turn on the [`nodejs_compat` compatibility flag](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) and set your [compatibility date](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) to `2024-09-23` or later.

  4. **Add an OpenNext configuration file.**

In your project root, create `open-next.config.ts`:
         
         import { defineCloudflareConfig } from "@opennextjs/cloudflare";
         
         export default defineCloudflareConfig();

Use this file to configure OpenNext features such as caching. For more information, refer to [OpenNext caching ↗︎](https://opennext.js.org/cloudflare/caching).

  5. **Update`package.json`.**

Add scripts for previewing, deploying, and generating Cloudflare types:
         
         {
           "scripts": {
             "preview": "opennextjs-cloudflare build && opennextjs-cloudflare preview",
             "deploy": "opennextjs-cloudflare build && opennextjs-cloudflare deploy",
             "cf-typegen": "wrangler types --env-interface CloudflareEnv cloudflare-env.d.ts"
           }
         }

Script usage

     * `preview`: Builds your app and serves it locally in the Workers runtime.
     * `deploy`: Builds your app and deploys it to Cloudflare Workers.
     * `cf-typegen`: Generates `cloudflare-env.d.ts` with Cloudflare binding types.
  6. **Develop locally.**

Start the Next.js development server.

npmyarnpnpm
         
         npm run dev
         
         yarn run dev
         
         pnpm run dev

  7. **Preview with OpenNext.**

Preview your application in the Workers runtime.

npmyarnpnpm
         
         npm run preview
         
         yarn run preview
         
         pnpm run preview

  8. **Deploy your project.**

Deploy your project to Cloudflare Workers.

npmyarnpnpm
         
         npm run deploy
         
         yarn run deploy
         
         pnpm run deploy




Workers Builds

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) requires you to configure environment variables in [Build variables and secrets](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-variables-and-secrets).

This ensures the Next.js build has access to both public `NEXT_PUBLIC_` variables and non-public variables required for static generation and server-side build work. For more information, refer to [OpenNext environment variables ↗︎](https://opennext.js.org/cloudflare/howtos/env-vars#workers-builds).

[PreviousNext.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/)[NextVue](https://developers.cloudflare.com/workers/framework-guides/web-apps/vue/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/opennext.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

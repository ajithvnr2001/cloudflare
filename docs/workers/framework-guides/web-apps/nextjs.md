---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/
title: Next.js \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:28.803577+00:00
---

# Next.js · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guides

  4. /Web applications
  5. /Next.js



# Next.js

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is Next.js?What is vinext?Supported featuresChoose a setup pathAdd vinext with an agentAdd vinext with the CLICreate a Cloudflare-ready projectAccess Cloudflare bindingsUse another Next.js deployment path

Use vinext to create or migrate a Next.js application and deploy it to Cloudflare Workers.

Cloudflare recommends [vinext ↗︎](https://vinext.dev/) as the default way to run Next.js applications on Cloudflare Workers. vinext gives you two starting points: scaffold a new Workers-ready app with `create-vinext-app`, or add vinext to an existing Next.js 16 app with a single non-destructive `vinext init` (your existing `next dev` keeps working). You do not need a Cloudflare-specific template either way.

Already on OpenNext? See other Next.js deployment paths.

## What is Next.js?

[Next.js ↗︎](https://nextjs.org/) is a [React ↗︎](https://react.dev/) framework for building full-stack applications.

Next.js supports server-side rendering, client-side rendering, static generation, React Server Components, Server Actions, route handlers, and middleware.

## What is vinext?

[vinext ↗︎](https://github.com/cloudflare/vinext) is a Vite plugin that reimplements the Next.js API surface. You can keep your existing `app/`, `pages/`, `next.config.js`, and `public/` directories while using the Vite toolchain.

vinext is in beta. Before adopting it for an existing production application, run the compatibility check from your project directory and review the [vinext compatibility dashboard ↗︎](https://vinext.dev/compatibility).

npmyarnpnpm
    
    
    npx vinext check
    
    
    yarn dlx vinext check
    
    
    pnpx vinext check

## Supported features

vinext supports most commonly used Next.js features on Cloudflare Workers:

Feature | vinext support | Notes  
---|---|---  
App Router | Supported | Includes layouts, route handlers, metadata, loading, error, and not-found routes.  
Pages Router | Supported | Includes `getStaticProps`, `getStaticPaths`, and `getServerSideProps`.  
React Server Components | Supported | Uses Vite's React Server Components support.  
Server Actions | Supported | Works with forms and server mutations.  
Server-side rendering | Supported | Includes streaming rendering.  
Static generation and static export | Supported | Use `output: "export"` for static exports.  
Incremental Static Regeneration (ISR) | Supported | Uses a stale-while-revalidate caching model so Workers can serve cached content while refreshing it in the background. Refer to [asynchronous revalidation](https://developers.cloudflare.com/cache/concepts/revalidation/#asynchronous-revalidation).  
Middleware and proxy routes | Supported | Includes `middleware.ts` and `proxy.ts`.  
`next/*` imports | Mostly supported | Review the compatibility dashboard for module-level details.  
Cloudflare bindings | Supported | Use `cloudflare:workers` in server components, route handlers, and server actions.  
Image optimization | Partially supported | Cloudflare image optimization is available at request time.  
  
For detailed compatibility results, refer to [vinext compatibility ↗︎](https://vinext.dev/compatibility).

## Choose a setup path

Most Next.js projects can start from the same workflow: open a Next.js app, check compatibility, add vinext, then deploy to Workers.

  * Use Add vinext with an agent if you want an agent to inspect the project and apply the migration.
  * Use Add vinext with the CLI if you want a direct, repeatable command-line setup.
  * Use Create a Cloudflare-ready project if you want to scaffold a new project already configured for Workers.



## Add vinext with an agent

Use the vinext Agent Skill when you want a coding agent to inspect your Next.js project, run compatibility checks, update configuration, and start the vinext development server.

  1. **Open your Next.js project.**

Use an existing project, or create a project with your preferred Next.js setup flow.

  2. **Install the vinext Agent Skill.**

npmyarnpnpm
         
         npx skills add cloudflare/vinext
         
         yarn dlx skills add cloudflare/vinext
         
         pnpx skills add cloudflare/vinext

  3. **Prompt your agent.**

In your coding agent, run the following prompt:
         
         migrate this project to vinext

The skill runs vinext compatibility checks, applies the migration, and flags issues that need manual attention.

  4. **Develop with vinext.**

Start the vinext development server.

npmyarnpnpm
         
         npm run dev:vinext
         
         yarn run dev:vinext
         
         pnpm run dev:vinext

  5. **Build with vinext.**

Build the production output with vinext.

npmyarnpnpm
         
         npm run build:vinext
         
         yarn run build:vinext
         
         pnpm run build:vinext

  6. **Deploy to Workers.**

Deploy with the vinext Cloudflare deploy command.

npmyarnpnpm
         
         npx @vinext/cloudflare deploy
         
         yarn dlx @vinext/cloudflare deploy
         
         pnpx @vinext/cloudflare deploy




## Add vinext with the CLI

Use `vinext init` when you want a direct command-line setup. The migration is non-destructive: your existing Next.js setup continues to work alongside vinext while you test the Cloudflare Workers deployment.

  1. **Open your Next.js project.**

Use an existing project, or create a project with your preferred Next.js setup flow.

  2. **Check compatibility.**

Run the vinext compatibility check from your Next.js project directory.

npmyarnpnpm
         
         npx vinext check
         
         yarn dlx vinext check
         
         pnpx vinext check

Review any reported compatibility issues before continuing.

  3. **Initialize vinext.**

Run the vinext initializer and choose Cloudflare Workers as the deployment target when prompted.

npmyarnpnpm
         
         npx vinext init
         
         yarn dlx vinext init
         
         pnpx vinext init

`vinext init` installs vinext and Vite dependencies, adds vinext scripts, generates the Vite configuration, and creates the Cloudflare Workers configuration.

  4. **Develop with vinext.**

Start the vinext development server.

npmyarnpnpm
         
         npm run dev:vinext
         
         yarn run dev:vinext
         
         pnpm run dev:vinext

  5. **Build with vinext.**

Build the production output with vinext.

npmyarnpnpm
         
         npm run build:vinext
         
         yarn run build:vinext
         
         pnpm run build:vinext

  6. **Deploy to Workers.**

Deploy with the vinext Cloudflare deploy command.

npmyarnpnpm
         
         npx @vinext/cloudflare deploy
         
         yarn dlx @vinext/cloudflare deploy
         
         pnpx @vinext/cloudflare deploy




## Create a Cloudflare-ready project

Use the create-cloudflare CLI (C3) when you want to scaffold a new Next.js project already configured for Cloudflare Workers.

  1. **Create a new project with C3.**

npmyarnpnpm
         
         npm create cloudflare@latest -- my-next-app --framework=next
         
         yarn create cloudflare my-next-app --framework=next
         
         pnpm create cloudflare@latest my-next-app --framework=next

Command behavior

C3 creates a new Next.js project, configures vinext for Cloudflare Workers, installs the required dependencies, and offers to deploy the application.

  2. **Develop with vinext.**

Change to your project directory and start the local development server.

npmyarnpnpm
         
         npm run dev
         
         yarn run dev
         
         pnpm run dev

  3. **Build your application.**

Run the generated build script before deploying or testing a production build.

npmyarnpnpm
         
         npm run build
         
         yarn run build
         
         pnpm run build

  4. **Deploy your project.**

Deploy your project to a [`*.workers.dev` subdomain](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) or a [custom domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/).

npmyarnpnpm
         
         npm run deploy
         
         yarn run deploy
         
         pnpm run deploy




## Access Cloudflare bindings

In vinext applications deployed to Workers, use `cloudflare:workers` to access bindings from server components, route handlers, and server actions. Define bindings in your Wrangler configuration, then generate types with [`wrangler types`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#types).

For example, you can import `env` from `cloudflare:workers` in server-side application code to access D1, R2, KV, Durable Objects, Workers AI, Queues, Vectorize, and other bindings.

## Use another Next.js deployment path

vinext is the recommended path for Next.js applications on Cloudflare Workers, but other deployment paths remain documented:

Path | Use when  
---|---  
[OpenNext adapter](https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/) | You maintain an existing OpenNext application that cannot yet migrate to vinext because of a compatibility gap.  
[Static Next.js on Pages](https://developers.cloudflare.com/pages/framework-guides/nextjs/deploy-a-static-nextjs-site/) | Your application is a static export and you specifically want to deploy it to Cloudflare Pages.  
  
[PreviousReact Router (formerly Remix)](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/)[NextOpenNext adapter](https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/nextjs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/workers/vite-plugin/
title: Vite plugin \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:04.092971+00:00
---

# Vite plugin · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/vite-plugin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Vite plugin



# Vite plugin

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/vite-plugin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesUse casesGet started

The Cloudflare Vite plugin enables a full-featured integration between [Vite ↗︎](https://vite.dev/) and the [Workers runtime](https://developers.cloudflare.com/workers/runtime-apis/). Your Worker code runs inside [workerd ↗︎](https://github.com/cloudflare/workerd), matching the production behavior as closely as possible and providing confidence as you develop and deploy your applications.

## Features

  * Uses the Vite [Environment API ↗︎](https://vite.dev/guide/api-environment) to integrate Vite with the Workers runtime
  * Provides direct access to [Workers runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/) and [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/)
  * Builds your front-end assets for deployment to Cloudflare, enabling you to build static sites, SPAs, and full-stack applications
  * Produces standard Build Output for `cf build` and `cf deploy`
  * Official support for [TanStack Start ↗︎](https://tanstack.com/start/) and [React Router v8 ↗︎](https://reactrouter.com/) with server-side rendering
  * Leverages Vite's hot module replacement for consistently fast updates
  * Supports `vite preview` for previewing your build output in the Workers runtime prior to deployment



## Use cases

  * [TanStack Start ↗︎](https://tanstack.com/start/)
  * [React Router v8 ↗︎](https://reactrouter.com/)
  * Static sites, such as single-page applications, with or without an integrated backend API
  * Standalone Workers
  * Multi-Worker applications



## Get started

To create a new application from a ready-to-go template, refer to the [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/), [React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/), [React](https://developers.cloudflare.com/workers/framework-guides/web-apps/react/) or [Vue](https://developers.cloudflare.com/workers/framework-guides/web-apps/vue/) framework guides.

To create a standalone Worker from scratch, refer to [Get started](https://developers.cloudflare.com/workers/vite-plugin/get-started/).

For a more in-depth look at adapting an existing Vite project and an introduction to key concepts, refer to the [Tutorial](https://developers.cloudflare.com/workers/vite-plugin/tutorial/).

[PreviousEnvironment variables and secrets](https://developers.cloudflare.com/workers/local-development/environment-variables/)[NextChoosing between Wrangler & Vite](https://developers.cloudflare.com/workers/local-development/wrangler-vs-vite/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/vite-plugin/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

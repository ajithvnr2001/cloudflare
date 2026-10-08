---
url: https://developers.cloudflare.com/changelog/post/2026-01-01-microfrontends/
title: Build microfrontend applications on Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:32.830298+00:00
---

# Build microfrontend applications on Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-01-microfrontends/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 1, 2026

## Build microfrontend applications on Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-01-microfrontends/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now deploy microfrontends to Cloudflare, splitting a single application into smaller, independently deployable units that render as one cohesive application. This lets different teams using different frameworks develop, test, and deploy each microfrontend without coordinating releases.

Microfrontends solve several challenges for large-scale applications:

  * **Independent deployments** : Teams deploy updates on their own schedule without redeploying the entire application
  * **Framework flexibility** : Build multi-framework applications (for example, Astro, Remix, and Next.js in one app)
  * **Gradual migration** : Migrate from a monolith to a distributed architecture incrementally



Create a microfrontend project:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe)

This template automatically creates a router worker with pre-configured routing logic, and lets you configure [Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) to Workers you have already deployed to your Cloudflare account. The router Worker analyzes incoming requests, matches them against configured routes, and forwards requests to the appropriate microfrontend via service bindings. The router automatically rewrites HTML, CSS, and headers to ensure assets load correctly from each microfrontend's mount path. The router includes advanced features like preloading for faster navigation between microfrontends, smooth page transitions using the View Transitions API, and automatic path rewriting for assets, redirects, and cookies.

Each microfrontend can be a full-framework application, a static site with Workers Static Assets, or any other Worker-based application.

Get started with the [microfrontends template ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe), or read the [microfrontends documentation](https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/) for implementation details.

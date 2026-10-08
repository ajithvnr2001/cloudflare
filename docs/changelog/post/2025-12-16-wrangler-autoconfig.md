---
url: https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/
title: Configure your framework for Cloudflare automatically \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:32.291500+00:00
---

# Configure your framework for Cloudflare automatically · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 16, 2025

## Configure your framework for Cloudflare automatically

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now supports automatic configuration for popular web frameworks in experimental mode, making it even easier to deploy to Cloudflare Workers.

Previously, if you wanted to deploy an application using a popular web framework like Next.js or Astro, you had to follow tutorials to set up your application for deployment to Cloudflare Workers. This usually involved creating a Wrangler file, installing adapters, or changing configuration options.

Now `wrangler deploy` does this for you. Starting with Wrangler 4.55, you can use `npx wrangler deploy --x-autoconfig` in the directory of any web application using one of the supported frameworks. Wrangler will then proceed to configure and deploy it to your Cloudflare account.

You can also configure your application without deploying it by using the new `npx wrangler setup` command. This enables you to easily review what changes we are making so your application is ready for Cloudflare Workers.

The following application frameworks are supported starting today:

  * Next.js
  * Astro
  * Nuxt
  * TanStack Start
  * SolidStart
  * React Router
  * SvelteKit
  * Docusaurus
  * Qwik
  * Analog



Automatic configuration also supports static sites by detecting the assets directory and build command. From a single index.html file to the output of a generator like Jekyll or Hugo, you can just run `npx wrangler deploy --x-autoconfig` to upload to Cloudflare.

We're really excited to bring you automatic configuration so you can do more with Workers. Please let us know if you run into challenges using this experimentally. We’ve opened a [GitHub discussion ↗︎](https://github.com/cloudflare/workers-sdk/discussions/11667) and would love to hear your feedback.

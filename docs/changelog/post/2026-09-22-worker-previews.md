---
url: https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/
title: Test every pull request in an isolated environment with Worker Previews \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:15.836361+00:00
---

# Test every pull request in an isolated environment with Worker Previews · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 22, 2026

## Test every pull request in an isolated environment with Worker Previews

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now test every change you make in an isolated, production-like environment with [Worker Previews ↗︎](https://blog.cloudflare.com/worker-previews/). [Each Preview](https://developers.cloudflare.com/workers/previews/) runs under the same Worker with its own code, configuration, URL, and observability, isolated from production and every other Preview.

#### Configure each Preview

Define the variables, bindings, and settings that new Previews start with in the [`previews` block of your Wrangler configuration file](https://developers.cloudflare.com/workers/previews/configuration/). Set secrets with Wrangler commands. You can override one Preview without changing production or other Previews.

For [Durable Objects](https://developers.cloudflare.com/workers/previews/resources/#durable-objects) and [Containers](https://developers.cloudflare.com/workers/previews/resources/#containers), Cloudflare automatically provisions separate namespaces, storage, apps, and instances for every Preview. State changes, sessions, memory, migrations, and concurrent tests remain scoped to that Preview. To isolate KV, D1, R2, or another account-level resource, [bind the Preview to a separate resource](https://developers.cloudflare.com/workers/previews/resources/).

![Diagram comparing production with three Previews, each with its own URL, code, configuration, and Durable Object state](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1370,format=webp/_astro/preview-resource-isolation.CyeUXRJS.png)

#### Deploy and share every change

Use Wrangler 4.135.0 or later to [deploy a Preview](https://developers.cloudflare.com/workers/previews/get-started/):
    
    
    npx wrangler preview

Or [connect your repository to Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-preview-builds) to create Previews automatically and post their URLs to pull requests.

Each Preview gets a [stable URL](https://developers.cloudflare.com/workers/previews/#urls) that updates with every push, so reviewers always see the latest changes. Each deployment also gets an immutable URL, so you can compare or return to an exact version.

After you create a Preview, use the environment breadcrumb next to your Worker's name to switch between Production and every Preview:

![Worker dashboard showing the Preview dropdown and an overview of bindings, metrics, and deployments](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2386,height=1304,format=webp/_astro/previews-dash-overview.BL1UHZHT.png)

#### Inspect and revise before production

Each Preview has its own [logs, errors, metrics, and traces](https://developers.cloudflare.com/workers/previews/test-and-debug/). Send traffic to its URL, inspect what happened, push a fix, and verify the next deployment before production.

![Preview Observability tab showing success and error events for a pull request](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1418,height=1236,format=webp/_astro/preview-observability.COYT0y5H.png)

#### Use production-like hostnames

Serve Preview URLs on `workers.dev`, a [custom domain](https://developers.cloudflare.com/workers/previews/custom-domains/), or both. Custom domains let authentication providers, cookies, cross-origin resource sharing (CORS), and OAuth redirects work as they will in production. You can also protect Preview URLs with Cloudflare Access.

Configure a domain for Preview traffic from the Worker's **Domains** tab:

![Domains tab showing a custom domain configured for Preview traffic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2876,height=1454,format=webp/_astro/customdomainonly.8AG_6tc-.png)

For setup instructions and current limitations, refer to the [Worker Previews documentation](https://developers.cloudflare.com/workers/previews/).

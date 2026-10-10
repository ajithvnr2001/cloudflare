---
url: https://developers.cloudflare.com/changelog/product/workers-for-platforms/
title: Workers for Platforms Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:02.323017+00:00
---

# Workers for Platforms Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/workers-for-platforms/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Dec 18, 2025

## [Workers for Platforms - Dashboard Improvements](https://developers.cloudflare.com/changelog/post/2025-12-18-dashboard-improvements/)

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) lets you build multi-tenant platforms on [Cloudflare Workers](https://developers.cloudflare.com/workers/), allowing your end users to deploy and run their own code on your platform. It's designed for anyone building an AI vibe coding platform, e-commerce platform, website builder, or any product that needs to securely execute user-generated code at scale.

Previously, setting up Workers for Platforms required using the API. Now, the Workers for Platforms UI supports namespace creation, dispatch worker templates, and tag management, making it easier for Workers for Platforms customers to build and manage multi-tenant platforms directly from the Cloudflare dashboard.

![Workers for Platforms Dashboard Improvements](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2226,height=1364,format=webp/_astro/dashboard-improvements.ChVWUo88.png)

#### Key improvements

  * **Namespace Management:** You can now create and configure [dispatch namespaces](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace) directly within the dashboard to start a new platform setup.
  * **Dispatch Worker Templates:** New Dispatch Worker templates allow you to quickly define how traffic is routed to individual Workers within your namespace. Refer to the [Dynamic Dispatch documentation](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/) for more examples.
  * **Tag Management:** You can now set and update [tags](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/) on User Workers, making it easier to group and manage your Workers.
  * **Binding Visibility:** [Bindings](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/) attached to User Workers are now visible directly within the User Worker view.
  * **Deploy Vibe Coding Platform in one-click:** Deploy a [reference implementation](https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-vibe-coding-platform/) of an AI vibe coding platform directly from the dashboard. Powered by the Cloudflare's [VibeSDK ↗︎](https://github.com/cloudflare/vibesdk), this starter kit integrates with Workers for Platforms to handle the deployment of AI-generated projects at scale.



To get started, go to **Workers for Platforms** under **Compute & AI** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/).

Sep 4, 2025

## [Increased static asset limits for Workers](https://developers.cloudflare.com/changelog/post/2025-09-02-increased-static-asset-limits/)

[Workers](https://developers.cloudflare.com/workers/)[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

You can now upload up to **100,000 static assets** per Worker version

  * Paid and Workers for Platforms users can now upload up to **100,000 static assets** per Worker version, a 5x increase from the previous limit of 20,000.
  * Customers on the free plan still have the same limit as before — 20,000 static assets per version of your Worker
  * The individual file size limit of 25 MiB remains unchanged for all customers.



This increase allows you to build larger applications with more static assets without hitting limits.

#### Wrangler

To take advantage of the increased limits, you must use **Wrangler version 4.34.0 or higher**. Earlier versions of Wrangler will continue to enforce the previous 20,000 file limit.

#### Learn more

For more information about Workers static assets, see the [Static Assets documentation](https://developers.cloudflare.com/workers/static-assets/) and [Platform Limits](https://developers.cloudflare.com/workers/platform/limits/#static-assets).

Jun 19, 2025

## [Automate Worker deployments with a simplified SDK and more reliable Terraform provider](https://developers.cloudflare.com/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/)

[D1](https://developers.cloudflare.com/d1/)[Workers](https://developers.cloudflare.com/workers/)[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

#### Simplified Worker Deployments with our SDKs

We've simplified the programmatic deployment of Workers via our [Cloudflare SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/). This update abstracts away the low-level complexities of the `multipart/form-data` upload process, allowing you to focus on your code while we handle the deployment mechanics.

This new interface is available in:

  * [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript) (4.4.1)
  * [cloudflare-python ↗︎](https://github.com/cloudflare/cloudflare-python) (4.3.1)



For complete examples, see our guide on [programmatic Worker deployments](https://developers.cloudflare.com/workers/platform/infrastructure-as-code).

#### The Old way: Manual API calls

Previously, deploying a Worker programmatically required manually constructing a `multipart/form-data` HTTP request, packaging your code and a separate `metadata.json` file. This was more complicated and verbose, and prone to formatting errors.

For example, here's how you would upload a Worker script previously with cURL:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/<account_id>/workers/scripts/my-hello-world-script \
      -X PUT \
      -H 'Authorization: Bearer <api_token>' \
      -F 'metadata={
            "main_module": "my-hello-world-script.mjs",
            "bindings": [
              {
                "type": "plain_text",
                "name": "MESSAGE",
                "text": "Hello World!"
              }
            ],
            "compatibility_date": "$today"
          };type=application/json' \
      -F 'my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module' <<EOF
    export default {
      async fetch(request, env, ctx) {
        return new Response(env.MESSAGE, { status: 200 });
      }
    };
    EOF

#### After: SDK interface

With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.

This approach allows you to specify metadata like `main_module`, `bindings`, and `compatibility_date` as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.

Here's how you can now programmatically deploy a Worker via the [`cloudflare-typescript` SDK ↗︎](https://github.com/cloudflare/cloudflare-typescript)
    
    
    import Cloudflare from "cloudflare";
    import { toFile } from "cloudflare/index";
    
    // ... client setup, script content, etc.
    
    const script = await client.workers.scripts.update(scriptName, {
    	account_id: accountID,
    	metadata: {
    		main_module: scriptFileName,
    		bindings: [],
    	},
    	files: {
    		[scriptFileName]: await toFile(Buffer.from(scriptContent), scriptFileName, {
    			type: "application/javascript+module",
    		}),
    	},
    });
    
    
    import Cloudflare from 'cloudflare';
    import { toFile } from 'cloudflare/index';
    
    // ... client setup, script content, etc.
    
    const script = await client.workers.scripts.update(scriptName, {
      account_id: accountID,
      metadata: {
        main_module: scriptFileName,
        bindings: [],
      },
      files: {
        [scriptFileName]: await toFile(Buffer.from(scriptContent), scriptFileName, {
          type: 'application/javascript+module',
        }),
      },
    });

View the complete example here: <https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts>[ ↗︎](https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts)

#### Terraform provider improvements

We've also made several fixes and enhancements to the [Cloudflare Terraform provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare):

  * Fixed the [`cloudflare_workers_script` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) resource in Terraform, which previously was producing a diff even when there were no changes. Now, your `terraform plan` outputs will be cleaner and more reliable.
  * Fixed the [`cloudflare_workers_for_platforms_dispatch_namespace` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace), where the provider would attempt to recreate the namespace on a `terraform apply`. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.
  * The [`cloudflare_workers_route` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route) resource now allows for the `script` property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes [docs](https://developers.cloudflare.com/workers/configuration/routing/routes)). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.
  * Using `primary_location_hint` in the [`cloudflare_d1_database` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database) resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.



#### API improvements

We've also properly documented the [Workers Script And Version Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/script_and_version_settings) in our public OpenAPI spec and SDKs.

Apr 15, 2025

## [Fixed and documented Workers Routes and Secrets API](https://developers.cloudflare.com/changelog/post/2025-04-15-workers-api-fixes/)

[Workers](https://developers.cloudflare.com/workers/)[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

#### Workers Routes API

Previously, a request to the Workers [Create Route API](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/create/) always returned `null` for "script" and an empty string for "pattern" even if the request was successful.

Example requestbash
    
    
    curl https://api.cloudflare.com/client/v4/zones/$CF_ACCOUNT_ID/workers/routes \
    -X PUT \
    -H "Authorization: Bearer $CF_API_TOKEN" \
    -H 'Content-Type: application/json' \
    --data '{ "pattern": "example.com/*", "script": "hello-world-script" }'

Example bad responsejson
    
    
    {
    	"result": {
    		"id": "bf153a27ba2b464bb9f04dcf75de1ef9",
    		"pattern": "",
    		"script": null,
    		"request_limit_fail_open": false
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

Now, it properly returns all values!

Example good responsejson
    
    
    {
    	"result": {
    		"id": "bf153a27ba2b464bb9f04dcf75de1ef9",
    		"pattern": "example.com/*",
    		"script": "hello-world-script",
    		"request_limit_fail_open": false
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

#### Workers Secrets API

The [Workers](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/) and [Workers for Platforms](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/) secrets APIs are now properly documented in the Cloudflare OpenAPI docs. Previously, these endpoints were not publicly documented, leaving users confused on how to directly manage their secrets via the API. Now, you can find the proper endpoints in our public documentation, as well as in our API Library SDKs such as [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript) (>4.2.0) and [cloudflare-python ↗︎](https://github.com/cloudflare/cloudflare-python) (>4.1.0).

Note the `cloudflare_workers_secret` and `cloudflare_workers_for_platforms_script_secret` [Terraform resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) are being removed in a future release. This resource is not recommended for managing secrets. Users should instead use the:

  * [Secrets Store](https://developers.cloudflare.com/api/resources/secrets_store/) with the "Secrets Store Secret" binding on Workers and Workers for Platforms Script Upload
  * "Secret Text" Binding on [Workers Script Upload](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/update/) and [Workers for Platforms Script Upload](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/)
  * Workers (and WFP) Secrets API



Apr 8, 2025

## [Full-stack frameworks are now Generally Available on Cloudflare Workers](https://developers.cloudflare.com/changelog/post/2025-04-08-fullstack-on-workers/)

[Workers](https://developers.cloudflare.com/workers/)[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

![Full-stack on Cloudflare Workers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=675,format=webp/_astro/fullstack-on-workers.D7fotYu2.png)

The following full-stack frameworks now have Generally Available ("GA") adapters for Cloudflare Workers, and are ready for you to use in production:

  * [React Router v7 (Remix)](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/)
  * [Astro](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/)
  * [Hono](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/)
  * [Vue.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/vue/)
  * [Nuxt](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/nuxt/)
  * [Svelte (SvelteKit)](https://developers.cloudflare.com/workers/framework-guides/web-apps/sveltekit/)
  * And [more](https://developers.cloudflare.com/workers/framework-guides/).



The following frameworks are now in **beta** , with GA support coming very soon:

  * [Next.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/), supported through [@opennextjs/cloudflare ↗︎](https://opennext.js.org/cloudflare) is now `v1.0-beta`.
  * [Angular](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/angular/)
  * [SolidJS (SolidStart)](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/solid/)



You can also build complete full-stack apps on Workers **without a framework** :

  * You can [“just use Vite" ↗︎](https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin) and React together, and build a back-end API in the same Worker. Follow our [React SPA with an API tutorial](https://developers.cloudflare.com/workers/vite-plugin/tutorial/) to learn how.



**Get started building today with our[framework guides](https://developers.cloudflare.com/workers/framework-guides/)**, or read our [Developer Week 2025 blog post ↗︎](https://blog.cloudflare.com/full-stack-development-on-cloudflare-workers) about all the updates to building full-stack applications on Workers.

Feb 20, 2025

## [Workers for Platforms - Instant dispatch for newly created User Workers](https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/)

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

[Workers for Platforms ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/) is an architecture wherein a centralized [dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker) processes incoming requests and routes them to isolated sub-Workers, called [User Workers](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers).

![Workers for Platforms Requests](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=711,format=webp/_astro/wfp-request.CZmZLaYf.png)

Previously, when a new User Worker was uploaded, there was a short delay before it became available for dispatch. This meant that even though an API request could return a 200 OK response, the script might not yet be ready to handle requests, causing unexpected failures for platforms that immediately dispatch to new Workers.

**With this update, first-time uploads of User Workers are now deployed synchronously**. A 200 OK response guarantees the script is fully provisioned and ready to handle traffic immediately, ensuring more predictable deployments and reducing errors.

Jan 31, 2025

## [Workers for Platforms now supports Static Assets](https://developers.cloudflare.com/changelog/post/2025-01-31-workers-platforms-static-assets/)

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Workers for Platforms customers can now attach static assets (HTML, CSS, JavaScript, images) directly to User Workers, removing the need to host separate infrastructure to serve the assets.

This allows your platform to serve entire front-end applications from Cloudflare's global edge, utilizing caching for fast load times, while supporting dynamic logic within the same Worker. Cloudflare automatically scales its infrastructure to handle high traffic volumes, enabling you to focus on building features without managing servers.

#### What you can build

**Static Sites:** Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites because static assets can be efficiently cached and delivered closer to the user, reducing latency and enhancing the overall user experience.

**Full-Stack Applications:** Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. If you're an e-commerce platform, you can serve your customers' product pages and run inventory checks from within the same Worker.

index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    
    		// Check real-time inventory
    		if (url.pathname === "/api/inventory/check") {
    			const product = url.searchParams.get("product");
    			const inventory = await env.INVENTORY_KV.get(product);
    			return new Response(inventory);
    		}
    
    		// Serve static assets (HTML, CSS, images)
    		return env.ASSETS.fetch(request);
    	},
    };

index.tsts
    
    
    export default {
      async fetch(request, env) {
        const url = new URL(request.url);
    
        // Check real-time inventory
        if (url.pathname === '/api/inventory/check') {
          const product = url.searchParams.get('product');
          const inventory = await env.INVENTORY_KV.get(product);
          return new Response(inventory);
        }
    
        // Serve static assets (HTML, CSS, images)
        return env.ASSETS.fetch(request);
      }
    };

**Get Started:** Upload static assets using the Workers for Platforms API or Wrangler. For more information, visit our [Workers for Platforms documentation. ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/)

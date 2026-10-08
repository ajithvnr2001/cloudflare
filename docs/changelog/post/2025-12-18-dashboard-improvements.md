---
url: https://developers.cloudflare.com/changelog/post/2025-12-18-dashboard-improvements/
title: Workers for Platforms - Dashboard Improvements \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:32.159072+00:00
---

# Workers for Platforms - Dashboard Improvements · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-18-dashboard-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 18, 2025

## Workers for Platforms - Dashboard Improvements

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-18-dashboard-improvements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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

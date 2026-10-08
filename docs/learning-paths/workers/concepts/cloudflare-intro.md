---
url: https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/
title: Introduction to Cloudflare \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:01.994278+00:00
---

# Introduction to Cloudflare · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Workers

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/workers/concepts/)
  5. /Introduction to Cloudflare



# Introduction to Cloudflare

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCloudflare Developer PlatformBuilt on CloudflareBuilt with CloudflareSummary

[Cloudflare ↗︎](https://www.cloudflare.com/learning/what-is-cloudflare/) is a global network of [servers ↗︎](https://www.cloudflare.com/learning/cdn/glossary/edge-server/). It is one of the largest [networks ↗︎](https://www.cloudflare.com/network/) on the Internet.

Cloudflare's product offering is composed of [SASE and SSE services ↗︎](https://www.cloudflare.com/zero-trust/), [application ↗︎](https://www.cloudflare.com/application-services/) and [infrastructure services ↗︎](https://www.cloudflare.com/network-services/), and [Developer Platform ↗︎](https://www.cloudflare.com/developer-platform/solutions/).

Cloudflare's products offer something to developers, private and public organizations, businesses, governments, and individual consumers.

## Cloudflare Developer Platform

The [Cloudflare Developer Platform ↗︎](https://www.cloudflare.com/developer-platform/products/) includes [Cloudflare Workers](https://developers.cloudflare.com/workers/), which allows you to deploy serverless code instantly across the globe. You will learn more about [the Developer Platform in this module](https://developers.cloudflare.com/learning-paths/workers/devplat/).

## Built on Cloudflare

If your application is built on Cloudflare, then Cloudflare would act as the origin server of your application.

An example tech stack for an application built on Cloudflare would look like:

  * [Domain Registrar](https://developers.cloudflare.com/registrar/) to buy a new domain.
  * [Cloudflare Pages](https://developers.cloudflare.com/pages/) to configure and deploy a front-end site.
  * [Cloudflare Workers](https://developers.cloudflare.com/workers/) or [Pages Functions](https://developers.cloudflare.com/pages/functions/) (which are Workers under the hood) to add dynamic functionality to your site.
  * [Storage resources](https://developers.cloudflare.com/workers/platform/storage-options/) to persist different types of data.
  * [Application security (DDoS protection, WAF, and more) ↗︎](https://www.cloudflare.com/application-services/products/#security-services) to secure your site.
  * [Application performance (CDN, Load Balancing, and more) ↗︎](https://www.cloudflare.com/application-services/products/#performance-services) to customize and enhance your site's performance.
  * [AI](https://developers.cloudflare.com/use-cases/ai/) to run machine learning models.



And more depending on your use case.

## Built with Cloudflare

When you add your application to Cloudflare, Cloudflare's global network of servers will sit in between requests to your application and your application's [origin server ↗︎](https://www.cloudflare.com/learning/cdn/glossary/origin-server/).

![Cloudflare sits in between requests and your origin server.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=419,format=svg/_astro/website-with-cloudflare.D3VGvGsa.svg)

After you add your application to [Cloudflare](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/), you can:

  * Use Workers to augment the application by deploying code.
  * Add storage resources available on the Developer Platform.
  * Enhance your application's performance by speeding up content delivery and user experience ([CDN ↗︎](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)).
  * Protect your website from malicious activity ([DDoS ↗︎](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) by configuring the [Web Application Firewall ↗︎](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)).
  * Route traffic ([Load balancing](https://developers.cloudflare.com/load-balancing/), [Waiting Room](https://developers.cloudflare.com/waiting-room/)).



And more depending on your use case.

## Summary

By reading this page, you have:

  * Learned the scale of Cloudflare's global network.
  * Explored the product offering to know what Cloudflare can offer for users like you.
  * Reviewed how you can build your applications with Cloudflare and Cloudflare Workers.



In the next section, you will be introduced to the fundamentals of serverless computing, the concept behind Cloudflare Workers.

[PreviousOverview](https://developers.cloudflare.com/learning-paths/workers/concepts/)[NextServerless computing](https://developers.cloudflare.com/learning-paths/workers/concepts/serverless-computing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/workers/concepts/cloudflare-intro.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

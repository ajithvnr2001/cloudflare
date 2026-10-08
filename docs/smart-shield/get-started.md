---
url: https://developers.cloudflare.com/smart-shield/get-started/
title: Get started \u00b7 Cloudflare Smart Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:32.745050+00:00
---

# Get started · Cloudflare Smart Shield docs

> Source: https://developers.cloudflare.com/smart-shield/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Smart Shield](https://developers.cloudflare.com/smart-shield/)
  3. /Get started



# Get started

Last updated Jun 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/smart-shield/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginStepsPackages and availability Smart Shield Smart Shield + Argo Smart Shield Advanced Smart Shield Smart Shield + Argo Smart Shield AdvancedFurther reading

Smart Shield reduces the load on your origin server and improves content delivery by consolidating requests through Cloudflare's caching infrastructure. It is available to all customers as an opt-in configuration.

## Before you begin

  * You must have a Cloudflare account and [onboard your domain](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/).
  * Verify that DNS records for the domain you want to protect are set to [proxied](https://developers.cloudflare.com/dns/proxy-status/). Smart Shield operates within Cloudflare's reverse proxy, so traffic from DNS-only records is not routed through it.



## Steps

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), and select your account and domain.
  2. Go to **Speed** > **Smart Shield**.
  3. (Optional) Explore the different available packages.
  4. Select **Get started for free** or choose a different package and select **Continue** to proceed to the guided onboarding flow.



After setup, you can monitor origin performance and cache effectiveness through the [Observatory](https://developers.cloudflare.com/speed/observatory/) dashboard.

## Packages and availability

Pro, Business, and Enterprise customers have access to [Health Checks](https://developers.cloudflare.com/smart-shield/configuration/health-checks/) for monitoring origin availability across all packages.

Enterprise customers have access to all Smart Shield packages, including Smart Shield Advanced.

### Smart Shield

The base package for reducing origin load through caching and connection optimization.

  * Includes [Smart Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/) and [Connection Reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/).



### Smart Shield + Argo

Adds network path optimization on top of the base package. Use when visitors are geographically distant from the origin server.

  * Includes [Smart Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/), [Connection Reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/), and [Argo Smart Routing](https://developers.cloudflare.com/smart-shield/configuration/argo/).



### Smart Shield Advanced

The full package with additional caching customization through regional and persistent storage options.

  * Includes [Smart Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/), [Connection Reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/), [Argo Smart Routing](https://developers.cloudflare.com/smart-shield/configuration/argo/), [Regional Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/), and [Cache Reserve](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/).



Enterprise customers have access to [Regional Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/) as part of their plan, regardless of which Smart Shield package they use.

Enterprise customers also have the option to configure [Dedicated CDN Egress IPs](https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/), allowing you to increase origin security by only allowing traffic from a small list of IP addresses. If you are interested, reach out to your account team.

Free, Pro, and Business customers can purchase Smart Shield and Smart Shield + Argo packages.

### Smart Shield

The base package for reducing origin load through caching and connection optimization.

  * Includes [Smart Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/) and [Connection Reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/).



### Smart Shield + Argo

Adds network path optimization on top of the base package. Use when visitors are geographically distant from the origin server.

  * Includes [Smart Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/), [Connection Reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/), and [Argo Smart Routing](https://developers.cloudflare.com/smart-shield/configuration/argo/).



### Smart Shield Advanced

Smart Shield Advanced is not currently available for Free, Pro, and Business customers. If you are interested in Smart Shield Advanced features such as [Regional Tiered Cache](https://developers.cloudflare.com/smart-shield/configuration/regional-tiered-cache/) and [Cache Reserve](https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/), contact our [Enterprise Sales team ↗︎](https://www.cloudflare.com/resource/contact-enterprise-sales/).

## Further reading

  * [Network diagram](https://developers.cloudflare.com/smart-shield/concepts/network-diagram/)
  * [Connection reuse](https://developers.cloudflare.com/smart-shield/concepts/connection-reuse/)



[PreviousOverview](https://developers.cloudflare.com/smart-shield/)[NextNetwork diagram](https://developers.cloudflare.com/smart-shield/concepts/network-diagram/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/smart-shield/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

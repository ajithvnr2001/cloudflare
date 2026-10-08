---
url: https://developers.cloudflare.com/style-guide/how-we-docs/our-site/
title: Our site \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:12.011811+00:00
---

# Our site · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/how-we-docs/our-site/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /[How we docs](https://developers.cloudflare.com/style-guide/how-we-docs/)
  4. /Our site



# Our site

Last updated Sep 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/how-we-docs/our-site/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewContent management systemSearchSite frameworkBuildsHostingAnalytics

We use a variety of tools to make our docs site work. You could use these tools to build up your own docs site and - in most cases - do so for free or starting on a free tier.

## Content management system

Our content lives in a public GitHub repository, [`cloudflare-docs` ↗︎](https://github.com/cloudflare/cloudflare-docs).

GitHub offers a generous [free tier ↗︎](https://github.com/pricing).

## Search

We use Cloudflare's [AI Search](https://developers.cloudflare.com/ai-search/) as our search provider.

We used to use Algolia, which is also great for open-source docs because you can be part of the free [DocSearch program ↗︎](https://docsearch.algolia.com/).

## Site framework

We use [Nimbus ↗︎](https://nimbus-docs.com/) for our docs, a documentation framework built on [Astro ↗︎](https://astro.build/).

Nimbus's component [registry ↗︎](https://nimbus-docs.com/registry/) and [linting ↗︎](https://nimbus-docs.com/writing/linting/) system have exponentially increased our [site's capabilities](https://developers.cloudflare.com/style-guide/build-the-page/components/) (without much extra work).

## Builds

We use [GitHub Actions ↗︎](https://github.com/features/actions) to build our site, which is then hosted on Cloudflare.

We are moving to [Workers CI/CD](https://developers.cloudflare.com/workers/ci-cd/), which currently runs in the background.

Both of these options include a free tier.

## Hosting

We host our content using [Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/), specifically using their built in values for [Astro sites](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/)

Workers offers a generous [free tier](https://developers.cloudflare.com/workers/platform/pricing/).

## Analytics

We send analytics to multiple destinations using [Cloudflare Zaraz](https://developers.cloudflare.com/zaraz/), which has a generous [free tier](https://developers.cloudflare.com/zaraz/pricing-info/).

Note

If you want to opt out of analytics tracking, use the icon at the bottom of your screen.

![Opt out of analytics with the icon at the bottom of your screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=755,height=88,format=webp/_astro/privacy-opt-out.Cthj3AFl.png)

[PreviousMetadata](https://developers.cloudflare.com/style-guide/how-we-docs/metadata/)[NextRedirects](https://developers.cloudflare.com/style-guide/how-we-docs/redirects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/how-we-docs/our-site.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

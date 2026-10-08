---
url: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/
title: Rocket Loader \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:34.656364+00:00
---

# Rocket Loader · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

Settings

  4. /Content optimizations
  5. /Rocket Loader



# Rocket Loader

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow toAvailabilityLimitations

Rocket Loader prioritizes your website's content (text, images, fonts, and more) by deferring the loading of all of your JavaScript until after rendering.

This type of loading (known as asynchronous loading) leads to earlier rendering of your page content. Rocket Loader handles both inline and external scripts, while maintaining order of execution. Cloudflare will detect incompatible browsers and disable Rocket Loader.

On pages with JavaScript, this results in a [much faster loading experience ↗︎](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/) for your users and improves the following performance metrics:

  * Time to First Paint (TTFP)
  * Time to First Contentful Paint (TTFCP)
  * Time to First Meaningful Paint (TTFMP)
  * Document Load



## How to

  * [Enable](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/)
  * [Ignore JavaScripts](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/)



## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## Limitations

Some of Cloudflare's optional features, including Rocket Loader and Email Obfuscation, use non standard tags that fail strict HTML validation via tools like [w3.org ↗︎](https://validator.w3.org/). These failures do not correlate to issues for your site visitors.

If you observe JavaScript or jQuery issues for your website, [disable Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/) and retest your website.

If you have a Content Security Policy (CSP) in place for your domain, you will need to [update your headers](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/#product-requirements) to support Rocket Loader.

  


[PreviousPrefetch URLs](https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/)[NextEnable](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/content/rocket-loader/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/
title: Web Analytics for Single Page Applications (SPAs) \u00b7 Cloudflare Web Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:53.650323+00:00
---

# Web Analytics for Single Page Applications (SPAs) · Cloudflare Web Analytics docs

> Source: https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)
  3. /[Get started](https://developers.cloudflare.com/web-analytics/get-started/)
  4. /Web Analytics for SPAs



# Web Analytics for SPAs

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDisable SPA measurement Google Tag Manager (GTM)

Cloudflare Web Analytics automatically tracks user interactions on Single Page Applications (SPAs) via one of the following three methods, depending on which is supported:

  1. Using the [Soft Navigations API ↗︎](https://developer.chrome.com/docs/web-platform/soft-navigations)
  2. Listening on `navigate` events via the [Navigation API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API)
  3. By patching the [History API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/History_API)'s `pushState` function and listening to the `onpopstate` event



## Disable SPA measurement

If you want to disable the automatic tracking for SPAs, you can do so by adding the `spa` option with a value of `false` in the data attribute of the script tag, as shown below:
    
    
    <script
      type="module"
      src="https://static.cloudflareinsights.com/beacon.min.js"
      data-cf-beacon='{"token": "...", "spa": false}'
    ></script>

Note: this requires using [the manual embedding approach](https://developers.cloudflare.com/web-analytics/get-started/#sites-not-proxied-through-cloudflare).

### Google Tag Manager (GTM)

If you are using Google Tag Manager (GTM), you can disable SPA tracking by passing the `spa=false` option via the query string in the script URL:
    
    
    <script
      type="module"
      src="https://static.cloudflareinsights.com/beacon.min.js?token=...&spa=false"
    ></script>

[PreviousOverview](https://developers.cloudflare.com/web-analytics/get-started/)[NextNotifications](https://developers.cloudflare.com/web-analytics/get-started/notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web-analytics/get-started/web-analytics-spa.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/
title: Verify APO works \u00b7 Cloudflare Automatic Platform Optimization docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.225126+00:00
---

# Verify APO works · Cloudflare Automatic Platform Optimization docs

> Source: https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)
  3. /[Get started](https://developers.cloudflare.com/automatic-platform-optimization/get-started/)
  4. /Verify APO works



# Verify APO works

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/automatic-platform-optimization/get-started/verify-apo-works/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewVerify the APO integration and WordPress integration work

You can check whether or not APO is working by verifying APO headers are present. When APO is working, three headers are present: `CF-Cache-Status`, `cf-apo-via`, `cf-edge-cache`.

  1. Visit [Uptrends.com ↗︎](https://www.uptrends.com/tools/http-response-header-check).
  2. In the text field, enter the URL for your WordPress homepage including the `https://www.`.
  3. Select **Start test**. The **Response Headers** table displays.
  4. Locate the three header responses and their description. APO is working correctly when the headers exactly match the headers below.


  * `CF-Cache-Status` | `HIT`
    * The `cf-cache-status` header displays if the asset is served from the cache or was considered dynamic and served from the origin.
  * `cf-apo-via` | `tcache`
    * The `cf-apo-via` header returns the APO status for the given request.
  * `cf-edge-cache` | `cache, platform=wordpress`
    * The `cf-edge-cache` headers confirms the WordPress plugin is installed and enabled.



In a terminal, use the following cURL. Include the `'accept: text/html'` header so the request is treated as a browser-like HTML request. This makes the test result deterministic. APO can also cache requests that omit the header, depending on the URL path. For more information, refer to [FAQ on `cf-cache-status` results](https://developers.cloudflare.com/automatic-platform-optimization/troubleshooting/faq/).
    
    
    curl -svo /dev/null -A "CF" 'https://example.com/' -H 'accept: text/html' 2>&1 | grep 'cf-cache-status\|cf-edge\|cf-apo-via'
    
    
    < cf-cache-status: HIT
    < cf-apo-via: cache
    < cf-edge-cache: cache,platform=wordpress

As always, `cf-cache-status` displays if the asset hit the cache or was considered dynamic and served from the origin.

  * `cf-apo-via` | `tcache`
    * The `cf-apo-via` header returns the APO status for the given request.
  * `cf-edge-cache` | `cache, platform=wordpress`
    * The `cf-edge-cache` headers confirms the WordPress plugin is installed and enabled.



## Verify the APO integration and WordPress integration work

Open your WordPress site and publish a change. When the integration is working, the page is cached with `cf-cache-status: HIT` and `cf-apo-via: tcache`.

[PreviousActivate the Cloudflare WordPress plugin](https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/)[NextOverview](https://developers.cloudflare.com/automatic-platform-optimization/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/automatic-platform-optimization/get-started/verify-apo-works.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/
title: Query parameters and cached responses \u00b7 Cloudflare Automatic Platform Optimization docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.457703+00:00
---

# Query parameters and cached responses · Cloudflare Automatic Platform Optimization docs

> Source: https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)
  3. /[Reference](https://developers.cloudflare.com/automatic-platform-optimization/reference/)
  4. /Query parameters and cached responses



# Query parameters and cached responses

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCookies prefixes that always bypass cache

Query parameters often signal the presence of dynamic content. As a result, if there are query parameters in the URL, APO bypasses the cache and attempts to get a new version of the page from the origin by default. Because query parameters are also often used for marketing attribution, like UTMs, quick loading times are especially important for users.

To add a query parameter to our allowlist, [create a post in the community ↗︎](https://community.cloudflare.com/) for consideration.

APO serves cached content as long as the query parameters in the URL are one of the following:

  * `ref`
  * `utm_source`
  * `utm_medium`
  * `utm_campaign`
  * `utm_term`
  * `utm_content`
  * `utm_expid`
  * `fbclid`
  * `fb_action_ids`
  * `fb_action_types`
  * `fb_source`
  * `mc_cid`
  * `mc_eid`
  * `gclid`
  * `dclid`
  * `_ga`
  * `campaignid`
  * `adgroupid`
  * `_ke`
  * `cn-reloaded`
  * `age-verified`
  * `ao_noptimize`
  * `usqp`
  * `mkt_tok`
  * `epik`
  * `ck_subscriber_id`



## Cookies prefixes that always bypass cache

  * `wp-`
  * `wordpress`
  * `comment_`
  * `woocommerce_`
  * `xf_`
  * `edd_`
  * `jetpack`
  * `yith_wcwl_session_`
  * `yith_wrvp_`
  * `wpsc_`
  * `ecwid`
  * `ec_`
  * `bookly_`
  * `bookly`



[PreviousOverview](https://developers.cloudflare.com/automatic-platform-optimization/reference/)[NextPage Rule integration with APO](https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/automatic-platform-optimization/reference/query-parameters.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/
title: Page Rule integration with APO \u00b7 Cloudflare Automatic Platform Optimization docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.407875+00:00
---

# Page Rule integration with APO · Cloudflare Automatic Platform Optimization docs

> Source: https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)
  3. /[Reference](https://developers.cloudflare.com/automatic-platform-optimization/reference/)
  4. /Page Rule integration with APO



# Page Rule integration with APO

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following Page Rules can control APO. Any changes to caching via Page Rules require purging the cache for the changes to take effect.

Caution

Consider using [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/) instead to control APO due to their enhanced configurability.

  * **Cache Level: Bypass** — APO bypasses pages with response header `cf-apo-via: origin,page-rules`

  * **Cache Level: Ignore Query String** — APO ignores all query strings when serving from Cache.

  * **Cache Level: Cache Everything** — APO caches pages with all query strings.

Caution

Automatic page purge via the WordPress plugin won’t clean all cached pages, only pages without query strings. Cached responses will be returned even with request header `cache-control: no-cache`.

  * **Bypass Cache on Cookie (Business and Enterprise plans only)** — APO applies custom bypass cookies in addition to the default list.

  * **Edge Cache TTL** — APO applies custom Edge TTL instead of 30 days. This page rule is helpful for pages that can generate CAPTCHAs or nonces.

  * **Browser Cache TTL** — APO applies custom Browser TTL.

  * `CDN-Cache-Control` and `Cloudflare-CDN-Cache-Control` – Enables users to have detailed control over cache TTLs without using a page rule. For more information on the `CDN-Cache-Control` and `Cloudflare-CDN-Cache-Control` headers, refer to [CDN-Cache-Control](https://developers.cloudflare.com/cache/concepts/cache-control/).




[PreviousQuery parameters and cached responses](https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/)[NextCache by device type](https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/automatic-platform-optimization/reference/page-rule-integration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

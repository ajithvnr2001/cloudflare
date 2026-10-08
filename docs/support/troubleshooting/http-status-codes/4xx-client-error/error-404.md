---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-404/
title: Error 404 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.514566+00:00
---

# Error 404 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-404/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 404



# Error 404

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-404/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview404 Not Found Common use cases Cloudflare-specific information

## 404 Not Found

The `404 Not Found` status code indicates that the origin server was unable to locate the requested resource. Typically, this means the host server could not find the resource. For a more permanent version of this error, the 410 Gone status code should be used.

For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.5).

### Common use cases

These errors typically occur when someone mistypes a URL on your site, when there is a broken link from another page, when a page that previously existed is moved or removed, or there is an error when a search engine indexes your site.

These errors typically account for approximately 3% of total page views for a typical site. However, they often go untracked by traditional analytics platforms, such as Google Analytics. To improve user experience, website owners usually implement a custom 404 page to be displayed when this error is generated.

### Cloudflare-specific information

Cloudflare does not generate `404s` for customer websites, we only proxy the request from the origin server. If you encounter a `404` error on a Cloudflare-powered site, the issue lies with the origin server. In such cases, contact your hosting provider for assistance.

[PreviousError 403](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/)[NextError 405](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-405/)

Was this helpful?

YesNo

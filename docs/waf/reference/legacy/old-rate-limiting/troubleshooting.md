---
url: https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/troubleshooting/
title: Troubleshoot Rate Limiting (previous version) \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:46.925976+00:00
---

# Troubleshoot Rate Limiting (previous version) · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

ReferenceLegacy features

  4. /[Rate Limiting (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/)
  5. /Troubleshooting



# Troubleshoot Rate Limiting (previous version)

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCommon API errors

A few common rate limiting configuration issues prevent proper request matches:

  * **Including HTTP or HTTPS protocol schemes in rule patterns** (such as `https://example.com/*`). To restrict rules to match only HTTP or HTTPS traffic, use the schemes array in the request match. For example, `"schemes": [ "HTTPS" ]`.
  * **Forgetting a trailing slash character (`/`)**. Cloudflare Rate Limiting only treats requests for the homepage (such as `example.com` and `example.com/`) as equivalent, but not any other path (such as `example.com/path/` and `example.com/path`). To match request paths both with and without the trailing slash, use a wildcard match (for example, `example.com/path*`).
  * **Including a query string or anchor** (such as `example.com/path?foo=bar` or `example.com/path#section1`). A rule like `example.com/path` will match requests for `example.com/path?foo=bar`.
  * **Overriding a rate limit with[IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)**.
  * **Including a port number** (such as `example.com:8443/api/`). Rate Limiting does not consider port numbers within rules. Remove the port number from the URL so that the rate limit rule triggers as expected.



## Common API errors

The following common errors may prevent configuring rate limiting rules via the [Cloudflare API](https://developers.cloudflare.com/api/resources/rate_limits/methods/create/):

  * `Decoding is not yet implemented` – Indicates that your request is missing the `Content-Type: application/json` header. Add the header to your API request to fix the issue.
  * `Ratelimit.api.not_entitled` – Enterprise customers must contact their account team before adding rules.



Note

The `origin_traffic` parameter can only be set on Enterprise plans. Setting `"origin_traffic" = false` for a rule on a Free, Pro, or Business domain is automatically converted into `"origin_traffic" = true`.

[PreviousOverview](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/)[NextRate limiting upgrade](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/reference/legacy/old-rate-limiting/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

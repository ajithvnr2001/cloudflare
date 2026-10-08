---
url: https://developers.cloudflare.com/rules/normalization/
title: URL normalization \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:48.866043+00:00
---

# URL normalization · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/normalization/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /URL normalization



# URL normalization

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/normalization/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityGet started

Cloudflare provides a URL normalization feature to modify the URLs of incoming requests so that they conform to a consistent formatting standard. This is important because the same resource can be requested using different URL formats (for example, `/hello` and `/%68ello` refer to the same path), and without normalization, security rules and other features might not match all variations of a URL.

When you enable URL normalization, all incoming URLs are normalized before they pass to subsequent global network features that accept a URL input, such as WAF custom rules, Workers, and Access. Rule expressions that filter traffic based on URLs will therefore trigger correctly, regardless of the format of the incoming URL. When URL normalization is disabled, Cloudflare forwards the URL to origin in its original form.

Caution

When traffic is proxied through Cloudflare, certain baseline URL normalization steps are always applied, even if you turn off URL normalization for your zone. For example, Cloudflare always converts two or more adjacent slashes into a single slash (such as `//page` to `/page`). You cannot disable these baseline normalizations.

URL normalization does not perform any redirects, and therefore it will not change the address displayed in the visitor's browser. The normalization operation, when enabled, occurs on the global network and affects Cloudflare features executed later and (optionally) the URL received at the origin server.

Note

URL normalization requires that you [proxy the DNS records](https://developers.cloudflare.com/dns/proxy-status/) of your domain (or subdomain) through Cloudflare.

* * *

## Availability

URL normalization is available in all Cloudflare plans.

## Get started

Learn more about [URL normalization](https://developers.cloudflare.com/rules/normalization/how-it-works/) and how to [configure URL normalization](https://developers.cloudflare.com/rules/normalization/manage/) in the Cloudflare dashboard.

[PreviousBilling and subscription](https://developers.cloudflare.com/rules/page-rules/troubleshooting/billing-and-subscription/)[NextHow it works](https://developers.cloudflare.com/rules/normalization/how-it-works/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/normalization/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

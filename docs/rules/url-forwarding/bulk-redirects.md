---
url: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/
title: Bulk Redirects \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:58.740867+00:00
---

# Bulk Redirects · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)
  4. /Bulk Redirects



# Bulk Redirects

Last updated Jun 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBulk Redirects and the WAFRelated resources

Bulk Redirects allow you to define a large number of URL redirects at the account level, which can apply across domains in your account. These redirects navigate the user from a source URL to a target URL using a given HTTP status code. URL redirection is also known as URL forwarding.

Unlike dynamic URL redirects created in [Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/), Bulk Redirects are essentially static. They do not support string replacement operations or regular expressions. However, you can configure URL redirect parameters that affect how source URLs are matched and how the redirect is performed.

For more complex and customized redirect logic, consider using [Snippets](https://developers.cloudflare.com/rules/snippets/).

* * *

## Bulk Redirects and the WAF

Bulk Redirects run after the WAF in the request processing pipeline. This means that:

  * If a [WAF custom rule](https://developers.cloudflare.com/waf/custom-rules/) or [rate limiting rule](https://developers.cloudflare.com/waf/rate-limiting-rules/) blocks a request, the Bulk Redirect will not execute.
  * If a WAF rule logs or challenges a request that subsequently passes, the firewall event will still appear in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/) and [Logpush](https://developers.cloudflare.com/logs/) — even though the request is later redirected. This is expected behavior.



For the complete request processing order, refer to [Rules execution order](https://developers.cloudflare.com/rules/url-forwarding/#execution-order).

* * *

## Related resources

  * [Availability](https://developers.cloudflare.com/rules/url-forwarding/#availability): Information on the Bulk Redirects quotas and features per Cloudflare plan.
  * [Execution order](https://developers.cloudflare.com/rules/url-forwarding/#execution-order): Execution order of the different Rules products.
  * [Trace a request](https://developers.cloudflare.com/rules/trace-request/): Use Cloudflare Trace to determine if a bulk redirect rule is triggering for a specific URL.



[PreviousAvailable settings](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/)[NextConcepts](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/bulk-redirects/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

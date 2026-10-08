---
url: https://developers.cloudflare.com/firewall/api/cf-filters/
title: Cloudflare Filters API \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.707825+00:00
---

# Cloudflare Filters API · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)
  4. /Cloudflare Filters API



# Cloudflare Filters API

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDifferences from other Cloudflare APIs

**Cloudflare Filters** is an API-only component of firewall rules for designing complex criteria that rely on boolean operators and other logic to examine incoming HTTP traffic and look for a match.

Deprecation notice

Cloudflare Firewall Rules has been deprecated. Cloudflare has moved existing firewall rules to [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/). For more information on this change, refer to the [upgrade guide](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/).

For example, a filter matching:

  * An HTTP user agent, and
  * The HTTP path, and
  * The source IP address



Associate a filter with a firewall rule to define the scope of that rule.

Use IP lists within a filter to refer collectively to a group of IP addresses. Refer to the [Lists API](https://developers.cloudflare.com/waf/tools/lists/lists-api/) for more information.

Before getting started with the Cloudflare Filters API, familiarize yourself with rule [expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/). For a complete reference, refer to [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/).

## Differences from other Cloudflare APIs

The Firewall Rules API behaves differently from most Cloudflare APIs in two ways:

  * API calls accept and return multiple items, and allow applying data changes to multiple items.
  * Although API calls return the [standard response](https://developers.cloudflare.com/fundamentals/api/), the error object follows the [JSON API standard ↗︎](http://jsonapi.org/format/#errors), such that in an error condition, it is clear which item produced the error and why.



To get started, review [What is a filter?](https://developers.cloudflare.com/firewall/api/cf-filters/what-is-a-filter/), followed by the Cloudflare Filters [JSON object](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/json-object/) and [Endpoints](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/).

[PreviousDELETE examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/)[NextWhat is a filter?](https://developers.cloudflare.com/firewall/api/cf-filters/what-is-a-filter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/
title: Firewall Rules API \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.139662+00:00
---

# Firewall Rules API · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-firewall-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)
  4. /Firewall Rules API



# Firewall Rules API

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDifferences from other Cloudflare APIs

Use the Firewall Rules API to programmatically manage your rules.

Deprecation notice

Cloudflare Firewall Rules has been deprecated. Cloudflare has moved existing firewall rules to [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/). For more information on this change, refer to the [upgrade guide](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/).

When working with the Firewall Rules API, refer to these topics for additional context:

  * [Firewall rules actions](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/)
  * [Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)



To get started with the API, review the Firewall Rules API [JSON object](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/json-object/) and [Endpoints](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/).

For more information on the Rules language used to write rule expressions, refer to [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/) in the Ruleset Engine documentation.

## Differences from other Cloudflare APIs

The Firewall Rules API behaves differently from most Cloudflare APIs in two ways:

  * API calls accept and return multiple items, and allow applying data changes to multiple items.
  * Although API calls return the [standard response](https://developers.cloudflare.com/fundamentals/api/), the error object follows the [JSON API standard ↗︎](http://jsonapi.org/format/#errors), such that in an error condition, it is clear which item produced the error and why.



[PreviousOverview](https://developers.cloudflare.com/firewall/api/)[NextJSON object](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/json-object/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-firewall-rules/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/
title: Fields reference \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:02.364787+00:00
---

# Fields reference · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /[Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)
  4. /Fields



# Fields

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDifferences from Wireshark display fields

The Cloudflare Rules language supports different types of fields such as:

  * Request fields that represent the basic properties of incoming requests, including specific fields for accessing request headers, URI components, and the request body.
  * Dynamic fields that represent computed or derived values, typically related to threat intelligence about an HTTP request.
  * Response fields that represent the basic properties of the received response.
  * Raw fields that preserve the original request values for later evaluations.



Refer to the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) for the list of available fields.

## Differences from Wireshark display fields

Most fields supported by the Cloudflare Rules language use the same naming conventions as [Wireshark display fields ↗︎](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html). However, there are some subtle differences between Cloudflare and Wireshark:

  * Wireshark supports [CIDR (Classless Inter-Domain Routing) notation ↗︎](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) for expressing IP address ranges in equality comparisons (`ip.src == 1.2.3.0/24`, for example). Cloudflare does not.

To evaluate a range of addresses using CIDR notation, use the [`in`](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#comparison-operators) comparison operator as in this example: `ip.src in {1.2.3.0/24 4.5.6.0/24}`.

  * In Wireshark, `ssl` is a protocol field containing hundreds of other fields of various types that are available for comparison in multiple ways. However, in the Rules language [`ssl`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ssl/) is a single Boolean field that indicates whether the connection from the client to Cloudflare is encrypted.

  * The Cloudflare Rules language does not support the `slice` operator.




[PreviousActions](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/)[NextFields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/rules-language/fields/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

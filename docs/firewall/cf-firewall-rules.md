---
url: https://developers.cloudflare.com/firewall/cf-firewall-rules/
title: About Cloudflare Firewall Rules \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:17.069594+00:00
---

# About Cloudflare Firewall Rules · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/cf-firewall-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /About



# About

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/cf-firewall-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Firewall Rules is a flexible and intuitive framework for filtering HTTP requests. It gives you fine-grained control over which requests reach your applications, proactively inspecting incoming site traffic and automatically responding to threats.

Deprecation notice

Cloudflare Firewall Rules has been deprecated. Cloudflare has moved existing firewall rules to [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/). For more information on this change, refer to the [upgrade guide](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/).

In a firewall rule you define an [expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/) that tells Cloudflare what to look for in a request, and specify the appropriate [action](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/) to take when those conditions are met. Expressions can reference [IP lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-lists) \- groups of IP addresses that you can reference collectively by name.

To write firewall rule expressions, use the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/), a powerful expression language inspired in the Wireshark Display Filter language.

[PreviousOverview](https://developers.cloudflare.com/firewall/)[NextActions](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/cf-firewall-rules/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

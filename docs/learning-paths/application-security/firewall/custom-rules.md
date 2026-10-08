---
url: https://developers.cloudflare.com/learning-paths/application-security/firewall/custom-rules/
title: Custom rules \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:43.027209+00:00
---

# Custom rules · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/firewall/custom-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Web Application Firewall](https://developers.cloudflare.com/learning-paths/application-security/firewall/)
  5. /Custom rules



# Custom rules

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/firewall/custom-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSkip rules

Custom rules allow you to control incoming traffic by filtering requests to a zone. They work as customized web application firewall (WAF) rules that you can use to perform actions like _Block_ or _Managed Challenge_ on incoming requests. You can also use the _Skip_ action in a custom rule to [skip one or more Cloudflare security features](https://developers.cloudflare.com/waf/custom-rules/skip/).

In the [new security dashboard](https://developers.cloudflare.com/security/), custom rules are one of the available types of [security rules](https://developers.cloudflare.com/security/rules/). Security rules perform security-related actions on incoming requests that match specified filters.

Like other rules evaluated by Cloudflare's [Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/), custom rules have the following basic parameters:

  * An [expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/) that specifies the criteria you are matching traffic on using the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/).
  * An [action](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/) that specifies what to perform when there is a match for the rule.



The [custom rules documentation](https://developers.cloudflare.com/waf/custom-rules/) includes examples for common use cases.

## Skip rules

You can skip one or more Cloudflare security features using a custom rule [configured with the _Skip_ action](https://developers.cloudflare.com/waf/custom-rules/skip/). These rules are also known as skip rules. Refer to [Skip options](https://developers.cloudflare.com/waf/custom-rules/skip/options/) for more information on the features you can skip.

[PreviousManaged Rules](https://developers.cloudflare.com/learning-paths/application-security/firewall/managed-rules/)[NextOverview](https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/firewall/custom-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

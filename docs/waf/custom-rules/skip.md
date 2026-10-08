---
url: https://developers.cloudflare.com/waf/custom-rules/skip/
title: Configure a custom rule with the Skip action \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:37.202463+00:00
---

# Configure a custom rule with the Skip action · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/skip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)
  4. /Configure a rule with the Skip action



# Configure a rule with the Skip action

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/skip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use the _Skip_ action in a custom rule to skip one or more security features. A rule configured with the _Skip_ action is also known as a skip rule.

Skip rules allow specific requests to bypass security features that would otherwise block or challenge them. Use skip rules when legitimate traffic matches a security rule unintentionally. For example, to allow a trusted API client through [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/), or to exempt an internal monitoring service from [Managed Rules](https://developers.cloudflare.com/waf/managed-rules/).

You can skip [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/), [Managed Rules](https://developers.cloudflare.com/waf/managed-rules/), [Super Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/) rules, and several other security products. However, you cannot skip [Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/) (available on the Free plan).

For more information on the available options, refer to [Available skip options](https://developers.cloudflare.com/waf/custom-rules/skip/options/).

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. [Create a custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) by selecting **Create rule** > **Custom rules** , or edit an existing custom rule.

  3. Define the rule name and the rule expression.

  4. Under **Choose action** , select _Skip_ from the dropdown.

![Available Skip action options when configuring a custom rule](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=900,height=670,format=webp/_astro/skip-action-options.N8Emdhwv.png)
  5. Configure the desired [skip options](https://developers.cloudflare.com/waf/custom-rules/skip/options/).

  6. Save your changes.




Use the [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/) to configure custom rules via API.

Refer to [API examples](https://developers.cloudflare.com/waf/custom-rules/skip/api-examples/) for examples of creating skip rules.

[PreviousCreate using Terraform ↗︎](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/)[NextAPI examples](https://developers.cloudflare.com/waf/custom-rules/skip/api-examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/skip/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

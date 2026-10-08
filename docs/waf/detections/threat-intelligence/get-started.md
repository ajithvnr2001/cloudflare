---
url: https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/
title: Get started \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:43.210424+00:00
---

# Get started · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Threat intelligence](https://developers.cloudflare.com/waf/detections/threat-intelligence/)
  5. /Get started



# Get started

Last updated Jun 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/threat-intelligence/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin1\. Create a rule from Threat Events2\. Review matches in Security Analytics3\. Switch to Block or Managed Challenge4\. (Alternative) Create a rule manually

## Before you begin

  * Your account must have an active [Cloudforce One subscription](https://developers.cloudflare.com/security-center/cloudforce-one/). Contact your account team for access.
  * The [WAF](https://developers.cloudflare.com/waf/) must be enabled on your zone.



## 1\. Create a rule from Threat Events

The fastest way to create a threat intelligence rule is from a saved view in the [Threat Events](https://developers.cloudflare.com/security-center/cloudforce-one/) dashboard. Filter the threats you care about, then export the filters directly to a WAF rule.

  1. In the Threat Events dashboard, build a saved view with the filters you want to act on (for example, _IPs targeting the financial sector in the last seven days_).

  2. Export the saved view to a WAF rule. Cloudflare generates a custom rule expression that matches the saved view filters.

  3. Review the generated rule. Set the action to _Log_ to validate matches before enforcing.

  4. Deploy the rule.




## 2\. Review matches in Security Analytics

Once the rule is deployed, matches appear in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/). You can see the threat event details — including threat actors, target industries, and countries — directly in the analytics view.

  1. In the Cloudflare dashboard, go to the **Analytics** page.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)
  2. Review the threat intelligence matches. Use the threat event details to decide which categories of traffic to block or challenge.




If no matches appear after deploying the rule, contact your account team to verify your Cloudforce One subscription is active.

## 3\. Switch to Block or Managed Challenge

Once you are confident in the match patterns, update the rule action from _Log_ to _Block_ or _Managed Challenge_.

For more examples, refer to [Example rules](https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/). For the full field list, refer to [Threat intelligence fields](https://developers.cloudflare.com/waf/detections/threat-intelligence/fields/).

## 4\. (Alternative) Create a rule manually

If you prefer to write expressions directly, you can create a rule from the dashboard or the API.

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/login) and select your account and domain.

  2. Go to **Security** > **Security rules**.

  3. Select **Create rule** > **Custom rules**.

  4. Enter a rule name.

  5. Select **Edit expression** and enter an expression using threat intelligence fields. For example:
         
         any(cf.intel.ip.target_countries[*] == "FR") and any(cf.intel.ip.datasets[*] == "ddos")

  6. Set the action to _Log_ to validate matches before enforcing.

  7. Select **Deploy**.




Threat intelligence fields work with the [Cloudflare API](https://developers.cloudflare.com/api/resources/rulesets/) and the [Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs). To create a custom rule via the API, refer to [Create a custom rule via API](https://developers.cloudflare.com/waf/custom-rules/create-api/).

Use the following expression to match IP addresses associated with DDoS activity targeting France:
    
    
    any(cf.intel.ip.target_countries[*] == "FR") and any(cf.intel.ip.datasets[*] == "ddos")

Set the action to `log` to validate matches before enforcing.

[PreviousOverview](https://developers.cloudflare.com/waf/detections/threat-intelligence/)[NextExample rules](https://developers.cloudflare.com/waf/detections/threat-intelligence/example-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/threat-intelligence/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

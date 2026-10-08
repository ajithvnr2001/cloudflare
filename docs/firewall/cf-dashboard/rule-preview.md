---
url: https://developers.cloudflare.com/firewall/cf-dashboard/rule-preview/
title: Preview firewall rules \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.849680+00:00
---

# Preview firewall rules · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/cf-dashboard/rule-preview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /[Manage rules in the dashboard](https://developers.cloudflare.com/firewall/cf-dashboard/)
  4. /Preview rules



# Preview rules

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/cf-dashboard/rule-preview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTest a firewall rule with Rule PreviewImportant notes

The expression of a firewall rule can become quite complex. In this situation, you should test your firewall rule before deploying it to ensure that the rule will behave as expected.

Rule Preview helps you understand the potential impact of a firewall rule, by testing the rule against a sample drawn from the last 72 hours of traffic. Rule Preview is built into the firewall rules Expression Editor so that you can test a rule as you edit it.

Caution

Rule Preview is only available to customers on an Enterprise plan.

## Test a firewall rule with Rule Preview

  1. Locate the desired rule in the rules list and select **Edit** (wrench icon).
  2. Select **Test rule** to trigger the test.

![The Test Rule button next to the Action drop-down list allows you to check the traffic that would be affected by the current firewall rule](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=600,format=webp/_astro/firewall-rules-preview-1.D1bW7NGh.png)

The results of the test are displayed in a plot that simulates how many of the total requests in the last 72 hours would have matched the tested expression.

In this screenshot, a rule that matches all User-Agents that contain the string `Mozilla` would block about 8% of requests to the zone:

![Example chart of a rule preview operation, stating that about 8% of the zone requests would be blocked by the current rule](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1295,format=webp/_astro/cf-firewall-rules-preview-rule-plot-chart.BW_d_L46.png)

## Important notes

**Consider the results of Firewall Preview an _indication_ of traffic levels**, not an exact calculation. The sample rate can be as little as 1% of your total traffic.

**Rule Preview does not take into account other firewall rules** that you have already configured. In effect, Rule Preview tests a single firewall rule in isolation. Security events or any other rules with a higher priority that may have blocked or challenged a request are ignored.

**You cannot test firewall rules that reference[IP lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-lists)**.

**Cloudflare does not store the entirety of requests, so only a limited number of fields are available to Rule Preview**. The table below lists the fields that Rule Preview supports (green cells), broken down by operator. Fields and operators that are not supported are not included in this table.

[PreviousCreate, edit, and delete rules](https://developers.cloudflare.com/firewall/cf-dashboard/create-edit-delete-rules/)[NextCreate a mTLS rule](https://developers.cloudflare.com/firewall/cf-dashboard/create-mtls-rule/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/cf-dashboard/rule-preview.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

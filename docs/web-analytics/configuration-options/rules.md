---
url: https://developers.cloudflare.com/web-analytics/configuration-options/rules/
title: Rules \u00b7 Cloudflare Web Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:53.294390+00:00
---

# Rules · Cloudflare Web Analytics docs

> Source: https://developers.cloudflare.com/web-analytics/configuration-options/rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)
  3. /[Configuration options](https://developers.cloudflare.com/web-analytics/configuration-options/)
  4. /Rules



# Rules

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web-analytics/configuration-options/rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use **Rules** to configure whether to track Web Analytics for specific websites or paths. By default, Web Analytics automatically creates a single rule for the zone that injects the JavaScript (JS) snippet for all pages.

Rules are only available for sites proxied through Cloudflare. For more information, refer to [Limits](https://developers.cloudflare.com/web-analytics/limits/).

  1. In the Cloudflare dashboard, go to the **Web Analytics** page.

[ Go to **Web analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/web-analytics)
  2. Find the site you want to configure and select **Manage site**.

  3. Select **Advanced options** > **Add rule**.

  4. Select the **Action** and fill in the hostname and path(s) you want to add a rule for.

  5. If you want to add additional rules, select **Add rule**. Otherwise select **Update** to save the rule.




Warning

Configuration rules have precedence over any Web Analytics rules. If a Web Analytics rule turns on analytics measurements for an incoming request and the same request matches a configuration rule turning off Web Analytics, the configuration rule will win.

[PreviousFilters](https://developers.cloudflare.com/web-analytics/configuration-options/filters/)[NextOverview](https://developers.cloudflare.com/web-analytics/data-metrics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web-analytics/configuration-options/rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

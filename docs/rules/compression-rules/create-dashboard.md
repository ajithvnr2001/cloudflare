---
url: https://developers.cloudflare.com/rules/compression-rules/create-dashboard/
title: Create a compression rule in the dashboard \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:47.186041+00:00
---

# Create a compression rule in the dashboard · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/compression-rules/create-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Compression Rules](https://developers.cloudflare.com/rules/compression-rules/)
  4. /Create a rule in the dashboard



# Create a compression rule in the dashboard

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/compression-rules/create-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

  1. In the Cloudflare dashboard, go to the Rules **Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)
  2. Select **Create rule** > **Compression Rule**.

  3. (Optional) Select one of the rule templates that address common use cases. Then, review and adjust the proposed rule configuration.

  4. Enter a descriptive name for the rule in **Rule name**.

  5. Under **When incoming requests match** , select if you wish to apply the rule to [default content types](https://developers.cloudflare.com/speed/optimization/content/compression/#compression-between-cloudflare-and-website-visitors) (content types that Cloudflare compresses by default), or to requests that match a custom filter expression.

  6. (Optional) To define a custom expression, use the Expression Builder (specifying one or more values for **Field** , **Operator** , and **Value**) or manually enter an expression using the Expression Editor. For more information, refer to [Edit expressions in the dashboard](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/).

  7. Under **Compression options** , set the [compression options](https://developers.cloudflare.com/rules/compression-rules/settings/#dashboard-configuration-settings).

  8. To save and deploy your rule, select **Deploy**. If you are not ready to deploy your rule, select **Save as Draft**.

If you are matching a hostname in your rule expression, you may be prompted to create a proxied DNS record for that hostname. Refer to [Troubleshooting](https://developers.cloudflare.com/rules/reference/troubleshooting/#this-rule-may-not-apply-to-your-traffic) for more information.




[PreviousOverview](https://developers.cloudflare.com/rules/compression-rules/)[NextCreate a rule via API](https://developers.cloudflare.com/rules/compression-rules/create-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/compression-rules/create-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

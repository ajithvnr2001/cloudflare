---
url: https://developers.cloudflare.com/rules/snippets/create-dashboard/
title: Create a snippet in the dashboard \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:52.236581+00:00
---

# Create a snippet in the dashboard · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/create-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Snippets](https://developers.cloudflare.com/rules/snippets/)
  4. /Create in the dashboard



# Create a snippet in the dashboard

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/create-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

  1. In the Cloudflare dashboard, go to the **Snippets** page.

[ Go to **Snippets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets)
  2. (Optional) If you have not created any snippets yet, select one of the snippet templates that addresses a common use case. Then, review and adjust the proposed snippet code.

To start from scratch, select **Create Snippet**.

  3. In **Snippet name** , enter a descriptive name for the snippet. You cannot change the name after creating the snippet.

  4. Enter the snippet's JavaScript code in the code editor. You can test how your snippet will handle incoming requests using the **HTTP** and **Preview** tabs.

  5. Select **Snippet rule** to configure when the snippet will run.

  6. Under **Run this Snippet if incoming requests match** , select if you wish to run the snippet only for requests that match a custom filter expression or for all incoming requests.

  7. (Optional) To define a custom expression, use the Expression Builder (specifying one or more values for **Field** , **Operator** , and **Value**) or manually enter an expression using the Expression Editor. For more information, refer to [Edit expressions in the dashboard](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/).

  8. Select **Done**.

  9. To deploy your snippet, select **Deploy**. If you are not ready to deploy your snippet, open the dropdown next to **Deploy** and select **Save as Draft**.

If you are matching a hostname in your rule expression, you may be prompted to create a proxied DNS record for that hostname. Refer to [Troubleshooting](https://developers.cloudflare.com/rules/reference/troubleshooting/#this-rule-may-not-apply-to-your-traffic) for more information.




[PreviousHow it works](https://developers.cloudflare.com/rules/snippets/how-it-works/)[NextConfigure via API](https://developers.cloudflare.com/rules/snippets/create-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/create-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

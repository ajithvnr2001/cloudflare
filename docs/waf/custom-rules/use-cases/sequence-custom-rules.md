---
url: https://developers.cloudflare.com/waf/custom-rules/use-cases/sequence-custom-rules/
title: Build a sequence rule within custom rules \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.202839+00:00
---

# Build a sequence rule within custom rules · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/use-cases/sequence-custom-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)

  4. /Common use cases
  5. /Build a sequence rule within custom rules



# Build a sequence rule within custom rules

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/use-cases/sequence-custom-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can build an [API sequence rule](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/custom-rules/) via the Cloudflare dashboard.

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. To create a new empty rule, select **Create rule** > **Custom rules**.

  3. Enter a descriptive name for the rule in **Rule name**.

  4. Under **When incoming requests match** , use the **Field** drop-down list to filter by **Sequences** and select from:

     * Current Operation
     * Previous Operations
     * Elapsed time
  5. Under **Value** , select the edit icon to use Builder and build a sequence on the side panel.

  6. Under **Select a hostname for this sequence** , choose all or a specific hostname from the dropdown list. Optionally, you can use the search bar to search for a specific hostname.

  7. From the **Methods** dropdown list, choose all methods or a specific request method.

  8. Select the checkbox for each endpoint in the order that you want them to appear in the sequence.

  9. Set the time to complete.

  10. Select **Save**.

  11. Under **Then take action** , select the rule action in the **Choose action** dropdown. For example, selecting _Block_ tells Cloudflare to refuse requests that match the conditions you specified.

  12. (Optional) If you selected the _Block_ action, you can configure a custom response.

  13. Under **Place at** , select the order of when the rule will fire.

  14. To save and deploy your rule, select **Deploy**. If you are not ready to deploy your rule, select **Save as Draft**.




Note

The fields in the custom rule are populated as a grouped sequence based on the values that you entered on Builder.

[PreviousBlock Worker subrequests from other zones](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-worker-subrequests/)[NextChallenge bad bots](https://developers.cloudflare.com/waf/custom-rules/use-cases/challenge-bad-bots/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/use-cases/sequence-custom-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

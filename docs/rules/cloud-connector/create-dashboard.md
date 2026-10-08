---
url: https://developers.cloudflare.com/rules/cloud-connector/create-dashboard/
title: Configure a Cloud Connector rule in the dashboard \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:45.612456+00:00
---

# Configure a Cloud Connector rule in the dashboard · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/cloud-connector/create-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)
  4. /Configure a rule in the dashboard



# Configure a Cloud Connector rule in the dashboard

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/cloud-connector/create-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To configure a Cloud Connector rule in the dashboard:

  1. In the Cloudflare dashboard, go to the **Cloud Connector** page.

[ Go to **Cloud Connector** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/cloud-connector)
  2. Select your [cloud provider](https://developers.cloudflare.com/rules/cloud-connector/providers/) (Cloudflare R2 or an external provider).

  3. If you selected Cloudflare R2 in the previous step, select your bucket and your custom domain, and select **Next**.  
If you selected a different storage provider, enter the bucket URL and select **Next**.

Caution

The bucket URL must follow a [specific format](https://developers.cloudflare.com/rules/cloud-connector/providers/) according to your provider.

  4. Enter a descriptive name for the rule in **Cloud Connector name**.

  5. Under **If** , select **Custom filter expression** and [enter an expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/) to define the traffic that will be redirected to the bucket. For example:

     * To route all requests matching `http*://example.com/images/*` (HTTPS and HTTP requests) you could enter the following expression:  
`http.request.full_uri wildcard "http*://example.com/images/*"`
     * To route all requests matching `http*://images.example.com/*` (HTTPS and HTTP requests) you could enter the following expression:  
`http.request.full_uri wildcard "http*://images.example.com/*"`

Alternatively, select **All incoming requests** to redirect all incoming traffic for your zone to the storage bucket you selected.

  6. To save and deploy your rule, select **Deploy**. If you are not ready to deploy the rule, select **Save as Draft**.

If you are matching a hostname in your rule expression, you may be prompted to create a proxied DNS record for that hostname. Refer to [Troubleshooting](https://developers.cloudflare.com/rules/reference/troubleshooting/#this-rule-may-not-apply-to-your-traffic) for more information.




[PreviousOverview](https://developers.cloudflare.com/rules/cloud-connector/)[NextConfigure a rule via API](https://developers.cloudflare.com/rules/cloud-connector/create-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/cloud-connector/create-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

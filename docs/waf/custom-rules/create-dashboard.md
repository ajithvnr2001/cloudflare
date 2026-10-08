---
url: https://developers.cloudflare.com/waf/custom-rules/create-dashboard/
title: Create a custom rule in the dashboard \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:36.643777+00:00
---

# Create a custom rule in the dashboard · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/custom-rules/create-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Custom rules](https://developers.cloudflare.com/waf/custom-rules/)
  4. /Create in the dashboard



# Create a custom rule in the dashboard

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure a custom response for blocked requests

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. To create a new empty rule, select **Create rule** > **Custom rules**. To duplicate an existing rule, select the three dots next to it > **Duplicate**.

  3. Enter a descriptive name for the rule in **Rule name**.

![Custom rule creation page in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=870,height=535,format=webp/_astro/firewall-custom-rule-create.tVXiVklq.png)
  4. Under **When incoming requests match** , use the **Field** drop-down list to choose an HTTP property. For each request, the value of the property you choose for **Field** is compared to the value you specify for **Value** using the operator selected in **Operator**.

  5. Under **Then take action** , select the rule action in the **Choose action** dropdown. For example, selecting _Block_ tells Cloudflare to refuse requests that match the conditions you specified.

  6. (Optional) If you selected the _Block_ action, you can configure a custom response.

  7. To save and deploy your rule, select **Deploy**. If you are not ready to deploy your rule, select **Save as Draft**.




## Configure a custom response for blocked requests

Note

This feature is only available on Pro plans and above.

When you select the _Block_ action in a rule you can optionally define a custom response.

The custom response has three settings:

  * **With response type** : Choose a content type or the default WAF block response from the list. The available custom response types are the following:

Dashboard value | API value  
---|---  
Custom HTML | `"text/html"`  
Custom Text | `"text/plain"`  
Custom JSON | `"application/json"`  
Custom XML | `"text/xml"`  
  
  * **With response code** : Choose an HTTP status code for the response, in the range 400-499. The default response code is 403.

  * **Response body** : The body of the response. Configure a valid body according to the response type you selected. The maximum field size is 2 KB.




[PreviousOverview](https://developers.cloudflare.com/waf/custom-rules/)[NextCreate via API](https://developers.cloudflare.com/waf/custom-rules/create-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/custom-rules/create-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

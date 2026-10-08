---
url: https://developers.cloudflare.com/security/security-insights/review-insights/
title: Review Security Insights \u00b7 Security dashboard docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:30.524753+00:00
---

# Review Security Insights · Security dashboard docs

> Source: https://developers.cloudflare.com/security/security-insights/review-insights/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security dashboard](https://developers.cloudflare.com/security/)
  3. /[Security Insights](https://developers.cloudflare.com/security/security-insights/)
  4. /Review Security Insights



# Review Security Insights

Last updated Jun 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/security/security-insights/review-insights/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewResolve an insightExport insightsArchive insightsEnable alerts

Check the **Security Insights** tab for a list of detected insights that you should address.

For each detected insight, you can resolve it or archive it, after understanding its risks.

  1. In the Cloudflare dashboard, go to the **Security Insights** page.

[ Go to **Security insights** ↗ ](https://dash.cloudflare.com/?to=/:account/security-center)
  2. Next to the insight you wish to address, select **Details** to review it.




## Resolve an insight

Caution

Insights will not be automatically removed from your dashboard when you address them. You must either manually archive insights, manually trigger another scan or wait for the automatic scan to run as per [scan frequency](https://developers.cloudflare.com/security/security-insights/how-it-works/#scan-frequency).

In the Resolve insights page, if you choose to update a configuration based on the recommendation actions, follow the instructions on the insight details page.

The following insights follow a different yet straightforward workflow to be resolved:

  * **Minimum Version of TLS 1.2 not enforced** : To resolve this insight: 
    * Go to **SSL/TLS** > **Edge Certificates**.
    * Select **TLS 1.2**.
  * **Domains without "Always use HTTPS"** : To resolve this insight: 
    * Go to **SSL/TLS** > **Edge Certificates**.
    * Select **Always Use HTTPS**.
  * **Turn on JavaScript Detections** : To resolve this insight: 
    * Go to **Security** > **Bots** > Select **Configure Bot Management**.
    * Select **JavaScript Detections**.



## Export insights

You can export security insights to a CSV format directly from the dashboard.

To export security insights:

  1. In the Cloudflare dashboard, go to the **Security Insights** page.

[ Go to **Security insights** ↗ ](https://dash.cloudflare.com/?to=/:account/security-center)
  2. Select **Export insights**.




Exporting security insights allow you to perform a deeper analysis of your insights.

The exported CSV file includes information such as the severity of your data, insight type scan date, issue class and additional optional fields, such as insight details, risk assessment, detection method, and recommended actions.

## Archive insights

You can archive one or more insights from the dashboard.

To archive insights:

  1. In the Cloudflare dashboard, go to the **Security Insights** page.

[ Go to **Security insights** ↗ ](https://dash.cloudflare.com/?to=/:account/security-center)
  2. Select the insight(s) you want to archive, then select **Archive selected**.




Alternatively, to archive an insight:

  1. Select the insight you want to archive and select **Details**. The dashboard will open a page where you will be able to review [insight properties](https://developers.cloudflare.com/security/security-insights/how-it-works/#scan-properties).
  2. Select **Archive insight**.



## Enable alerts

You can enable alerts for critical insights.

To enable alerts:

  1. In the Cloudflare dashboard, go to the **Security Insights** page.

[ Go to **Security insights** ↗ ](https://dash.cloudflare.com/?to=/:account/security-center)
  2. Select the security insight(s) you want to create an alert for, then select **Create alert for selected classes**.

  3. Enter the notification name, and choose one or more insights classes to filter a notification.

  4. Select **Add email recipient** and enter an email address to receive the alert.

  5. Select **Save**.




[PreviousHow it works](https://developers.cloudflare.com/security/security-insights/how-it-works/)[NextRoles and permissions](https://developers.cloudflare.com/security/security-insights/roles-and-permissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security/security-insights/review-insights.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

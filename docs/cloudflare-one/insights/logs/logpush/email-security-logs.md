---
url: https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/
title: Email security logs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:52.676955+00:00
---

# Email security logs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)

  4. /[Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/)
  5. /Email security logs



# Email security logs

Last updated Apr 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable detection logsEnable user action logs

Email security allows you to configure Logpush to export two types of log data: detection logs (records of threats identified in email traffic) and user action logs (records of administrative actions taken via the API or the dashboard). Each log type requires separate configuration.

## Enable detection logs

Detection logs record each threat identified by Email security, including metadata such as the message sender, recipient, and detection verdict.

To enable detection logs, refer to [Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/). When configuring the Logpush job, select **Email security alerts** as the dataset.

## Enable user action logs

User action logs record all administrative actions taken via the [API](https://developers.cloudflare.com/api/resources/email_security/) or the dashboard.

Before you can enable user action logs for Email security, you must have a Logpush job configured for your storage destination. Refer to [Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) to enable logs on destinations such as Cloudflare R2, HTTP, Amazon S3, and more.

Once you have configured your destination, you can set up user action logs:

  1. In the Cloudflare dashboard, go to the **Logpush** page.

[ Go to **Logpush** ↗ ](https://dash.cloudflare.com/?to=/:account/logs)
  2. Select your storage destination.

  3. Select the three dots > **Edit**.

  4. Under **Configure logpush job** :



  * **Job name** : Enter the job name, if it is not already prepopulated.
  * **If logs match** > Select **Filtered logs** to capture only Email security events: 
    * **Field** : Choose `ResourceType` (the type of resource that was changed).
    * **Operator** : Choose `starts with`.
    * **Value** : Enter `email_security`.


  5. Select **Submit**.



You can now view logs via the Cloudflare dashboard.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/)[NextIDS logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/logs/logpush/email-security-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

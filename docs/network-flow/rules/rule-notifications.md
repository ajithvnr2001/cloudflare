---
url: https://developers.cloudflare.com/network-flow/rules/rule-notifications/
title: Configure rule notifications \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:23.975703+00:00
---

# Configure rule notifications · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/rules/rule-notifications/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /[Rules](https://developers.cloudflare.com/network-flow/rules/)
  4. /Configure rule notifications



# Configure rule notifications

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/rules/rule-notifications/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNotification configuration fieldsRule Auto-Advertisement notificationsConfigure rule notifications

Network Flow (formerly Magic Network Monitoring) can notify you by email, webhook, or PagerDuty when a rule is triggered. When a rule detects a traffic anomaly, notifications alert your team so you can respond — or, if you use Magic Transit with auto-advertisement, Cloudflare can begin mitigating the attack automatically.

For more information on the notification platform, refer to [Notifications documentation](https://developers.cloudflare.com/notifications/). You can also:

  * [Configure Cloudflare notifications](https://developers.cloudflare.com/notifications/get-started/)
  * [Configure PagerDuty](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/)
  * [Configure webhooks](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/)
  * [Test a notification](https://developers.cloudflare.com/notifications/get-started/#manage-alerts)
  * [Notification History](https://developers.cloudflare.com/notifications/notification-history/)



## Notification configuration fields

Field | Description  
---|---  
**Notification name** | A label to identify this notification in your notifications list.  
**Description (optional)** | The description of the notification.  
**Webhooks** | One or more webhooks to deliver the notification to.  
**Notification email** | One or more email addresses to deliver the notification to.  
  
## Rule Auto-Advertisement notifications

Webhook, PagerDuty, and email notifications are sent following an auto-advertisement attempt for all prefixes inside the flagged rule.

You will receive the status of the advertisement for each prefix with the following available statuses:

  * **Advertised** : The prefix was successfully advertised.
  * **Already Advertised** : The prefix was advertised prior to the auto advertisement attempt.
  * **Delayed** : The prefix cannot currently be advertised but will attempt advertisement. After the prefix can be advertised, a new notification is sent with the updated status.
  * **Locked** : The prefix is locked and cannot be advertised.
  * **Could not Advertise** : Cloudflare was unable to advertise the prefix. This status can occur for multiple reasons, but usually occurs when you are not allowed to advertise a prefix.
  * **Error** : A general error occurred during prefix advertisement.



## Configure rule notifications

To configure notifications for Network Flow rules:

  1. In the Cloudflare dashboard, go to the **Notifications** page.

[ Go to **Notifications** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)

  2. Select **Add**.
  3. Select _Magic Transit_ from the product drop-down menu.
  4. Find the appropriate Network Flow alert and select **Select** : 
     * **Network Flow: Volumetric Attack** \- for static threshold and dynamic threshold notifications
     * **Network Flow: DDoS Attack** \- for sFlow DDoS attack notifications
  5. Fill in the notification configuration details.
  6. Select **Save**.



[PrevioussFlow DDoS attack rule](https://developers.cloudflare.com/network-flow/rules/s-flow-ddos-attack/)[NextCloud flow logs](https://developers.cloudflare.com/network-flow/cloud-flow-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/rules/rule-notifications.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

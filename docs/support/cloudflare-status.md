---
url: https://developers.cloudflare.com/support/cloudflare-status/
title: Cloudflare Status \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:51.409920+00:00
---

# Cloudflare Status · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/cloudflare-status/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /Cloudflare Status



# Cloudflare Status

Last updated Aug 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/cloudflare-status/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure notifications Status page notifications Cloudflare NotificationsCheck location statusUse the APIRelated resources

Cloudflare provides updates on the status of our services and network on the [Cloudflare Status page ↗︎](https://www.cloudflarestatus.com/), which you should check if you notice unexpected behavior with Cloudflare.

Beyond looking at the page itself, there are programmatic ways to consume this information.

## Configure notifications

There are two ways to be notified about Cloudflare incidents and maintenance.

### Status page notifications

The status page has its own notification system, delivered independently of Cloudflare infrastructure, so these notifications fire even if Cloudflare itself is down. You can subscribe by email, webhook, Slack, Discord, or Google Chat.

For more information, refer to [status page notifications ↗︎](https://www.cloudflarestatus.com/docs/notifications).

### Cloudflare Notifications

Cloudflare offers a dedicated notification called **Incident Alerts** , which lets you know when Cloudflare is experiencing an incident. Because it runs on your account, it delivers to the destinations you have already configured and can be filtered to the impact levels and components you care about.

You can configure this notification to send via [email](https://developers.cloudflare.com/notifications/get-started/), [Webhooks](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/), or [PagerDuty](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/).

A separate **Maintenance Notification** covers planned maintenance. For more information, refer to [Disruptive Maintenance](https://developers.cloudflare.com/support/disruptive-maintenance/).

## Check location status

The [locations view ↗︎](https://www.cloudflarestatus.com/locations) lists the status of each Cloudflare data center as **Operational** , **Re-routed** , or **Partially Re-routed**. A location that has been removed from the network for planned or unplanned maintenance is listed as **Re-routed**.

## Use the API

Cloudflare also provides status information through the [Cloudflare Status API ↗︎](https://www.cloudflarestatus.com/api).

Incidents and maintenance are published as separate feeds, each available in RSS and Atom:

Feed | RSS | Atom  
---|---|---  
Incidents | `https://www.cloudflarestatus.com/api/v3/incidents.rss` | `https://www.cloudflarestatus.com/api/v3/incidents.atom`  
Maintenance | `https://www.cloudflarestatus.com/api/v3/maintenance.rss` | `https://www.cloudflarestatus.com/api/v3/maintenance.atom`  
  
## Related resources

  * [Available RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) (for the [Cloudflare changelog](https://developers.cloudflare.com/changelog/))
  * [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/)
  * [Planned maintenance windows](https://developers.cloudflare.com/support/disruptive-maintenance/)



[PreviousRestoring original visitor IPs](https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/)[NextDisruptive Maintenance](https://developers.cloudflare.com/support/disruptive-maintenance/)

Was this helpful?

YesNo

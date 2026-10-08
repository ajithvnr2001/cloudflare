---
url: https://developers.cloudflare.com/notifications/notification-available/
title: Available alerts \u00b7 Cloudflare Notifications docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:25.703812+00:00
---

# Available alerts · Cloudflare Notifications docs

> Source: https://developers.cloudflare.com/notifications/notification-available/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Notifications](https://developers.cloudflare.com/notifications/)
  3. /Available alerts



# Available alerts

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/notifications/notification-available/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCustom Alerts (Beta) Alert details Alert query Detection methods Evaluation and notification frequency Query previewBuilt-in alerts

The alerts available to you depend on your Cloudflare plan. Cloudflare offers alerts across products including [DDoS Protection](https://developers.cloudflare.com/ddos-protection/), [SSL/TLS](https://developers.cloudflare.com/ssl/), [Magic Transit](https://developers.cloudflare.com/magic-transit/), [Billing](https://developers.cloudflare.com/billing/), and more.

## Custom Alerts (Beta)

Custom Alerts evaluate a SQL API query on a schedule. Cloudflare sends a notification when the query result meets your detection criteria.

The datasets available to Custom Alerts depend on your plan and permissions. The dashboard only lists datasets available to the selected account or zone. For more information about dataset scopes and sampling, refer to [SQL API datasets](https://developers.cloudflare.com/analytics/sql-api/datasets/).

### Alert details

Each Custom Alert has the following details:

Option | Required | Description  
---|---|---  
Name | Yes | Identifies the alert in notifications and the Cloudflare dashboard.  
Description | No | Records additional context about the alert.  
Destination | Yes | Sends notifications to at least one email address, webhook, or PagerDuty service.  
  
You can add up to 20 email recipients. All plans can use webhooks. PagerDuty requires a Business or higher zone.

### Alert query

Use the query builder or enter custom SQL. The query builder supports these options:

Option | Description  
---|---  
Dataset scope | Limits dataset selection to account-level datasets or datasets for one zone.  
Dataset | Selects one dataset available within the dataset scope.  
Metric | Applies `COUNT` or a supported aggregate function to a numeric field. The builder returns the result as `value`.  
Time range | In Manual mode, sets a fixed data window relative to each evaluation and adds the timestamp bounds.  
Filters | Restricts rows by field value. Available operators depend on the field data type. Multiple filters use `AND`.  
  
For adaptively sampled datasets, the builder uses `APPROX_MIN` and `APPROX_MAX` instead of `MIN` and `MAX`. The SQL API automatically applies sample weights to `COUNT`, `SUM`, and `AVG`.

A custom SQL query must meet these requirements:

  * Return one numeric value in a column named `value`.
  * Read one schema-qualified SQL API dataset.
  * Include an account or zone filter.
  * Include a lower timestamp bound when using Manual time-range mode.
  * Use the [supported SQL syntax](https://developers.cloudflare.com/analytics/sql-api/sql-reference/).
  * Omit a trailing semicolon.



Custom SQL supports two time-range modes:

  * **Automatic** (recommended): Omit the timestamp filter. When the alert runs, Cloudflare supplies a time range ending at the evaluation time and spanning the execution interval.
  * **Manual** : Add a fixed time range to the SQL query. Relative ranges end at the evaluation time.



For example, this query returns the number of server errors during the previous five minutes:
    
    
    SELECT COUNT(*) AS value
    FROM events.httpRequests
    WHERE accountTag = '<ACCOUNT_TAG>'
      AND timestamp >= NOW() - INTERVAL '5' MINUTE
      AND edgeResponseStatus >= 500

Custom Alerts validate the query before saving. Query errors identify unsupported syntax, unavailable datasets or fields, and invalid scope. For SQL API query limits, refer to [Limits](https://developers.cloudflare.com/analytics/sql-api/limits/).

### Detection methods

Choose how Cloudflare evaluates the query result:

Method | Description  
---|---  
Threshold | Compares the query result with a fixed numeric value.  
Anomaly detection | Compares the query result with its historical baseline and detects spikes or drops.  
Service-level objective | Compares the ratio of successful events to total events with a service-level objective (SLO) target.  
  
#### Threshold

A threshold alert supports these options:

Option | Description  
---|---  
Query | Produces the numeric value to evaluate.  
Evaluation window | Sets the data window for each evaluation. You can select a preset or enter a custom duration.  
Comparison operator | Compares the result with the threshold. Supported operators are `<`, `>`, `<=`, `>=`, `==`, and `!=`.  
Threshold | Sets the numeric value used by the comparison.  
  
#### Anomaly detection

Anomaly detection calculates the number of standard deviations between the current result and its historical baseline. It supports these options:

Option | Description  
---|---  
Query | Produces the numeric value to evaluate.  
Evaluation window | Sets the current data window. You can select a preset or enter a custom duration.  
Baseline window | Sets the historical comparison window. The value must be at least six times the evaluation window and no more than `24h`.  
Alert on | Detects spikes, drops, or both spikes and drops.  
Sensitivity | Sets the z-score threshold. Lower values detect smaller changes. You can select a preset or enter a custom value.  
Minimum event count | Optionally suppresses alerts for low-volume evaluation windows.  
  
New anomaly alerts require at least 30 minutes of historical data before they can trigger.

#### Service-level objective

An SLO alert calculates the successful-event percentage from bad and total event counts. Both queries must return a numeric column named `value`. It supports these options:

Option | Description  
---|---  
Bad events query | Counts events that do not meet your success criteria.  
Total events query | Counts all events in the same population as the bad events query.  
Short window | Measures the successful-event percentage over a short period so the alert reacts and resolves quickly.  
Long window | Measures the successful-event percentage over a longer period so brief failures do not trigger the alert.  
SLO target | Triggers when `(1 - bad events / total events) × 100` is below this value for both windows. You can select a preset or customize it.  
Minimum event count | Optionally suppresses alerts for low-volume evaluation windows.  
  
Use equivalent filters in both queries. The bad events query should represent a subset of the total events query.

### Evaluation and notification frequency

Custom Alerts support two independent frequency settings:

Option | Description  
---|---  
Execution interval | Controls how often Cloudflare runs the query. Leave this option at _Default_ to use the fastest interval supported by the dataset. You can select a preset or enter a custom duration of at least one minute.  
Repeat notification interval | Controls how often Cloudflare sends another notification while the alert remains active. You can select a preset or enter a custom duration from one minute through `168h`. The default is `1h`.  
  
Most SQL API datasets support a one-minute execution interval. Log Explorer datasets support a minimum execution interval of 10 minutes. Cloudflare rejects an interval shorter than the selected dataset supports.

### Query preview

The query preview validates and charts an approximation of the signal before you save. Select a preview range to inspect how the alert might behave. The data shown in the preview may differ from the data evaluated by an alert, including historical evaluations.

Threshold previews show the configured threshold. SLO previews show the calculated percentage and target. A query that returns no rows produces no signal and cannot trigger the alert for that evaluation.

## Built-in alerts

Refer to the list below to understand what each alert does and what action to take when you receive one.

## Billing

Usage Based Billing

**Who is it for?**

Customers who want to receive a notification when the usage of a product goes above a set level.

**Other options / filters**

You can choose the product that you want to be notified about and the threshold that fires the notification. Thresholds depend on the product chosen.

For example:

  * Argo Smart Routing has **Notify when total bytes of traffic exceeds** as a threshold.
  * Load Balancing has **Notify when total number of DNS Queries exceeds** as a threshold.

**Included with**

Professional plans or higher.

**Note:** Usage-based billing notifications are available to Pay-as-you-go accounts only. Most Enterprise contract accounts are not supported.

**What should you do if you receive one?**

Review your product usage and adjust the configuration and/or increase the alerting threshold.

## Bots

Bot Detection Alert

**Who is it for?**

Enterprise customers who want to be notified when Cloudflare detects a spike in bot traffic on their zones.

**Other options / filters**

None.

**Included with**

Accounts with at least one Enterprise zone.

**What should you do if you receive one?**

Select the [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) link enclosed in the alert message. Contact support if additional advice is needed on how to investigate the attack further.

**Additional information**

After an alert is created on the dashboard, it may take up to 30 minutes before sufficient data is available to begin detecting traffic anomalies. Verified bot traffic is excluded from bot alerts.

Custom Bot Detection Alert

**Who is it for?**

Enterprise customers who want to be notified when Cloudflare detects a spike in bot traffic on their zones.

**Other options / filters**

Refer to the [alert logic](https://developers.cloudflare.com/bots/reference/alerts/#alert-logic) for more information on additional filters or groupings.

**Included with**

Accounts with at least one Enterprise zone.

**What should you do if you receive one?**

Select the [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) link enclosed in the alert message. Contact support if additional advice is needed on how to investigate the attack further.

**Additional information**

After an alert is created on the dashboard, it may take up to 30 minutes before sufficient data is available to begin detecting traffic anomalies. Verified bot traffic is excluded from both basic and advanced bot alerts.

Alerts with grouping could cause potential noise if you set them up for a high-traffic zone. Grouping alerts function as if you set up separate policies with a filter for each value. Alerts may trigger multiple values in the same group as long as the traffic for each value reaches the threshold of 200.

## Client-side security

Client-side security New Code Change Detection Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when JavaScript dependencies change in the pages of their domain.

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Investigate to confirm that it is an expected change.

**Additional information**

Triggered daily. If configured with a zone filter, the alert is triggered immediately.

Client-side security New Domain Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when resources from new host domains appear in their domain.

**Other options / filters**

None.

**Included with**

Business plans or higher.

**What should you do if you receive one?**

Investigate to confirm that it is an expected change.

**Additional information**

Triggered hourly. If configured with a zone filter, the alert is triggered immediately.

Client-side security New Malicious Domain Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when resources from a known malicious domain appear in their domain. For more information, refer to [Malicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.

For more information, refer to [Review scripts and connections considered malicious](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/).

Client-side security New Malicious Script Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when Cloudflare classifies JavaScript dependencies in their domain as malicious. For more information, refer to [Malicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.

For more information, refer to [Review scripts and connections considered malicious](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/).

Client-side security New Malicious URL Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when resources from a known malicious URL appear in their domain. For more information, refer to [Malicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.

For more information, refer to [Review scripts and connections considered malicious](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/).

Client-side security New Resources Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when new resources appear in their domain.

**Other options / filters**

None.

**Included with**

Business plans or higher.

**What should you do if you receive one?**

Investigate to confirm that it is an expected change.

**Additional information**

Triggered daily. If configured with a zone filter, the alert is triggered immediately.

Client-side security New Resource Exceeds Max URL Length Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when a resource's URL exceeds the maximum allowed length.

**Other options / filters**

None.

**Included with**

Business plans or higher.

**What should you do if you receive one?**

Manually check the resource.

## Cloudflare Access

Expiring Access Service Token Alert

**Who is it for?**

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) customers who want to receive a notification when their service token is about to expire.

**Other options / filters**

None.

**Included with**

Purchase of Access

**What should you do if you receive one?**

Extend the expiration date of the service token. For more details, refer to [Renew your service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#renew-service-tokens).

## Cloudflare Images

Image Notifications

**Who is it for?**

Customers using [Direct creator uploads](https://developers.cloudflare.com/images/upload-images/direct-creator-upload/) to upload images.

**Other options / filters**

None.

**Included with**

Cloudflare images subscription.

**What should you do if you receive one?**

No action is needed.

Image Transformation Notifications

**Who is it for?**

Customers who are using free image transformations and want to be notified if they exceed their free quota.

**Other options / filters**

None.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

No action is needed.

## Cloudflare Status

Maintenance Notification

**Who is it for?**

Customers interested in knowing about planned [Cloudflare maintenance](https://developers.cloudflare.com/support/troubleshooting/disruptive-maintenance/) for specific data centers. The notification lets you know when maintenance has been scheduled, changed, or canceled on an entire point of presence.

**Other options / filters**

You can filter maintenance notifications for specific points of presence and updates (scheduled, changed, canceled).

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

If the notification is announcing new scheduled maintenance, you may want to add the maintenance to your calendar. During these maintenance windows, you may experience a slight increase in latency to the edge location which is under maintenance.

Incident Alerts

**Who is it for?**

Customers interested in knowing about Cloudflare incidents. The notification lets you know when Cloudflare incidents are created, updated, and resolved.

**Other options / filters**

You can filter incident alerts to specific impact levels (minor, major, critical).

Additionally, incident alerts can be filtered to incidents affecting specific components. By default, incident alerts will trigger a notification for incident updates across all impact levels and components.

The impact level and affected components of an incident may change as the incident progresses. A notification will only be sent if the configured filters match at the time of the incident update. Updates will not be sent retroactively.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

Review your [analytics](https://developers.cloudflare.com/analytics/) page to see if your domain is impacted.

## DDoS Protection

HTTP DDoS Attack Alert

**Who is it for?**

[WAF](https://developers.cloudflare.com/waf/) or [CDN](https://developers.cloudflare.com/cache/) customers who want to receive a notification when Cloudflare has mitigated HTTP attacks that generate more than 100 requests per second.

**Other options / filters**

None.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

No action needed. Refer to [DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/) for more information.

Layer 3/4 DDoS Attack Alert

**Who is it for?**

[BYOIP](https://developers.cloudflare.com/byoip/) and [Spectrum](https://developers.cloudflare.com/spectrum/) customers with [Network Analytics](https://developers.cloudflare.com/analytics/network-analytics/) who want to receive a notification when Cloudflare has mitigated attacks that generate an average of at least 12,000 packets per second over a five-second period, with a duration of one minute or more.

**Other options / filters**

None.

**Included with**

Purchase of Magic Transit and/or BYOIP.

**What should you do if you receive one?**

No action needed. Refer to [DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/) for more information.

Advanced HTTP DDoS Attack Alert

**Who is it for?**

[WAF](https://developers.cloudflare.com/waf/) or [CDN](https://developers.cloudflare.com/cache/) customers with the [Advanced DDoS Protection](https://developers.cloudflare.com/ddos-protection/) subscription who want to receive a notification when Cloudflare has mitigated attacks that generate more than the configured number of requests per second (100 rps by default).

**Other options / filters**

You can choose when to trigger a notification.

Available filters include:

  * The zones in the account for which you wish to receive notifications.
  * The specific hostnames for which you wish to receive notifications.
  * The minimum requests-per-second rate that will trigger the alert (100 rps by default).

**Included with**

Enterprise plans with the Advanced DDoS Protection add-on.

**What should you do if you receive one?**

No action needed. Refer to [DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/) for more information.

Advanced Layer 3/4 DDoS Attack Alert

**Who is it for?**

[BYOIP](https://developers.cloudflare.com/byoip/) and [Magic Transit](https://developers.cloudflare.com/magic-transit/) customers with [Network Analytics](https://developers.cloudflare.com/analytics/network-analytics/) who want to receive a notification when Cloudflare has mitigated attacks that generate more than the configured number of packets per second (12,000 pps by default).

**Other options / filters**

You can choose when to trigger a notification.

Available filters include:

  * The IP prefixes for which you wish to receive notifications.
  * The specific IP addresses for which you wish to receive notifications.
  * The minimum packets-per-second rate that will trigger the alert (12,000 pps by default).
  * The minimum megabits-per-second rate that will trigger the alert.
  * The protocols for which you wish to receive notifications (all protocols by default).



If you specify multiple filters, Cloudflare applies an `AND` logic. This means the alert will only trigger if all filters you set are true. Keep this in mind when setting up this alert with more than one filter.

**Included with**

Purchase of Magic Transit and/or BYOIP (Enterprise plans).

**What should you do if you receive one?**

No action needed. Refer to [DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/) for more information.

## DEX

Device connectivity anomaly

**Who is it for?**

Zero Trust customers who want to be notified when Cloudflare detects a spike or drop in the number of devices connected to the WARP client.

**Other options / filters**

  * **Alert configuration** : Choose when to trigger a notification. Available options are _Connectivity spike_ , _Connectivity drop_ , and _Connectivity spike or drop_.
  * Filters: 
    * **Colo** : Cloudflare data center that the device is connected to.
    * **Platform** : Operating system of the device.
    * **Version** : WARP client version (for example, `2024.3.409.0`).
    * **Mode** : [WARP mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/) deployed on the device.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

Review your [fleet status](https://developers.cloudflare.com/cloudflare-one/insights/dex/fleet-status/) to investigate why the spike or drop occurred and which devices are impacted.

**Additional information**

To learn more about the alert logic, refer to [Z-score](https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/#z-score).

DEX test latency

**Who is it for?**

Zero Trust customers who wish to receive alerts when there is a spike or drop in application latency, as measured by the HTTP test [Resource Fetch time](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/#test-results) or Traceroute test [Round trip time](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/#test-results). Requires setting up a [DEX test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/).

**Other options / filters**

  * **Alert configuration** : Choose when to trigger a notification. Available options are _Latency spike_ , _Latency drop_ , and _Latency spike or drop_.
  * Filters: 
    * **Colo** : Cloudflare data center that the device is connected to.
    * **Platform** : Operating system of the device.
    * **Version** : WARP client version (for example, `2024.3.409.0`).
    * **Test name** : Choose which DEX test the alert should monitor. You will receive individual notifications for each test.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

View your [test results](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/) to investigate why the spike occurred.

**Additional information**

To learn more about the alert logic, refer to [Z-score](https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/#z-score).

DEX test low availability

**Who is it for?**

Zero Trust customers who wish to receive alerts when the percentage of successful HTTP or traceroute requests to an application drops below the selected service-level objective (SLO). Requires setting up a [DEX test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/).

**Other options / filters**

  * **Service Level Objective (SLO)** : Specify the availability threshold that will trigger an alert. Enter a percentage in `xx.x` format (for example, `98.0`).
  * Filters: 
    * **Colo** : Cloudflare data center that the device is connected to.
    * **Platform** : Operating system of the device.
    * **Version** : WARP client version (for example, `2024.3.409.0`).
    * **Test name** : Choose which DEX test the alert should monitor. You will receive individual notifications for each test.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

View your [test results](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/) to investigate why the degradation occurred.

**Additional information**

To learn more about the alert logic, refer to [SLO](https://developers.cloudflare.com/cloudflare-one/insights/dex/notifications/#slo).

## DNS

Secondary DNS all Primaries Failing

**Who is it for?**

Enterprise customers who have at least one secondary zone in their account and want to receive a notification if all of their primary nameservers are failing.

**Other options / filters**

None.

**Included with**

Purchase of Secondary DNS

**What should you do if you receive one?**

  1. Confirm that your primary nameservers are up and running.
  2. Confirm that the [Access Control Lists (ACLs)](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/) on your primary nameservers are configured correctly.
  3. Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).



Secondary DNS Primaries Failing

**Who is it for?**

Enterprise customers who have at least one secondary zone and want to receive a notification if at least one of their primary nameservers is failing while transfers from at least one other primary are still successful.

**Other options / filters**

None.

**Included with**

Purchase of Secondary DNS.

**What should you do if you receive one?**

  1. Confirm that your primary nameservers are up and running.
  2. Confirm that the [Access Control Lists (ACLs)](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/) on your primary nameservers are configured correctly.
  3. Confirm that your primary nameservers are configured correctly in your Cloudflare account (correct IP, port, TSIG).



Secondary DNS Successfully Updated

**Who is it for?**

Enterprise customers who have at least one secondary zone in their account and want to receive a notification on successful zone transfers.

**Other options / filters**

None.

**Included with**

Purchase of Secondary DNS.

**What should you do if you receive one?**

No action needed. Everything is working correctly.

Secondary DNS Warning

**Who is it for?**

Customers who are using Cloudflare for Secondary DNS and want to receive notifications about warnings issued by the transferred zone.

**Other options / filters**

None.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

Actions for failure notifications will depend on the type of failure.

## Health Checks

Health Checks status notification

**Who is it for?**

Customers who want to be warned about changes to server health as determined by [health checks](https://developers.cloudflare.com/health-checks/).

**Other options / filters**

Available filters include:

  * You can search for and add health checks from your list of health checks.
  * You can choose a trigger to fire the notification when your server becomes **unhealthy** , **healthy** , or **either healthy or unhealthy**.

**Included with**

Professional plans or higher.

**What should you do if you receive one?**

Review your [health check analytics](https://developers.cloudflare.com/health-checks/health-checks-analytics/#common-error-codes).

## Load Balancing

Pool Enablement

**Who is it for?**

Customers who want to be warned about status changes (enabled/disabled) in their pools.

**Other options / filters**

Available filters include:

  * You can search for and add pools from your list of pools. If no pools are selected, the alert will apply to all pools in the account.
  * You can also choose the trigger that fires the notification when the Load Balancing pool is **enabled** , **disabled** , and **either enabled or disabled**.

**Included with**

Purchase of [Load Balancing](https://developers.cloudflare.com/load-balancing/get-started/enable-load-balancing/).

**What should you do if you receive one?**

No action is needed.

Load Balancing Health Alert

**Who is it for?**

Customers who want to be warned about [changes in health status](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/) in their pools or origins.

**Other options / filters**

Available filters include:

  * You can search for and add pools from your list of pools, as well as **Include future pools** (if all pools are selected).
  * You can choose the trigger that fires the notification when the health status becomes **unhealthy** , **healthy** , or **either unhealthy or healthy**
  * You can choose the trigger that fires the notification when the event source health status changes in **pool** , **origin** , or **either pool or origin**.

**Included with**

Purchase of [Load Balancing](https://developers.cloudflare.com/load-balancing/get-started/enable-load-balancing/).

**What should you do if you receive one?**

Evaluate [load balancing analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) to review changes in health status over time.

## Logpush

Failing Logpush Job Disabled

**Who is it for?**

Enterprise customers who use [Logpush](https://developers.cloudflare.com/logs/) and want to monitor their job health.

**Other options / filters**

  * Notification Name: A custom name for the notification.
  * Description (optional): A custom description for the notification.
  * Notification Email (can be multiple emails): The email address of the recipient for the notification.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

In the email for the notification, you can find the destination name for the failing Logpush job. With this destination name, you should be able to figure out which zone this relates to. There can be multiple reasons why a job fails, but it is best to test that the destination endpoint is healthy, and that necessary credentials are still working. You can also check that the destination has allowlisted [Cloudflare IPs](https://www.cloudflare.com/ips/).

## Magic Transit

Network Flow - Auto Advertisement

**Who is it for?**

[Magic Transit on-demand](https://developers.cloudflare.com/magic-transit/on-demand/) customers who use Flow-Based Monitoring and want alerts when Magic Transit is automatically enabled.

**Other options / filters**

None.

**Included with**

Purchase of Magic Transit.

**What should you do if you receive one?**

No action is needed. You can go to the [Cloudflare dashboard](https://dash.cloudflare.com/?to=/:account/magic-transit) to review the health and status of your tunnels.

Network Flow - DDoS Attack

**Who is it for?**

[BYOIP](https://developers.cloudflare.com/byoip/) and [Spectrum](https://developers.cloudflare.com/spectrum/) customers with [Network Analytics](https://developers.cloudflare.com/analytics/network-analytics/) who want to receive a notification when Cloudflare has mitigated attacks that generate an average of at least 12,000 packets per second over a five-second period, with a duration of one minute or more.

**Other options / filters**

None.

**Included with**

Purchase of Magic Transit and/or BYOIP.

**What should you do if you receive one?**

No action needed. Refer to [DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/) for more information.

Network Flow - Volumetric Attack

**Who is it for?**

[Magic Transit on-demand](https://developers.cloudflare.com/magic-transit/on-demand/) customers who are using Flow-Based Monitoring to detect attacks when Magic Transit is disabled.

**Other options / filters**

None.

**Included with**

Purchase of Magic Transit.

**What should you do if you receive one?**

If you do not have auto advertisement enabled, you need to advertise your IP prefixes to enable Magic Transit. For more information, refer to [Dynamic advertisement](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/).

Magic Tunnel Health Check Alert

**Who is it for?**

Magic Transit and Cloudflare WAN customers who wish to receive alerts when the percentage of tunnel states meeting the selected service-level objective (SLO) drops below the defined threshold for a Magic Tunnel.

**Other options / filters**

  * Notification Name: A custom name for the notification.
  * Description (optional): A custom description for the notification.
  * Notification Email (can be multiple emails): The email address of recipient for the notification.
  * Webhooks
  * Tunnels: Choose one or more tunnels to monitor.
  * SLO: Define SLO threshold for Magic Tunnel health alerts. Available options are _High_ , _Medium_ , and _Low_.

**Included with**

Purchase of Magic Transit and Cloudflare WAN.

**What should you do if you receive one?**

Refer to the [Magic Transit tunnel health](https://developers.cloudflare.com/magic-transit/network-health/check-tunnel-health-dashboard/) or [Cloudflare WAN IPsec/GRE tunnel health](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/) for more information on what the issue might be.

## Network Interconnect

Connection Maintenance Alert

**Who is it for?**

[Classic CNI](https://developers.cloudflare.com/network-interconnect/classic-cni/) customers who want to be alerted to maintenance events that might affect Classic CNI.

**Other options / filters**

None.

**Included with**

Purchase of Cloudflare Network Interconnect (CNI).

**What should you do if you receive one?**

No action is needed.

## Pages

Project updates

**Who is it for?**

Customers who want to receive notifications about project-level events in [Cloudflare Pages](https://developers.cloudflare.com/pages/).

**Other options / filters**

Available filters include:

  * Pages projects
  * Environments
  * Different events: **Deployment started** , **Deployment failed** , or **Deployment success**

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

For failed deployments, review our [debugging guide](https://developers.cloudflare.com/pages/configuration/debugging-pages/#check-your-build-log).

## Radar

Radar Alerts

**Who is it for?**

Customers who want to receive a notification when traffic anomalies, outages, route hijacks, or route leaks are impacting one or more countries, regions, or autonomous systems (ASNs) of interest.

**Other options / filters**

Filters include:

  * Notification type (anomaly, outage, route hijack, route leak)
  * Location (country or region)
  * Autonomous systems (ASNs)



You have the option to send the notification via email, webhook, or PagerDuty.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

Further action will depend on your role. Refer to the [Radar documentation](https://developers.cloudflare.com/radar/) for more information.

## Route Leak Detection

Route Leak Detection Alert

**Who is it for?**

[BYOIP customers](https://developers.cloudflare.com/byoip/) who want to receive a notification when their prefixes are advertised in places they should not be.

**Other options / filters**

None.

**Included with**

Purchase of BYOIP.

**What should you do if you receive one?**

Confirm your traffic is healthy. Reach out to your transit providers to ensure you are behaving as expected and ask them to follow up with any providers accepting the unauthorized routes.

## SSL/TLS

Access mTLS Certificate Expiration Alert

**Who is it for?**

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) customers that use client certificates for mutual TLS authentication. This notification will be sent 30 and 14 days before the expiration of the certificate.

**Other options / filters**

None.

**Included with**

Purchase of [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/) and/or [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/).

**What should you do if you receive one?**

Upload a [renewed certificate](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#add-mtls-authentication-to-your-access-configuration).

Advanced Certificate Alert

**Who is it for?**

Customers with [advanced certificates](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) that want to be alerted on validation, issuance, renewal, and expiration of certificates.

**Other options / filters**

None.

**Included with**

When an advanced certificate is validated, issued, renewed, or expired.

**What should you do if you receive one?**

Action only needed if notification is about a certificate that failed to be issued. Refer to [SSL expired or SSL mismatch errors](https://developers.cloudflare.com/ssl/troubleshooting/version-cipher-mismatch/) for more information.

Hostname-level Authenticated Origin Pulls Certificate Expiration Alert

**Who is it for?**

Customers that upload their own certificate to use with hostname-level Authenticated Origin Pull (AOP) to secure connections from Cloudflare to their origin server. AOP certificate expiration notifications are sent 30 days and 14 days before the certificate expiry.

**Other options / filters**

None.

**Included with**

Authenticated Origin Pull.

**What should you do if you receive one?**

Upload a renewed certificate to use for [hostname-level AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/).

SSL for SaaS Custom Hostnames Alert

**Who is it for?**

Customers with custom hostname certificates who want to receive a notification on validation, issuance, renewal, and expiration of certificates. For more details around data formatting for webhooks, refer to the [Cloudflare for SaaS docs](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/webhook-definitions/).

**Other options / filters**

None.

**Included with**

Purchase of [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/).

**What should you do if you receive one?**

You only need to take action if you are notified that you have a certificate that failed. You can find the reasons why a certificate is not being issued in [Troubleshooting SSL errors](https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/).

Universal SSL Alert

**Who is it for?**

Customers with universal certificates who want to receive a notification on validation, issuance, renewal, and expiration notices.

**Other options / filters**

None.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

You only need to take action if you are notified that you have a certificate that failed. You can find the reasons why a certificate is not being issued in [Troubleshooting SSL errors](https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/).

Zone-level Authenticated Origin Pulls Certificate Expiration Alert

**Who is it for?**

Customers that upload their own certificate to use with zone-level Authenticated Origin Pull (AOP) to secure connections from Cloudflare to their origin server. AOP certificate expiration notifications are sent 30 days and 14 days before the certificate expiry.

**Other options / filters**

None.

**Included with**

Authenticated Origin Pull.

**What should you do if you receive one?**

Upload a renewed certificate to use for [zone-level AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/).

mTLS Certificate Store Certificate Expiration Alert

**Who is it for?**

Customers that upload their own client certificates for mTLS via [bring your own CA](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/).

This notification will be sent 30 and 14 days before the expiration of the certificate.

**Other options / filters**

None.

**Included with**

[Bring your own CA](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/).

The mTLS Certificate Store refers to customer uploaded certificates and does not include client certificates generated with the [Cloudflare CA](https://developers.cloudflare.com/ssl/client-certificates/#how-it-works).

**What should you do if you receive one?**

Upload a renewed certificate.

## Security Center

Brand Protection Alerts

**Who is it for?**

Customers who want a summary of activity related to [Brand Protection](https://developers.cloudflare.com/security-center/brand-protection/).

**Other options / filters**

You can set up Brand Protection Alerts on individual monitored queries. For more details, refer to [Brand Protection Alerts](https://developers.cloudflare.com/security-center/brand-protection/#brand-protection-alerts).

**Included with**

Professional plans or higher.

**What should you do if you receive one?**

Investigate and potentially block any suspicious domains that may be trying to impersonate your brand.

Brand Protection Digest

**Who is it for?**

Customers who want a summary of activity related to [Brand Protection](https://developers.cloudflare.com/security-center/brand-protection/).

**Other options / filters**

You can set up Brand Protection Digest on individual monitored queries. For more details, refer to [Brand Protection Alerts](https://developers.cloudflare.com/security-center/brand-protection/#brand-protection-alerts).

**Included with**

Professional plans or higher.

**What should you do if you receive one?**

Investigate and potentially block any suspicious domains that may be trying to impersonate your brand.

Logo Match Alerts

**Who is it for?**

Customers who want to receive a notification when the [Brand Protection](https://developers.cloudflare.com/security-center/brand-protection/) system detects a new domain which is using the uploaded logo and might be infringing copyright.

**Other options / filters**

You can select the query that you want to be alerted on.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

Review the domains and URLs that are potentially impersonating your brand.

Security Insights

**Who is it for?**

Customers who want to receive notifications based on security insights findings.

**Other options / filters**

You can select the insight(s) you want to be alerted on.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

Review the insight and decide whether you want to resolve it, archive it, or export it.

Abuse report

**Who is it for?**

Customers who want to be alerted in the event that an abuse report is filed against their website.

**Other options / filters**

You can filter the reports based on date, report status, report type, and domain.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

View our guidance on [customer abuse report obligations](https://developers.cloudflare.com/fundamentals/reference/report-abuse/abuse-report-obligations/) and more information on how to [view and submit abuse reports](https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/).

## Stream

Stream Live Notifications

**Who is it for?**

Customers who are using [Stream](https://developers.cloudflare.com/stream/) and want to receive webhooks with the status of their videos.

**Other options / filters**

You can input Stream Live IDs to receive notifications only about those inputs. If left blank, you will receive a list for all inputs.

The following input states will fire notifications. You can toggle them on or off:

  * `live_input.connected`
  * `live_input.disconnected`

**Included with**

Stream subscription.

**What should you do if you receive one?**

Stream notifications are entirely customizable by the customer. Action will depend on the customizations enabled.

## Traffic Monitoring

Advanced Error Rate Alert

**Who is it for?**

Enterprise customers who want to receive a notification when Cloudflare detects edge and/or origin errors. Refer to [HTTP Traffic Alerts](https://developers.cloudflare.com/notifications/reference/traffic-alerts/) for more information.

**Other options / filters**

Available filters include:

  * You can search and add domains from your list of domains.
  * You can filter alerts by **edge status code** , **origin status code** , and the **IP Address**.
  * You can also choose the trigger that fires the notification. Available triggers are **low sensitivity** , **medium sensitivity** , **high sensitivity** , or **very high sensitivity**.



You can also toggle Alert Grouping to receive separate alerts for your domain, edge status code, and/or origin status code.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

  1. Use the link in the notification you received to see which error codes Cloudflare is seeing.
  2. Depending on the statuses you are alerting on, refer to [Troubleshooting Cloudflare 5XX errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/).

**Limitations**

Traffic Monitoring alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.

These thresholds cannot be configured. Service level objectives (SLOs) are used to determine the threshold.

Origin Error Rate Alert

**Who is it for?**

Enterprise customers who want to receive a notification when Cloudflare is unable to access their origin server. Refer to [HTTP Traffic Alerts](https://developers.cloudflare.com/notifications/reference/traffic-alerts/) for more information.

**Other options / filters**

Multiple filters available:

  * You can search and add domains from your list of domains.
  * You can also choose the trigger that fires the notification. Available triggers are **low sensitivity** , **medium sensitivity** , **high sensitivity** , or **very high sensitivity**.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

  1. Use the link in the Notification you received to see which error codes Cloudflare is seeing from your origin.
  2. Refer to [Troubleshooting Cloudflare 5XX errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/) to learn how to troubleshoot these errors.

**Limitations**

Traffic Monitoring alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.

These thresholds cannot be configured. Service level objectives (SLOs) are used to determine the threshold.

Traffic Anomalies Alert

**Who is it for?**

Enterprise customers who want to receive a notification when one zone is experiencing an unexpected spike or drop in traffic. Refer to [HTTP Traffic Alerts](https://developers.cloudflare.com/notifications/reference/traffic-alerts/) for more information.

**Other options / filters**

Multiple filters available:

  * You can search and add domains from your list of domains.
  * You can include or exclude traffic mitigated by the [Web Application Firewall (WAF)](https://developers.cloudflare.com/waf/).
  * You can choose whether to be notified of either spikes or drops in traffic.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

Use the link in the Notification you received to view if the spike or drop is significant enough to require further actions.

**Limitations**

Traffic Monitoring alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.

These thresholds cannot be configured. Z-score is used to determine the threshold.

## Trust and Safety Blocks

Block Review Rejection

**Who is it for?**

Customers who want to be notified when Cloudflare Trust & Safety rejects a request for block removal.

**Other options / filters**

None.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

Take care of any abuse on your website. Then, go to the [Cloudflare dashboard](https://dash.cloudflare.com/) and request a review.

New Blocks

**Who is it for?**

Customers who want to be notified when Cloudflare Trust & Safety places a block on their website.

**Other options / filters**

None.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

Take care of any abuse on your website. Then, go to the [Cloudflare dashboard](https://dash.cloudflare.com/) and request a review.

Removed Blocks

**Who is it for?**

Customers who want to be notified when Cloudflare Trust & Safety removes a block from their website.

**Other options / filters**

None.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

This is informational follow up.

## Tunnel

Tunnel Creation or Deletion Event

**Who is it for?**

Customers who want to receive a notification when Cloudflare Tunnels are created or deleted in their account.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

No action is needed.

Tunnel Health Alert

**Who is it for?**

Customers who want to be warned about changes in health status for their Cloudflare Tunnels.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

Monitor tunnel health over time and consider deploying [`cloudflared` replicas or load balancers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/).

**Additional information**

Refer to [Tunnel status](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status) to review the list of possible tunnel statuses (`Healthy`, `Inactive`, `Down` and `Degraded`).

## Web Analytics

Weekly summary

**Who is it for?**

Customers using [Web Analytics](https://developers.cloudflare.com/web-analytics/) to monitor their website's performance.

**Other options / filters**

None.

**Included with**

All Cloudflare plans.

**What should you do if you receive one?**

No action is needed. This notification is a weekly summary with reports from your Web Analytics account. Refer to [Notifications](https://dash.cloudflare.com/?to=/:account/notifications) in the Cloudflare dashboard to refine your notifications settings.

## Web Application Firewall (WAF)

Advanced Security Events Alert

**Who is it for?**

Enterprise customers who want to receive alerts about spikes in specific services that generate log entries in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/). For more information, refer to [WAF alerts](https://developers.cloudflare.com/waf/reference/alerts/).

**Other options / filters**

A mandatory [`filters`](https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/create/) selection is needed when you create a notification policy which includes the list of services and zones that you want to be alerted on.

  * You can search for and add domains from your list of Enterprise zones.
  * You can choose which services the alert should monitor (Managed Firewall, Rate Limiting, etc.).
  * You can filter events by a targeted action.

**Included with**

Enterprise plans.

**What should you do if you receive one?**

Review the information in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/) to identify any possible attack or misconfiguration.

**Additional information**

The mean time to detection is five minutes.

When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately and can be selected as a filter.

**Limitations**

Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.

These thresholds cannot be configured. Z-score is used to determine the threshold.

Security Events Alert

**Who is it for?**

Business and Enterprise customers who want to receive alerts about spikes across all services that generate log entries in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/). For more information, refer to [WAF alerts](https://developers.cloudflare.com/waf/reference/alerts/).

**Other options / filters**

A mandatory [`filters`](https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/create/) selection is needed when you create a notification policy which includes the list of zones that you want to be alerted on.

  * You can also search for and add domains from your list of business or enterprise zones. The notification will be sent for the domains chosen.
  * You can filter events by a targeted action.

**Included with**

Business and Enterprise plans.

**What should you do if you receive one?**

Review the information in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/) to identify any possible attack or misconfiguration.

**Additional information**

The mean time to detection is five minutes.

When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately.

**Limitations**

Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.

These thresholds cannot be configured. Z-score is used to determine the threshold.

[PreviousConfigure webhooks](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/)[NextAlert history](https://developers.cloudflare.com/notifications/notification-history/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/notifications/notification-available.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

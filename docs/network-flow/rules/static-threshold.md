---
url: https://developers.cloudflare.com/network-flow/rules/static-threshold/
title: Static threshold rule \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:24.050692+00:00
---

# Static threshold rule · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/rules/static-threshold/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /[Rules](https://developers.cloudflare.com/network-flow/rules/)
  4. /Static threshold rule



# Static threshold rule

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/rules/static-threshold/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRule configuration fieldsAPI documentationRecommended rule configuration Rule IP prefixes Rule threshold Rule duration Adjusting rules over time

A static threshold rule monitors your network traffic against a fixed threshold you define, measured in bits or packets per second. Network Flow (formerly Magic Network Monitoring) compares total traffic across all IP prefixes and addresses in the rule against this threshold. If traffic exceeds the threshold for the configured duration, Network Flow sends an alert.

To use static threshold rules, you must send NetFlow or sFlow data to Cloudflare.

## Rule configuration fields

Field | Description  
---|---  
**Rule name** | Must be unique and cannot contain spaces. Supports characters `A-Z`, `a-z`, `0-9`, underscore (`_`), dash (`-`), period (`.`), and tilde (`~`). Maximum of 256 characters.  
**Rule type** | threshold  
**Rule threshold type** | Can be defined in either bits per second or packets per second.  
**Rule threshold** | The number of bits per second or packets per second for the rule alert. When this value is exceeded for the rule duration, an alert notification is sent. Minimum of `1` and no maximum.  
**Rule duration** | The amount of time in minutes the rule threshold must exceed to send an alert notification. Choose from the following values: `1`, `5`, `10`, `15`, `20`, `30`, `45`, or `60` minutes.  
**Auto-advertisement** | If you are a Magic Transit On Demand customer, you can enable this feature to automatically enable Magic Transit if the rule alert is triggered. Network Flow (formerly Magic Network Monitoring) supports Magic Transit's supernet capability. To learn more refer to Auto-Advertisement section.  
**Rule IP prefix** | The IP prefix associated with the rule for monitoring traffic volume. Must be a CIDR range such as `160.168.0.1/24`. Max is 5,000 unique CIDR entries. To learn more, refer to Rule IP prefixes.  
  
## API documentation

To review an example static threshold rule, go to the [Rules](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/) section in the Network Flow API documentation.

## Recommended rule configuration

Follow the guidelines in Rule IP prefixes, Rule threshold, and Rule duration to create appropriate Network Flow rules and set accurate thresholds.

### Rule IP prefixes

Cloudflare recommends starting with one Network Flow rule for each public `/24` IP prefix in your network. Including the range of the `/24` prefix in the rule name makes it easier to find and filter in Network Flow analytics.

As you become more familiar with traffic patterns across each prefix, create more specific rules with IP prefixes smaller or larger than `/24` depending on your needs. You can also combine multiple IP prefixes in a single rule.

### Rule threshold

Follow the steps in Initial rule configuration and Setting the appropriate threshold to configure appropriate rule thresholds.

#### Initial rule configuration

When you first configure Network Flow, you may not know the typical traffic patterns for each IP prefix. Set an initial threshold high enough that it is unlikely to trigger during setup — Cloudflare recommends 10 Gbps or 10 Mpps.

This lets you collect baseline traffic data without receiving alerts. After configuring your initial rules, monitor for alerts and review traffic in Network Flow Analytics. Over time, update each rule's threshold based on historical traffic data.

Threshold type | Recommended rule threshold to collect initial data  
---|---  
Bits | 10 Gbps (10,000,000,000 bits per second)  
Packets | 10 Mpps (10,000,000 packets per second)  
  
#### Setting the appropriate threshold

After creating the initial set of rules to monitor your network traffic, you should collect 14-30 days of historical traffic volume data for each rule.

Cloudflare recommends that you set a rule threshold that is two times larger than the maximum non-attack traffic observed for a one minute time interval within a Network Flow rule.

To find the maximum non-attack traffic for a one minute time interval over the past 14-30 days, filter for the specific rule you want to analyze:

  1. Go to the **Network flow** page.

[ Go to **Network flow** ↗ ](https://dash.cloudflare.com/?to=/:account/networking-insights/analytics/network-analytics/flow-analytics)

  2. Select **Add filter**.
  3. In **New filter** , use the drop-down menus to create the following filter:



Field | Operator | Rule name  
---|---|---  
_Monitoring Rule_ | _equals_ | `<RULE_NAME>`  
  
Once the rule filter is selected in Network Flow Analytics, you can check the historical traffic volume data for the rule over the selected time period. Cloudflare recommends reviewing historical data in seven-day increments, since that is the largest window that shows one-hour time intervals. To select a custom seven-day range, go to the top right corner of Network Flow analytics, open the time window drop-down menu, and select **Custom range**.

You should review the selected seven-day time range and identify the largest traffic volume peak. Then, click and drag on the largest traffic peak to view the traffic volume data for a smaller time window. Continue until you are viewing the traffic volume data in one-minute intervals.

Record the largest traffic volume peak for the rule in a spreadsheet, then repeat this process across 14-30 days of data. The rule threshold should be updated to be two times the largest traffic spike for a one minute time interval across 14-30 days of data. You should go through this process to set the threshold for each Network Flow rule.

### Rule duration

Your IP prefixes may experience inconsistent spikes across one-minute intervals. Set a rule duration of at least two minutes to reduce false positive alerts from short-term non-malicious traffic spikes. A two-minute duration means traffic must stay above the threshold for two minutes before an alert fires.

### Adjusting rules over time

After updating your first set of thresholds based on historical data, monitor for Network Flow alerts to verify the thresholds are appropriate. Adjust thresholds and duration over time to find the right alert sensitivity for your network environment.

[PreviousOverview](https://developers.cloudflare.com/network-flow/rules/)[NextDynamic threshold rule](https://developers.cloudflare.com/network-flow/rules/dynamic-threshold/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/rules/static-threshold.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

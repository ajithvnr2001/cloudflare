---
url: https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/
title: Adjust the data displayed in Network Analytics \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.645713+00:00
---

# Adjust the data displayed in Network Analytics · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Network analytics](https://developers.cloudflare.com/analytics/network-analytics/)

  4. /Configure
  5. /Adjust the displayed data



# Adjust the displayed data

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSelect the appropriate tabSelect high-level metricSelect a dimensionApply filters Select Add filter Select a stat filterCreate a Network Firewall rule from the applied filtersShow IP prefix eventsView logged or monitored traffic

## Select the appropriate tab

To perform a broad analysis of layer 3/4 traffic and DDoS attacks, use the **All traffic** tab.

To focus on a specific mitigation system, select one of the [other available tabs](https://developers.cloudflare.com/analytics/network-analytics/understand/main-dashboard/#available-tabs). The tabs displayed in the dashboard depend on your Cloudflare services.

## Select high-level metric

To toggle your view of the data, select the **Total packets** or **Total bytes** side panels.

![Network Analytics side panels allowing you to use packets or bits/bytes as the base unit for the dashboard.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1440,height=602,format=webp/_astro/high-level-metrics.DFUDKbKH.png)

_Note: Labels in this image may reflect a previous product name._

The selected metric will determine the base units (packets or bits/bytes) used in the several dashboard analytics panels.

## Select a dimension

Under **Packets summary** or **Bits summary** , select one of the [available dimensions](https://developers.cloudflare.com/analytics/network-analytics/understand/main-dashboard/#available-dimensions) to view the data along that dimension. The default dimension is **Action**.

## Apply filters

You can apply multiple filters and exclusions to adjust the scope of the data displayed in Network Analytics. Filters affect all the data displayed in the dashboard.

There are two ways to filter Network Analytics data: select **Add filter** or select one of the stat filters.

### Select Add filter

Select **Add filter** to open the **New filter** popover. Specify a field, an operator, and a value to complete your filter expression. Select **Apply** to update the view.

Notes about filtering

When applying filters, observe these guidelines:

  * Wildcards are not supported.
  * You do not need to wrap values in quotes.
  * When specifying an ASN number, leave out the `AS` prefix. For example, enter `1423` instead of `AS1423`.



### Select a stat filter

To filter based on the type of data associated with one of the Network Analytics stats, use the **Filter** and **Exclude** buttons that display when you hover over the stat.

## Create a Network Firewall rule from the applied filters

Note

This feature is only available to Magic Transit and Cloudflare WAN (formerly Magic WAN) users.

Select **Create Network Firewall rule** to create a [Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) rule that will block all traffic matching the selected filters in Network Analytics.

Note that some filters will not be added to the new Network Firewall rule definition. However, you can further configure the rule in Network Firewall.

## Show IP prefix events

Enable the **Show annotations** toggle to show or hide annotations for advertised/withdrawn IP prefix events in the **Network Analytics** view. Select each annotation to get more details.

![Network Analytics chart displaying IP prefix-related annotations.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=785,height=555,format=webp/_astro/view-annotations.D18njKAr.png)

## View logged or monitored traffic

[Network DDoS managed rules](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/) and [Advanced DDoS Protection systems](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/) provide a `log` or `monitoring` mode that does not drop traffic. These `log` and `monitoring` mode events are based on **Verdict** and **Outcome** /**Action** fields.

To filter for these traffic events:

  1. In the Cloudflare dashboard, go to the **Network Analytics** page.

[ Go to **Network analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/networking-insights/analytics/network-analytics/transport-analytics)
  2. Go to **DDoS managed rules** tab.

  3. Select **Add filter**.

     * Set `Verdict equals drop`.
     * Set `Action equals pass`.
  4. Select **Apply**.




By setting `verdict` to `drop` and `outcome` as `pass`, we are filtering for traffic that was marked as a detection (that is, verdict was `drop`) but was not dropped (for example, outcome was `pass`).

[PreviousAdjust the time range](https://developers.cloudflare.com/analytics/network-analytics/configure/time-range/)[NextShare and export data](https://developers.cloudflare.com/analytics/network-analytics/configure/share-export/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/network-analytics/configure/displayed-data.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

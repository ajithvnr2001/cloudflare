---
url: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/
title: View test results \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:50.647942+00:00
---

# View test results · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Digital experience](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

  4. /[Synthetic tests](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/)
  5. /View test results



# View test results

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesView results for all devicesView results for an individual deviceExport DEX application test logsRelated resources

Use the results of a Digital Experience Monitoring (DEX) test to monitor availability and performance for a specific application. DEX stores test results for 7 days on all plans, according to the [log retention policy](https://developers.cloudflare.com/cloudflare-one/insights/logs/#log-retention).

## Prerequisites

  * At least one [test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) has been created under **DEX** > **Tests**.
  * Admins must have at least the [Cloudflare Zero Trust Reporting role](https://developers.cloudflare.com/cloudflare-one/roles-permissions/#zero-trust-roles).



## View results for all devices

To view an overview of test results for all devices:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Insights** > **Digital experience**.
  2. Select the **Tests** tab.
  3. Select a test to view detailed results.



## View results for an individual device

To view analytics on a per-device level:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Team & Resources** > **Devices** > **Your devices**.
  2. Select the device you want to view, and then select **View details**.
  3. Select the **Tests** tab.
  4. Select a test to view detailed results.



## Export DEX application test logs

You can use [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) to export [DEX application test](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/) data to [R2](https://developers.cloudflare.com/r2/) (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the [7-day log retention period](https://developers.cloudflare.com/cloudflare-one/insights/logs/#log-retention) or correlate DEX data with other log sources.

## Related resources

  * [DEX HTTP test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/) \- Send a `GET` request from enrolled devices to a web application and measure response times.
  * [DEX Traceroute test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/) \- Map the network route between a device and a server, showing each hop along the path.
  * [DEX rules](https://developers.cloudflare.com/cloudflare-one/insights/dex/rules/) \- Define which users or groups a test applies to, using selectors such as user email, user group, operating system, or managed network.



[PreviousTraceroute test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/)[NextRules](https://developers.cloudflare.com/cloudflare-one/insights/dex/rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/dex/tests/view-results.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

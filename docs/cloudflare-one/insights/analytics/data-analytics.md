---
url: https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/
title: Data security analytics \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:47.437433+00:00
---

# Data security analytics · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)

  4. /[Dashboards](https://developers.cloudflare.com/cloudflare-one/insights/analytics/)
  5. /Data security analytics



# Data security analytics

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesAvailable insights SaaS and Cloud findings by count Posture findings by Severity DLP matches in HTTP requests over time

The Data security analytics dashboard reports security issues and sensitive data found within your SaaS applications, cloud environments, and HTTP traffic. It combines Cloud Access Security Broker (CASB) findings with activity from Data Loss Prevention (DLP) policies. If neither DLP policies nor CASB integrations are configured in your account, the dashboard appears empty.

To view the Data security analytics dashboard:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights**.
  2. Go to **Dashboards**.
  3. Select **Data security analytics**.



Refer to [Insights overview](https://developers.cloudflare.com/cloudflare-one/insights/) to learn how to use Analytics dashboards together with [Analytics Overview](https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/) and [Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) for complete visibility and troubleshooting.

## Prerequisites

To populate this dashboard with partial data, you need at least one of the following:

  * At least one HTTP policy that references a [DLP profile](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/).
  * At least one SaaS integration enrolled in [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/).
  * At least one Cloud integration enrolled in [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/).
  * At least one SaaS or Cloud integration enrolled in [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) and a DLP profile applied to it.



To learn which sensitive data types appear in your Gateway traffic before creating a DLP policy, use [Passive Detection](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/). It shows sampled detections separately from the policy activity on this dashboard.

## Available insights

The dashboard includes the following panels and metrics:

  * [SaaS and Cloud findings by count](https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/#saas-and-cloud-findings-by-count)
  * [Posture findings by Severity](https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/#posture-findings-by-severity)
  * [DLP matches in HTTP requests over time](https://developers.cloudflare.com/cloudflare-one/insights/analytics/data-analytics/#dlp-matches-in-http-requests-over-time)
  * Top integrations by posture findings
  * Top integrations by content findings
  * Top cloud resources by findings
  * Top users by DLP policies triggered



### SaaS and Cloud findings by count

The SaaS and Cloud findings by count chart shows a time series view of Posture and Content findings. [Posture findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#posture-findings) are configuration and access issues detected by CASB, such as misconfigurations, unauthorized user activity, and other data security issues. [Content findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#content-findings) are instances of potential data exposure as identified by [DLP](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/).

Each bar represents the total number of findings detected within a given time interval. You can use this view to observe patterns or spikes in findings over time. Hover over any bar to view the exact count of Posture and Content findings for that period.

To review findings in detail, log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and go to **Zero Trust** > **Cloud & SaaS findings** > **Posture Findings** or **Content Findings**.

### Posture findings by Severity

The Posture findings by severity chart displays the distribution of CASB findings based on their [severity levels](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels). Each segment of the circle represents the number of posture issues classified as `Critical`, `High`, `Medium`, or `Low`.

To review findings in detail, log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and go to **Zero Trust** > **Cloud & SaaS findings** > **Posture Findings**.

### DLP matches in HTTP requests over time

The DLP matches in HTTP requests over time chart displays when [DLP policies](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/) were triggered by users over a specified period of time.

Unlike the SaaS and Cloud findings by count chart, which shows CASB findings from data at rest (files already stored in your connected SaaS applications), the DLP matches in HTTP requests over time chart shows DLP detections in HTTP traffic — data actively moving through your network.

To review DLP detections in detail, log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and go to **Zero Trust** > **Insights** > **Logs** > **HTTP request logs**. Use the **DLP profiles** or **DLP match data** filters to view HTTP requests that triggered a DLP policy.

[PreviousApplication Access Report](https://developers.cloudflare.com/cloudflare-one/insights/analytics/application-access/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/analytics/data-analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

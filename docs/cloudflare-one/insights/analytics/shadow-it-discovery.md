---
url: https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/
title: Shadow IT SaaS analytics \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:48.131818+00:00
---

# Shadow IT SaaS analytics · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)

  4. /[Dashboards](https://developers.cloudflare.com/cloudflare-one/insights/analytics/)
  5. /Shadow IT SaaS analytics



# Shadow IT SaaS analytics

Last updated Sep 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/analytics/shadow-it-discovery/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesUse Shadow IT SaaS analytics 1\. Review applications 2\. Monitor usage 3\. Create policiesAvailable insights Understanding user counts

Shadow IT SaaS analytics provides visibility into the SaaS applications your users are visiting. The dashboard aggregates data from Gateway HTTP traffic to track application usage across your organization. This information allows you to create identity and device-driven Cloudflare One policies to secure your users and data.

To access Shadow IT SaaS analytics:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights**.
  2. Go to **Dashboards**.
  3. Select **Shadow IT: SaaS analytics**.



Refer to [Insights overview](https://developers.cloudflare.com/cloudflare-one/insights/) to learn how to use Analytics dashboards together with [Analytics Overview](https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/) and [Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) for complete visibility and troubleshooting.

## Prerequisites

To allow Cloudflare to discover shadow IT in your traffic, you must set up [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/).

## Use Shadow IT SaaS analytics

### 1\. Review applications

The first step in using the Shadow IT SaaS analytics dashboard is to review applications in the [Application Library](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/). The App Library synchronizes application review statuses with approval statuses from the Shadow IT Discovery SaaS analytics dashboard.

To organize applications into their approval status for your organization, you can mark them as **Unreviewed** (default), **In review** , **Approved** , and **Unapproved**.

Status | API value | Description  
---|---|---  
Approved | `approved` | Applications that have been marked as sanctioned by your organization.  
Unapproved | `unapproved` | Applications that have been marked as unsanctioned by your organization.  
In review | `in review` | Applications in the process of being reviewed by your organization.  
Unreviewed | `unreviewed` | Unknown applications that are neither sanctioned nor being reviewed by your organization at this time.  
  
To set the status of an application:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Team & Resources** > **Applications**.
  2. Locate the card for the application.
  3. In the three-dot menu, select the option to mark your desired status.



Once you mark the status of an application, its badge will change. You can filter applications by their status to review each application in the list for your organization. The review status for an application in the App Library and Shadow IT Discovery will update within one hour.

Note

Approval status does not impact a user's ability to access an application. Users are allowed or blocked according to your [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) and [Gateway policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/). To filter traffic based on approval status, use the [_Application Status_](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#application-approval-status) selector.

### 2\. Monitor usage

Review the Shadow IT SaaS analytics dashboard for application usage. Filter the view based on:

Field | Description  
---|---  
Application | SaaS application's name and logo.  
Application type | [Application type](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/#app-types) assigned by Cloudflare One.  
Application status | Application's approval status.  
Hostname | Hostname of the requested SaaS application.  
Country | Country code associated with the user's source IP address.  
  
To manage application statuses in bulk, select **Set Application Statuses** to review applications your users commonly visit and update their approval statuses.

### 3\. Create policies

After marking applications, you can create [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) based on application review status. For example, you can create policies that:

  * Launch all **Unreviewed** and **In review** applications in an [isolated browser](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/common-policies/#1-isolate-unreviewed-or-in-review-applications).
  * [Block access](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/common-policies/#2-block-unapproved-applications) to all **Unapproved** applications.
  * Limit file upload capabilities for specific application statuses.



To create an HTTP status policy directly from Shadow IT Discovery:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights**.
  2. Select **Dashboards** > **Shadow IT: SaaS analytics**.
  3. Select **Set application statuses**.
  4. Select **Manage HTTP status policies** , then choose an application status and select **Create policy**.



## Available insights

The Shadow IT SaaS analytics dashboard includes several insights to help you monitor and manage SaaS application usage.

  * **Number of applications by status** : A breakdown of how many applications have been categorized into each approval status. The list of applications is available in the [App Library](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/).
  * **Data uploaded per application status** : A time-series graph showing the amount of data uploaded to applications in the given status.
  * **Data downloaded per application status** : A time-series graph showing the amount of data downloaded from applications in the given status.
  * **User count per application status** : A time-series graph showing the number of unique users who have interacted with at least one application in a given status. A single user can appear in multiple status categories if they access applications with different statuses. For example, a user who accesses both an **Approved** application and an **Unapproved** application will be counted in both status categories.
  * **Top-N metrics** : A collection of metrics providing insights into top applications, users, devices, and countries.



### Understanding user counts

The user count chart displays unique users in two ways:

  * **Time-series bars** : Show unique users per time interval (for example, per hour or per day). The same user can appear in multiple time intervals if they were active during those periods.
  * **Legend totals** : Show unique users across the entire selected time range, deduplicated. Each user is counted only once per status, regardless of how many time intervals they appeared in.



For example, if User A accesses an Approved application every hour for three hours, they will appear in each hourly bar but will only be counted once in the legend total.

[PreviousGateway analytics (DNS, HTTP, network sessions)](https://developers.cloudflare.com/cloudflare-one/insights/analytics/gateway/)[NextAI prompt logs ↗︎](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/analytics/shadow-it-discovery.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/
title: Analytics overview \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:46.740437+00:00
---

# Analytics overview · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)
  4. /Analytics overview



# Analytics overview

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGlobal statusAccessGateway Proxy traffic Gateway (network requests) DNS traffic Gateway insights CASB metrics

The Cloudflare One Analytics overview provides a dashboard that reports on how Cloudflare One is protecting your organization and networks. Use this page to monitor usage and potential security concerns within your organization.

To view the Analytics overview, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com) and go to **Overview**.

The Analytics overview includes reports and insights across the following products and categories:

  * Global status of your Zero Trust Organization
  * Access
  * Gateway 
    * HTTP traffic
    * Network traffic
    * DNS traffic
    * Firewall policies



Refer to [Insights overview](https://developers.cloudflare.com/cloudflare-one/insights/) to learn how to use Analytics dashboards together with [Analytics Overview](https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/) and [Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) for complete visibility and troubleshooting.

## Global status

In **Global status** , you can view a report on your organization's Cloudflare One adoption that contains the following metrics:

  * Access apps configured
  * Gateway HTTP policies
  * Gateway network policies
  * Gateway DNS policies
  * SaaS integrations
  * Data Loss Prevention (DLP) profiles



You can also view a report on your [seat usage](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/) across your Zero Trust Organization that contains the following metrics. A seat is a billable unit consumed when a user authenticates to your Zero Trust organization.

  * Total seats
  * Used seats
  * Unused seats



## Access

In **Access** , you can view a report on your [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) configuration that contains:

**Metrics:**

  * Total access attempts
  * Granted access
  * Denied (policy violation)
  * Active logins over time
  * Top applications with most logins



**Filters:**

  * Access data by country



## Gateway

### Proxy traffic

In **Proxy traffic** , you can view a report on your [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) HTTP traffic that contains:

**Metrics:**

  * Total requests over time
  * Allowed requests
  * Blocked requests
  * Isolated requests (served through [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/))
  * Do not inspect requests
  * Top bandwidth consumers (GB)
  * Top denied users



**Filters:**

  * Gateway HTTP traffic data by country



### Gateway (network requests)

In **Gateway (network requests)** , you can view a report on your Gateway network traffic that contains:

**Metrics:**

  * Total sessions
  * Authenticated sessions
  * Blocked sessions
  * Allowed sessions
  * Override sessions
  * Top bandwidth consumers in GB
  * Top denied users



**Filters:**

  * Gateway network traffic data by country



### DNS traffic

In **DNS traffic** , you can view a report on your Gateway DNS traffic that contains:

**Metrics:**

  * Total DNS queries
  * Allowed DNS queries
  * Blocked DNS queries
  * Override DNS queries
  * Safe Search DNS queries
  * Restricted DNS queries
  * Other DNS queries



**Filters:**

  * Gateway DNS traffic by query type
  * Gateway DNS traffic by country



### Gateway insights

In **Gateway insights** , you can view a report on your Gateway firewall policies that contains the following metrics:

  * Top domain blocking policies
  * Most user queries
  * Top devices
  * Top countries



### CASB metrics

In **CASB** , you can review instances of security issues — such as misconfigurations, unauthorized user activity, and shadow IT — found in your SaaS integrations by [Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/).

  * Integrations by number of findings
  * [DLP](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) findings by profile name



[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/insights/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/insights/analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/analytics-overview.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

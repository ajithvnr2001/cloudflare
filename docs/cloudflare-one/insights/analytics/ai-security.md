---
url: https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/
title: AI security \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:47.136523+00:00
---

# AI security · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)

  4. /[Dashboards](https://developers.cloudflare.com/cloudflare-one/insights/analytics/)
  5. /AI security



# AI security

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/analytics/ai-security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesAvailable insights Top 5 visited AI applications by user count Statuses applied to AI applications by application count Data uploaded to Artificial Intelligence applications by status MCP servers behind Access over time Access login events to MCP servers

The AI security report dashboard summarizes your organization's AI usage and potential security risks.

To view the AI security report dashboard:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights**.
  2. Go to **Dashboards**.
  3. Select **AI security report**.



Refer to [Insights overview](https://developers.cloudflare.com/cloudflare-one/insights/) to learn how to use Analytics dashboards together with [Analytics Overview](https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/) and [Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) for complete visibility and troubleshooting.

## Prerequisites

To populate the AI security report dashboard, you must have:

  * [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) enabled to inspect outbound HTTP and DNS traffic.
  * User traffic to SaaS AI applications (for example, ChatGPT or Gemini) sent through Cloudflare Gateway.
  * [Model Context Protocol (MCP) servers](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/) behind [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) policies.



## Available insights

The AI security report dashboard includes the following panels and metrics:

  * Top 5 visited AI applications by user count
  * Statuses applied to AI applications by application count
  * Data uploaded to Artificial Intelligence applications by status
  * MCP servers behind Access over time
  * Access login events to MCP servers



### Top 5 visited AI applications by user count

Displays the most accessed AI tools in your organization and the number of users visiting each application in a time-series graph.  
Each bar represents user activity for a specific AI application (for example, ChatGPT or Gemini) over time.

Use this chart to monitor adoption trends and detect new or unauthorized AI tools being accessed.

### Statuses applied to AI applications by application count

Reports the total number of AI applications identified and their review statuses.  
Statuses include:

  * Unreviewed — Applications not yet evaluated by administrators.
  * In Review — Applications currently under review for approval.
  * Unapproved — Applications that are restricted or blocked.
  * Approved — Applications explicitly permitted for organizational use.



### Data uploaded to Artificial Intelligence applications by status

Reports the amount of data transferred to AI tools, broken down by review status (Unreviewed, In Review, Unapproved, Approved).  
Use this report to understand whether sensitive data is being sent to unapproved or unreviewed AI applications.

### MCP servers behind Access over time

Displays the number of Model Context Protocol (MCP) servers protected by [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) policies over time. Use this panel to verify that newly deployed MCP servers are protected.

### Access login events to MCP servers

Reports the number of login events to MCP servers protected by Access policies. Use this panel to identify unusual login patterns, such as spikes in access from unexpected users.

[PreviousPassive Detection ↗︎](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/)[NextApplication Access Report](https://developers.cloudflare.com/cloudflare-one/insights/analytics/application-access/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/analytics/ai-security.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

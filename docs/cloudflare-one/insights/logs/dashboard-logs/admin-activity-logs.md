---
url: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/
title: Admin activity logs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:51.069810+00:00
---

# Admin activity logs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)

  4. /[Dashboard logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)
  5. /Admin activity logs



# Admin activity logs

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExplanation of the fieldsExport admin activity logs

Admin activity logs record configuration changes made by members of your Cloudflare account. These logs are useful for auditing who changed a policy or setting and investigating unexpected configuration changes. Use these logs to monitor when a member creates, updates, or deletes configurations in your [Zero Trust organization](https://developers.cloudflare.com/cloudflare-one/setup/#create-a-zero-trust-organization).

To view admin activity logs, log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and go to **Zero Trust** > **Insights** > **Logs** > **Admin activity logs**.

## Explanation of the fields

Field | Description | Example Value  
---|---|---  
Email | User who performed the action | [josephli@cloudflare.com](mailto:josephli@cloudflare.com)  
Product | Cloudflare product being modified | Tunnel  
Resource | Specific resource type within the product | Route  
Event | Action performed (Create, Update, Delete) | Create  
Date | Timestamp of when the action occurred | April 30, 2026 • 12:19 AM  
User IP Address | IP address of the user who made the change | 2a09:bac6:6447:523::83:30  
Interface | How the change was initiated | API  
Audit record | Unique identifier for the audit log entry | caf1a547-17cc-484a-b4ce-5d3b32771a8f  
Old value | Previous configuration state (empty for creates) |   
New value | New configuration state after the change | JSON object with fields like comment, network, tun_type, tunnel_id, virtual_network_id  
  
## Export admin activity logs

Enterprise users can export admin activity logs to a third-party storage destination or SIEM using [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/). For a list of all available fields, refer to [Audit Logs V2](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/).

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)[NextAccess authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/logs/dashboard-logs/admin-activity-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

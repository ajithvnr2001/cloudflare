---
url: https://developers.cloudflare.com/changelog/product/log-explorer/
title: Log Explorer Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:06.621448+00:00
---

# Log Explorer Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/log-explorer/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 7, 2026

## [Query Log Explorer datasets from Observability Logs](https://developers.cloudflare.com/changelog/post/2026-10-07-log-search-in-observability-logs/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer datasets are now queried from the [Logs](https://developers.cloudflare.com/observability/logs/) page under **Observability** in the Cloudflare dashboard. The Logs page brings Log Explorer and Workers Observability datasets together with a shared filter builder, SQL editor, and visualizations.

As part of this change, the **Log Explorer** menu is no longer shown in the dashboard navigation.

  * Your enabled datasets, saved queries, and SQL queries continue to work on the Logs page.
  * To manage datasets, open the dataset selector on the Logs page and select **Configure** next to the Log Explorer datasets.
  * The previous Log Search page remains available at its direct URL.



For more information, refer to [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) and the [Logs overview](https://developers.cloudflare.com/observability/logs/).

Aug 28, 2026

## [Improved dataset configuration in Log Explorer](https://developers.cloudflare.com/changelog/post/2026-08-28-dataset-configuration/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer has a refreshed dataset configuration experience in the Cloudflare dashboard. The new controls make it easier to choose which fields and events Log Explorer ingests.

  * **Grouped field selection** organizes fields by category and shows the number selected in each group.
  * **Field details** identify each field's data type and mark required or deprecated fields.
  * **Bulk controls** let you select all fields or reset the selection to the dataset defaults.
  * **Ingestion filters** let you ingest all events or only events that match your conditions.



These controls are available when you add a dataset or select **Actions** > **Edit** for an enabled dataset.

For more information, refer to [Configure fields and filters](https://developers.cloudflare.com/log-explorer/manage-datasets/#configure-fields-and-filters).

Aug 26, 2026

## [Delete Log Explorer datasets](https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.

Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to [Manage datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/), disable deletion protection for the dataset, select **Delete** , and enter the dataset name to confirm.

To delete a dataset through the API, first set `deletion_protection` to `false` with the [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/) method. Then use the [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/) method.

Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.

Aug 20, 2026

## [Per-zone post-quantum visibility in Logpush and Log Explorer](https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/)

[Logs](https://developers.cloudflare.com/logs/)[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Cloudflare Radar ↗︎](https://radar.cloudflare.com/post-quantum) publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the [`http_requests`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) Logpush dataset — also queryable in [Log Explorer](https://developers.cloudflare.com/log-explorer/) — includes a new `ClientTLSKeyExchangeGroup` field.

The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as `X25519MLKEM768`, and classical connections appear as `X25519`, `P-256`, or another named group. A value of `UNK` means the group could not be determined, and `NONE` means either RSA key exchange was used or TLS was not used.

With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/).

Apr 22, 2026

## [Custom dashboards available to all customers](https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/)

[Analytics](https://developers.cloudflare.com/analytics/)[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.

This update significantly expands the data available for visualization. Build charts based on any of the **100+ datasets** available via the Cloudflare GraphQL API, covering everything from WAF events and Workers metrics to Load Balancing and Zero Trust logs.

#### Log Explorer integration

Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.

#### Key benefits

  * **Unified visibility** : Consolidate signals from different Cloudflare products (for example, HTTP Traffic and R2 Storage) into a single view.
  * **Flexible monitoring** : Create charts that focus on specific status codes, ASN regions, or security actions that matter to your business.
  * **Expanded limits** : Log Explorer customers can create up to **100 dashboards** (up from 25 for standard customers).

![Custom Dashboards home page showing dashboard list and chart previews](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1079,height=793,format=webp/_astro/customdashboardshome.BIpSvImM.jpg)

To get started, refer to the [Custom Dashboards documentation](https://developers.cloudflare.com/analytics/custom-dashboards/).

Mar 11, 2026

## [Ingest field selection for Log Explorer](https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.

Previously, ingesting logs often meant taking an "all or nothing" approach to data fields. With **Ingest Field Selection** , you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.

#### Key capabilities

  * **Granular control:** Select only the specific fields you need when enabling a new dataset.
  * **Dynamic updates:** Update fields for existing, already enabled logstreams at any time.
  * **Historical consistency:** Even if you disable a field later, you can still query and receive results for that field for the period it was captured.
  * **Data integrity:** Core fields, such as `Timestamp`, are automatically retained to ensure your logs remain searchable and chronologically accurate.



#### Example configuration

When configuring a dataset via the dashboard or API, you can define a specific set of fields. The `Timestamp` field remains mandatory to ensure data indexability.
    
    
    {
      "dataset": "firewall_events",
      "enabled": true,
      "fields": [
        "Timestamp",
        "ClientRequestHost",
        "ClientIP",
        "Action",
        "EdgeResponseStatus",
        "OriginResponseStatus"
      ]
    }

For more information, refer to the [Log Explorer documentation](https://developers.cloudflare.com/log-explorer/).

Feb 9, 2026

## [Tabs and pivots](https://developers.cloudflare.com/changelog/post/2026-02-09-tabs-and-pivots/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer now supports multiple concurrent queries with the new Tabs feature. Work with multiple queries simultaneously and pivot between datasets to investigate malicious activity more effectively.

#### Key capabilities

  * **Multiple tabs:** Open and switch between multiple query tabs to compare results across different datasets.
  * **Quick filtering:** Select the filter button from query results to add a value as a filter to your current query.
  * **Pivot to new tab:** Use Cmd + click on the filter button to start a new query tab with that filter applied.
  * **Preserved progress:** Your query progress is preserved on each tab if you navigate away and return.



For more information, refer to the [Log Explorer documentation](https://developers.cloudflare.com/log-explorer/).

Nov 13, 2025

## [Fixed custom SQL date picker inconsistencies](https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

We've resolved a bug in Log Explorer that caused inconsistencies between the custom SQL date field filters and the date picker dropdown. Previously, users attempting to filter logs based on a custom date field via a SQL query sometimes encountered unexpected results or mismatching dates when using the interactive date picker.

This fix ensures that the custom SQL date field filters now align correctly with the selection made in the date picker dropdown, providing a reliable and predictable filtering experience for your log data. This is particularly important for users creating custom log views based on time-sensitive fields.

Nov 13, 2025

## [Log Explorer adds 14 new datasets](https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

We've significantly enhanced Log Explorer by adding support for 14 additional Cloudflare product datasets.

This expansion enables Operations and Security Engineers to gain deeper visibility and telemetry across a wider range of Cloudflare services. By integrating these new datasets, users can now access full context to efficiently investigate security incidents, troubleshoot application performance issues, and correlate logged events across different layers (like application and network) within a single interface. This capability is crucial for a complete and cohesive understanding of event flows across your Cloudflare environment.

The newly supported datasets include:

#### Zone Level

  * `Dns_logs`
  * `Nel_reports`
  * `Page_shield_events`
  * `Spectrum_events`
  * `Zaraz_events`



#### Account Level

  * `Audit Logs`
  * `Audit_logs_v2`
  * `Biso_user_actions`
  * `DNS firewall logs`
  * `Email_security_alerts`
  * `Magic Firewall IDS`
  * `Network Analytics`
  * `Sinkhole HTTP`
  * `ipsec_logs`



Note

`Auditlog` and `Auditlog_v2` datasets require `audit-log.read` permission for querying.

The `biso_user_actions` dataset requires either the `Super Admin` or `ZT PII` role for querying.

#### Example: Correlating logs

You can now use Log Explorer to query and filter with each of these datasets. For example, you can identify an IP address exhibiting suspicious behavior in the `FW_event` logs, and then instantly pivot to the `Network Analytics` logs or `Access` logs to see its network-level traffic profile or if it bypassed a corporate policy.

To learn more and get started, refer to the [Log Explorer documentation](https://developers.cloudflare.com/log-explorer/) and the [Cloudflare Logs documentation](https://developers.cloudflare.com/logs/).

Nov 11, 2025

## [Resize your custom SQL window in Log Explorer](https://developers.cloudflare.com/changelog/post/2025-11-11-resize-sql-window/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

We're excited to announce a quality-of-life improvement for Log Explorer users. You can now resize the custom SQL query window to accommodate longer and more complex queries.

Previously, if you were writing a long custom SQL query, the fixed-size window required excessive scrolling to view the full query. This update allows you to easily drag the bottom edge of the query window to make it taller. This means you can view your entire custom query at once, improving the efficiency and experience of writing and debugging complex queries.

To learn more and get started, refer to the [Log Explorer documentation](https://developers.cloudflare.com/log-explorer/).

Nov 4, 2025

## [Log Explorer now supports query cancellation](https://developers.cloudflare.com/changelog/post/2025-11-04-query-cancellation/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

We're excited to announce that Log Explorer users can now cancel queries that are currently running.

This new feature addresses a common pain point: waiting for a long, unintended, or misconfigured query to complete before you can submit a new, correct one. With query cancellation, you can immediately stop the execution of any undesirable query, allowing you to quickly craft and submit a new query, significantly improving your investigative workflow and productivity within Log Explorer.

Nov 4, 2025

## [Log Explorer now shows query result distribution](https://developers.cloudflare.com/changelog/post/2025-11-13-query-result-distribution/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

We're excited to announce a new feature in Log Explorer that significantly enhances how you analyze query results: the Query results distribution chart.

This new chart provides a graphical distribution of your results over the time window of the query. Immediately after running a query, you will see the distribution chart above your result table. This visualization allows Log Explorer users to quickly spot trends, identify anomalies, and understand the temporal concentration of log events that match their criteria. For example, you can visually confirm if a spike in traffic or errors occurred at a specific time, allowing you to focus your investigation efforts more effectively. This feature makes it faster and easier to extract meaningful insights from your vast log data.

The chart will dynamically update to reflect the logs matching your current query.

Sep 11, 2025

## [Contextual pivots](https://developers.cloudflare.com/changelog/post/2025-09-11-contextual-pivots/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Directly from [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) results, customers can pivot to other parts of the Cloudflare dashboard to immediately take action as a result of their investigation.

From the `http_requests` or `fw_events` dataset results, right click on an IP Address or JA3 Fingerprint to pivot to the Investigate portal to lookup the reputation of an IP address or JA3 fingerprint.

![Investigate IP address](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1038,height=486,format=webp/_astro/investigate-ip-address.BMVSMzDi.png)

Easily learn about error codes by linking directly to our documentation from the **EdgeResponseStatus** or **OriginResponseStatus** fields.

![View documentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1186,height=476,format=webp/_astro/view-documentation.Cem5QgeO.png)

From the `gateway_http` dataset, click on a **policyid** to link directly to the Zero Trust dashboard to review or make changes to a specific Gateway policy.

![View policy](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1274,height=498,format=webp/_astro/policyid.CVjEdahj.png)

Sep 11, 2025

## [New results table view](https://developers.cloudflare.com/changelog/post/2025-09-11-new-results-table-view/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

The results table view of **Log Search** has been updated with additional functionality and a more streamlined user experience. Users can now easily:

  * Remove/add columns.
  * Resize columns.
  * Sort columns.
  * Copy values from any field.

![New results table view](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1786,height=342,format=webp/_astro/new-table.C2Q8mWJ9.png)

Sep 3, 2025

## [Logging headers and cookies using custom fields](https://developers.cloudflare.com/changelog/post/2025-09-03-log-headers-and-cookies/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) now supports logging and filtering on header or cookie fields in the [`http_requests` dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/).

Create a custom field to log desired header or cookie values into the `http_requests` dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.

![Edit Custom fields](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1790,height=404,format=webp/_astro/edit-custom-fields.Cy4qXSpL.png)

For more details, refer to [Headers and cookies](https://developers.cloudflare.com/log-explorer/log-search/#headers-and-cookies).

Aug 15, 2025

## [Extended retention](https://developers.cloudflare.com/changelog/post/2025-08-15-extended-retention/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Customers can now rely on Log Explorer to meet their log retention compliance requirements.

Contract customers can choose to store their logs in Log Explorer for up to two years, at an additional cost of $0.10 per GB per month. Customers interested in this feature can contact their account team to have it added to their contract.

Jul 9, 2025

## [Usage tracking](https://developers.cloudflare.com/changelog/post/2025-07-09-usage-tracking/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) customers can now monitor their data ingestion volume to keep track of their billing. Monthly usage is displayed at the top of the [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) and [Manage Datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/) screens in Log Explorer.

![Ingested data](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=418,height=157,format=webp/_astro/ingested-data.D2flqRIu.png)

Jun 18, 2025

## [Log Explorer is GA](https://developers.cloudflare.com/changelog/post/2025-06-18-log-explorer-ga/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/) is now GA, providing native observability and forensics for traffic flowing through Cloudflare.

Search and analyze your logs, natively in the Cloudflare dashboard. These logs are also stored in Cloudflare's network, eliminating many of the costs associated with other log providers.

![Log Explorer dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=512,height=208,format=webp/_astro/log-explorer-dash.CJSVLZ7Y.png)

With Log Explorer, you can now:

  * **Monitor security and performance issues with custom dashboards** – use natural language to define charts for measuring response time, error rates, top statistics and more.
  * **Investigate and troubleshoot issues with Log Search** – use data type-aware search filters or custom sql to investigate detailed logs.
  * **Save time and collaborate with saved queries** – save Log Search queries for repeated use or sharing with other users in your account.
  * **Access Log Explorer at the account and zone level** – easily find Log Explorer at the account and zone level for querying any dataset.



For help getting started, refer to [our documentation](https://developers.cloudflare.com/log-explorer/).

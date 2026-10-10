---
url: https://developers.cloudflare.com/observability/logs/datasets/
title: Datasets \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:26.091081+00:00
---

# Datasets · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/logs/datasets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /[Logs](https://developers.cloudflare.com/observability/logs/)
  4. /Datasets



# Datasets

Last updated Oct 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported datasetsSampled analytics datasetsPricing Included in the new Observability pricing

Cloudflare Observability supports logs from the products listed in the table. Turn on each dataset in the location shown under **Enablement**. Datasets enabled through [Log Explorer](https://developers.cloudflare.com/log-explorer/) appear in Logs once your account has Log Explorer and that dataset turned on. Event sizes are estimates and vary by record.

You can also query sampled analytics datasets for your zones in Logs without turning anything on.

## Supported datasets

Dataset | Identifier | Enablement | Average event size | Default retention  
---|---|---|---|---  
[Workers](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) | `workers` | [On Worker](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#enable-workers-logs) | 4.84 KB | 7 days  
[Containers](https://developers.cloudflare.com/containers/faq/#how-do-container-logs-work) | `containers` | [On Worker](https://developers.cloudflare.com/containers/faq/#how-do-container-logs-work) | 1.88 KB | 7 days  
[R2 Data Access Logs](https://developers.cloudflare.com/r2/buckets/data-access-logs/) | `r2` | [On Bucket](https://developers.cloudflare.com/r2/buckets/data-access-logs/#turn-on-data-access-logs) | 1.55 KB | 7 days  
[AI Gateway](https://developers.cloudflare.com/ai-gateway/observability/logging/) | `ai-gateway` | [On Gateway](https://developers.cloudflare.com/ai-gateway/observability/logging/) | 2 KB | 7 days  
[Issues](https://developers.cloudflare.com/workers/observability/issues/) | `real-time-issues` | [On Worker](https://developers.cloudflare.com/workers/observability/issues/) | 2.64 KB | 7 days  
[HTTP Requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) | `http_requests` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.56 KB | 30 days  
[Firewall Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/) | `firewall_events` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.36 KB | 30 days  
[Access Requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/) | `access_requests` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 446 B | 30 days  
[Audit Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/) | `audit_logs` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 2.69 KB | 30 days  
[Audit Logs v2](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/) | `audit_logs_v2` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.73 KB | 30 days  
[Browser Isolation User Actions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/) | `biso_user_actions` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | Not published | 30 days  
[CASB Findings](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/) | `casb_findings` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 2.67 KB | 30 days  
[DEX Application Tests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/) | `dex_application_tests` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 3.29 KB | 30 days  
[DEX Device State Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_device_state_events/) | `dex_device_state_events` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.98 KB | 30 days  
[Device Posture Results](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/device_posture_results/) | `device_posture_results` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 730 B | 30 days  
[DNS Firewall Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dns_firewall_logs/) | `dns_firewall_logs` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 387 B | 30 days  
[DNS Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/dns_logs/) | `dns_logs` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 199 B | 30 days  
[Email Security Alerts](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/email_security_alerts/) | `email_security_alerts` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 6.74 KB | 30 days  
[Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/) | `gateway_dns` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.44 KB | 30 days  
[Gateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/) | `gateway_http` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.47 KB | 30 days  
[Gateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/) | `gateway_network` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 877 B | 30 days  
[IPsec Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/) | `ipsec_logs` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 207 B | 30 days  
[Magic BGP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/) | `magic_bgp_logs` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | Not published | 30 days  
[Magic IDS Detections](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/) | `magic_ids_detections` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 334 B | 30 days  
[NEL Reports](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/) | `nel_reports` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 204 B | 30 days  
[Network Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/network_analytics_logs/) | `network_analytics_logs` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.31 KB | 30 days  
[Page Shield Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/) | `page_shield_events` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 443 B | 30 days  
[Sinkhole HTTP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/) | `sinkhole_http_logs` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 705 B | 30 days  
[Spectrum Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/spectrum_events/) | `spectrum_events` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 685 B | 30 days  
[WARP Toggle Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/) | `warp_toggle_changes` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 327 B | 30 days  
[Zaraz Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/zaraz_events/) | `zaraz_events` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 7.30 KB | 30 days  
[Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) | `zero_trust_network_sessions` | [On Account](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer) | 1.21 KB | 30 days  
  
## Sampled analytics datasets

Logs also lists HTTP requests and firewall events from the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). These datasets need no enablement and have no additional charge. The following sampled analytics datasets are available:

Dataset | GraphQL dataset | Availability | Retention  
---|---|---|---  
HTTP requests | `httpRequestsAdaptive` | All plans | At least 31 days  
Firewall events | `firewallEventsAdaptive` | Pro, Business, and Enterprise | At least 31 days  
  
These datasets use [adaptive sampling](https://developers.cloudflare.com/analytics/graphql-api/sampling/). Results can omit individual events, and counts can be estimates. Available fields, exact retention, and how far back charts reach depend on your plan. Refer to [GraphQL Analytics API limits](https://developers.cloudflare.com/analytics/graphql-api/limits/) for details.

To query these datasets for a zone, you need the Zone Analytics Read permission for that zone. Account administrators can grant it on the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)

For unsampled HTTP requests and firewall events, turn on those datasets through [Log Explorer](https://developers.cloudflare.com/log-explorer/manage-datasets/#enable-log-explorer). Log Explorer is a paid add-on. Refer to Pricing for the unsampled security dataset price.

## Pricing

Beginning December 1, 2026, all Cloudflare logs and traces will use the same pricing model. Unsampled security datasets have a different price point of $1 per GB ingested and include 30-day retention. Queries, dashboards, alerts, and analytics do not incur additional charge.

### Included in the new Observability pricing

The following logs and traces share account-level ingestion and storage allowances:

  * [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/)
  * [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)
  * [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/)
  * [Containers logs](https://developers.cloudflare.com/containers/faq/#how-do-container-logs-work)
  * [R2 Data Access Logs](https://developers.cloudflare.com/r2/buckets/data-access-logs/)
  * [AI Gateway logs](https://developers.cloudflare.com/ai-gateway/observability/logging/)
  * [Issues](https://developers.cloudflare.com/workers/observability/issues/)



[PreviousOverview](https://developers.cloudflare.com/observability/logs/)[NextOverview](https://developers.cloudflare.com/observability/traces/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/logs/datasets.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/log-explorer/manage-datasets/
title: Manage datasets \u00b7 Cloudflare Log Explorer docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:08.770271+00:00
---

# Manage datasets · Cloudflare Log Explorer docs

> Source: https://developers.cloudflare.com/log-explorer/manage-datasets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Log Explorer](https://developers.cloudflare.com/log-explorer/)
  3. /Manage datasets



# Manage datasets

Last updated Oct 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/log-explorer/manage-datasets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported datasets Zone level Account levelEnable Log Explorer Dashboard APIDelete a dataset

Log Explorer allows you to enable, disable, or delete datasets available to query in Log Search.

Note

Canceling a Log Explorer subscription stops renewal, but it does not automatically stop log ingestion during the current billing cycle. To completely turn off Log Explorer, refer to [How do I turn off Log Explorer?](https://developers.cloudflare.com/log-explorer/faq/#how-do-i-turn-off-log-explorer).

## Supported datasets

Log Explorer currently supports the following datasets:

### Zone level

  * [HTTP Requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) (`http_requests`)
  * [Firewall Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/) (`firewall_events`)
  * [DNS Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/dns_logs/) (`dns_logs`)
  * [NEL Reports](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/nel_reports/) (`nel_reports`)
  * [Page Shield Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/page_shield_events/) (`page_shield_events`) (events for client-side security)
  * [Spectrum Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/spectrum_events/) (`spectrum_events`)
  * [Zaraz Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/zaraz_events/) (`zaraz_events`)



### Account level

  * [Access requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/access_requests/) (`access_requests`)
  * [CASB findings](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/) (`casb_findings`)
  * [Device posture results](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/device_posture_results/) (`device_posture_results`)
  * [Gateway DNS](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_dns/) (`gateway_dns`)
  * [Gateway HTTP](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_http/) (`gateway_http`)
  * [Gateway Network](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/gateway_network/) (`gateway_network`)
  * [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) (`zero_trust_network_sessions`)
  * [Audit Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs/) (`audit_logs`)
  * [Audit_logs_v2](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/audit_logs_v2/) (`audit_logs_v2`)
  * [Browser Isolation User Actions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/) (`biso_user_actions`)
  * [DNS firewall logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dns_firewall_logs/) (`dns_firewall_logs`)
  * [Email security alerts](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/email_security_alerts/) (`email_security_alerts`)
  * [Magic BGP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/) (`magic_bgp_logs`)
  * [Magic IDS Detections](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/) (`magic_ids_detections`)
  * [Network Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/network_analytics_logs/) (`network_analytics_logs`)
  * [Sinkhole HTTP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/) (`sinkhole_http_logs`)
  * [IP Sec Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/) (`ipsec_logs`)



## Enable Log Explorer

To begin storing logs, enable the desired datasets through the dashboard or API.

### Dashboard

  1. In the Cloudflare dashboard, open the **Manage datasets** page. From **Observability** > **Logs** , open the dataset selector and select **Configure** next to the Log Explorer datasets, or use the button below.

[ Go to **Manage datasets** ↗ ](https://dash.cloudflare.com/?to=/:account/log-explorer/manage-sources)
  2. Select **Add dataset**.

  3. Choose a dataset and, for zone-level datasets, a zone.

  4. Under **Select fields** , choose the fields that Log Explorer should ingest.

  5. Under **Filter logs** , choose whether to ingest all events or only events that match a filter.

  6. Select **Add**.




Note

It may take a few minutes for the logs to become available for querying.

#### Configure fields and filters

Use **Select fields** to control which data points Log Explorer stores. Fields are grouped by category, and each category shows its selected field count. Select a category to add or remove all fields in that group, or expand the category to select individual fields. Each field shows its data type.

Required fields remain selected and are marked **Required**. Fields that Cloudflare no longer recommends are marked **Deprecated**. Select **Select all** to include every available field, or **Reset to default** to restore the dataset defaults.

Use **Filter logs** to ingest **All events** or **Only events matching a filter**. A filter condition consists of a field, an operator, and a value. All conditions within a group must match. An event can match any filter group.

To change the fields or filter for an enabled dataset, open the **Manage datasets** page. Find the dataset, select **Actions** > **Edit** , update the configuration, and select **Update**.

### API

Use the Log Explorer API to enable each dataset you want to store. It may take a few minutes after a log stream is enabled before you can view the logs.

The following `curl` command is an example for enabling the zone-level dataset `http_requests`, as well as the expected response when the command succeeds.
    
    
    curl https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/explorer/datasets \
    --header "Authorization: Bearer <API_TOKEN>" \
    --json '{
      "dataset": "http_requests"
    }'
    
    
    {
    	"result": {
    		"dataset": "http_requests",
    		"object_type": "zone",
    		"object_id": "<ZONE ID>",
    		"created_at": "2025-06-03T14:33:16Z",
    		"updated_at": "2025-06-03T14:33:16Z",
    		"dataset_id": "01973635f7e273a1964a02f4d4502499",
    		"enabled": true,
    		"deletion_protection": true
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

To enable an account-level dataset, replace `zones/{zone_id}` with `accounts/{account_id}` in the `curl` command. For example:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/explorer/datasets \
    --header "Authorization: Bearer <API_TOKEN>" \
    --json '{
      "dataset": "access_requests"
    }'

## Delete a dataset

Deleting a dataset permanently removes the dataset and its stored data. Deletion runs asynchronously. You cannot recreate the same dataset for the account or zone while deletion is in progress.

Caution

Dataset deletion is irreversible. Deleted data cannot be recovered.

  1. In the Cloudflare dashboard, open the **Manage datasets** page.

[ Go to **Manage datasets** ↗ ](https://dash.cloudflare.com/?to=/:account/log-explorer/manage-sources)
  2. Find the dataset and select **Actions** > **Delete**.

  3. If deletion protection is enabled, disable it in the confirmation dialog.

  4. Enter the dataset name and select **Delete**.




  1. Set `deletion_protection` to `false` with the [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/) method.
  2. Delete the dataset with the [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/) method.



[PreviousExample SQL queries](https://developers.cloudflare.com/log-explorer/example-queries/)[NextLog Explorer API](https://developers.cloudflare.com/log-explorer/api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/log-explorer/manage-datasets.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

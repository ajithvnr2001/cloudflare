---
url: https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/
title: Log Explorer adds 14 new datasets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:29.647109+00:00
---

# Log Explorer adds 14 new datasets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 13, 2025

## Log Explorer adds 14 new datasets

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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

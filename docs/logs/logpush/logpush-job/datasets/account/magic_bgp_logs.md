---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/
title: Magic BGP Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.511019+00:00
---

# Magic BGP Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Magic BGP Logs



# Magic BGP Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDirectionEventDataEventKindEventTimestampTunnelIDTunnelName

The descriptions below detail the fields available for `magic_bgp_logs`.

## Direction

Type: `string`

Direction of the event relative to Cloudflare. Possible values are _to_cloudflare_ | _from_cloudflare_ , or empty for non-message events.

## EventData

Type: `object`

Payload describing the event. Schema depends on `EventKind`.  
_open_message_ carries `peer_asn`, `cloudflare_asn`, `bgp_id`, `hold_time`, and `capabilities`.  
_update_message_ carries `announced`, `as_path`, and `origin`.  
_notification_message_ carries `code`, `subcode`, and `reason`.  
_route_refresh_message_ carries `afi` and `safi`.  
_bgp_state_transition_ carries `from_state`, `to_state`, and `event`.  
_tcp_handshake_failed_ carries `reason`, `message`, `src`, and `dst`.  
_stale_path_timer_expired_ carries `purged_route_count`.  
_session_config_changed_ carries `disabled` and the changed fields.  
_filter_config_changed_ carries `import` and `export` filter change flags.  
_redistribute_config_changed_ carries a single boolean.

## EventKind

Type: `string`

BGP event type. Possible values are _open_message_ | _update_message_ | _notification_message_ | _route_refresh_message_ | _bgp_state_transition_ | _tcp_handshake_failed_ | _stale_path_timer_expired_ | _session_config_changed_ | _filter_config_changed_ | _redistribute_config_changed_.

## EventTimestamp

Type: `int or string`

Timestamp of when the event occurred.

## TunnelID

Type: `string`

UUID (hex, no hyphens) of the IPsec / GRE tunnel the event belongs to.

## TunnelName

Type: `string`

Name of the IPsec / GRE tunnel the event belongs to.

[PreviousIPSec Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/)[NextMagic IDS Detections](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/magic_bgp_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

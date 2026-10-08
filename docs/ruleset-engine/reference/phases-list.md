---
url: https://developers.cloudflare.com/ruleset-engine/reference/phases-list/
title: Phases list \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:02.111189+00:00
---

# Phases list · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/reference/phases-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /Reference
  4. /Phases list



# Phases list

Last updated Sep 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNetwork layerApplication layer Request phases Response phases

The following tables list the [phases](https://developers.cloudflare.com/ruleset-engine/about/phases/) of Cloudflare products powered by the Ruleset Engine, in the order those phases are executed. Some products such as the Cloudflare Web Application Firewall have more than one associated phase.

## Network layer

[Network-layer ↗︎](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) phases apply to packets received on the Cloudflare global network.

Phase name | Used in product/feature  
---|---  
`ddos_l4` | [Network-layer DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-api/)  
`magic_transit` | [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/add-policies/)  
`magic_transit_managed` | [Cloudflare Network Firewall managed rulesets](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/)  
`magic_transit_ratelimit` | [Cloudflare Network Firewall rate limiting policies](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/create-rate-limiting-policies/)  
`magic_transit_ids_managed` | [Cloudflare Network Firewall Intrusion Detection System (IDS)](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/)  
  
## Application layer

[Application-layer ↗︎](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) phases apply to requests received on the Cloudflare global network.

### Request phases

The phases execute in the order they appear in the table.

Phase name | Used in product/feature  
---|---  
`http_request_dynamic_redirect` | [Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/)  
`http_request_sanitize` | [URL normalization](https://developers.cloudflare.com/rules/normalization/)  
`http_request_transform` | [URL Rewrite Rules](https://developers.cloudflare.com/rules/transform/url-rewrite/)  
_N/A_ (internal phase) | [Waiting Room Rules](https://developers.cloudflare.com/waiting-room/additional-options/waiting-room-rules/)  
_N/A_ (internal detection phase)† | [API Shield](https://developers.cloudflare.com/api-shield/)  
`http_config_settings` | [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/)  
`http_request_origin` | [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/)  
`ddos_l7`* | [HTTP DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/)  
`http_request_firewall_custom` | [Custom rules (Web Application Firewall)](https://developers.cloudflare.com/waf/custom-rules/)  
`http_ratelimit` | [Rate limiting rules (WAF)](https://developers.cloudflare.com/waf/rate-limiting-rules/)  
_N/A_ (internal mitigation phase)‡ | [API Shield](https://developers.cloudflare.com/api-shield/)  
`http_request_firewall_managed` | [WAF Managed Rules](https://developers.cloudflare.com/waf/managed-rules/)  
`http_request_sbfm` | [Super Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/)  
_N/A_ (internal phase) | [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) application check  
`http_request_redirect` | [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)  
_N/A_ (internal phase) | [Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/)  
`http_request_late_transform` | [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/)  
`http_request_cache_settings` | [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)  
`http_request_snippets` | [Snippets](https://developers.cloudflare.com/rules/snippets/)  
`http_request_cloud_connector` | [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)  
  
* _This phase is for configuration purposes only — the corresponding rules will not be executed at this stage in the request handling process._

† _Detections run at this phase. Detection results are available to later phases._

‡ _Mitigation actions can run at this stage if configured._

For Cloudflare Access, the `Cloudflare Access` row refers to Access application checking. Access enforcement and handling run in later internal phases, after Bulk Redirects.

Change notice for Super Bot Fight Mode rulesets

Updating Super Bot Fight Mode rules via the Rulesets API is no longer supported and may cause unexpected behavior if you do so.

### Response phases

The phases execute in the order they appear in the table.

Phase name | Used in product/feature  
---|---  
`http_custom_errors` | [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/)  
_N/A_ (internal phase) | [Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/)  
`http_response_headers_transform` | [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/)  
`http_ratelimit` | [Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) (when they use response information)  
`http_response_compression` | [Compression Rules](https://developers.cloudflare.com/rules/compression-rules/)  
`http_response_firewall_managed` | [Cloudflare Sensitive Data Detection](https://developers.cloudflare.com/waf/managed-rules/) (Data Loss Prevention)  
`http_log_custom_fields` | [Logpush custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/)  
  
[PreviousValidate rule changes before deployment](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/reference/phases-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

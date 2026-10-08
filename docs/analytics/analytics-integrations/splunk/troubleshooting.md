---
url: https://developers.cloudflare.com/analytics/analytics-integrations/splunk/troubleshooting/
title: Troubleshooting \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:11.483336+00:00
---

# Troubleshooting · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-integrations/splunk/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Analytics integrations](https://developers.cloudflare.com/analytics/analytics-integrations/)

  4. /[Splunk](https://developers.cloudflare.com/analytics/analytics-integrations/splunk/)
  5. /Troubleshooting



# Troubleshooting

Last updated Sep 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-integrations/splunk/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFirewall Events carry incorrect _time valuesThe Cloudflare Security (WAF) dashboard is emptyStill not resolved

Use this guide to resolve common issues when analyzing [Cloudflare Logs ↗︎](https://www.cloudflare.com/products/cloudflare-logs/) through the [Cloudflare App for Splunk](https://developers.cloudflare.com/analytics/analytics-integrations/splunk/).

Support scope

Cloudflare Support can help you troubleshoot Cloudflare-side log delivery, including [Logpush](https://developers.cloudflare.com/logs/logpush/) job configuration. Configuring or troubleshooting your Splunk environment — including index administration, HTTP Event Collector (HEC) configuration, dashboards, or app deployment — is outside the scope of Cloudflare Support. Contact your Splunk representative or your integration partner for assistance with those components.

## Firewall Events carry incorrect `_time` values

Events under the `cloudflare:json` sourcetype for the Firewall Events dataset carry `_time` values that do not match the event's actual time, and `splunkd.log` shows entries similar to:
    
    
    WARN DateParserVerbose - Failed to parse timestamp.
    Defaulting to timestamp of previous event.

**Cause:** In older versions of the Cloudflare App for Splunk, the `cloudflare:json` sourcetype extracts `_time` from the `EdgeStartTimestamp` JSON key, which only exists in HTTP requests logs. Firewall Events use a different key (`Datetime`), so timestamp extraction fails and Splunk silently falls back to the timestamp of the most recently indexed event.

**Fix:** Upgrade to the latest version of the [Cloudflare App for Splunk ↗︎](https://splunkbase.splunk.com/app/4501/). The current release parses both `EdgeStartTimestamp` and `Datetime` under the `cloudflare:json` sourcetype.

If you cannot upgrade immediately, or if you maintain a customized `props.conf`, update the `cloudflare:json` stanza on your indexer or heavy forwarder to match both keys, then restart the Splunk service:
    
    
    [cloudflare:json]
    TRUNCATE = 100000
    TIME_PREFIX = "(?:EdgeStartTimestamp|Datetime)"\s*:\s*"
    TIME_FORMAT = %Y-%m-%dT%H:%M:%SZ
    MAX_TIMESTAMP_LOOKAHEAD = 150

**Verify:** Newly indexed Firewall Events carry accurate `_time` values, and `DateParserVerbose` warnings no longer appear in `splunkd.log`. Events indexed before the fix retain their original `_time` values unless they are re-indexed.

## The Cloudflare Security (WAF) dashboard is empty

The `Cloudflare – Security (WAF)` dashboard in the Cloudflare App for Splunk loads without errors, but all panels are empty. Other dashboards (Overview, Performance, Reliability) populate normally, and running the WAF panels' underlying SPL directly in the search bar also returns zero results — even when WAF and security events are confirmed present in the target index.

**Cause:** In older versions of the Cloudflare App for Splunk, the WAF dashboard SPL references Cloudflare log fields that were [removed from the HTTP Requests dataset](https://developers.cloudflare.com/logs/reference/change-notices/2023-02-01-security-fields-updates/#http-requests-dataset-changes):

Deprecated field | Current field  
---|---  
`FirewallMatchesRuleIDs{}` | `SecurityRuleIDs`  
`WAFRuleMessage` | `SecurityRuleDescription`  
  
Splunk does not raise an error when a search references a field that is absent from all indexed events — it completes the search and returns zero results, leaving every dashboard panel empty.

**Fix:** Upgrade to the latest version of the [Cloudflare App for Splunk ↗︎](https://splunkbase.splunk.com/app/4501/). The current release references `SecurityRuleIDs` and `SecurityRuleDescription` throughout the WAF dashboard, saved searches, and macros.

If you maintain a customized fork of the app, replace all references to `FirewallMatchesRuleIDs{}` and `WAFRuleMessage` in your dashboard XML, saved searches, and macros with `SecurityRuleIDs` and `SecurityRuleDescription`, respectively.

**Verify:** Reload the `Cloudflare – Security (WAF)` dashboard. Panels should populate with recent WAF and security events. A direct search such as `index=<your-index> sourcetype=cloudflare:json SecurityRuleIDs=*` should also return matching events.

## Still not resolved

If your issue is not covered here:

  * Consult the [Cloudflare App for Splunk page ↗︎](https://splunkbase.splunk.com/app/4501/) on Splunkbase for the latest version and release notes.
  * Review the [Cloudflare Logs change notices](https://developers.cloudflare.com/logs/reference/change-notices/) for recent schema changes that may affect your searches or dashboards.
  * [Contact Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) for issues involving Cloudflare-side log delivery.
  * Contact your Splunk representative or your integration partner for issues within your Splunk environment.



[PreviousOverview](https://developers.cloudflare.com/analytics/analytics-integrations/splunk/)[NextOverview](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-integrations/splunk/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

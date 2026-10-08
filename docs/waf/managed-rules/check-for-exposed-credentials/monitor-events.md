---
url: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/monitor-events/
title: Monitor exposed credentials events \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:43.507650+00:00
---

# Monitor exposed credentials events · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/monitor-events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Check for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)
  5. /Monitor exposed credentials events



# Monitor exposed credentials events

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/monitor-events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImportant notes

Deprecation notice

Exposed credentials check has been deprecated.

Switch from exposed credentials check to [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) for improved security. To upgrade your current configuration, refer to the [upgrade guide](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/).

**Sampled logs** in [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/) shows entries for requests with exposed credentials identified by rules with the _Log_ action.

Check for exposed credentials events in the Security Events dashboard, filtering by a specific rule ID. For more information on filtering events, refer to [Adjust displayed data](https://developers.cloudflare.com/waf/analytics/security-events/#adjust-displayed-data).

## Important notes

Exposed credentials events are only logged after you activate the Exposed Credentials Check Managed Ruleset or create a custom rule checking for exposed credentials.

The log entries will not contain the values of the exposed credentials (username, email, or password). However, if [matched payload logging](https://developers.cloudflare.com/waf/managed-rules/payload-logging/) is enabled, the log entries will contain the values of the fields in the rule expression that triggered the rule. These values might be the values of credential fields, depending on your rule configuration.

[PreviousTest your configuration](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/)[NextUpgrade to leaked credentials detection](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/check-for-exposed-credentials/monitor-events.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

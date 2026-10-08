---
url: https://developers.cloudflare.com/waf/detections/
title: Traffic detections \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:39.676259+00:00
---

# Traffic detections · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Traffic detections



# Traffic detections

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityTurn on a settings-managed detectionMore resources

Traffic detections check incoming requests for malicious, potentially malicious, or non-conforming activity. Each enabled detection scores or classifies requests by populating one or more fields. These fields appear as filters in the [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) dashboard, and you can use them in rule expressions.

Detections are always on once enabled, even if you have not configured any security rules that use them. You can review detection results in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) to identify traffic patterns and spot potentially malicious traffic. For example, you can analyze traffic based on [attack score](https://developers.cloudflare.com/waf/detections/attack-score/), [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/), [content scan results](https://developers.cloudflare.com/waf/detections/malicious-uploads/), or the [presence of personally identifiable information (PII)](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) in large language model (LLM) prompts.

[Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/) compare requests with application-specific expected structures. Profile detections do not mitigate traffic without a security rule.

[Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/) evaluates requests against Cloudflare attack signatures. It exposes match metadata independently from mitigation.

Attack Signature Detection is available in Early Access. Contact your Cloudflare account team to request access.

Application Profiles availability

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed-beta access does not imply future plan availability or pricing.

Cloudflare provides the following detections:

  * [WAF attack score](https://developers.cloudflare.com/waf/detections/attack-score/)
  * [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/)
  * [Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/)
  * [Leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/)
  * [Malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/)
  * [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)
  * [Threat intelligence](https://developers.cloudflare.com/waf/detections/threat-intelligence/)
  * [Bot score](https://developers.cloudflare.com/bots/concepts/bot-score/)



## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Malicious uploads detection | No | No | No | Paid add-on  
Leaked credentials detection | Yes | Yes | Yes | Yes  
Leaked credentials fields | Password Leaked | Password Leaked, User and Password Leaked | Password Leaked, User and Password Leaked | All leaked credentials fields  
Number of custom detection locations | 0 | 0 | 0 | 10  
Attack score | No | No | One field only | Yes  
AI Security for Apps | No | No | No | Yes  
  
For more information on bot score, refer to [Bot scores](https://developers.cloudflare.com/bots/concepts/bot-score/).

## Turn on a settings-managed detection

For detections managed through Security settings:

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **Detection tools**.

  3. Turn on the desired detections.




Detections enabled through Security settings run for all incoming traffic. Application Profiles instead evaluate requests after a learned or uploaded profile becomes available.

Notes

  * On Free plans, the leaked credentials detection is enabled by default, and no action is required.
  * Currently, you cannot manage the [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/) and [attack score](https://developers.cloudflare.com/waf/detections/attack-score/) detections from the **Settings** page. Refer to the documentation of each feature for availability details.



## More resources

For more information on detection versus mitigation, refer to [Concepts](https://developers.cloudflare.com/waf/concepts/#detection-versus-mitigation).

[PreviousConcepts](https://developers.cloudflare.com/waf/concepts/)[NextAttack score](https://developers.cloudflare.com/waf/detections/attack-score/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

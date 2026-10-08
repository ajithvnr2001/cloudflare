---
url: https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/
title: Enforce profiles with Custom Rules \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:40.657681+00:00
---

# Enforce profiles with Custom Rules · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/)
  5. /Enforce with Custom Rules



# Enforce profiles with Custom Rules

Last updated Aug 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSelect a detection fieldScope by applicationCombine security signalsRoll out mitigation

Application Profiles separate detection from mitigation. Cloudflare runs an **always-on detection** after a profile becomes available.

A violation does not block a request automatically. Use a [Custom Rule](https://developers.cloudflare.com/waf/custom-rules/) when you are ready to mitigate traffic.

## Select a detection field

Use this expression for learned Schema Profiles:
    
    
    cf.schema_validation.learned.violated

Use this expression for uploaded Schema Profiles:
    
    
    cf.schema_validation.uploaded.violated

Monitor the selected field in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) before creating a blocking rule.

## Scope by application

Limit mitigation to the intended hostname and path:
    
    
    cf.schema_validation.learned.violated and http.host eq "api.example.com" and starts_with(http.request.uri.path, "/v1/orders/")

Scope mitigation to an operation using its complete identity. Include the HTTP method, hostname, and path:
    
    
    cf.schema_validation.learned.violated and http.request.method eq "POST" and http.host eq "api.example.com" and http.request.uri.path eq "/v1/orders"

## Combine security signals

Combine a profile violation with [Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/):
    
    
    cf.schema_validation.learned.violated and cf.waf.score lt 20

Combine an uploaded profile violation with [Bot Score](https://developers.cloudflare.com/bots/concepts/bot-score/):
    
    
    cf.schema_validation.uploaded.violated and cf.bot_management.score lt 10

## Roll out mitigation

Review production traffic and sampled violation reasons first. Then [create a Custom Rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) with a suitable action.

Follow these rollout practices:

  * Start with monitoring in Security Analytics.
  * Limit the first rule to one operation.
  * Review the effect before expanding scope.
  * Recheck profiles after application releases.
  * Recheck violations after client changes.



For field details, refer to [Application Profile fields](https://developers.cloudflare.com/waf/detections/application-profiles/fields/).

[PreviousAnalyze profile detections](https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/)[NextFields](https://developers.cloudflare.com/waf/detections/application-profiles/fields/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/application-profiles/enforce-profiles-with-custom-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

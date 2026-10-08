---
url: https://developers.cloudflare.com/waf/detections/application-profiles/
title: Application Profiles \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:40.539441+00:00
---

# Application Profiles · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/application-profiles/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Traffic detections](https://developers.cloudflare.com/waf/detections/)
  4. /Application Profiles



# Application Profiles

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/application-profiles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUnderstand the profile lifecycleComplement existing detectionsExplore Application ProfilesSee also

Application Profiles define application-specific expectations and classify requests against them. They add a positive-security model to your existing protections.

Schema Profile is the only current profile type. It models supported request fields, types, formats, ranges, and values.

Note

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed-beta access does not imply future plan availability or pricing.

## Understand the profile lifecycle

A Schema Profile can come from observed traffic or an uploaded [OpenAPI schema](https://developers.cloudflare.com/api-shield/security/schema-validation/). Both sources produce the same profile type.

An operation is Cloudflare's term for an endpoint identified by HTTP method, hostname pattern, and path pattern. [Web Assets](https://developers.cloudflare.com/security/web-assets/) continuously discovers operations, and you can add operations manually.

Discovery and manual creation only add operations to your inventory. Profiling starts when you select **Learn profile** for an operation.

After the profile becomes available, Cloudflare runs an **always-on detection**. The detection classifies requests but does not mitigate traffic.

Review results in **Profile Analysis** before creating a [Custom Rule](https://developers.cloudflare.com/waf/custom-rules/). This keeps detection, investigation, and mitigation as separate steps.

## Complement existing detections

Positive security identifies requests outside your expected application structure. A non-conforming request does not need to match an attack signature.

Application Profiles complement [Managed Rules](https://developers.cloudflare.com/waf/managed-rules/), [Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/), and other negative-security detections. You can combine these signals in Custom Rules.

## Explore Application Profiles

  * [Get started](https://developers.cloudflare.com/waf/detections/application-profiles/get-started/)
  * [Schema Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/schema-profiles/)
  * [Analyze profile detections](https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/)
  * [Enforce profiles with Custom Rules](https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/)
  * [Fields](https://developers.cloudflare.com/waf/detections/application-profiles/fields/)



## See also

  * [Schema learning](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/)
  * [Schema validation](https://developers.cloudflare.com/api-shield/security/schema-validation/)



[PreviousFields](https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/)[NextGet started](https://developers.cloudflare.com/waf/detections/application-profiles/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/application-profiles/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

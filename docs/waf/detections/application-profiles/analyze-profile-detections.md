---
url: https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/
title: Analyze profile detections \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:40.935386+00:00
---

# Analyze profile detections · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/)
  5. /Analyze profile detections



# Analyze profile detections

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUnderstand request statusesUnderstand violation detailsReview detectionsInterpret violations

Use **Profile Analysis** in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) to investigate profile detections.

## Understand request statuses

Profile Analysis classifies requests with these statuses:

  * **Conforms:** The evaluated request matched its applicable profile.
  * **Violates:** The evaluated request did not match its applicable profile.
  * **Not evaluated:** No applicable profile is available, or the profile does not apply.



## Understand violation details

Sampled violations include structured details about the first detected validation failure:

Detail | Meaning | Example  
---|---|---  
Location | The request component containing the violation. | `body`  
Error class | A stable, broad category for grouping similar violations. | `constraint_violation`  
Error detail | An optional, specific reason within the error class. | `number_not_in_range`  
Target | An optional parameter, header, cookie, or JSON body path associated with the violation. | `$.items[0].quantity`  
  
The error detail or target can be empty when the other fields fully describe the violation. For example, a missing request body has the `missing_required` error class without a target.

For all possible error classes and details, refer to [Fields](https://developers.cloudflare.com/waf/detections/application-profiles/fields/#violation-details).

## Review detections

  1. In the Cloudflare dashboard, go to **Security** > **Analytics**.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)
  2. Open **Profile Analysis** and select a profile.

  3. Review conformance trends over your selected time range.

  4. Inspect sampled violations for the request component and affected field.

  5. Review each sampled violation reason before configuring mitigation.

  6. Filter by `cf.schema_validation.learned.violated` or `cf.schema_validation.uploaded.violated` to inspect the corresponding source.




## Interpret violations

A non-conforming request is not necessarily malicious. Releases, new clients, and valid edge cases can produce violations.

Cloudflare runs an **always-on detection** after a profile becomes available. Detection does not block requests by itself.

After reviewing representative traffic, refer to [Enforce profiles with Custom Rules](https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/).

[PreviousSchema Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/schema-profiles/)[NextEnforce with Custom Rules](https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/application-profiles/analyze-profile-detections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

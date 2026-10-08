---
url: https://developers.cloudflare.com/waf/detections/application-profiles/get-started/
title: Get started \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:40.894133+00:00
---

# Get started · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/application-profiles/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/)
  5. /Get started



# Get started

Last updated Aug 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/application-profiles/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReview learning requirementsLearn and review a profileUse an uploaded schema

Create a learned Schema Profile for one operation. Then review its detections before configuring mitigation.

Note

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed-beta access does not imply future plan availability or pricing.

## Review learning requirements

Cloudflare learns profiles weekly from qualifying traffic during the previous seven days. Only requests that received a `2xx` response qualify.

An operation needs 1,000 qualifying requests for the field-learning threshold. It needs 10,000 qualifying requests for the boundary-learning threshold.

After meeting the field-learning threshold, Cloudflare can learn request fields. After meeting the boundary-learning threshold, Cloudflare can learn constraints such as numeric ranges and string lengths.

The first profile appears after the next weekly learning run. This can take up to seven days after meeting the relevant threshold.

## Learn and review a profile

  1. In the Cloudflare dashboard, go to **Web Assets** > **Operations**.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Select a discovered operation or [add one manually](https://developers.cloudflare.com/security/web-assets/manage-operations/#add-operations-manually). An operation uses an HTTP method, hostname pattern, and path pattern.

  3. From the operation overflow menu, select **Learn profile**. Discovery and manual creation do not start profiling.

  4. Allow Cloudflare to collect enough qualifying traffic.

  5. From the operation overflow menu, select **View details**. Review the learned schema under **Security overview**.

  6. In **Security** > **Analytics** , open **Profile Analysis**. Review request time series for profile conformance and violations.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)
  7. Drill into sampled logs to review violation reasons.

  8. After reviewing representative production traffic, [create a Custom Rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/).

  9. Scope the rule to the intended hostname, path, or operation. Then choose a mitigation action.




After the profile becomes available, Cloudflare runs an **always-on detection**. It does not mitigate requests without a Custom Rule.

If no learned schema appears, confirm that you selected **Learn profile**. Cloudflare may still be collecting enough qualifying traffic.

For learning details and limitations, refer to [Schema Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/schema-profiles/).

## Use an uploaded schema

If you have an OpenAPI schema, upload it through [Schema validation](https://developers.cloudflare.com/api-shield/security/schema-validation/). Uploaded schemas produce detections through `cf.schema_validation.uploaded.violated`.

The API Shield reference covers upload formats, OpenAPI requirements, API configuration, Terraform configuration, and limitations.

[PreviousOverview](https://developers.cloudflare.com/waf/detections/application-profiles/)[NextSchema Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/schema-profiles/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/application-profiles/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

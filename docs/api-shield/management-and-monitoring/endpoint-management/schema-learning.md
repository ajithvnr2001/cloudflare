---
url: https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/
title: Schema learning \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:17.953003+00:00
---

# Schema learning · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /…

Management and Monitoring

  4. /[Endpoint Management](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/)
  5. /Schema learning



# Schema learning

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStart profile learningMeet learning requirementsExport a schemaLearned schema contents

Note

Schema Learning is the learned source for a Schema Profile. For the shared detection and mitigation model, refer to [Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/).

Schema Learning observes qualifying traffic for selected operations. It learns expected request fields and constraints for a Schema Profile.

## Start profile learning

  1. In the Cloudflare dashboard, go to **Web Assets** > **Operations**.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Open the operation overflow menu and select **Learn profile**.

  3. After the profile becomes available, select **View details**.

  4. Review the learned schema under **Security overview**.




Cloudflare runs an **always-on detection** after the learned profile becomes available. The detection does not mitigate requests by itself.

To investigate results, refer to [Analyze profile detections](https://developers.cloudflare.com/waf/detections/application-profiles/analyze-profile-detections/). To mitigate violations, refer to [Enforce profiles with Custom Rules](https://developers.cloudflare.com/waf/detections/application-profiles/enforce-profiles-with-custom-rules/).

## Meet learning requirements

Learning runs weekly using qualifying traffic from the previous seven days. Only requests that received a `2xx` response contribute.

The field-learning threshold requires 1,000 qualifying requests. The boundary-learning threshold requires 10,000 qualifying requests.

The first profile appears after the next weekly learning run. This can take up to seven days after meeting the relevant threshold.

For supported request components, constraints, and limitations, refer to [Schema Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/schema-profiles/).

## Export a schema

Export availability depends on your plan. Each export creates a point-in-time OpenAPI file from the current learned profile. It does not change the profile or its detection.

  1. In the Cloudflare dashboard, go to the **Web Assets** page.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Go to the **Operations** tab.

  3. Select **Export schema** and choose a hostname to export.

  4. Select whether to include learned parameters and rate limit recommendations.

  5. Select **Export schema** and choose a location to save the file.




Note

The schema is saved as a JSON file in OpenAPI `v3.0.0` format.

## Learned schema contents

Exported schemas include the listed hostname in the servers section. They also include operations by hostname, method, and path.

For operations that receive sufficient traffic, exported schemas also include:

  * Detected path variables and formats
  * Detected query parameters and formats
  * Detected `POST`, `PUT`, and `PATCH` body variable names and formats for `application/json` content types



Exported schemas can optionally include API Shield rate limit recommendations.

For a fixed Schema Profile, upload the exported file through [Schema validation](https://developers.cloudflare.com/api-shield/security/schema-validation/).

[PreviousOverview](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/)[NextLabeling service](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/management-and-monitoring/endpoint-management/schema-learning.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

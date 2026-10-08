---
url: https://developers.cloudflare.com/api-shield/management-and-monitoring/developer-portal/
title: Build developer portals \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:17.838545+00:00
---

# Build developer portals · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/management-and-monitoring/developer-portal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /Management and Monitoring
  4. /Build developer portals



# Build developer portals

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/management-and-monitoring/developer-portal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Custom domainsAvailabilityLimitations

Once your endpoints are saved, API Shield doubles as an API catalog. API Shield can build an interactive documentation portal with the knowledge it has of your APIs, or you can upload a new OpenAPI schema file to build a documentation portal ad-hoc.

To create a developer portal:

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **API abuse**.

  3. On **Create a developer portal** , select **Create site**.

  4. Upload an OpenAPI v3.0 schema file or choose to select an existing schema from API Shield.

Note

If you do not have a schema to upload or to select from a pre-existing schema, export your Endpoint Management schema. For best results, include the learned parameters.

Only API schemas uploaded to Schema validation 2.0 are available when selecting existing schemas.

  5. Select **Download project files** to save a local copy of the files that will be uploaded to Cloudflare Pages. Downloading the project files can be helpful if you wish to modify the project in any way and then upload the new version manually to Pages.

  6. Select **Create pages project** to continue to Cloudflare Pages. Pages creates the project and imports your API schema with the supporting static content. This step does not deploy the site.

  7. In Pages, select **Deploy site** to deploy the portal.




### Custom domains

To create a vanity domain instead of using the pages.dev domain, refer to the [Pages custom domain documentation](https://developers.cloudflare.com/pages/configuration/custom-domains/).

## Availability

Building developer portals is available to all API Shield subscribers. This feature uses Cloudflare Pages to host the resulting portal. Refer to [Pages](https://developers.cloudflare.com/pages/) for any limitations of your current subscription plan.

## Limitations

This feature currently uses the open source [Redoc ↗︎](https://github.com/Redocly/redoc) project from [Redocly ↗︎](https://redocly.com/). For custom theme and branding options, visit the [Redoc GitHub repository ↗︎](https://github.com/Redocly/redoc).

To modify the resulting page, download the project files before creating the Pages project. You can create a new Pages project with the modified files you have made to meet your branding guidelines.

[PreviousAPI Routing](https://developers.cloudflare.com/api-shield/management-and-monitoring/api-routing/)[NextClassic Schema validation](https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/management-and-monitoring/developer-portal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

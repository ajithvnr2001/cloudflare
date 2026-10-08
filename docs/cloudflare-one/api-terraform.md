---
url: https://developers.cloudflare.com/cloudflare-one/api-terraform/
title: API and Terraform \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:24.645954+00:00
---

# API and Terraform · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/api-terraform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /API and Terraform



# API and Terraform

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/api-terraform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet dashboard to read-onlyScoped API tokens

You can manage your Cloudflare Zero Trust configuration using the API or Terraform. For more information, refer to the following links:

  * [API reference](https://developers.cloudflare.com/api/)
  * [Terraform provider reference ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
  * [Terraform how-to documentation](https://developers.cloudflare.com/terraform/)



Detailed API and Terraform examples for Cloudflare Zero Trust are available in our [implementation guides](https://developers.cloudflare.com/cloudflare-one/implementation-guides/) and throughout the Cloudflare Zero Trust documentation.

## Set dashboard to read-only

Super Administrators can lock all settings as read-only in the Cloudflare One dashboard. Read-only mode ensures that all updates for the account are made through the API or Terraform.

To enable read-only mode:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Settings** > **Admin controls**.
  2. Enable **Set dashboard to read-only**.



All users, regardless of [user permissions](https://developers.cloudflare.com/cloudflare-one/roles-permissions/), will be prevented from making configuration changes through the UI.

## Scoped API tokens

The administrators managing policies and groups in Cloudflare Zero Trust might be different from those responsible for configuring WAF custom rules or other Cloudflare settings. You can configure scoped API tokens so that team members and automated systems can manage Cloudflare Zero Trust settings without having permission to modify other configurations in Cloudflare.

You can create a scoped API token [via the dashboard](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) or [via the API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/). For a list of available token permissions, refer to [API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/).

[PreviousFAQ](https://developers.cloudflare.com/cloudflare-one/faq/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/api-terraform.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

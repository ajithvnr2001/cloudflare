---
url: https://developers.cloudflare.com/terraform/advanced-topics/provider-customization/
title: Provider customization \u00b7 Cloudflare Terraform docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:00.578151+00:00
---

# Provider customization · Cloudflare Terraform docs

> Source: https://developers.cloudflare.com/terraform/advanced-topics/provider-customization/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Terraform](https://developers.cloudflare.com/terraform/)
  3. /Advanced topics
  4. /Provider customization



# Provider customization

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/terraform/advanced-topics/provider-customization/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdjust the default Cloudflare provider settings

Terraform communicates with cloud and global network provider APIs such as Cloudflare through modules known as providers. These providers are [installed automatically](https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/#2-initialize-terraform-and-the-cloudflare-provider) when you run `terraform init` in a directory that has a `.tf` file containing a provider.

Typically, the only required parameters to the provider are those required to authenticate. However, you may want to customize the provider to your needs. The following section covers some [optional settings ↗︎](https://www.terraform.io/docs/providers/cloudflare/#argument-reference) that you can pass to the Cloudflare Terraform provider.

## Adjust the default Cloudflare provider settings

Note

The examples below build on the [Cloudflare Terraform tutorial](https://developers.cloudflare.com/terraform/tutorial/).

You can customize the Cloudflare Terraform provider using configuration parameters, specified either in your `.tf` configuration files or via environment variables. Using environment variables may make sense when running Terraform from a CI/CD system or when the change is temporary and does not need to be persisted in your configuration history.

[PreviousImport Cloudflare resources](https://developers.cloudflare.com/terraform/advanced-topics/import-cloudflare-resources/)[NextRemote R2 backend](https://developers.cloudflare.com/terraform/advanced-topics/remote-backend/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/terraform/advanced-topics/provider-customization.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

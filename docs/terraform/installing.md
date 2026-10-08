---
url: https://developers.cloudflare.com/terraform/installing/
title: Install Terraform \u00b7 Cloudflare Terraform docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:00.887815+00:00
---

# Install Terraform · Cloudflare Terraform docs

> Source: https://developers.cloudflare.com/terraform/installing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Terraform](https://developers.cloudflare.com/terraform/)
  3. /Get started



# Get started

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/terraform/installing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMacLinuxWindows

Install the latest version of the Terraform CLI from [HashiCorp's official installation guide ↗︎](https://developer.hashicorp.com/terraform/install).

Caution

Terraform maintains your configuration state, which can be broken when you make configuration changes through both Terraform and either the Cloudflare Dashboard or API.

To avoid this state, make sure you manage Terraform resources only in Terraform. For more details, refer to our [best practices](https://developers.cloudflare.com/terraform/advanced-topics/best-practices/).

## Mac
    
    
    brew tap hashicorp/tap
    brew install hashicorp/tap/terraform

## Linux

Install via your distribution's package manager:
    
    
    sudo apt install terraform

## Windows

Download the installer from [HashiCorp's installation page ↗︎](https://developer.hashicorp.com/terraform/install) and follow the setup instructions.

[PreviousOverview](https://developers.cloudflare.com/terraform/)[NextOverview](https://developers.cloudflare.com/terraform/tutorial/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/terraform/installing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/1.1.1.1/setup/azure/
title: Set up 1.1.1.1 on Azure \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:04.356594+00:00
---

# Set up 1.1.1.1 on Azure · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/setup/azure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Set up](https://developers.cloudflare.com/1.1.1.1/setup/)
  4. /Azure



# Azure

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/azure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

These steps configure 1.1.1.1 as the DNS resolver for an Azure Virtual Network (VNet). This applies to all resources in the VNet, including virtual machines.

  1. Log in to your Azure portal.
  2. From the Azure portal side menu, select **Virtual Networks**.
  3. Select the virtual network you want to configure.
  4. Select **DNS Servers** > **Custom** , and add two entries: 
         
         1.1.1.1
         1.0.0.1

  5. Select **Save**.



[PreviousAndroid](https://developers.cloudflare.com/1.1.1.1/setup/android/)[NextGaming consoles](https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/setup/azure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

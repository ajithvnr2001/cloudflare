---
url: https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/
title: Set up 1.1.1.1 on Google Cloud \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:04.481474+00:00
---

# Set up 1.1.1.1 on Google Cloud · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Set up](https://developers.cloudflare.com/1.1.1.1/setup/)
  4. /Google Cloud



# Google Cloud

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Google Cloud lets you configure custom DNS servers at the Virtual Private Cloud (VPC) network level using [outbound server policies ↗︎](https://cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-out) in Cloud DNS. When you create an outbound server policy, all resources in that VPC network — including existing virtual machines — use the specified DNS servers.

Note

If you are using [Cloudflare Zero Trust](https://developers.cloudflare.com/cloudflare-one/), you can assign [locations](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/) to apply custom [DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/) via Gateway.

To configure 1.1.1.1 for your Google Cloud VPC network:

  1. Open the [Google Cloud Console ↗︎](https://console.cloud.google.com).
  2. Go to **Network Services** > **Cloud DNS** and select [**DNS Server Policies** ↗︎](https://console.cloud.google.com/net-services/dns/policies).
  3. Select **Create Policy**.
  4. Enter a name for your policy (for example, `cloudflare-1-1-1-1`) and select the VPC networks to apply it to.
  5. Under **Alternate DNS servers** , select **Add Item** and enter: 
         
         1.1.1.1
         1.0.0.1

  6. Select **Create**.



DNS requests within the configured VPC networks will now use 1.1.1.1.

[PreviousGaming consoles](https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/)[NextiOS](https://developers.cloudflare.com/1.1.1.1/setup/ios/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/setup/google-cloud.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

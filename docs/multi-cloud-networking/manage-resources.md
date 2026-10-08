---
url: https://developers.cloudflare.com/multi-cloud-networking/manage-resources/
title: Manage resources \u00b7 Cloudflare Multi-Cloud Networking docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:22.403630+00:00
---

# Manage resources · Cloudflare Multi-Cloud Networking docs

> Source: https://developers.cloudflare.com/multi-cloud-networking/manage-resources/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/)
  3. /Manage resources



# Manage resources

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/multi-cloud-networking/manage-resources/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCloud resource catalogEdit Cloud integrationsDownload cloud resource catalog

## Cloud resource catalog

Your cloud environment is built from individual cloud resources, like virtual private clouds (VPCs), subnets, virtual machines (VMs), route tables, and routes. Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta) discovers all of your cloud resources and stores their configuration and status in the Cloud resource catalog, a read-only snapshot of your cloud environment. Discovery runs regularly in the background, keeping your catalog up to date as your environment changes.

To browse the resources in your catalog:

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)
  2. Select the **Cloud (beta)** tab.

  3. In **Cloud resources** , select a resource to inspect its details.




## Edit Cloud integrations

You can change which cloud account the integration is linked to or delete the integration.

  1. Go to **Cloud integrations**.

[ Go to **Cloud integrations** ↗ ](https://dash.cloudflare.com/?to=/:account/mcn/integrations)
  2. Select your integration > **Edit**.

  3. In **Linked account details** , select **Link integration to a different cloud account**.

  4. Select **Save** when you are finished.

  5. (Optional) You can also select **Delete** to delete your cloud integration.




## Download cloud resource catalog

You can download a JSON file containing metadata and configuration for all your cloud resources:

  1. Go to the **Connectors** page.

[ Go to **Connectors** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/connections)
  2. Select the **Cloud (beta)** tab.

  3. In **Cloud resources** , select **Download catalog**.




After your browser finishes downloading the ZIP file, expand it to access the JSON with the information about your cloud resources.

[PreviousCloud on-ramps](https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/)[NextReference](https://developers.cloudflare.com/multi-cloud-networking/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/multi-cloud-networking/manage-resources.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/
title: Enable Logpush to other providers \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:15.760266+00:00
---

# Enable Logpush to other providers · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup

  4. /[Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/)
  5. /Enable other providers



# Enable other providers

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManage via the Cloudflare dashboardManage via API

Cloudflare Logpush supports pushing logs to a limited set of services providers. However, you can configure Logpush via API.

## Manage via the Cloudflare dashboard

Refer to [Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) for the list of services you can configure to use with Logpush through the Cloudflare dashboard. Interested in a different service? Take this [survey ↗︎](https://docs.google.com/forms/d/e/1FAIpQLScwOSabROywVajpMX2ZYCVl3saYs11cP4NIC8QR-wmOAnxOtA/viewform).

## Manage via API

The Cloudflare Logpush API allows you to configure and manage jobs via create, retrieve, update, and delete operations (CRUD).

With Logpush, you can create a job to upload logs of the metadata Cloudflare collects in batches as soon as possible to your cloud service provider. The default number of jobs that you can setup per dataset per domain is four, but you can setup more jobs depending on your plan and subscriptions.

Ensure **Log Share** permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the [Roles section](https://developers.cloudflare.com/logs/logpush/permissions/#roles).

  


To get started:

  1. Set up a storage provider and grant Cloudflare access. Your storage provider may request your Cloudflare API credentials and other information including:

     * Email address
     * Cloudflare API key
     * Zone ID
     * Destination access details for your cloud service provider
  2. Configure your Logpush job. For more information on how to configure a Logpush job, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/).




[PreviousEnable IBM Cloud Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/)[NextOverview](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/third-party/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/enable-destinations/other-providers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/health-checks/get-started/
title: Get started \u00b7 Cloudflare Health Checks docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:28.594697+00:00
---

# Get started · Cloudflare Health Checks docs

> Source: https://developers.cloudflare.com/health-checks/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Health Checks](https://developers.cloudflare.com/health-checks/)
  3. /Get started



# Get started

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/health-checks/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a Health CheckManage Health Checks

Smart Shield

This functionality is now offered as part of Cloudflare's origin server safeguard, Smart Shield. [Learn more](https://developers.cloudflare.com/smart-shield/).

This guide will get you started with creating and managing configured Health Checks.

## Create a Health Check

  1. In the Cloudflare dashboard, go to the **Health Checks** page.

[ Go to **Health Checks** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/traffic/health-checks)
  2. Select **Create** and fill out the form, paying special attention to:

     * The values for **Interval** and **Check regions** , because decreasing the **Interval** and increasing **Check regions** may increase the load on your origin server.
     * **Retries** , which specify the number of retries to attempt in case of a timeout before marking the origin as unhealthy.
     * **Response body** , which specifies a substring that must be present in the first 10 KB of the response body for the check to succeed.
  3. Select **Save and Deploy**.




## Manage Health Checks

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and select your account and domain.
  2. Go to **Traffic** > **Health Checks**.
  3. Navigate to your health check and select **Edit**.
  4. Edit your Health Check.
  5. Select **Save**.



Note

You can also enable, disable, or delete configured Health Checks.

Note

Authenticated origin pull is not supported by Standalone Health Checks.

[PreviousOverview](https://developers.cloudflare.com/health-checks/)[NextHealth Checks Analytics](https://developers.cloudflare.com/health-checks/health-checks-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/health-checks/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

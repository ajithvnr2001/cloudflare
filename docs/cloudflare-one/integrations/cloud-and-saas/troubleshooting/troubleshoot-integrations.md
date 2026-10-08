---
url: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/
title: Troubleshoot integrations \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:01.112072+00:00
---

# Troubleshoot integrations · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations[Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

  4. /Troubleshooting
  5. /Troubleshoot integrations



# Troubleshoot integrations

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIdentify unhealthy or outdated integrationsRepair an unhealthy integrationUpgrade an integration

Cloudflare CASB detects when integrations are unhealthy or outdated.

Common integration issues include changes to SaaS app or cloud environment configurations, user access, or permission scope. Integrations may need to be updated to support new features or permissions.

## Identify unhealthy or outdated integrations

To identify unhealthy CASB integrations, go to **Integrations** > **Cloud & SaaS integrations**. If an integration is unhealthy, CASB will set its status to **Broken**. If an integration is outdated, CASB will set its status to **Upgrade**.

## Repair an unhealthy integration

Repair limitation

If CASB does not support self-service repairs for an integration, you will need to [delete](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/#delete-an-integration) and recreate the integration to continue scanning.

You can repair unhealthy CASB integrations through your list of integrations or findings.

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Integrations** > **Cloud & SaaS integrations**.
  2. Choose your unhealthy integration.
  3. Select **Reauthorize**.
  4. In your SaaS app or cloud environment, reauthorize your account.



## Upgrade an integration

Upgrading an outdated integration will allow the integration to access new features and permissions.

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Integrations** > **Cloud & SaaS integrations**.
  2. Choose your outdated integration.
  3. Select **Upgrade integration**.
  4. In your SaaS app or cloud environment, upgrade your app and reauthorize your account.



[PreviousCASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/casb/)[NextTroubleshoot compute accounts](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-compute-accounts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/troubleshooting/troubleshoot-integrations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

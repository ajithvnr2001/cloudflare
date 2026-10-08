---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/
title: Secure with Cloudflare Access \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:03.609437+00:00
---

# Secure with Cloudflare Access · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /[Security](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/)
  5. /Secure with Cloudflare Access



# Secure with Cloudflare Access

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSetup

Cloudflare Access provides visibility and control over who has access to your [custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/). You can allow or block users based on identity, device posture, and other [Access rules](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Prerequisites

  * You must have an active custom hostname. For setup instructions, refer to [Configuring Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/).
  * You must have a Cloudflare Zero Trust plan in your SaaS provider account. Learn more about [getting started with Zero Trust](https://developers.cloudflare.com/cloudflare-one/setup/).
  * You can only run Access on custom hostnames if they are managed externally to Cloudflare or in a separate Cloudflare account. If the custom hostname zone is in the same account as the SaaS zone, the Access application will not be applied.



## Setup

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select your SaaS provider account and go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application**.
  3. Select **Self-hosted and private**.
  4. Select **Add public hostname**.
  5. Select **Switch to custom input**.
  6. In **Hostname** , enter your custom hostname (for example, `mycustomhostname.com`).
  7. Follow the remaining [self-hosted application creation steps](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) to publish the application.



[PreviousManaged rulesets](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/)[NextOverview](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

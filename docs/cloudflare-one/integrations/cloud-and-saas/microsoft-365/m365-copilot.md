---
url: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/
title: Microsoft 365 Copilot \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:58.371504+00:00
---

# Microsoft 365 Copilot · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations[Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

  4. /[Microsoft 365](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/)
  5. /Microsoft 365 Copilot



# Microsoft 365 Copilot

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntegration prerequisitesIntegration permissionsSecurity findings Data Loss Prevention (optional)

The Microsoft 365 Copilot integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Microsoft 365 account that could leave you and your organization vulnerable.

## Integration prerequisites

  * A Microsoft 365 account with an active Microsoft Business Basic, Microsoft Business Standard, Microsoft 365 E3, Microsoft 365 E5, or Microsoft 365 F3 subscription
  * [Global admin role ↗︎](https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#commonly-used-microsoft-365-admin-center-roles) or equivalent permissions in Microsoft 365



## Integration permissions

Refer to [Microsoft 365 integration permissions](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/#integration-permissions) for information on which API permissions to enable.

## Security findings

The Microsoft 365 Copilot integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by [severity level](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels).

To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its [RSS feed](https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/microsoft-365/copilot.mdx.atom).

### Data Loss Prevention (optional)

These findings will only appear if you [added DLP profiles](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/) to your CASB integration.

Detect DLP matches in content used and shared within Microsoft's artificial intelligence (AI) offering, Microsoft 365 Copilot.

Finding type | FindingTypeID | Severity  
---|---|---  
Microsoft: Copilot Referenced File with DLP Profile match | `fa7b06bd-cf63-41fc-9afa-a20598f7a52d` | High  
Microsoft: Copilot AI Response with DLP Profile match | `176b9299-0cee-4bbb-9c59-b18611228454` | High  
Microsoft: Copilot User Prompt with DLP Profile match | `1c5f1cdf-3e08-4a83-baf9-fc8e123877ab` | High  
  
[PreviousSharePoint](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/sharepoint/)[NextAdmin Center (FedRAMP)](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/admin-center-fedramp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/microsoft-365/m365-copilot.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

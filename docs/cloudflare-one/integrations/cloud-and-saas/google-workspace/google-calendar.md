---
url: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar/
title: Google Calendar \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:57.261994+00:00
---

# Google Calendar · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations[Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

  4. /[Google Workspace](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/)
  5. /Google Calendar



# Google Calendar

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntegration prerequisitesIntegration permissionsSecurity findings Calendar sharing

The Google Calendar integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Google Workspace account that could leave you and your organization vulnerable.

## Integration prerequisites

  * A Google Workspace account with a Business Starter, Business Standard, Business Plus or Enterprise plan
  * A Google Workspace user with [Super Admin privileges ↗︎](https://support.google.com/a/answer/2405986) and [Owner permissions ↗︎](https://cloud.google.com/iam/docs/understanding-roles) in the Google Cloud Platform (GCP) project used



## Integration permissions

Refer to [Google Workspace integration permissions](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/#integration-permissions) for information on which API permissions to enable.

## Security findings

The Google Calendar integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by [severity level](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels).

To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its [RSS feed](https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar.mdx.atom).

### Calendar sharing

Finding type | FindingTypeID | Severity | Description  
---|---|---|---  
Google Workspace: Calendar is publicly accessible | `ec68bf68-b0c0-47b3-ad48-fcb3d7eaf8b6` | Medium | A user's Google Calendar is publicly accessible on the Internet that anyone can read.  
  
[PreviousGoogle Admin](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-admin/)[NextGoogle Drive](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-drive/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/google-workspace/google-calendar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

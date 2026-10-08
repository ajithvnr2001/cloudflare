---
url: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/
title: Slack \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:00.179706+00:00
---

# Slack · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)
  5. /Slack



# Slack

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/slack/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntegration prerequisitesIntegration permissionsSecurity findings User account settings Channel sharing File sharing

The Slack integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Slack Workspace that could leave you and your organization vulnerable.

## Integration prerequisites

  * A Slack user account
  * Membership in a Slack Workspace (Free, Pro, Business+, or Enterprise Grid)
  * If you are not the Workspace Owner and the `Require App Approval` setting is enabled for the Workspace, [request permission ↗︎](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace) to install apps.



## Integration permissions

For the Slack integration to function, Cloudflare CASB requires the following Slack API permissions:

  * `channels:read`
  * `files:read`
  * `groups:read`
  * `users:read`



These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the [Slack Permission scopes reference ↗︎](https://api.slack.com/scopes).

## Security findings

The Slack integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by [severity level](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels).

To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its [RSS feed](https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/slack.mdx.atom).

### User account settings

Finding type | FindingTypeID | Severity | Description  
---|---|---|---  
Slack: User with two-factor authentication disabled | `d1cc8596-d22c-435c-9f94-3ba068f019cd` | Critical | A user in the Slack Workspace does not have two-factor authentication (2FA) enabled for their account.  
Slack: User with unverified email | `9fa4ae7c-07f0-453a-b232-e734b0f8877c` | High | A user in the Slack Workspace has not verified the email they use to sign in.  
  
### Channel sharing

Finding type | FindingTypeID | Severity | Description  
---|---|---|---  
Slack: Channel shared externally | `d298ba64-f013-4e28-b68a-63f758380355` | High | A channel in the Slack Workspace has been shared with users who are not members of the Workspace.  
  
### File sharing

Finding type | FindingTypeID | Severity | Description  
---|---|---|---  
Slack: File publicly accessible with view access | `9d96d3a2-696b-4802-98aa-c6c8572e806e` | Medium | An external link has been created for a file uploaded to the Slack Workspace.  
Slack: File larger than 2 GB | `c16d64a8-9f78-4f24-99ff-de7fcdc6871b` | Low | A file ≥ 2 GB has been uploaded to the Slack Workspace.  
  
[PreviousServiceNow](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/servicenow/)[NextCASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/troubleshooting/casb/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/slack.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

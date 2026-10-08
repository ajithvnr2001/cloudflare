---
url: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/
title: Anthropic \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:54.280892+00:00
---

# Anthropic · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)
  5. /Anthropic



# Anthropic

Last updated May 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntegration prerequisitesIntegration permissionsSecurity findings API key hygiene Access security Data Loss Prevention (optional)

The Anthropic integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated Anthropic account that could leave you and your organization vulnerable.

This integration covers the following Anthropic products:

  * Claude Console (organizations, workspaces/projects, users, invites)
  * Anthropic API Platform (organization and project API keys)



Note

To detect data loss prevention and posture findings, your organization must have Anthropic's Compliance API enabled. Contact your Anthropic representative to request access. When enabled, admin keys created in the Claude Console automatically include the `read:compliance_activities` scope.

## Integration prerequisites

  * An Anthropic [Enterprise or Platform organization ↗︎](https://www.anthropic.com/pricing#team-&-enterprise)
  * [Organization-level admin (or equivalent) privileges in Anthropic ↗︎](https://support.anthropic.com/articles/10186004-api-console-roles-and-permissions) to view organization metadata and manage API keys



## Integration permissions

For the Anthropic integration to function, Cloudflare CASB requires authorization via **API keys** :

  * `Admin API key (organization-level)`: Grants read-only access to organization/workspace metadata, members and invites, key metadata, and compliance activities used for findings.
  * (Optional) `Project API key (project-level)`: Grants read-only access to project metadata and keys when you include project scopes in the scan.



These credentials follow the principle of least privilege so that only the minimum required access is granted.

## Security findings

The Anthropic integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by [severity level](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels).

To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its [RSS feed](https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/anthropic.mdx.atom).

### API key hygiene

Detect API keys that may be unused or overdue for rotation.

Finding type | Severity  
---|---  
Anthropic: Unused API key | Medium  
  
### Access security

Flag organization access issues to help enforce best practices.

Finding type | Severity  
---|---  
Anthropic: High-privilege invite | High  
Anthropic: Stale pending invite | Low  
Anthropic: Claude Project visible across organization | Low  
Anthropic: Claude Cowork enabled for role | High  
Anthropic: Claude Connector always allowed enabled for role | High  
Anthropic: Claude for Chrome enabled for role | High  
  
### Data Loss Prevention (optional)

These findings will only appear if you [added DLP profiles](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/) to your CASB integration.

Finding type | Severity  
---|---  
Anthropic: Downloadable File with DLP Profile match | High  
Anthropic: Claude Chat User Prompt with DLP Profile match | High  
Anthropic: Claude Chat Assistant Response with DLP Profile match | High  
Anthropic: Claude Chat Uploaded File with DLP Profile match | High  
Anthropic: Claude Chat Generated File with DLP Profile match | High  
Anthropic: Claude Project File with DLP Profile match | High  
Anthropic: Claude Project Document with DLP Profile match | High  
Anthropic: Claude Chat Artifact with DLP Profile match | High  
Anthropic: Claude Project Instructions with DLP Profile match | High  
  
[PreviousWebhooks](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/)[NextAtlassian Confluence](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/atlassian-confluence/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/anthropic.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

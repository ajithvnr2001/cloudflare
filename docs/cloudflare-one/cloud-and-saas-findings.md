---
url: https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/
title: Cloud and SaaS findings \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:28.294859+00:00
---

# Cloud and SaaS findings · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /Cloud and SaaS findings



# Cloud and SaaS findings

Last updated Oct 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFinding terminologyManage CASB integrations Prerequisites Add an integration Pause an integration Delete an integration

Availability

Available for all Zero Trust users.

Free users can configure up to two CASB integrations. You must upgrade to an Enterprise plan to view the details of a finding instance.

Cloudflare's [Cloud Access Security Broker ↗︎](https://www.cloudflare.com/learning/access-management/what-is-a-casb/) (CASB) connects to SaaS application and cloud environment APIs to scan for security issues that can occur after a user has successfully logged in. These include misconfigurations (such as overly permissive sharing settings), unauthorized user activity, [shadow IT](https://www.cloudflare.com/learning/access-management/what-is-shadow-it/), and other data security issues.

For a list of supported finding types, refer to [Cloud and SaaS integrations](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/). You can also send posture finding instances to external systems with [CASB webhooks](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/webhooks/).

## Finding terminology

CASB uses the following terms for posture findings:

Term | Definition  
---|---  
Finding type | A definition of a specific security issue that CASB detects. It includes detection logic and metadata for one vendor and asset class, such as files or users. One finding type can apply to multiple integrations.  
Posture finding | A summary of detections of one finding type within one integration. Each row in **Posture Findings** represents a finding and groups its instances.  
Finding instance | An individual occurrence of a posture finding affecting a specific asset within that integration. One asset can have instances of different finding types.  
  
For example, CASB detects publicly viewable files in two Google Workspace integrations. **Posture Findings** shows two findings for the **Google Workspace: File publicly accessible with view access** finding type, one per integration. Each affected file, such as `budget.xlsx`, is a separate finding instance within its integration.

Content findings use a different grouping. Each row in **Content Findings** represents one asset within an integration and groups its matching [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) profiles.

To review detected findings and their affected assets, refer to [Manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/).

## Manage CASB integrations

When you integrate a third-party SaaS application or cloud environment with Cloudflare CASB, you allow CASB to make API calls to its endpoint and read relevant data on your behalf. The CASB integration permissions are read-only and follow the least privileged model. In other words, only the minimum access required to perform a scan is granted.

### Prerequisites

Before you can integrate a SaaS application or cloud environment with CASB, your account with that integration must meet certain requirements. Refer to the SaaS application or cloud environment's [integration guide](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) to learn more about the prerequisites and permissions.

### Add an integration

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Cloud & SaaS findings** > **Integrations**.
  2. Select **Connect an integration** or **Add integration**.
  3. Browse the available integrations and select the application you would like to add.
  4. Follow the step-by-step integration instructions in the UI.
  5. To run your first scan, select **Save integration**.



After the first scan, CASB will automatically scan your SaaS application or cloud environment on a frequent basis to keep up with any changes. Scan intervals will vary due to each application having their own set of requirements, but the frequency is typically between every 1 hour and every 24 hours.

Once CASB detects at least one finding, you can [view and manage your findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/).

### Pause an integration

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Cloud & SaaS findings** > **Integrations**.
  2. Find the integration you would like to pause and select **Configure**.
  3. To stop scanning the application, turn off **Scan for findings**.
  4. Select **Save integration**.



You can resume CASB scanning at any time by turning on **Scan for findings**.

### Delete an integration

Caution

When you delete an integration, all keys and OAuth data will be deleted. This means you cannot restore a deleted integration or its scanned data.

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Cloud & SaaS findings** > **Integrations**.
  2. Find the integration you would like to delete and select **Configure**.
  3. Select **Disenroll**.



To resume scanning the integration for findings, you will need to add the integration again.

[PreviousTroubleshooting](https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshooting/)[NextManage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/cloud-and-saas-findings/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

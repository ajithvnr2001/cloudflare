---
url: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles/
title: Integration profiles \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:31.667695+00:00
---

# Integration profiles · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Data loss prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

  4. /[DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/)
  5. /Integration profiles



# Integration profiles

Last updated Jun 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMicrosoft Purview Information Protection (MIP) sensitivity labels Setup Syncing

Note

Integration profiles require [Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/).

Integration profiles let you use data classifications from a third-party platform (such as Microsoft Purview sensitivity labels) directly in Cloudflare DLP. Instead of recreating classification rules yourself, Cloudflare retrieves them from the third-party platform and populates them as [detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/) in a DLP profile. You can then enable the entries you want and create a DLP policy to allow or block matching data.

Detection entries in integration profiles are managed by the third-party platform. You cannot manually add, edit, or delete these entries within Cloudflare DLP.

## Microsoft Purview Information Protection (MIP) sensitivity labels

Microsoft provides [Purview Information Protection sensitivity labels ↗︎](https://learn.microsoft.com/en-us/purview/sensitivity-labels) to classify and protect sensitive data.

Caution

DLP does not filter or log [MIP sublabels ↗︎](https://learn.microsoft.com/purview/sensitivity-labels#sublabels-that-use-parent-labels-or-label-groups). Only top-level sensitivity labels will be detected, filtered, and logged.

To ensure DLP will detect and filter all sensitive data, use only [MIP top-level labels ↗︎](https://learn.microsoft.com/purview/sensitivity-labels#top-level-labels).

### Setup

To add MIP sensitivity labels to a DLP profile, integrate your Microsoft account with [Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/). A new integration profile will appear under **Zero Trust** > **Data loss prevention** > **Profiles**. The profile is named **MIP Sensitivity Labels** followed by the name of the CASB integration.

MIP sensitivity labels can also be added to a [custom DLP profile](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile) as an existing entry.

### Syncing

Allow 24 hours for label additions and edits in your Microsoft account to propagate to Cloudflare DLP. Deletions in your Microsoft account will not delete entries in your Cloudflare DLP profile.

[PreviousPredefined profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/)[NextProfile settings](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

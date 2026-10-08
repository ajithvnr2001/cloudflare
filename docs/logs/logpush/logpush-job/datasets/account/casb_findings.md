---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/
title: CASB Findings \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.468277+00:00
---

# CASB Findings · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /CASB Findings



# CASB Findings

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/casb_findings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAssetDisplayNameAssetExternalIDAssetLinkAssetMetadataDetectedTimestampFindingTypeDisplayNameFindingTypeIDFindingTypeSeverityInstanceIDIntegrationDisplayNameIntegrationIDIntegrationPolicyVendor

The descriptions below detail the fields available for `casb_findings`.

## AssetDisplayName

Type: `string`

Asset display name (for example, 'My File Name.docx').

## AssetExternalID

Type: `string`

Unique identifier for an asset of this type. Format will vary by policy vendor.

## AssetLink

Type: `string`

URL to the asset. This may not be available for some policy vendors and asset types.

## AssetMetadata

Type: `object`

Metadata associated with the asset. Structure will vary by policy vendor.

## DetectedTimestamp

Type: `int or string`

Date and time the finding was first identified (for example, '2021-07-27T00:01:07Z').

## FindingTypeDisplayName

Type: `string`

Human-readable name of the finding type (for example, 'File Publicly Accessible Read Only').

## FindingTypeID

Type: `string`

UUID of the finding type in Cloudflare's system.

## FindingTypeSeverity

Type: `string`

Severity of the finding type (for example, 'High').

## InstanceID

Type: `string`

UUID of the finding in Cloudflare's system.

## IntegrationDisplayName

Type: `string`

Human-readable name of the integration (for example, 'My Google Workspace Integration').

## IntegrationID

Type: `string`

UUID of the integration in Cloudflare's system.

## IntegrationPolicyVendor

Type: `string`

Human-readable vendor name of the integration's policy (for example, 'Google Workspace Standard Policy').

[PreviousBrowser Isolation User Actions](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/biso_user_actions/)[NextDevice posture results](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/device_posture_results/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/casb_findings.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

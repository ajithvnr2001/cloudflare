---
url: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/
title: DLP profiles \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:31.241950+00:00
---

# DLP profiles · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Data loss prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)
  4. /DLP profiles



# DLP profiles

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure a predefined profileBuild a custom profile

A DLP profile defines what sensitive data Cloudflare detects in your traffic. A profile combines one or more of the following building blocks:

  * **[Detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/)** — reusable detection logic that identifies sensitive content, such as patterns, datasets, document fingerprints, predefined detections, and AI prompt topics.
  * **Data classes** — reusable classification rules that combine detection entries and other signals into a single rule.
  * **Labels** — sensitivity levels and data tags that describe matched content.



Data classes and labels are part of [Data Classification](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/). Cloudflare DLP offers three types of profiles:

  * **[Predefined profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/)** — Cloudflare-managed profiles for common sensitive data types such as credit card numbers, national identifiers, and AI prompts.
  * **Custom profiles** — profiles you build from detection entries, data classes, and labels, specific to your data, organization, and risk tolerance.
  * **[Integration profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles/)** — profiles populated with data classifications from a third-party platform, such as Microsoft Purview sensitivity labels (requires Cloudflare CASB).



To decide which data types to focus on, use [Passive Detection](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/) to explore detections in sampled Gateway traffic before creating a DLP policy.

## Configure a predefined profile

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Data loss prevention** > **Profiles**.
  2. Choose a [predefined profile](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/) and select **Edit**.
  3. Enable one or more **Detection entries** according to your preferences.
  4. Select **Save profile**.



Most predefined profiles match when any enabled detection entry matches. The **Personally Identifiable Information (PII) Record** profile is an exception and requires at least three unique detection entries in close proximity before the profile matches.

You can now use this profile in a [DLP policy](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy), [CASB integration](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/), [AI Gateway DLP policy](https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/), or [Email Security outbound DLP policy](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/).

## Build a custom profile

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Data loss prevention** > **Profiles**.

  2. Select **Create profile**.

  3. Enter a name and optional description for the profile.

  4. Add detection entries to the profile.

Create a custom entry

     1. Select **Create custom entry**.

     2. Choose the type of detection entry you want to create and configure its values.

For information on supported detection entry types, refer to [Configure detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/).

     3. To save the detection entry, select **Done**.

Add existing entries

Existing entries include [predefined](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/) and [user-defined](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/) detection entries that you manage from the Detection entries section.

     1. Select **Add existing entries**.
     2. Choose which entries you want to add, then select **Confirm**.
     3. To finish, select **Done**.
  5. (Optional) Add data classes to include reusable classification rules.

     * Select **Add data classes**
     * Choose the data classes you want to add, then select **Confirm**
  6. (Optional) Use labels as match criteria for the profile.

     * Select a sensitivity schema and minimum sensitivity level.
     * Select a data tag group and one or more data tags.

For more information on labels, templates, and data classes, refer to [Data Classification](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/).

  7. (Optional) Configure [**profile settings**](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/) for the profile.

  8. Select **Save profile**.




Before you apply a custom profile to production traffic, use [Test scan](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/test-scan/) to confirm that it detects the content you expect.

You can now use this profile in a [DLP policy](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy), [CASB integration](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/casb-dlp/), [AI Gateway DLP policy](https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/), or [Email Security outbound DLP policy](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/).

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)[NextPredefined profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/data-loss-prevention/dlp-profiles/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

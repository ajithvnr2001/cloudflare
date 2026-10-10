---
url: https://developers.cloudflare.com/changelog/post/2026-04-14-configurable-payload-log-masking/
title: Configure how sensitive data appears in DLP payload logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.602449+00:00
---

# Configure how sensitive data appears in DLP payload logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-14-configurable-payload-log-masking/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 14, 2026

## Configure how sensitive data appears in DLP payload logs

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure how sensitive data matches are displayed in your DLP payload match logs — giving your incident response team the context they need to validate alerts without compromising your security posture.

To get started, go to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select **Zero Trust** > **Data loss prevention** > **DLP settings** and find the **Payload log masking** card.

Previously, all DLP payload logs used a single masking mode that obscured matched data entirely and hid the original character count, making it difficult to distinguish true positives from false positives. This update introduces three options:

  * **Full Mask (default):** Masks the match while preserving character count and visual formatting (for example, `***-**-****` for a Social Security Number). This is an improvement over the previous default, which did not preserve character count.
  * **Partial Mask:** Reveals 25% of the matched content while masking the remainder (for example, `***-**-6789`).
  * **Clear Text:** Stores the full, unmasked violation for deep investigation (for example, `123-45-6789`).



**Important:** The masking level you select is applied at detection time, before the payload is encrypted. This means the chosen format is what your team will see after decrypting the log with your private key — the existing encryption workflow is unchanged.

**Applies to all enabled detections:** When a masking level other than Full Mask is selected, it applies to all sensitive data matches found within a payload window — not just the match that triggered the policy. Any data matched by your enabled DLP detection entries will be masked at the selected level.

For more information, refer to [DLP logging options](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules).

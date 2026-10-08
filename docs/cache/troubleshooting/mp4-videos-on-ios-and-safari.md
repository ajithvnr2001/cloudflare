---
url: https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/
title: Issues with MP4 videos on iOS and Safari \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:46.656109+00:00
---

# Issues with MP4 videos on iOS and Safari · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Troubleshooting
  4. /Issues with MP4 videos on iOS and Safari



# Issues with MP4 videos on iOS and Safari

Last updated May 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/troubleshooting/mp4-videos-on-ios-and-safari/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Create the strong ETags rule2\. Create the bypass cache ruleWhy this order matters

When traffic is proxied through Cloudflare, Safari on macOS and iOS devices may fail to load MP4 video files.

This issue occurs because Safari handles HTTP range requests differently than other browsers, particularly in how it processes ETags during video streaming.

Safari and iOS devices rely on HTTP range requests to support video features such as seeking to specific timestamps and resuming interrupted downloads.

When Cloudflare's caching layer processes these range requests with weak ETags, Safari may reject the cached response entirely, resulting in videos that fail to load or display as black screens.

To resolve this issue, configure two cache rules in the following order.

## 1\. Create the strong ETags rule

Create a [cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) that applies to all MP4 files, marks them as eligible for cache, and turns on the Respect Strong ETags setting.

  1. In the Cloudflare dashboard, go to the **Cache Rules** page.

[ Go to **Cache Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules)
  2. Select **Create rule** > **Cache rules**.

  3. Enter a descriptive name for the rule in **Rule name**.

  4. In the **When incoming requests match…** section, create a filter that applies to all MP4 files, for example `URI Full` `Wildcard` `*.mp4`.

  5. Select **Eligible for cache** in the **Cache eligibility** section.

  6. Select **\+ Add Setting** for **Respect strong ETags** and turn on the toggle.

  7. Select **Last** as **Place at**.




## 2\. Create the bypass cache rule

Create another cache rule that applies to all MP4 files and bypasses cache entirely.

  1. In the Cloudflare dashboard, go to the **Cache Rules** page.

[ Go to **Cache Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules)
  2. Select **Create rule** > **Cache rules**.

  3. Enter a descriptive name for the rule in **Rule name**.

  4. In the **When incoming requests match…** section, create the same filter for MP4 files, for example `URI Full` `Wildcard` `*.mp4`.

  5. Select **Bypass cache** in the **Cache eligibility** section.

  6. Select **Last** as **Place at**.




## Why this order matters

The first rule preserves strong ETags for MP4 files, which satisfies Safari's requirements for range request handling. The second rule bypasses cache so that Cloudflare forwards range requests to the origin server instead of serving cached responses with potentially mismatched ETags.

The first rule must appear above the second rule in the Cache Rules list.

[PreviousDynamic content and login issues](https://developers.cloudflare.com/cache/troubleshooting/dynamic-content-and-login-issues/)[NextInvestigate latency on tiered requests](https://developers.cloudflare.com/cache/troubleshooting/investigating-tiered-cache-latency/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/troubleshooting/mp4-videos-on-ios-and-safari.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

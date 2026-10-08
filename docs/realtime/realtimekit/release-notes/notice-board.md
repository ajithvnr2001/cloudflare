---
url: https://developers.cloudflare.com/realtime/realtimekit/release-notes/notice-board/
title: Notices \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:08.782667+00:00
---

# Notices · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/release-notes/notice-board/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Release notes](https://developers.cloudflare.com/realtime/realtimekit/release-notes/)
  5. /Notices



# Notices

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/release-notes/notice-board/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Subscribe to RSS](https://developers.cloudflare.com/realtime/realtimekit/release-notes/notice-board/index.xml)

## 2026-01-30

**Chat Pagination Overhaul**

**Affected SDKs:** Web Core SDK 1.2.4+ and Web UI Kit 1.0.9+ (Angular/React/Web Components)

To streamline RealtimeKit SDK offerings, non-operational chat channel APIs have been removed. If you have a custom chat implementation using lower-level components instead of `rtk-chat`, please review the release notes thoroughly and test your implementation after upgrading.

## 2025-11-21

**Support for legacy media engine has been removed**

**Affected SDKs:** Web Core SDK 1.2.0+ (Angular/React/Web Components)

Legacy media engine support has been removed.

If your organization was created before March 1, 2025 and you are upgrading to `1.2.0` or above, you may experience recording issues.

Please contact support to migrate you to the new Cloudflare SFU media engine to ensure continued recording functionality.

## 2025-11-21

**Update on meeting join issues in firefox 144+**

**Affected SDKs:** Web Core SDK < 1.2.0 (Angular/React/Web Components)

In firefox 144+, users were not able to join the meetings, due to the browser's datachannel behavior change.

Error: `x.data.arrayBuffer is not a function`

Please upgrade to atleast `v1.2.0` to fix this. It is advised to periodically upgrade the SDKs.

[PreviousFlutter UI Kit](https://developers.cloudflare.com/realtime/realtimekit/release-notes/flutter-ui-kit/)[NextPricing](https://developers.cloudflare.com/realtime/realtimekit/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/release-notes/notice-board.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

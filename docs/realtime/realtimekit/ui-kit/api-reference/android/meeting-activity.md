---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-activity/
title: RtkMeetingActivity \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:13.664287+00:00
---

# RtkMeetingActivity · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-activity/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkMeetingActivity



# RtkMeetingActivity

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-activity/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUsage Examples Basic Usage

The main meeting activity that manages the full meeting lifecycle. Handles transitions between loading, setup, waiting room, group call, webinar, and error states. This is the activity launched by `RealtimeKitUI.startMeeting()`.

## Usage Examples

### Basic Usage
    
    
    val meetingInfo = RtkMeetingInfo(authToken = authToken, baseUrl = baseUrl)
    val realtimeKitUIInfo = RealtimeKitUIInfo(activity = this, rtkMeetingInfo = meetingInfo)
    val realtimeKitUI = RealtimeKitUIBuilder.build(realtimeKitUIInfo)
    realtimeKitUI.startMeeting()

[PreviousRtkLoaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/loader-view/)[NextRtkMeetingControlBarView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/meeting-activity.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

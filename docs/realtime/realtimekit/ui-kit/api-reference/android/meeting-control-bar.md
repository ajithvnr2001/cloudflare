---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-control-bar/
title: RtkMeetingControlBarView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:14.017886+00:00
---

# RtkMeetingControlBarView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-control-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkMeetingControlBarView



# RtkMeetingControlBarView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-control-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A pre-built control bar for group call meetings. Contains mic toggle, camera toggle, more toggle, and leave button.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the control bar to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbars.RtkMeetingControlBarView
        android:id="@+id/rtk_meeting_control_bar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val controlBar = findViewById<RtkMeetingControlBarView>(R.id.rtk_meeting_control_bar)
    controlBar.activate(meeting)

[PreviousRtkMeetingActivity](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-activity/)[NextRtkMeetingHeaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/meeting-control-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

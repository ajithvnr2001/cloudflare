---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-button/
title: RtkLeaveButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:12.658300+00:00
---

# RtkLeaveButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkLeaveButton



# RtkLeaveButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A button which toggles visibility of the leave confirmation dialog.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkLeaveButton
        android:id="@+id/rtk_leave_button"
        android:layout_width="48dp"
        android:layout_height="48dp" />

### With Methods
    
    
    val leaveButton = findViewById<RtkLeaveButton>(R.id.rtk_leave_button)
    leaveButton.activate(meeting)

[PreviousRtkJoinStageDialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-stage-dialog/)[NextRtkLeaveMeetingView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-meeting-dialog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/leave-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

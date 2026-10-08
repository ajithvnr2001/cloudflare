---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-title-view/
title: RtkMeetingTitleView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:14.240285+00:00
---

# RtkMeetingTitleView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-title-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkMeetingTitleView



# RtkMeetingTitleView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-title-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A text view that displays the meeting title. It automatically updates when the meeting title changes.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the view to the meeting state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkMeetingTitleView
        android:id="@+id/rtk_meeting_title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val titleView = findViewById<RtkMeetingTitleView>(R.id.rtk_meeting_title)
    titleView.activate(meeting)

[PreviousRtkMeetingOptionBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-option-bottomsheet/)[NextRtkMicToggleButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/meeting-title-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

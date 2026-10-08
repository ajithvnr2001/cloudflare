---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/clock-view/
title: RtkClockView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:11.036401+00:00
---

# RtkClockView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/clock-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkClockView



# RtkClockView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/clock-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A clock component which shows the elapsed time of a meeting.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the clock to the meeting state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkClockView
        android:id="@+id/rtk_clock_view"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val clockView = findViewById<RtkClockView>(R.id.rtk_clock_view)
    clockView.activate(meeting)

[PreviousRtkChatBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/chat/)[NextRtkControlBarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/control-bar-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/clock-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

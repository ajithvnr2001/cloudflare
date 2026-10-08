---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/recording-indicator/
title: RtkRecordingIndicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:15.742745+00:00
---

# RtkRecordingIndicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/recording-indicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkRecordingIndicator



# RtkRecordingIndicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/recording-indicator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A component which indicates the recording status of a meeting. It does not render anything if no recording is taking place.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the indicator to the meeting state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkRecordingIndicator
        android:id="@+id/rtk_recording_indicator"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val recordingIndicator = findViewById<RtkRecordingIndicator>(R.id.rtk_recording_indicator)
    recordingIndicator.activate(meeting)

[PreviousRtkPollsBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/polls/)[NextRtkSettingsBottomsheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-bottomsheet/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/recording-indicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

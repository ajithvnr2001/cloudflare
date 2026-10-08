---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle/
title: RtkMicToggleButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:14.144279+00:00
---

# RtkMicToggleButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkMicToggleButton



# RtkMicToggleButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A button which toggles the local user's microphone. It automatically listens to self audio events to update its state.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state  
`deactivate` | - | Unbind the button and remove event listeners  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkMicToggleButton
        android:id="@+id/btn_mic_toggle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val micToggleButton = findViewById<RtkMicToggleButton>(R.id.btn_mic_toggle)
    micToggleButton.activate(meeting)

[PreviousRtkMeetingTitleView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-title-view/)[NextRtkMoreToggleButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

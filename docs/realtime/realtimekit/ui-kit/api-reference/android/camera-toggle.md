---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/camera-toggle/
title: RtkCameraToggleButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:10.480369+00:00
---

# RtkCameraToggleButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/camera-toggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkCameraToggleButton



# RtkCameraToggleButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/camera-toggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A button which toggles the local user's camera. It automatically listens to self video events to update its state.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state  
`deactivate` | - | Unbind the button and remove event listeners  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkCameraToggleButton
        android:id="@+id/btn_camera_toggle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val cameraToggleButton = findViewById<RtkCameraToggleButton>(R.id.btn_camera_toggle)
    cameraToggleButton.activate(meeting)

[PreviousRtkButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/button/)[NextRtkChatBottomSheet](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/chat/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/camera-toggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

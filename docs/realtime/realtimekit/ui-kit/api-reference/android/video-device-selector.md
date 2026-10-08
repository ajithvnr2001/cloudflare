---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/video-device-selector/
title: RtkVideoDeviceSelector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:16.589789+00:00
---

# RtkVideoDeviceSelector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/video-device-selector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkVideoDeviceSelector



# RtkVideoDeviceSelector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/video-device-selector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesMethodsUsage Examples Basic Usage With Methods

A video device selector component which can be used to select video devices.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`rtk_ds_label` | `string` | ❌ | `Video` | Custom label text  
  
## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the selector to the meeting state  
`disableLabel` | - | Disable the label text above the dropdown  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkVideoDeviceSelector
        android:id="@+id/videoSelector"
        app:rtk_ds_label="Camera"
        android:layout_width="0dp"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val videoSelector = findViewById<RtkVideoDeviceSelector>(R.id.videoSelector)
    videoSelector.activate(meeting)

[PreviousRtkTabSyncToggleButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/tab-sync-toggle-button/)[NextRtkVideoPeer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/video-peer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/video-device-selector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

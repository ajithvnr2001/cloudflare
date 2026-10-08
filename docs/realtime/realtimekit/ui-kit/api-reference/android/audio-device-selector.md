---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/audio-device-selector/
title: RtkAudioDeviceSelector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:12.105904+00:00
---

# RtkAudioDeviceSelector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/audio-device-selector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkAudioDeviceSelector



# RtkAudioDeviceSelector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/audio-device-selector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesMethodsUsage Examples Basic Usage With Methods

An audio device selector component which can be used to select audio devices.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`rtk_ds_label` | `string` | ❌ | `Audio` | Custom label text  
  
## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the selector to the meeting state  
`disableLabel` | - | Disable the label text above the dropdown  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkAudioDeviceSelector
        android:id="@+id/audioSelector"
        app:rtk_ds_label="Audio"
        android:layout_width="0dp"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val audioSelector = findViewById<RtkAudioDeviceSelector>(R.id.audioSelector)
    audioSelector.activate(meeting)

[PreviousBreakout Rooms](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/)[NextRtkAvatarView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/avatar-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/audio-device-selector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

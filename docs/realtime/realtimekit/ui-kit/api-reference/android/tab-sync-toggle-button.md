---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/tab-sync-toggle-button/
title: RtkTabSyncToggleButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:16.490035+00:00
---

# RtkTabSyncToggleButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/tab-sync-toggle-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkTabSyncToggleButton



# RtkTabSyncToggleButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/tab-sync-toggle-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A toggle button for syncing plugin tabs.

## Methods

Method | Parameters | Description  
---|---|---  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkTabSyncToggleButton
        android:id="@+id/rtk_tab_sync"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val tabSyncButton = findViewById<RtkTabSyncToggleButton>(R.id.rtk_tab_sync)
    tabSyncButton.isActivated = true

[PreviousRtkSetupFragment](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/setup-screen/)[NextRtkVideoDeviceSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/video-device-selector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/tab-sync-toggle-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

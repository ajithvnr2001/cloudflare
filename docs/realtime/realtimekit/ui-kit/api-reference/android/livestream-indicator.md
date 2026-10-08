---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator/
title: RtkLivestreamIndicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:13.490061+00:00
---

# RtkLivestreamIndicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkLivestreamIndicator



# RtkLivestreamIndicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A visual indicator that shows when a livestream is active.

## Methods

Method | Parameters | Description  
---|---|---  
`refresh` | `meeting: RealtimeKitClient` | Update the indicator based on the current livestream state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkLivestreamIndicator
        android:id="@+id/rtk_livestream_indicator"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val indicator = findViewById<RtkLivestreamIndicator>(R.id.rtk_livestream_indicator)
    indicator.refresh(meeting)

[PreviousRtkLivestreamHeaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-header-view/)[NextRtkLivestreamToggleButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

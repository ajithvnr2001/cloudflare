---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-header-view/
title: RtkLivestreamHeaderView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:13.070438+00:00
---

# RtkLivestreamHeaderView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-header-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkLivestreamHeaderView



# RtkLivestreamHeaderView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-header-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A pre-built header for livestream meetings. Contains the livestream indicator, viewer count, clock, and meeting title.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the header to the meeting state  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkLivestreamHeaderView
        android:id="@+id/rtk_livestream_header"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val header = findViewById<RtkLivestreamHeaderView>(R.id.rtk_livestream_header)
    header.activate(meeting)

[PreviousRtkLivestreamControlBarView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-control-bar/)[NextRtkLivestreamIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/livestream-header-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

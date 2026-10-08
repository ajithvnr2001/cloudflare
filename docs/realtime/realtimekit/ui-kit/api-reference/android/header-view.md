---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/header-view/
title: RtkHeaderView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:12.806683+00:00
---

# RtkHeaderView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/header-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkHeaderView



# RtkHeaderView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/header-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A base header view component. Provides background styling and design token support.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the header to the meeting state  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.headers.RtkHeaderView
        android:id="@+id/rtk_header"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

### With Methods
    
    
    val header = findViewById<RtkHeaderView>(R.id.rtk_header)
    header.activate(meeting)

[PreviousRtkGridView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-view/)[NextRtkJoinButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/header-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

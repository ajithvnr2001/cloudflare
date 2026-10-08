---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-view/
title: RtkGridView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:12.211939+00:00
---

# RtkGridView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Android
  5. /RtkGridView



# RtkGridView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

The main grid component which handles the participant grid layout, pagination, and focus modes.

## Methods

Method | Parameters | Description  
---|---|---  
`activate` | `meeting: RealtimeKitClient` | Bind the grid to the meeting state  
`refresh` | `force: Boolean` | Force a refresh of the grid layout and participants  
`enableFocusMode` | - | Enable focus mode, which hides the horizontal peer strip and full-screen toggle to keep attention on the primary speaker or shared content  
`applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.grid.RtkGridView
        android:id="@+id/rtk_grid"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

### With Methods
    
    
    val grid = findViewById<RtkGridView>(R.id.rtk_grid)
    grid.activate(meeting)

[PreviousRtkGridPaginatorView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/grid-paginator/)[NextRtkHeaderView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/header-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/android/grid-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/grid-view/
title: GridView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:56.417949+00:00
---

# GridView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/grid-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /GridView



# GridView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/grid-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage Update layout

A generic grid layout view that arranges child views in a responsive grid. Supports both portrait and landscape orientations with configurable maximum item count.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`maxItems` | `UInt` | ❌ | `9` | Maximum number of items the grid can display  
`showingCurrently` | `UInt` | ✅ | - | Number of items currently visible in the grid  
`getChildView` | `@escaping () -> CellContainerView` | ✅ | - | Factory closure that creates a new child view for each grid cell  
  
## Methods

Method | Return Type | Description  
---|---|---  
`settingFrames(visibleItemCount:animation:completion:)` | `Void` | Lays out child views in portrait orientation with optional animation  
`settingFramesForLandScape(visibleItemCount:animation:completion:)` | `Void` | Lays out child views in landscape orientation with optional animation  
`childView(index:)` | `CellContainerView?` | Returns the child view at the specified index  
`prepareForReuse(childView:)` | `Void` | Prepares a child view for reuse  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let gridView = GridView(
        maxItems: 6,
        showingCurrently: 4,
        getChildView: {
            return CellContainerView()
        }
    )
    view.addSubview(gridView)

### Update layout
    
    
    import RealtimeKitUI
    
    let gridView = GridView(
        maxItems: 9,
        showingCurrently: 3,
        getChildView: {
            return CellContainerView()
        }
    )
    view.addSubview(gridView)
    
    // Update layout with animation
    gridView.settingFrames(
        visibleItemCount: 4,
        animation: true,
        completion: {
            print("Layout updated")
        }
    )

[PreviousDesignLibrary](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/)[NextMeetingViewController](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/meeting-view-controller/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/grid-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/
title: RtkMeetingHeaderView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:58.642744+00:00
---

# RtkMeetingHeaderView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkMeetingHeaderView



# RtkMeetingHeaderView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage With page navigation

Meeting header view that displays the meeting title, participant count, elapsed time clock, recording indicator, and camera switch button.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance for the active meeting  
  
## Methods

Method | Return Type | Description  
---|---|---  
`setContentTop(offset: CGFloat)` | `Void` | Sets the top content offset for the header layout  
`refreshNextPreviousButtonState()` | `Void` | Refreshes the enabled state of next and previous page buttons  
`setClicks(nextButton:previousButton:)` | `Void` | Assigns tap handlers for the next and previous page buttons  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let headerView = RtkMeetingHeaderView(meeting: rtkClient)
    view.addSubview(headerView)

### With page navigation
    
    
    import RealtimeKitUI
    
    let headerView = RtkMeetingHeaderView(meeting: rtkClient)
    headerView.setClicks(
        nextButton: { print("Next page") },
        previousButton: { print("Previous page") }
    )
    headerView.refreshNextPreviousButtonState()
    view.addSubview(headerView)

[PreviousRtkMeetingControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-control-bar/)[NextRtkMeetingNameTag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-name-tag/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

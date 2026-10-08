---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-tile-view/
title: RtkParticipantTileView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.857618+00:00
---

# RtkParticipantTileView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-tile-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkParticipantTileView



# RtkParticipantTileView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-tile-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersPropertiesMethodsUsage Examples Basic Usage Local user tile with screen share

A complete participant tile view that displays video, avatar, name tag, and pin indicator. Combines `RtkVideoView`, `RtkAvatarView`, and `RtkMeetingNameTag` into a single composable view.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`rtkClient` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`participant` | `RtkMeetingParticipant` | ✅ | - | The participant to display  
`isForLocalUser` | `Bool` | ✅ | - | Whether this tile represents the local user  
`showScreenShareVideoView` | `Bool` | ❌ | `false` | Whether to show the screen share video instead of camera video  
  
## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`nameTag` | `RtkMeetingNameTag!` | - | - | The name tag view displayed on the tile  
`viewModel` | `VideoPeerViewModel` | - | - | The view model managing participant data (read-only)  
  
## Methods

Method | Return Type | Description  
---|---|---  
`pinView(show: Bool)` | `Void` | Shows or hides the pin indicator on the tile  
`refreshVideo()` | `Void` | Refreshes the video renderer for the participant  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let tileView = RtkParticipantTileView(
        rtkClient: rtkClient,
        participant: participant,
        isForLocalUser: false
    )
    view.addSubview(tileView)

### Local user tile with screen share
    
    
    import RealtimeKitUI
    
    let localTile = RtkParticipantTileView(
        rtkClient: rtkClient,
        participant: localParticipant,
        isForLocalUser: true,
        showScreenShareVideoView: true
    )
    view.addSubview(localTile)

[PreviousRtkParticipantCountView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view/)[NextRtkPluginScreenShareTabButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugin-screen-share-tab-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-tile-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view/
title: RtkParticipantCountView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.966075+00:00
---

# RtkParticipantCountView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkParticipantCountView



# RtkParticipantCountView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With custom appearance

A label that displays the current participant count. Automatically updates when participants join or leave the meeting.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance for the active meeting  
`appearance` | `RtkTextAppearance` | ❌ | `AppTheme.shared.participantCountAppearance` | Text appearance configuration for font and color  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let countView = RtkParticipantCountView(meeting: rtkClient)
    view.addSubview(countView)

### With custom appearance
    
    
    import RealtimeKitUI
    
    let appearance = RtkTextAppearance(
        font: UIFont.systemFont(ofSize: 14, weight: .medium),
        textColor: .lightGray
    )
    let countView = RtkParticipantCountView(
        meeting: rtkClient,
        appearance: appearance
    )
    view.addSubview(countView)

[PreviousRtkNotificationConfig](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/)[NextRtkParticipantTileView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-tile-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

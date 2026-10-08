---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-join-button/
title: RtkJoinButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:58.017745+00:00
---

# RtkJoinButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-join-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkJoinButton



# RtkJoinButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-join-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With tap handler

A pre-configured button that joins the meeting. Validates the participant name before joining.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance  
`onClick` | `((RtkJoinButton, Bool) -> Void)?` | ❌ | `nil` | Closure called when the button is tapped. The `Bool` parameter indicates whether the join was successful.  
`appearance` | `RtkButtonAppearance` | ❌ | - | Appearance configuration for the button  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let joinButton = RtkJoinButton(meeting: rtkClient)
    view.addSubview(joinButton)

### With tap handler
    
    
    import RealtimeKitUI
    
    let joinButton = RtkJoinButton(
        meeting: rtkClient,
        onClick: { button, success in
            if success {
                print("Joined meeting")
            } else {
                print("Join failed")
            }
        }
    )
    view.addSubview(joinButton)

[PreviousRtkImage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/)[NextRtkLabel](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-label/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-join-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

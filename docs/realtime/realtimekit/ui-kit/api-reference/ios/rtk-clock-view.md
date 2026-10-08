---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-clock-view/
title: RtkClockView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:57.124527+00:00
---

# RtkClockView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-clock-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkClockView



# RtkClockView

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-clock-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With custom appearance

A label that displays the elapsed meeting time in `HH:MM:SS` format. Updates every second while the meeting is active.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance for the active meeting  
`appearance` | `RtkTextAppearance` | ❌ | `AppTheme.shared.clockViewAppearance` | Text appearance configuration for font and color  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let clockView = RtkClockView(meeting: rtkClient)
    view.addSubview(clockView)

### With custom appearance
    
    
    import RealtimeKitUI
    
    let appearance = RtkTextAppearance(
        font: UIFont.monospacedDigitSystemFont(ofSize: 14, weight: .regular),
        textColor: .white
    )
    let clockView = RtkClockView(
        meeting: rtkClient,
        appearance: appearance
    )
    view.addSubview(clockView)

[PreviousRtkButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/)[NextRtkControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-clock-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

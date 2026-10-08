---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/
title: RtkButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:57.332122+00:00
---

# RtkButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkButton



# RtkButton

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With custom style

A versatile button that follows the RTK Design System. Supports multiple styles, states, and sizes.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`style` | `Style` | ❌ | `.solid` | The button style (solid, line, icon-left, and others)  
`rtkButtonState` | `States` | ❌ | `.active` | The initial state of the button  
`size` | `Size` | ❌ | `.large` | The size of the button  
`appearance` | `RtkButtonAppearance` | ❌ | - | Appearance configuration for colors and fonts  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let button = RtkButton()
    button.setTitle("Join", for: .normal)
    view.addSubview(button)

### With custom style
    
    
    import RealtimeKitUI
    
    let button = RtkButton(
        style: .line,
        rtkButtonState: .active,
        size: .large
    )
    button.setTitle("Cancel", for: .normal)
    view.addSubview(button)

[PreviousRtkAvatarView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view/)[NextRtkClockView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-clock-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

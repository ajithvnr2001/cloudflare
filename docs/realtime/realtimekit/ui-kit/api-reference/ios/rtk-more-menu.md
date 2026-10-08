---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/
title: RtkMoreMenu \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.359614+00:00
---

# RtkMoreMenu · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkMoreMenu



# RtkMoreMenu

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersMethodsUsage Examples Basic Usage With title

A bottom sheet menu that displays meeting action options such as chat, polls, and participant list.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`title` | `String?` | ❌ | `nil` | Optional title displayed at the top of the menu  
`features` | `[MenuType]` | ✅ | - | Array of menu items to display  
`onSelect` | `@escaping (MenuType) -> Void` | ✅ | - | Closure called when the user selects a menu item  
  
## Methods

Method | Return Type | Description  
---|---|---  
`show(on:)` | `Void` | Presents the menu as a bottom sheet on the specified `UIView`  
`reload(title:features:)` | `Void` | Reloads the menu with a new title and set of features  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let menu = RtkMoreMenu(
        features: [.chat, .polls, .participants],
        onSelect: { menuType in
            print("Selected: \(menuType)")
        }
    )
    menu.show(on: self.view)

### With title
    
    
    import RealtimeKitUI
    
    let menu = RtkMoreMenu(
        title: "More Options",
        features: [.chat, .polls, .participants],
        onSelect: { menuType in
            switch menuType {
            case .chat:
                print("Open chat")
            case .polls:
                print("Open polls")
            case .participants:
                print("Open participants")
            default:
                break
            }
        }
    )
    menu.show(on: self.view)

[PreviousRtkMoreButtonControlBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar/)[NextRtkNameTag](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

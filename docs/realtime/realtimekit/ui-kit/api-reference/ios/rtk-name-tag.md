---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag/
title: RtkNameTag \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:59.153518+00:00
---

# RtkNameTag · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /iOS
  5. /RtkNameTag



# RtkNameTag

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With subtitle

Base name tag view with an icon, title, and optional subtitle. Serves as the foundation for `RtkMeetingNameTag`.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`image` | `RtkImage` | ✅ | - | The icon image displayed in the name tag  
`appearance` | `RtkNameTagAppearance` | ❌ | - | Appearance configuration for the name tag  
`title` | `String` | ✅ | - | The primary text displayed in the name tag  
`subtitle` | `String` | ❌ | `""` | Optional secondary text displayed below the title  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let nameTag = RtkNameTag(
        image: RtkImage(image: UIImage(systemName: "mic")),
        title: "John Doe"
    )
    view.addSubview(nameTag)

### With subtitle
    
    
    import RealtimeKitUI
    
    let nameTag = RtkNameTag(
        image: RtkImage(image: UIImage(systemName: "mic")),
        title: "John Doe",
        subtitle: "Host"
    )
    view.addSubview(nameTag)

[PreviousRtkMoreMenu](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/)[NextRtkNavigationBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

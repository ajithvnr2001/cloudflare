---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-list-view/
title: rtk-message-list-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:27.250729+00:00
---

# rtk-message-list-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-list-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-message-list-view



# rtk-message-list-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-list-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders list of messages.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`estimateItemSize` | `number` | ✅ | - | Estimated height of an item  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`loadMore` | `(lastMessage: Message)` | ✅ | - | Function to load more messages. Messages returned from this will be prepended  
`messages` | `Message[]` | ✅ | - | Messages to render  
`renderer` | `(message: Message, index: number)` | ✅ | - | Render function of the message  
`visibleItemsCount` | `number` | ✅ | - | Maximum visible messages  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-message-list-view></rtk-message-list-view>

### With Properties
    
    
    <!-- component.html -->
    <rtk-message-list-view
     estimateItemSize="42"
     [loadMore]="(lastmessage: message)"
     [messages]="[]">
    </rtk-message-list-view>

[Previousrtk-menu-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list/)[Nextrtk-message-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-list-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/
title: rtk-chat-selector-ui \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:20.274724+00:00
---

# rtk-chat-selector-ui · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-chat-selector-ui



# rtk-chat-selector-ui

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`groups` | `ChatGroup[]` | ✅ | - | Participants  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`selectedGroupId` | `string` | ✅ | - | Selected participant  
`selfUserId` | `string` | ✅ | - | Self User ID  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`unreadCounts` | `Record<string, number>` | ✅ | - | Unread counts  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-chat-selector-ui></rtk-chat-selector-ui>

### With Properties
    
    
    <!-- component.html -->
    <rtk-chat-selector-ui
     [groups]="[]"
     selectedGroupId="example"
     selfUserId="example">
    </rtk-chat-selector-ui>

[Previousrtk-chat-selector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector/)[Nextrtk-chat-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

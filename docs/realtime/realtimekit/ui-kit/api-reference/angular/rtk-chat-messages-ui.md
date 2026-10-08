---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui/
title: rtk-chat-messages-ui \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:20.060008+00:00
---

# rtk-chat-messages-ui · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-chat-messages-ui



# rtk-chat-messages-ui

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated Use `rtk-chat-messages-ui-paginated` instead.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`canPinMessages` | `boolean` | ✅ | - | Can current user pin/unpin messages  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`messages` | `Chat[]` | ✅ | - | Chat Messages  
`selectedGroup` | `string` | ✅ | - | Selected group key  
`selfUserId` | `string` | ✅ | - | User ID of self user  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-chat-messages-ui></rtk-chat-messages-ui>

### With Properties
    
    
    <!-- component.html -->
    <rtk-chat-messages-ui
     [canPinMessages]="true"
     [messages]="[]"
     selectedGroup="example">
    </rtk-chat-messages-ui>

[Previousrtk-chat-message](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-message/)[Nextrtk-chat-messages-ui-paginated](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui-paginated/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

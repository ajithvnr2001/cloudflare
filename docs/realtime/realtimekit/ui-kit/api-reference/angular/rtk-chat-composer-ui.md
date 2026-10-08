---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/
title: rtk-chat-composer-ui \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:19.480511+00:00
---

# rtk-chat-composer-ui · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-chat-composer-ui



# rtk-chat-composer-ui

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated . This component is deprecated, please use rtk-chat-composer-view instead.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages  
`canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`prefill` | `{ suggestedReplies?: string[]; editMessage?: TextMessage; replyMessage?: TextMessage; }` | ❌ | - | prefill the composer  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-chat-composer-ui></rtk-chat-composer-ui>

### With Properties
    
    
    <!-- component.html -->
    <rtk-chat-composer-ui
     [canSendFiles]="true"
     [canSendTextMessage]="true"
     size="md">
    </rtk-chat-composer-ui>

[Previousrtk-chat](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat/)[Nextrtk-chat-composer-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

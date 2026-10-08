---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-view/
title: rtk-chat-composer-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:20.542506+00:00
---

# rtk-chat-composer-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-chat-composer-view



# rtk-chat-composer-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a chat composer

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages  
`canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`inputTextPlaceholder` | `string` | ✅ | - | Placeholder for text input  
`isEditing` | `boolean` | ✅ | - | Sets composer to edit mode  
`maxLength` | `number` | ✅ | - | Max length for text input  
`message` | `string` | ✅ | - | Message to be pre-populated  
`quotedMessage` | `string` | ✅ | - | Quote message to be displayed  
`rateLimits` | `{ period: number; maxInvocations: number; }` | ✅ | - | Rate limits  
`storageKey` | `string` | ✅ | - | Key for storing message in localStorage  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-chat-composer-view></rtk-chat-composer-view>

### With Properties
    
    
    <!-- component.html -->
    <rtk-chat-composer-view
     [canSendFiles]="true"
     [canSendTextMessage]="true"
     inputTextPlaceholder="example">
    </rtk-chat-composer-view>

[Previousrtk-chat-composer-ui](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/)[Nextrtk-chat-header](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

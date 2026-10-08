---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-message/
title: rtk-chat-message \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:19.818186+00:00
---

# rtk-chat-message · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-message/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-chat-message



# rtk-chat-message

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-message/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-chat-message` is deprecated and will be removed soon. Use `rtk-message-view` instead.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`alignRight` | `boolean` | ✅ | - | aligns message to right  
`canDelete` | `boolean` | ✅ | - | can delete message  
`canEdit` | `boolean` | ✅ | - | can edit message  
`canPin` | `boolean` | ✅ | - | can pin this message  
`canReply` | `boolean` | ✅ | - | can quote reply this message  
`child` | `HTMLElement` | ✅ | - | Child  
`disableControls` | `boolean` | ✅ | - | disables controls  
`hideAvatar` | `boolean` | ✅ | - | hides avatar  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`isContinued` | `boolean` | ✅ | - | is continued  
`isSelf` | `boolean` | ✅ | - | if sender is self  
`isUnread` | `boolean` | ✅ | - | is unread  
`leftAlign` | `boolean` | ✅ | - | Whether to left align the chat bubbles  
`message` | `Message` | ✅ | - | message item  
`senderDisplayPicture` | `string` | ✅ | - | sender display picture url  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-chat-message></rtk-chat-message>

### With Properties
    
    
    <!-- component.html -->
    <rtk-chat-message
     [alignRight]="true"
     [canDelete]="true"
     [canEdit]="true">
    </rtk-chat-message>

[Previousrtk-chat-header](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-header/)[Nextrtk-chat-messages-ui](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-messages-ui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-message.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/
title: RtkChatMessage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:47.046740+00:00
---

# RtkChatMessage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatMessage



# RtkChatMessage

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkChatMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatMessage />;
    }

### With Properties
    
    
    import { RtkChatMessage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatMessage
          alignRight={true}
          canDelete={true}
          canEdit={true}
        />
      );
    }

[PreviousRtkChatHeader](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatheader/)[NextRtkChatMessagesUi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatMessage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

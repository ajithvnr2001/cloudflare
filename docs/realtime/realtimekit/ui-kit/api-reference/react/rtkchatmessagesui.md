---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/
title: RtkChatMessagesUi \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:47.109672+00:00
---

# RtkChatMessagesUi · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatMessagesUi



# RtkChatMessagesUi

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkChatMessagesUi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatMessagesUi />;
    }

### With Properties
    
    
    import { RtkChatMessagesUi } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatMessagesUi
          canPinMessages={true}
          messages={[]}
          selectedGroup="example"
        />
      );
    }

[PreviousRtkChatMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessage/)[NextRtkChatMessagesUiPaginated](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatMessagesUi.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

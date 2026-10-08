---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/
title: RtkChatMessagesUiPaginated \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:15.438218+00:00
---

# RtkChatMessagesUiPaginated · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatMessagesUiPaginated



# RtkChatMessagesUiPaginated

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`privateChatRecipient` | `Participant | null` | ✅ | - | Selected recipient for private chat; when unset, messages are loaded for public chat (Everyone).  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChatMessagesUiPaginated } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatMessagesUiPaginated />;
    }

### With Properties
    
    
    import { RtkChatMessagesUiPaginated } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatMessagesUiPaginated
          meeting={meeting}
          privateChatRecipient={participant | null}
          size="md"
        />
      );
    }

[PreviousRtkChatMessagesUi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesui/)[NextRtkChatSearchResults](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatMessagesUiPaginated.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

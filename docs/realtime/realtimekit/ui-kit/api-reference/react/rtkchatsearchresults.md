---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/
title: RtkChatSearchResults \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:46.815524+00:00
---

# RtkChatSearchResults · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatsearchresults/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatSearchResults



# RtkChatSearchResults

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-chat-search-results` is deprecated and will be removed soon. Use `rtk-chat-messages-ui-paginated` instead. -

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`channelId` | `string` | ✅ | - | Channel id  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`query` | `string` | ✅ | - | Search query  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChatSearchResults } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatSearchResults />;
    }

### With Properties
    
    
    import { RtkChatSearchResults } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatSearchResults
          channelId="example"
          meeting={meeting}
          query="example"
        />
      );
    }

[PreviousRtkChatMessagesUiPaginated](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatmessagesuipaginated/)[NextRtkChatSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatSearchResults.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

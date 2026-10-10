---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/
title: RtkMessageListView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:42.590240+00:00
---

# RtkMessageListView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMessageListView



# RtkMessageListView

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    import { RtkMessageListView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMessageListView />;
    }

### With Properties
    
    
    import { RtkMessageListView } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMessageListView
          estimateItemSize={42}
          loadMore={(lastmessage: message)}
          messages={[]}
        />
      );
    }

[PreviousRtkMenuList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/)[NextRtkMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMessageListView.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

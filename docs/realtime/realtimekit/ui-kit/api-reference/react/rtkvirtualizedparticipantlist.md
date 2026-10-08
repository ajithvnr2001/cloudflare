---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkvirtualizedparticipantlist/
title: RtkVirtualizedParticipantList \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:30.460553+00:00
---

# RtkVirtualizedParticipantList · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkvirtualizedparticipantlist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkVirtualizedParticipantList



# RtkVirtualizedParticipantList

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkvirtualizedparticipantlist/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`bufferedItemsCount` | `number` | ✅ | - | Buffer items to render before and after the visible area  
`emptyListElement` | `HTMLElement` | ✅ | - | Element to render if list is empty  
`itemHeight` | `number` | ✅ | - | Height of each item in pixels (assumed fixed)  
`items` | `Peer1[]` | ✅ | - | Items to be virtualized  
`renderItem` | `(item: Peer1, index: number)` | ✅ | - | Function to render each item  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkVirtualizedParticipantList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkVirtualizedParticipantList />;
    }

### With Properties
    
    
    import { RtkVirtualizedParticipantList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkVirtualizedParticipantList
          bufferedItemsCount={42}
          emptyListElement={htmlelement}
          itemHeight={42}
        />
      );
    }

[PreviousRtkViewerCount](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/)[NextRtkWaitingScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkVirtualizedParticipantList.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

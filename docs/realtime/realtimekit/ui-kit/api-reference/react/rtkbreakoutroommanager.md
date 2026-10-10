---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/
title: RtkBreakoutRoomManager \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:48.352284+00:00
---

# RtkBreakoutRoomManager · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkBreakoutRoomManager



# RtkBreakoutRoomManager

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`allowDelete` | `boolean` | ✅ | - | allow room delete  
`assigningParticipants` | `boolean` | ✅ | - | Enable updating participants  
`defaultExpanded` | `boolean` | ✅ | - | display expanded card by default  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isDragMode` | `boolean` | ✅ | - | Drag mode  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`mode` | `'edit' | 'create'` | ✅ | - | Mode in which selector is used  
`room` | `DraftMeeting` | ✅ | - | Connected Room Config Object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkBreakoutRoomManager } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkBreakoutRoomManager />;
    }

### With Properties
    
    
    import { RtkBreakoutRoomManager } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkBreakoutRoomManager
          allowDelete={true}
          assigningParticipants={true}
          defaultExpanded={true}
        />
      );
    }

[PreviousRtkAvatar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkavatar/)[NextRtkBreakoutRoomParticipants](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkBreakoutRoomManager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

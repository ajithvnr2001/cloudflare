---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipanttile/
title: RtkParticipantTile \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:40.055377+00:00
---

# RtkParticipantTile · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipanttile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantTile



# RtkParticipantTile

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which plays a participants video and allows for placement of components like `rtk-name-tag`, `rtk-audio-visualizer` or any other component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isPreview` | `boolean` | ✅ | - | Whether tile is used for preview  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`nameTagPosition` | `| 'bottom-left' | 'bottom-right' | 'bottom-center' | 'top-left' | 'top-right' | 'top-center'` | ✅ | - | Position of name tag  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'gradient'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantTile } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantTile />;
    }

### With Properties
    
    
    import { RtkParticipantTile } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantTile
          isPreview={true}
          meeting={meeting}
          nameTagPosition={| 'bottom-left'
        | 'bottom-right'
        | 'bottom-center'
        | 'top-left'
        | 'top-right'
        | 'top-center'}
        />
      );
    }

[PreviousRtkParticipantsWaitingList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantswaitinglist/)[NextRtkPermissionsMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpermissionsmessage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipantTile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

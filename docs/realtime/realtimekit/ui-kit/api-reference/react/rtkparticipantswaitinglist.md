---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantswaitinglist/
title: RtkParticipantsWaitingList \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:25.498648+00:00
---

# RtkParticipantsWaitingList · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantswaitinglist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantsWaitingList



# RtkParticipantsWaitingList

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantswaitinglist/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantsWaitingList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantsWaitingList />;
    }

### With Properties
    
    
    import { RtkParticipantsWaitingList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantsWaitingList
          meeting={meeting}
          size="md"
          view={participantsviewmode}
        />
      );
    }

[PreviousRtkParticipantsViewerList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/)[NextRtkParticipantTile](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipanttile/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipantsWaitingList.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

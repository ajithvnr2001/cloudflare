---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/
title: RtkParticipantsViewerList \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:40.812355+00:00
---

# RtkParticipantsViewerList · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantsViewerList



# RtkParticipantsViewerList

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`hideHeader` | `boolean` | ✅ | - | Hide Viewer Count Header  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`search` | `string` | ✅ | - | Search  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantsViewerList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantsViewerList />;
    }

### With Properties
    
    
    import { RtkParticipantsViewerList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantsViewerList
          hideHeader={true}
          meeting={meeting}
          search="example"
        />
      );
    }

[PreviousRtkParticipantsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/)[NextRtkParticipantsWaitingList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantswaitinglist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipantsViewerList.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

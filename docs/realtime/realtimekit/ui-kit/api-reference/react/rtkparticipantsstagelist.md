---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagelist/
title: RtkParticipantsStageList \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:40.746579+00:00
---

# RtkParticipantsStageList · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagelist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantsStageList



# RtkParticipantsStageList

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`hideHeader` | `boolean` | ✅ | - | Hide Stage Participants Count Header  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`search` | `string` | ✅ | - | Search  
`size` | `Size` | ✅ | - | Size  
`states` | `States1` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantsStageList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantsStageList />;
    }

### With Properties
    
    
    import { RtkParticipantsStageList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantsStageList
          hideHeader={true}
          meeting={meeting}
          search="example"
        />
      );
    }

[PreviousRtkParticipantSetup](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsetup/)[NextRtkParticipantsStageQueue](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagequeue/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipantsStageList.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/
title: RtkParticipantsToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:40.579970+00:00
---

# RtkParticipantsToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantstoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantsToggle



# RtkParticipantsToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visibility of participants. When clicked it emits a `rtkStateUpdate` event with the data:
    
    
    { activeSidebar: boolean; sidebar: 'participants' }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantsToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantsToggle />;
    }

### With Properties
    
    
    import { RtkParticipantsToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantsToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkParticipantsStageQueue](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagequeue/)[NextRtkParticipantsViewerList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsviewerlist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipantsToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

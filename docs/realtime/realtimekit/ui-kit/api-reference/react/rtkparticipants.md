---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/
title: RtkParticipants \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:41.222871+00:00
---

# RtkParticipants · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipants



# RtkParticipants

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`defaultParticipantsTabId` | `ParticipantsTabId` | ✅ | - | Default section  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipants } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipants />;
    }

### With Properties
    
    
    import { RtkParticipants } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipants
          defaultParticipantsTabId={participantstabid}
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkParticipantCount](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantcount/)[NextRtkParticipantsAudio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipants.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

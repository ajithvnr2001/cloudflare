---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipant/
title: RtkParticipant \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:40.892116+00:00
---

# RtkParticipant · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipant/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipant



# RtkParticipant

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A participant entry component used inside `rtk-participants` which shows data like: name, picture and media device status. You can perform privileged actions on the participant too.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`participant` | `Peer` | ✅ | - | Participant object  
`states` | `States1` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`view` | `ParticipantViewMode` | ✅ | - | Show participant summary  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipant } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipant />;
    }

### With Properties
    
    
    import { RtkParticipant } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipant
          meeting={meeting}
          participant={participant}
          view={participantviewmode}
        />
      );
    }

[PreviousRtkPaginatedList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpaginatedlist/)[NextRtkParticipantCount](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantcount/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipant.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

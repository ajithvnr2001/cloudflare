---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/
title: RtkBreakoutRoomParticipants \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:13.538863+00:00
---

# RtkBreakoutRoomParticipants · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkBreakoutRoomParticipants



# RtkBreakoutRoomParticipants

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomparticipants/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`participantIds` | `string[]` | ✅ | - | Participant ids  
`selectedParticipantIds` | `string[]` | ✅ | - | selected participants  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkBreakoutRoomParticipants } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkBreakoutRoomParticipants />;
    }

### With Properties
    
    
    import { RtkBreakoutRoomParticipants } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkBreakoutRoomParticipants
          meeting={meeting}
          participantIds="example"
          selectedParticipantIds="example"
        />
      );
    }

[PreviousRtkBreakoutRoomManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/)[NextRtkBreakoutRoomsManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomsmanager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkBreakoutRoomParticipants.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

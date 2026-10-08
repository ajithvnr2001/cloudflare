---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-participants/
title: rtk-breakout-room-participants \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:37.583331+00:00
---

# rtk-breakout-room-participants · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-participants/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-breakout-room-participants



# rtk-breakout-room-participants

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-participants/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    <rtk-breakout-room-participants></rtk-breakout-room-participants>

### With Properties
    
    
    <rtk-breakout-room-participants
     participantIds="example"
     selectedParticipantIds="example">
    </rtk-breakout-room-participants>
    
    
    <script>
      const el = document.querySelector("rtk-breakout-room-participants");
    
      el.meeting= meeting
      el.participantIds= [];
      el.selectedParticipantIds= [];
    </script>

[Previousrtk-breakout-room-manager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-manager/)[Nextrtk-breakout-rooms-manager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-rooms-manager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-participants.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

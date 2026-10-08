---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/
title: rtk-participant \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:48.739516+00:00
---

# rtk-participant · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-participant



# rtk-participant

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    <rtk-participant></rtk-participant>

### With Properties
    
    
    <rtk-participant>
    </rtk-participant>
    
    
    <script>
      const el = document.querySelector("rtk-participant");
    
      el.meeting= meeting
      el.participant= participant
    </script>

[Previousrtk-paginated-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-paginated-list/)[Nextrtk-participant-count](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-count/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

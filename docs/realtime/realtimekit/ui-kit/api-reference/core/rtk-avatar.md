---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/
title: rtk-avatar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:37.395590+00:00
---

# rtk-avatar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-avatar



# rtk-avatar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Avatar component which renders a participant's image or their initials.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`participant` | `Peer | WaitlistedParticipant | { name: string; picture: string }` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `AvatarVariant` | ✅ | - | Avatar type  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-avatar></rtk-avatar>

### With Properties
    
    
    <rtk-avatar
     participant="example"
     size="md"
     variant="circular">
    </rtk-avatar>
    
    
    <script>
      const el = document.querySelector("rtk-avatar");
    
      el.participant= {};
    </script>

[Previousrtk-audio-visualizer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-visualizer/)[Nextrtk-breakout-room-manager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-manager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-avatar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

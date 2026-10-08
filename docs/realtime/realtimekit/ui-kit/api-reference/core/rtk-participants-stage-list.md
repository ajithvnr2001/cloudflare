---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-list/
title: rtk-participants-stage-list \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:49.301026+00:00
---

# rtk-participants-stage-list · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-participants-stage-list



# rtk-participants-stage-list

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    <rtk-participants-stage-list></rtk-participants-stage-list>

### With Properties
    
    
    <rtk-participants-stage-list
     search="example">
    </rtk-participants-stage-list>
    
    
    <script>
      const el = document.querySelector("rtk-participants-stage-list");
    
      el.hideHeader= true;
      el.meeting= meeting
    </script>

[Previousrtk-participants-audio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-audio/)[Nextrtk-participants-stage-queue](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-queue/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

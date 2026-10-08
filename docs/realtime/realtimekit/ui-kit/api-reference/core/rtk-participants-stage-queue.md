---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-queue/
title: rtk-participants-stage-queue \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:49.099670+00:00
---

# rtk-participants-stage-queue · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-queue/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-participants-stage-queue



# rtk-participants-stage-queue

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-queue/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-participants-stage-queue></rtk-participants-stage-queue>

### With Properties
    
    
    <rtk-participants-stage-queue
     size="md">
    </rtk-participants-stage-queue>
    
    
    <script>
      const el = document.querySelector("rtk-participants-stage-queue");
    
      el.meeting= meeting
    </script>

[Previousrtk-participants-stage-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-list/)[Nextrtk-participants-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-stage-queue.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

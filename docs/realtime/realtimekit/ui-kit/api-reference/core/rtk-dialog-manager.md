---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog-manager/
title: rtk-dialog-manager \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:42.150618+00:00
---

# rtk-dialog-manager · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog-manager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-dialog-manager



# rtk-dialog-manager

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog-manager/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which handles all dialog elements in a component such as:

  * rtk-settings
  * rtk-leave-meeting
  * rtk-permissions-message
  * rtk-image-viewer
  * rtk-breakout-rooms-manager This components depends on the values from `states` object.



## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-dialog-manager></rtk-dialog-manager>

### With Properties
    
    
    <rtk-dialog-manager
     size="md">
    </rtk-dialog-manager>
    
    
    <script>
      const el = document.querySelector("rtk-dialog-manager");
    
      el.meeting= meeting
    </script>

[Previousrtk-dialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog/)[Nextrtk-draft-attachment-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-draft-attachment-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog-manager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-viewer-list/
title: rtk-participants-viewer-list \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:49.807567+00:00
---

# rtk-participants-viewer-list · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-viewer-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-participants-viewer-list



# rtk-participants-viewer-list

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-viewer-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`hideHeader` | `boolean` | ✅ | - | Hide Viewer Count Header  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`search` | `string` | ✅ | - | Search  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
`view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-participants-viewer-list></rtk-participants-viewer-list>

### With Properties
    
    
    <rtk-participants-viewer-list
     search="example">
    </rtk-participants-viewer-list>
    
    
    <script>
      const el = document.querySelector("rtk-participants-viewer-list");
    
      el.hideHeader= true;
      el.meeting= meeting
    </script>

[Previousrtk-participants-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-toggle/)[Nextrtk-participants-waiting-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-waiting-list/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-viewer-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

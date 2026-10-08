---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tab-bar/
title: rtk-tab-bar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:54.412076+00:00
---

# rtk-tab-bar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tab-bar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-tab-bar



# rtk-tab-bar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tab-bar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`activeTab` | `Tab` | ✅ | - | Active tab  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack  
`layout` | `GridLayout1` | ✅ | - | Grid Layout  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`tabs` | `Tab[]` | ✅ | - | Tabs  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-tab-bar></rtk-tab-bar>

### With Properties
    
    
    <rtk-tab-bar>
    </rtk-tab-bar>
    
    
    <script>
      const el = document.querySelector("rtk-tab-bar");
    
      el.meeting= meeting
    </script>

[Previousrtk-switch](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/)[Nextrtk-text-composer-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-composer-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-tab-bar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

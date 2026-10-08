---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar/
title: rtk-sidebar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:33.587408+00:00
---

# rtk-sidebar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-sidebar



# rtk-sidebar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which handles the sidebar and you can customize which sections you want, and which section you want as the default.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`defaultSection` | `RtkSidebarSection` | ✅ | - | Default section  
`enabledSections` | `RtkSidebarTab[]` | ✅ | - | Enabled sections in sidebar  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`view` | `RtkSidebarView` | ✅ | - | View type  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-sidebar></rtk-sidebar>

### With Properties
    
    
    <!-- component.html -->
    <rtk-sidebar
     [defaultSection]="rtksidebarsection"
     [enabledSections]="[]"
     [meeting]="meeting">
    </rtk-sidebar>

[Previousrtk-setup-screen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-setup-screen/)[Nextrtk-sidebar-ui](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar-ui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-sidebar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

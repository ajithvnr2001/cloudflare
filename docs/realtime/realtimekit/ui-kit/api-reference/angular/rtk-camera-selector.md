---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-selector/
title: rtk-camera-selector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:19.014698+00:00
---

# rtk-camera-selector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-selector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-camera-selector



# rtk-camera-selector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-selector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lets to manage your audio devices and audio preferences. Emits `rtkStateUpdate` event with data for muting notification sounds:
    
    
    {
     prefs: {
       muteNotificationSounds: boolean
     }
    }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'full' | 'inline'` | ✅ | - | variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-camera-selector></rtk-camera-selector>

### With Properties
    
    
    <!-- component.html -->
    <rtk-camera-selector
     [meeting]="meeting"
     size="md"
     [variant]="'full' | 'inline'">
    </rtk-camera-selector>

[Previousrtk-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/)[Nextrtk-camera-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-selector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

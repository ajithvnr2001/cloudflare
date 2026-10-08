---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/
title: rtk-recording-indicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:32.095536+00:00
---

# rtk-recording-indicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-recording-indicator



# rtk-recording-indicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which indicates the recording status of a meeting. It will not render anything if no recording is taking place.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-recording-indicator></rtk-recording-indicator>

### With Properties
    
    
    <!-- component.html -->
    <rtk-recording-indicator
     [meeting]="meeting"
     size="md">
    </rtk-recording-indicator>

[Previousrtk-polls-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-polls-toggle/)[Nextrtk-recording-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

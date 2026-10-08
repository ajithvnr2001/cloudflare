---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-spotlight-indicator/
title: rtk-spotlight-indicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:34.285195+00:00
---

# rtk-spotlight-indicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-spotlight-indicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-spotlight-indicator



# rtk-spotlight-indicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-spotlight-indicator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-spotlight-indicator></rtk-spotlight-indicator>

### With Properties
    
    
    <!-- component.html -->
    <rtk-spotlight-indicator
     [meeting]="meeting"
     size="md">
    </rtk-spotlight-indicator>

[Previousrtk-spotlight-grid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-spotlight-grid/)[Nextrtk-stage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-stage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-spotlight-indicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

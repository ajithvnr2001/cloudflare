---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-viewer/
title: rtk-image-viewer \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:24.895322+00:00
---

# rtk-image-viewer · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-viewer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-image-viewer



# rtk-image-viewer

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-viewer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows an image sent via chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`image` | `ImageMessage` | ✅ | - | Image message  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-image-viewer></rtk-image-viewer>

### With Properties
    
    
    <!-- component.html -->
    <rtk-image-viewer
     [image]="imagemessage"
     size="md">
    </rtk-image-viewer>

[Previousrtk-image-message-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message-view/)[Nextrtk-information-tooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-information-tooltip/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-viewer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

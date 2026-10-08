---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/
title: rtk-file-dropzone \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:23.360437+00:00
---

# rtk-file-dropzone · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-file-dropzone



# rtk-file-dropzone

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`hostEl` | `HTMLElement` | ✅ | - | Host element on which drop events to attach  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-file-dropzone></rtk-file-dropzone>

### With Properties
    
    
    <!-- component.html -->
    <rtk-file-dropzone
     [hostEl]="htmlelement">
    </rtk-file-dropzone>

[Previousrtk-ended-screen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ended-screen/)[Nextrtk-file-message](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

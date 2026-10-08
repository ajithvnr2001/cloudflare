---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-viewer-count/
title: rtk-viewer-count \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:36.197556+00:00
---

# rtk-viewer-count · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-viewer-count/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-viewer-count



# rtk-viewer-count

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-viewer-count/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows count of total joined participants in a meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ViewerCountVariant` | ✅ | - | Viewer count variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-viewer-count></rtk-viewer-count>

### With Properties
    
    
    <!-- component.html -->
    <rtk-viewer-count
     [meeting]="meeting"
     variant="primary">
    </rtk-viewer-count>

[Previousrtk-ui-provider](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ui-provider/)[Nextrtk-virtualized-participant-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-virtualized-participant-list/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-viewer-count.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

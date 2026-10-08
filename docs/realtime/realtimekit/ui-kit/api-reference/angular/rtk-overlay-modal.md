---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-overlay-modal/
title: rtk-overlay-modal \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:28.991459+00:00
---

# rtk-overlay-modal · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-overlay-modal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-overlay-modal



# rtk-overlay-modal

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-overlay-modal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A confirmation modal.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-overlay-modal></rtk-overlay-modal>

### With Properties
    
    
    <!-- component.html -->
    <rtk-overlay-modal
     [meeting]="meeting">
    </rtk-overlay-modal>

[Previousrtk-notifications](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-notifications/)[Nextrtk-paginated-list](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-overlay-modal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

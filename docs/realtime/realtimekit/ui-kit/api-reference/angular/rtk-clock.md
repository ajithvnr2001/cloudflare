---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/
title: rtk-clock \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:20.911452+00:00
---

# rtk-clock · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-clock



# rtk-clock

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Shows the time elapsed in a meeting.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-clock></rtk-clock>

### With Properties
    
    
    <!-- component.html -->
    <rtk-clock
     [meeting]="meeting"
     size="md">
    </rtk-clock>

[Previousrtk-chat-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-toggle/)[Nextrtk-confirmation-modal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-confirmation-modal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

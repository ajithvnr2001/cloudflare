---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/
title: rtk-button \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:18.920081+00:00
---

# rtk-button · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-button



# rtk-button

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button that follows RTK Design System.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`disabled` | `boolean` | ✅ | - | Where the button is disabled or not  
`kind` | `ButtonKind` | ✅ | - | Button type  
`reverse` | `boolean` | ✅ | - | Whether to reverse order of children  
`size` | `Size` | ✅ | - | Size  
`type` | `HTMLButtonElement['type']` | ✅ | - | Button type  
`variant` | `ButtonVariant` | ✅ | - | Button variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-button></rtk-button>

### With Properties
    
    
    <!-- component.html -->
    <rtk-button
     [disabled]="true"
     [kind]="buttonkind"
     [reverse]="true">
    </rtk-button>

[Previousrtk-broadcast-message-modal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-broadcast-message-modal/)[Nextrtk-camera-selector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-selector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tooltip/
title: rtk-tooltip \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:35.318904+00:00
---

# rtk-tooltip · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tooltip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-tooltip



# rtk-tooltip

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tooltip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Tooltip component which follows RTK Design System.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`delay` | `number` | ✅ | - | Delay before showing the tooltip  
`disabled` | `boolean` | ✅ | - | Disabled  
`kind` | `TooltipKind` | ✅ | - | Tooltip kind  
`label` | `string` | ✅ | - | Tooltip label  
`open` | `boolean` | ✅ | - | Open  
`placement` | `Placement` | ✅ | - | Placement of menu  
`size` | `Size` | ✅ | - | Size  
`variant` | `TooltipVariant` | ✅ | - | Tooltip variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-tooltip></rtk-tooltip>

### With Properties
    
    
    <!-- component.html -->
    <rtk-tooltip
     delay="42"
     [disabled]="true"
     [kind]="tooltipkind">
    </rtk-tooltip>

[Previousrtk-text-message-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-text-message-view/)[Nextrtk-transcript](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tooltip.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

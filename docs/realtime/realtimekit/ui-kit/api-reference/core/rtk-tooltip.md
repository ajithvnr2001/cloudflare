---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/
title: rtk-tooltip \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:54.882978+00:00
---

# rtk-tooltip · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-tooltip



# rtk-tooltip

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    
    
    <rtk-tooltip></rtk-tooltip>

### With Properties
    
    
    <rtk-tooltip>
    </rtk-tooltip>
    
    
    <script>
      const el = document.querySelector("rtk-tooltip");
    
      el.delay= 42;
      el.disabled= true;
    </script>

[Previousrtk-text-message-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-message-view/)[Nextrtk-transcript](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-transcript/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination/
title: rtk-grid-pagination \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:43.237653+00:00
---

# rtk-grid-pagination · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-grid-pagination



# rtk-grid-pagination

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which allows you to change current page and view mode of active participants list. This is reflected in the `rtk-grid` component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size Prop  
`states` | `States` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `GridPaginationVariants` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-grid-pagination></rtk-grid-pagination>

### With Properties
    
    
    <rtk-grid-pagination
     size="md">
    </rtk-grid-pagination>
    
    
    <script>
      const el = document.querySelector("rtk-grid-pagination");
    
      el.meeting= meeting
    </script>

[Previousrtk-grid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid/)[Nextrtk-header](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-grid-pagination.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

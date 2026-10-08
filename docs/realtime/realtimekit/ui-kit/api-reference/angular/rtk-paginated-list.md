---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list/
title: rtk-paginated-list \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:28.687142+00:00
---

# rtk-paginated-list · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-paginated-list



# rtk-paginated-list

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`autoScroll` | `boolean` | ✅ | - | auto scroll list to bottom  
`createNodes` | `(data: unknown[])` | ✅ | - | Create nodes  
`emptyListLabel` | `string` | ✅ | - | label to show when empty  
`fetchData` | `(timestamp: number, size: number, reversed: boolean)` | ✅ | - | Fetch the data  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`pageSize` | `number` | ✅ | - | Page Size  
`pagesAllowed` | `number` | ✅ | - | Number of pages allowed to be shown  
`rerenderList` | `()` | ✅ | - | Rerender paginated list  
`reset` | `(timestamp?: number)` | ❌ | - | Resets the paginated list to a given timestamp  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-paginated-list></rtk-paginated-list>

### With Properties
    
    
    <!-- component.html -->
    <rtk-paginated-list
     [autoScroll]="true"
     [createNodes]="[]"
     emptyListLabel="example">
    </rtk-paginated-list>

[Previousrtk-overlay-modal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-overlay-modal/)[Nextrtk-participant](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participant/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-paginated-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

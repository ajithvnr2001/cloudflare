---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-virtualized-participant-list/
title: rtk-virtualized-participant-list \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:36.076952+00:00
---

# rtk-virtualized-participant-list · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-virtualized-participant-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-virtualized-participant-list



# rtk-virtualized-participant-list

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-virtualized-participant-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`bufferedItemsCount` | `number` | ✅ | - | Buffer items to render before and after the visible area  
`emptyListElement` | `HTMLElement` | ✅ | - | Element to render if list is empty  
`itemHeight` | `number` | ✅ | - | Height of each item in pixels (assumed fixed)  
`items` | `Peer1[]` | ✅ | - | Items to be virtualized  
`renderItem` | `(item: Peer1, index: number)` | ✅ | - | Function to render each item  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-virtualized-participant-list></rtk-virtualized-participant-list>

### With Properties
    
    
    <!-- component.html -->
    <rtk-virtualized-participant-list
     bufferedItemsCount="42"
     [emptyListElement]="htmlelement"
     itemHeight="42">
    </rtk-virtualized-participant-list>

[Previousrtk-viewer-count](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-viewer-count/)[Nextrtk-waiting-screen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-waiting-screen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-virtualized-participant-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

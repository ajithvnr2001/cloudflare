---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message-view/
title: rtk-file-message-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:23.470489+00:00
---

# rtk-file-message-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-file-message-view



# rtk-file-message-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a file message.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`name` | `string` | ✅ | - | Name of the file  
`size` | `number` | ✅ | - | Size of the file  
`url` | `string` | ✅ | - | Url of the file  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-file-message-view></rtk-file-message-view>

### With Properties
    
    
    <!-- component.html -->
    <rtk-file-message-view
     name="example"
     size="42"
     url="example">
    </rtk-file-message-view>

[Previousrtk-file-message](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message/)[Nextrtk-file-picker-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-picker-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-message-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

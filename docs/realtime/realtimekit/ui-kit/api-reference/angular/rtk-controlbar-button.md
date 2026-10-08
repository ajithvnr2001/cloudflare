---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar-button/
title: rtk-controlbar-button \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:21.419078+00:00
---

# rtk-controlbar-button · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar-button/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-controlbar-button



# rtk-controlbar-button

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar-button/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A skeleton component used for composing custom controlbar buttons.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`brandIcon` | `boolean` | ✅ | - | Whether icon requires brand color  
`disabled` | `boolean` | ✅ | - | Whether button is disabled  
`icon` | `string` | ✅ | - | Icon  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isLoading` | `boolean` | ✅ | - | Loading state Ignores current icon and shows a spinner if true  
`label` | `string` | ✅ | - | Label of button  
`showWarning` | `boolean` | ✅ | - | Whether to show warning icon  
`size` | `Size` | ✅ | - | Size  
`variant` | `ControlBarVariant1` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-controlbar-button></rtk-controlbar-button>

### With Properties
    
    
    <!-- component.html -->
    <rtk-controlbar-button
     [brandIcon]="true"
     [disabled]="true"
     icon="example">
    </rtk-controlbar-button>

[Previousrtk-controlbar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar/)[Nextrtk-counter](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-counter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar-button.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

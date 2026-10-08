---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-draft-attachment-view/
title: rtk-draft-attachment-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:22.835727+00:00
---

# rtk-draft-attachment-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-draft-attachment-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-draft-attachment-view



# rtk-draft-attachment-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-draft-attachment-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders the draft attachment to send

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`attachment` | `{ type: 'image' | 'file'; file: File; }` | ✅ | - | Attachment to display  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-draft-attachment-view></rtk-draft-attachment-view>

### With Properties
    
    
    <!-- component.html -->
    <rtk-draft-attachment-view
     [attachment=]"{}">
    </rtk-draft-attachment-view>

[Previousrtk-dialog-manager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog-manager/)[Nextrtk-emoji-picker](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-emoji-picker/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-draft-attachment-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/
title: rtk-poll \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:31.508131+00:00
---

# rtk-poll · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-poll



# rtk-poll

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A poll component. Shows a poll where a user can vote.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`permissions` | `RTKPermissionsPreset` | ✅ | - | Permissions Object  
`poll` | `Poll` | ✅ | - | Poll  
`self` | `string` | ✅ | - | Self ID  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-poll></rtk-poll>

### With Properties
    
    
    <!-- component.html -->
    <rtk-poll
     [permissions]="rtkpermissionspreset"
     [poll]="poll"
     self="example">
    </rtk-poll>

[Previousrtk-plugins-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-plugins-toggle/)[Nextrtk-poll-form](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll-form/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

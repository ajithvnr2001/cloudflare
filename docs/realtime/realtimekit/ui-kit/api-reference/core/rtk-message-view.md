---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-view/
title: rtk-message-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:46.494471+00:00
---

# rtk-message-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-message-view



# rtk-message-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`actions` | `MessageAction[]` | ✅ | - | List of actions to show in menu  
`authorName` | `string` | ✅ | - | Author display label  
`avatarUrl` | `string` | ✅ | - | Avatar image url  
`hideAuthorName` | `boolean` | ✅ | - | Hides author display label  
`hideAvatar` | `boolean` | ✅ | - | Hides avatar  
`hideMetadata` | `boolean` | ✅ | - | Hides metadata (time)  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`isEdited` | `boolean` | ✅ | - | Has the message been edited  
`isSelf` | `boolean` | ✅ | - | Is the message sent by the current user  
`messageType` | `Message['type']` | ✅ | - | Type of message  
`pinned` | `boolean` | ✅ | - | Is message pinned  
`time` | `Date` | ✅ | - | Time when message was sent  
`variant` | `'plain' | 'bubble'` | ✅ | - | Appearance  
`viewType` | `'incoming' | 'outgoing'` | ✅ | - | Render  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-message-view></rtk-message-view>

### With Properties
    
    
    <rtk-message-view
     authorName="example"
     avatarUrl="example">
    </rtk-message-view>
    
    
    <script>
      const el = document.querySelector("rtk-message-view");
    
      el.actions= [];
    </script>

[Previousrtk-message-list-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-list-view/)[Nextrtk-mic-toggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mic-toggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-message-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

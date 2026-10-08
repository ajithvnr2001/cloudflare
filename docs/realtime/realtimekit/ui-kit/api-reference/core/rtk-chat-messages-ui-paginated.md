---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/
title: rtk-chat-messages-ui-paginated \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:39.359743+00:00
---

# rtk-chat-messages-ui-paginated · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-chat-messages-ui-paginated



# rtk-chat-messages-ui-paginated

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`privateChatRecipient` | `Participant | null` | ✅ | - | Selected recipient for private chat; when unset, messages are loaded for public chat (Everyone).  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-chat-messages-ui-paginated></rtk-chat-messages-ui-paginated>

### With Properties
    
    
    <rtk-chat-messages-ui-paginated
     size="md">
    </rtk-chat-messages-ui-paginated>
    
    
    <script>
      const el = document.querySelector("rtk-chat-messages-ui-paginated");
    
      el.meeting= meeting
    </script>

[Previousrtk-chat-messages-ui](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui/)[Nextrtk-chat-search-results](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/
title: rtk-chat-search-results \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:39.558744+00:00
---

# rtk-chat-search-results · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-chat-search-results



# rtk-chat-search-results

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-chat-search-results` is deprecated and will be removed soon. Use `rtk-chat-messages-ui-paginated` instead. -

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`channelId` | `string` | ✅ | - | Channel id  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`query` | `string` | ✅ | - | Search query  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-chat-search-results></rtk-chat-search-results>

### With Properties
    
    
    <rtk-chat-search-results
     channelId="example"
     query="example">
    </rtk-chat-search-results>
    
    
    <script>
      const el = document.querySelector("rtk-chat-search-results");
    
      el.meeting= meeting
    </script>

[Previousrtk-chat-messages-ui-paginated](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/)[Nextrtk-chat-selector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

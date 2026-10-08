---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message/
title: rtk-file-message \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:42.893600+00:00
---

# rtk-file-message · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-file-message



# rtk-file-message

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-file-message` is deprecated and will be removed soon. Use `rtk-file-message-view` instead. A component which renders a file message from chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user  
`message` | `FileMessage` | ✅ | - | Text message object  
`now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates  
`showBubble` | `boolean` | ✅ | - | show message in bubble  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-file-message></rtk-file-message>

### With Properties
    
    
    <rtk-file-message>
    </rtk-file-message>
    
    
    <script>
      const el = document.querySelector("rtk-file-message");
    
      el.isContinued= true;
    </script>

[Previousrtk-file-dropzone](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-dropzone/)[Nextrtk-file-message-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

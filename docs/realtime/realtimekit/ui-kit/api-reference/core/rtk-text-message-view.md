---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-message-view/
title: rtk-text-message-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:54.527067+00:00
---

# rtk-text-message-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-message-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-text-message-view



# rtk-text-message-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-message-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a text message from chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`isMarkdown` | `boolean` | ✅ | - | Renders text as markdown (default = true)  
`text` | `string` | ✅ | - | Text message  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-text-message-view></rtk-text-message-view>

### With Properties
    
    
    <rtk-text-message-view
     text="example">
    </rtk-text-message-view>
    
    
    <script>
      const el = document.querySelector("rtk-text-message-view");
    
      el.isMarkdown= true;
    </script>

[Previousrtk-text-message](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-message/)[Nextrtk-tooltip](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-text-message-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

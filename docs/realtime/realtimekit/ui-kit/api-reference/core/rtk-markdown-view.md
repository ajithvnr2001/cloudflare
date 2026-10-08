---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-markdown-view/
title: rtk-markdown-view \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:46.070285+00:00
---

# rtk-markdown-view · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-markdown-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-markdown-view



# rtk-markdown-view

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-markdown-view/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`maxLength` | `number` | ✅ | - | max length of text to render as markdown  
`text` | `string` | ✅ | - | raw text to render as markdown  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-markdown-view></rtk-markdown-view>

### With Properties
    
    
    <rtk-markdown-view
     text="example">
    </rtk-markdown-view>
    
    
    <script>
      const el = document.querySelector("rtk-markdown-view");
    
      el.maxLength= 42;
    </script>

[Previousrtk-logo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-logo/)[Nextrtk-meeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-meeting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-markdown-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

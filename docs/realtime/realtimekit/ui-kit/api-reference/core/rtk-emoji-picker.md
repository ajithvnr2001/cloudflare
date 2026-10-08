---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/
title: rtk-emoji-picker \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:42.262194+00:00
---

# rtk-emoji-picker · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Web Components (HTML)
  5. /rtk-emoji-picker



# rtk-emoji-picker

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A very simple emoji picker component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`focusWhenOpened` | `boolean` | ✅ | - | Controls whether or not to focus on mount  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <rtk-emoji-picker></rtk-emoji-picker>

### With Properties
    
    
    <rtk-emoji-picker>
    </rtk-emoji-picker>
    
    
    <script>
      const el = document.querySelector("rtk-emoji-picker");
    
      el.focusWhenOpened= true;
    </script>

[Previousrtk-draft-attachment-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-draft-attachment-view/)[Nextrtk-emoji-picker-button](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker-button/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

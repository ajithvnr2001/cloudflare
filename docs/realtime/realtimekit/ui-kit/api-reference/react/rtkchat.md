---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/
title: RtkChat \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:14.524206+00:00
---

# RtkChat · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChat



# RtkChat

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Fully featured chat component with image & file upload, emoji picker and auto-scroll.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`overrides` | `Overrides` | ❌ | `defaultOverrides` | UI Overrides  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChat } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChat />;
    }

### With Properties
    
    
    import { RtkChat } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChat
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkCaptionToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/)[NextRtkChatComposerUi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatcomposerui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChat.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

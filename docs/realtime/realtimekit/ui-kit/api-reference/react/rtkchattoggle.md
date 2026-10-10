---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchattoggle/
title: RtkChatToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:46.739921+00:00
---

# RtkChatToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchattoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkChatToggle



# RtkChatToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visibility of chat. You need to pass the `meeting` object to it to see the unread messages count badge. When clicked it emits a `rtkStateUpdate` event with the data:
    
    
    { activeSidebar: boolean; sidebar: 'chat' }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChatToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkChatToggle />;
    }

### With Properties
    
    
    import { RtkChatToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkChatToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkChatSelectorUi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselectorui/)[NextRtkClock](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkChatToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

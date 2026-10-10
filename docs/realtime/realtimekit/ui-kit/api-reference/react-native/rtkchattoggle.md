---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchattoggle/
title: RtkChatToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:55.917737+00:00
---

# RtkChatToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchattoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkChatToggle



# RtkChatToggle

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Toggle button to open the chat sidebar panel. Hides if chat permissions are not available.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Icon size  
`states` | `States` | ❌ | - | UI state object  
`variant` | `'button' | 'horizontal'` | ❌ | - | Layout variant  
`iconPack` | `IconPack` | ❌ | - | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkChatToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkChatToggle meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkChatToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkChatToggle meeting={meeting} size="md" variant="button" />;
    }

[PreviousRtkChat](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchat/)[NextRtkClock](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkclock/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkChatToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

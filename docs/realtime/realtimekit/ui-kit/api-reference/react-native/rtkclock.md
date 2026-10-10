---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkclock/
title: RtkClock \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:56.107007+00:00
---

# RtkClock · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkclock/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkClock



# RtkClock

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays elapsed meeting time as a running clock (HH:MM:SS or MM:SS).

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkClock } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkClock meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkClock } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkClock meeting={meeting} iconPack={customIconPack} />;
    }

[PreviousRtkChatToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchattoggle/)[NextRtkControlbar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkClock.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomsmanager/
title: RtkBreakoutRoomsManager \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:01.846255+00:00
---

# RtkBreakoutRoomsManager · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomsmanager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkBreakoutRoomsManager



# RtkBreakoutRoomsManager

Last updated Jul 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomsmanager/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Custom Icon Pack

Full-screen modal for managing breakout rooms. Hosts can create rooms, assign participants, rename rooms, shuffle participants randomly, and start, update, or close a breakout session. Participants without alter permissions see a simplified room-switcher view instead.

The component is visibility-controlled by the `activeBreakoutRoomsManager` field in the UI state. Use `RtkBreakoutRoomsToggle` to open it, or set the state directly.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`states` | `States` | ❌ | - | UI state object  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkBreakoutRoomsManager } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkBreakoutRoomsManager meeting={meeting} />;
    }

### With Custom Icon Pack
    
    
    import { RtkBreakoutRoomsManager } from "@cloudflare/realtimekit-react-native-ui";
    import { myIconPack } from "./icons";
    
    function MyComponent() {
    	return <RtkBreakoutRoomsManager meeting={meeting} iconPack={myIconPack} />;
    }

[PreviousRtkAvatar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkavatar/)[NextRtkBreakoutRoomsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkBreakoutRoomsManager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

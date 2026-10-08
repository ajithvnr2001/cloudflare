---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomstoggle/
title: RtkBreakoutRoomsToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:01.954744+00:00
---

# RtkBreakoutRoomsToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomstoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkBreakoutRoomsToggle



# RtkBreakoutRoomsToggle

Last updated Jul 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomstoggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Size

Control bar button that opens and closes the `RtkBreakoutRoomsManager`. Automatically hides if the local participant has neither `canAlterConnectedMeetings` nor `canSwitchConnectedMeetings` permission.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Icon size  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkBreakoutRoomsToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkBreakoutRoomsToggle meeting={meeting} />;
    }

### With Size
    
    
    import { RtkBreakoutRoomsToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkBreakoutRoomsToggle meeting={meeting} size="md" />;
    }

[PreviousRtkBreakoutRoomsManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbreakoutroomsmanager/)[NextRtkButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkBreakoutRoomsToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

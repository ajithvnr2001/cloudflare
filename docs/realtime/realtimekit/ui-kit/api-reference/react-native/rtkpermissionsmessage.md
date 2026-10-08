---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpermissionsmessage/
title: RtkPermissionsMessage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:08.543932+00:00
---

# RtkPermissionsMessage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpermissionsmessage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkPermissionsMessage



# RtkPermissionsMessage

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpermissionsmessage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays a message when device permissions (camera/microphone) are denied, with options to continue or open system settings.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPermissionsMessage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPermissionsMessage meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkPermissionsMessage } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPermissionsMessage meeting={meeting} iconPack={customIconPack} />;
    }

[PreviousRtkParticipantWaiting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipantwaiting/)[NextRtkPluginMain](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpluginmain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkPermissionsMessage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettings/
title: RtkSettings \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:10.305788+00:00
---

# RtkSettings · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSettings



# RtkSettings

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Settings dialog with audio device selection, video device selection, and network connection status.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`states` | `States` | ❌ | - | UI state object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`onClose` | `any` | ❌ | - | Callback to close the settings dialog  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSettings } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSettings meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkSettings } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkSettings
    			meeting={meeting}
    			size="md"
    			onClose={() => setSettingsOpen(false)}
    		/>
    	);
    }

[PreviousRtkScreenshareView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/)[NextRtkSettingsAudio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsaudio/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSettings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

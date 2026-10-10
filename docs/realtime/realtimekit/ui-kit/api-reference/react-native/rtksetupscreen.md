---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksetupscreen/
title: RtkSetupScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:49.876929+00:00
---

# RtkSetupScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksetupscreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSetupScreen



# RtkSetupScreen

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Pre-join setup screen with video preview, mic/camera toggles, display name input, camera switch, and join button.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSetupScreen } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSetupScreen meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkSetupScreen } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkSetupScreen
    			meeting={meeting}
    			config={customConfig}
    			size="md"
    			iconPack={customIconPack}
    		/>
    	);
    }

[PreviousRtkSettingsVideo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsvideo/)[NextRtkSidebar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksidebar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSetupScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

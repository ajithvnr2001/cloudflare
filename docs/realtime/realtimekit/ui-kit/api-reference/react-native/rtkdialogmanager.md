---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialogmanager/
title: RtkDialogManager \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:55.653158+00:00
---

# RtkDialogManager · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialogmanager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkDialogManager



# RtkDialogManager

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Manages and renders modal dialogs for leave confirmation, settings, join stage confirmation, and permissions messages.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Size variant  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`onRtkStateUpdate` | `(e) => void` | ❌ | `() => \{\}` | Callback when UI state changes  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDialogManager } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkDialogManager meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkDialogManager } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkDialogManager
    			meeting={meeting}
    			config={customConfig}
    			size="md"
    			onRtkStateUpdate={(e) => handleStateUpdate(e)}
    		/>
    	);
    }

[PreviousRtkDialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialog/)[NextRtkEndedScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkendedscreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkDialogManager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

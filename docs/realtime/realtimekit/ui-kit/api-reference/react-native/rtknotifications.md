---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotifications/
title: RtkNotifications \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:52.290348+00:00
---

# RtkNotifications · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotifications/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkNotifications



# RtkNotifications

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Container that manages and displays meeting notifications (participant join/leave, chat messages, polls, network status) with sound effects.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ✅ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ✅ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ✅ | `'sm'` | Size variant  
`states` | `States` | ✅ | - | UI state object  
`t` | `RtkI18n` | ✅ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import {
    	RtkNotifications,
    	useLanguage,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	const t = useLanguage();
    	return (
    		<RtkNotifications
    			meeting={meeting}
    			config={config}
    			iconPack={iconPack}
    			size="sm"
    			states={states}
    			t={t}
    		/>
    	);
    }

### With Properties
    
    
    import {
    	RtkNotifications,
    	defaultConfig,
    	defaultIconPack,
    	useLanguage,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	const t = useLanguage();
    	return (
    		<RtkNotifications
    			meeting={meeting}
    			config={defaultConfig}
    			iconPack={defaultIconPack}
    			size="md"
    			states={states}
    			t={t}
    		/>
    	);
    }

[PreviousRtkNotification](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtknotification/)[NextRtkParticipant](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkparticipant/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkNotifications.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

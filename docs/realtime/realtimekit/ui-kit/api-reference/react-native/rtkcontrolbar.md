---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbar/
title: RtkControlbar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:02.918818+00:00
---

# RtkControlbar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkControlbar



# RtkControlbar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

The main control bar container that renders meeting controls (mic, camera, leave, and more) using the declarative UI config system.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`variant` | `'boxed' | 'solid'` | ❌ | `'solid'` | Visual style variant  
`iconPack` | `IconPack` | ❌ | - | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkControlbar } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkControlbar meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkControlbar } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkControlbar
    			meeting={meeting}
    			variant="solid"
    			size="md"
    			config={customConfig}
    		/>
    	);
    }

[PreviousRtkClock](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkclock/)[NextRtkControlbarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbarbutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkControlbar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

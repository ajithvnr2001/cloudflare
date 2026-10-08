---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksimplegrid/
title: RtkSimpleGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:11.309328+00:00
---

# RtkSimpleGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksimplegrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSimpleGrid



# RtkSimpleGrid

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksimplegrid/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A simple grid layout that arranges participant tiles in rows and columns with automatic sizing based on participant count.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`participants` | `Peer[]` | ✅ | - | Array of participants to display  
`aspectRatio` | `string` | ❌ | `'3:4'` | Aspect ratio for grid tiles  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`gap` | `number` | ❌ | `8` | Gap between grid tiles in pixels  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`style` | `StyleProp<any>` | ❌ | - | Custom styles for the grid container  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSimpleGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSimpleGrid meeting={meeting} participants={participants} />;
    }

### With Properties
    
    
    import { RtkSimpleGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkSimpleGrid
    			meeting={meeting}
    			participants={participants}
    			aspectRatio="16:9"
    			gap={12}
    			size="md"
    		/>
    	);
    }

[PreviousRtkSidebar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksidebar/)[NextRtkSpinner](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspinner/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSimpleGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

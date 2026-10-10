---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspotlightgrid/
title: RtkSpotlightGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:49.420365+00:00
---

# RtkSpotlightGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspotlightgrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSpotlightGrid



# RtkSpotlightGrid

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A grid layout that highlights pinned participants in a larger view with other participants in a smaller strip. Handles livestream player display for off-stage viewers.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`participants` | `Peer[]` | ✅ | - | Array of active participants  
`pinnedParticipants` | `Peer[]` | ✅ | - | Array of pinned participants to spotlight  
`aspectRatio` | `string` | ❌ | `'3:4'` | Aspect ratio for grid tiles  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`gap` | `number` | ❌ | `4` | Gap between grid tiles in pixels  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSpotlightGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkSpotlightGrid
    			meeting={meeting}
    			participants={participants}
    			pinnedParticipants={pinned}
    		/>
    	);
    }

### With Properties
    
    
    import { RtkSpotlightGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkSpotlightGrid
    			meeting={meeting}
    			participants={participants}
    			pinnedParticipants={pinned}
    			aspectRatio="16:9"
    			gap={8}
    			size="md"
    		/>
    	);
    }

[PreviousRtkSpinner](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspinner/)[NextRtkText](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktext/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSpotlightGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

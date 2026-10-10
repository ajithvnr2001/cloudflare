---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/
title: RtkGrid \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:54.236226+00:00
---

# RtkGrid · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkGrid



# RtkGrid

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

The main participant grid that automatically switches between simple, mixed, spotlight, and livestream layouts based on meeting state.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
`aspectRatio` | `string` | ❌ | `'3:4'` | Aspect ratio for grid tiles  
`gap` | `number` | ❌ | `8` | Gap between grid tiles in pixels  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkGrid meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkGrid } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkGrid meeting={meeting} aspectRatio="16:9" gap={12} size="md" />;
    }

[PreviousRtkFileMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkfilemessage/)[NextRtkGridPagination](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgridpagination/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkGrid.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

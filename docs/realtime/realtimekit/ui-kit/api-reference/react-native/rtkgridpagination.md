---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgridpagination/
title: RtkGridPagination \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:54.983996+00:00
---

# RtkGridPagination · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgridpagination/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkGridPagination



# RtkGridPagination

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Pagination controls for navigating between pages of participants in the grid. Shows page numbers and navigation arrows.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkGridPagination } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkGridPagination meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkGridPagination } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkGridPagination
    			meeting={meeting}
    			iconPack={customIconPack}
    			states={states}
    		/>
    	);
    }

[PreviousRtkGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/)[NextRtkHeader](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkheader/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkGridPagination.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

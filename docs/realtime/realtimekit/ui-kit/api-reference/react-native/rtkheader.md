---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkheader/
title: RtkHeader \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:54.574921+00:00
---

# RtkHeader · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkheader/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkHeader



# RtkHeader

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

The meeting header bar that renders logo, title, participant count, clock, and other header elements using the declarative UI config system.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ❌ | - | Custom icon pack  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkHeader } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkHeader meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkHeader } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkHeader meeting={meeting} config={customConfig} states={states} />;
    }

[PreviousRtkGridPagination](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgridpagination/)[NextRtkIcon](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkicon/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkHeader.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

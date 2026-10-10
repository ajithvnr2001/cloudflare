---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpolls/
title: RtkPolls \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:50.965010+00:00
---

# RtkPolls · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpolls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkPolls



# RtkPolls

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Full polls panel showing all polls with voting and a create poll form for hosts.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPolls } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPolls meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkPolls } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPolls meeting={meeting} size="md" config={customConfig} />;
    }

[PreviousRtkPollForm](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollform/)[NextRtkPollsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpollstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkPolls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

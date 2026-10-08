---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksidebar/
title: RtkSidebar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:11.037366+00:00
---

# RtkSidebar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksidebar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSidebar



# RtkSidebar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksidebar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Full-screen sidebar modal with tabbed navigation for chat, participants, polls, and plugins panels.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`states` | `States` | ❌ | - | UI state object  
`defaultSection` | `'chat' | 'none' | 'participants' | 'plugins' | 'polls'` | ❌ | `'chat'` | Default active tab  
`enabledSections` | `SidebarSection[]` | ❌ | `['chat', 'polls', 'participants', 'plugins']` | Which sidebar sections to display  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSidebar } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSidebar meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkSidebar } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkSidebar
    			meeting={meeting}
    			defaultSection="chat"
    			enabledSections={["chat", "participants", "polls"]}
    			size="md"
    		/>
    	);
    }

[PreviousRtkSetupScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksetupscreen/)[NextRtkSimpleGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksimplegrid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSidebar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

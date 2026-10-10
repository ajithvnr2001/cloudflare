---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamviewercount/
title: RtkLiveStreamViewerCount \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:53.074653+00:00
---

# RtkLiveStreamViewerCount · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamviewercount/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkLiveStreamViewerCount



# RtkLiveStreamViewerCount

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays the current livestream viewer count. Only visible in livestream mode.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ✅ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import {
    	RtkLiveStreamViewerCount,
    	useLanguage,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	const t = useLanguage();
    	return <RtkLiveStreamViewerCount meeting={meeting} t={t} />;
    }

### With Properties
    
    
    import {
    	RtkLiveStreamViewerCount,
    	useLanguage,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	const t = useLanguage();
    	return (
    		<RtkLiveStreamViewerCount
    			meeting={meeting}
    			t={t}
    			iconPack={customIconPack}
    		/>
    	);
    }

[PreviousRtkLiveStreamToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamtoggle/)[NextRtkLogo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklogo/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkLiveStreamViewerCount.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

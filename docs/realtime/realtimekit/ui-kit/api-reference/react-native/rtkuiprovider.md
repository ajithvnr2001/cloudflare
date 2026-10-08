---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkuiprovider/
title: RtkUIProvider \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:11.843198+00:00
---

# RtkUIProvider · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkuiprovider/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkUIProvider



# RtkUIProvider

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkuiprovider/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Context provider component that wraps the meeting UI. Provides SafeAreaView, state management, and back button handling. Must wrap all Rtk UI components.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`children` | `ReactNode` | ✅ | - | Child components to wrap  
  
## Usage Examples

### Basic Usage
    
    
    import {
    	RtkUIProvider,
    	RtkMeeting,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function App() {
    	return (
    		<RtkUIProvider>
    			<RtkMeeting meeting={meeting} />
    		</RtkUIProvider>
    	);
    }

### With Properties
    
    
    import {
    	RtkUIProvider,
    	RtkGrid,
    	RtkControlbar,
    	RtkHeader,
    } from "@cloudflare/realtimekit-react-native-ui";
    
    function App() {
    	return (
    		<RtkUIProvider>
    			<RtkHeader meeting={meeting} />
    			<RtkGrid meeting={meeting} />
    			<RtkControlbar meeting={meeting} />
    		</RtkUIProvider>
    	);
    }

[PreviousRtkTextField](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktextfield/)[NextRtkWaitingScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwaitingscreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkUIProvider.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

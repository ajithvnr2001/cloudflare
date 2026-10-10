---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwaitingscreen/
title: RtkWaitingScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:48.805686+00:00
---

# RtkWaitingScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwaitingscreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkWaitingScreen



# RtkWaitingScreen

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Screen displayed while waiting to join (waitlist, kicked, disconnected states).

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | - | UI configuration object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkWaitingScreen } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkWaitingScreen />;
    }

### With Properties
    
    
    import { RtkWaitingScreen } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkWaitingScreen config={customConfig} />;
    }

[PreviousRtkUIProvider](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkuiprovider/)[NextRtkWebinarStageToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwebinarstagetoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkWaitingScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

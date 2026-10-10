---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkendedscreen/
title: RtkEndedScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:55.226446+00:00
---

# RtkEndedScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkendedscreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkEndedScreen



# RtkEndedScreen

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Screen displayed when the meeting has ended.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ❌ | - | The RealtimeKit meeting instance  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Size variant  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkEndedScreen } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkEndedScreen />;
    }

### With Properties
    
    
    import { RtkEndedScreen } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkEndedScreen meeting={meeting} config={customConfig} size="md" />;
    }

[PreviousRtkDialogManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialogmanager/)[NextRtkFileMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkfilemessage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkEndedScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwebinarstagetoggle/
title: RtkWebinarStageToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:48.868042+00:00
---

# RtkWebinarStageToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwebinarstagetoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkWebinarStageToggle



# RtkWebinarStageToggle

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Toggle button for requesting to join or leave the webinar stage. Only visible in webinar mode for participants with stage access permissions.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | - | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`variant` | `'button' | 'horizontal'` | ❌ | `'button'` | Layout variant  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkWebinarStageToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkWebinarStageToggle meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkWebinarStageToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkWebinarStageToggle meeting={meeting} size="md" variant="button" />;
    }

[PreviousRtkWaitingScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkwaitingscreen/)[Nextrtk-ai](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkWebinarStageToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

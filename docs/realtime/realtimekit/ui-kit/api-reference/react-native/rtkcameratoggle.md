---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcameratoggle/
title: RtkCameraToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:56.168566+00:00
---

# RtkCameraToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcameratoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkCameraToggle



# RtkCameraToggle

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Toggle button to enable or disable the local participant's camera. Automatically hides if the participant lacks video production permissions.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Icon size  
`variant` | `'button' | 'horizontal'` | ❌ | - | Layout variant  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkCameraToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkCameraToggle meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkCameraToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkCameraToggle meeting={meeting} size="md" variant="button" />;
    }

[PreviousRtkButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/)[NextRtkChat](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkchat/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkCameraToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

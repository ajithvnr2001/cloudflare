---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsvideo/
title: RtkSettingsVideo \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:10.629942+00:00
---

# RtkSettingsVideo · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsvideo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSettingsVideo



# RtkSettingsVideo

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsvideo/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Video settings panel with camera selection dropdown and live video preview.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`states` | `States` | ❌ | - | UI state object  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSettingsVideo } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSettingsVideo meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkSettingsVideo } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSettingsVideo meeting={meeting} size="md" states={states} />;
    }

[PreviousRtkSettingsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingstoggle/)[NextRtkSetupScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksetupscreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSettingsVideo.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

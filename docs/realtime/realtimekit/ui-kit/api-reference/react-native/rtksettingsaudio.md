---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsaudio/
title: RtkSettingsAudio \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:50.381785+00:00
---

# RtkSettingsAudio · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsaudio/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSettingsAudio



# RtkSettingsAudio

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Audio settings panel with device selection dropdown, audio visualizer preview, and notification sound toggle.

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
    
    
    import { RtkSettingsAudio } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSettingsAudio meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkSettingsAudio } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSettingsAudio meeting={meeting} size="md" states={states} />;
    }

[PreviousRtkSettings](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettings/)[NextRtkSettingsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSettingsAudio.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

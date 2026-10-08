---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingstoggle/
title: RtkSettingsToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:10.524881+00:00
---

# RtkSettingsToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingstoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkSettingsToggle



# RtkSettingsToggle

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingstoggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Toggle button to open the settings dialog. Hides if no audio or video permissions are available.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Icon size  
`states` | `States` | ❌ | - | UI state object  
`variant` | `'button' | 'horizontal'` | ❌ | - | Layout variant  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSettingsToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSettingsToggle />;
    }

### With Properties
    
    
    import { RtkSettingsToggle } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkSettingsToggle size="md" variant="button" states={states} />;
    }

[PreviousRtkSettingsAudio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsaudio/)[NextRtkSettingsVideo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtksettingsvideo/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkSettingsToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

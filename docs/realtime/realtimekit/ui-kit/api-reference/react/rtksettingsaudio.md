---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/
title: RtkSettingsAudio \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:27.492275+00:00
---

# RtkSettingsAudio · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSettingsAudio



# RtkSettingsAudio

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lets to manage your audio devices and audio preferences. Emits `rtkStateUpdate` event with data for muting notification sounds:
    
    
    {
     prefs: {
       muteNotificationSounds: boolean
     }
    }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSettingsAudio } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSettingsAudio />;
    }

### With Properties
    
    
    import { RtkSettingsAudio } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSettingsAudio
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkSettings](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/)[NextRtkSettingsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSettingsAudio.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

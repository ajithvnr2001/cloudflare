---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspeakerselector/
title: RtkSpeakerSelector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:28.663545+00:00
---

# RtkSpeakerSelector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspeakerselector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSpeakerSelector



# RtkSpeakerSelector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspeakerselector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
`variant` | `'full' | 'inline'` | ✅ | - | variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSpeakerSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSpeakerSelector />;
    }

### With Properties
    
    
    import { RtkSpeakerSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSpeakerSelector
          meeting={meeting}
          size="md"
          variant={'full' | 'inline'}
        />
      );
    }

[PreviousRtkSimpleGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/)[NextRtkSpinner](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSpeakerSelector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

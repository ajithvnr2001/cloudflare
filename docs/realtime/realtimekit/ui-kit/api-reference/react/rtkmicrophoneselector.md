---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/
title: RtkMicrophoneSelector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:42.277459+00:00
---

# RtkMicrophoneSelector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMicrophoneSelector



# RtkMicrophoneSelector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'full' | 'inline'` | ✅ | - | variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMicrophoneSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMicrophoneSelector />;
    }

### With Properties
    
    
    import { RtkMicrophoneSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMicrophoneSelector
          meeting={meeting}
          size="md"
          variant={'full' | 'inline'}
        />
      );
    }

[PreviousRtkMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessageview/)[NextRtkMicToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmictoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMicrophoneSelector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

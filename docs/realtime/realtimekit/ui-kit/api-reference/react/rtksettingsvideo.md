---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/
title: RtkSettingsVideo \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:27.837698+00:00
---

# RtkSettingsVideo · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSettingsVideo



# RtkSettingsVideo

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lets to manage your camera devices and your video preferences. Emits `rtkStateUpdate` event with data for toggling mirroring of self video:
    
    
    {
     prefs: {
       mirrorVideo: boolean
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
    
    
    import { RtkSettingsVideo } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSettingsVideo />;
    }

### With Properties
    
    
    import { RtkSettingsVideo } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSettingsVideo
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkSettingsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingstoggle/)[NextRtkSetupScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSettingsVideo.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

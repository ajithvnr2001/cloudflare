---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/
title: RtkSettings \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:38.497349+00:00
---

# RtkSettings · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSettings



# RtkSettings

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A settings component to see and change your audio/video devices as well as see your connection quality.

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
    
    
    import { RtkSettings } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSettings />;
    }

### With Properties
    
    
    import { RtkSettings } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSettings
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkScreenshareView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreenshareview/)[NextRtkSettingsAudio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSettings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

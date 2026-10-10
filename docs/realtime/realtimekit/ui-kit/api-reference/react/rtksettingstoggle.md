---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingstoggle/
title: RtkSettingsToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:38.815263+00:00
---

# RtkSettingsToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingstoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSettingsToggle



# RtkSettingsToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visibility of settings module. When clicked it emits a `rtkStateUpdate` event with the data:
    
    
    { activeSettings: boolean; }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSettingsToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSettingsToggle />;
    }

### With Properties
    
    
    import { RtkSettingsToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSettingsToggle
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkSettingsAudio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/)[NextRtkSettingsVideo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSettingsToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

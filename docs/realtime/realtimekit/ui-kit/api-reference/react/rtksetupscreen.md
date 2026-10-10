---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/
title: RtkSetupScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:38.362981+00:00
---

# RtkSetupScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSetupScreen



# RtkSetupScreen

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A screen shown before joining the meeting, where you can edit your display name, and media settings.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSetupScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSetupScreen />;
    }

### With Properties
    
    
    import { RtkSetupScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSetupScreen
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkSettingsVideo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/)[NextRtkSidebar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSetupScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

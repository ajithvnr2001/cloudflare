---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/
title: RtkWaitingScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:36.279712+00:00
---

# RtkWaitingScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkWaitingScreen



# RtkWaitingScreen

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkWaitingScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkWaitingScreen />;
    }

### With Properties
    
    
    import { RtkWaitingScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkWaitingScreen
          meeting={meeting}
        />
      );
    }

[PreviousRtkVirtualizedParticipantList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkvirtualizedparticipantlist/)[NextRtkAudioVisualizer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkaudiovisualizer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkWaitingScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

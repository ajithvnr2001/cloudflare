---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsetup/
title: RtkParticipantSetup \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:40.350560+00:00
---

# RtkParticipantSetup · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsetup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantSetup



# RtkParticipantSetup

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isPreview` | `boolean` | ✅ | - | Whether tile is used for preview  
`nameTagPosition` | `| 'bottom-left' | 'bottom-right' | 'bottom-center' | 'top-left' | 'top-right' | 'top-center'` | ✅ | - | Position of name tag  
`participant` | `Peer` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'gradient'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantSetup } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantSetup />;
    }

### With Properties
    
    
    import { RtkParticipantSetup } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantSetup
          isPreview={true}
          nameTagPosition={| 'bottom-left'
        | 'bottom-right'
        | 'bottom-center'
        | 'top-left'
        | 'top-right'
        | 'top-center'}
          participant={participant}
        />
      );
    }

[PreviousRtkParticipantsAudio](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/)[NextRtkParticipantsStageList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsstagelist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipantSetup.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

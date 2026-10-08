---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/
title: RtkParticipantsAudio \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:24.526543+00:00
---

# RtkParticipantsAudio · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkParticipantsAudio



# RtkParticipantsAudio

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsaudio/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which plays all the audio from participants and screenshares.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`preloadedAudioElem` | `HTMLAudioElement` | ✅ | - | Pass existing audio element  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkParticipantsAudio } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkParticipantsAudio />;
    }

### With Properties
    
    
    import { RtkParticipantsAudio } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkParticipantsAudio
          meeting={meeting}
          preloadedAudioElem={htmlaudioelement}
        />
      );
    }

[PreviousRtkParticipants](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipants/)[NextRtkParticipantSetup](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipantsetup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkParticipantsAudio.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

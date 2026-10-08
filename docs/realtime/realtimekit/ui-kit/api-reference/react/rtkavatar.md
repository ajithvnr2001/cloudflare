---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkavatar/
title: RtkAvatar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:13.150819+00:00
---

# RtkAvatar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkavatar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkAvatar



# RtkAvatar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkavatar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Avatar component which renders a participant's image or their initials.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`participant` | `Peer | WaitlistedParticipant | { name: string; picture: string }` | ✅ | - | Participant object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `AvatarVariant` | ✅ | - | Avatar type  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAvatar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkAvatar />;
    }

### With Properties
    
    
    import { RtkAvatar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkAvatar
          participant="example"
          size="md"
          variant="circular"
        />
      );
    }

[PreviousRtkAudioVisualizer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/)[NextRtkBreakoutRoomManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroommanager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkAvatar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

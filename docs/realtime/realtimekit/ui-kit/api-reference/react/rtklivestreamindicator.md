---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/
title: RtkLivestreamIndicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:20.941886+00:00
---

# RtkLivestreamIndicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkLivestreamIndicator



# RtkLivestreamIndicator

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamindicator/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLivestreamIndicator } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkLivestreamIndicator />;
    }

### With Properties
    
    
    import { RtkLivestreamIndicator } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkLivestreamIndicator
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkLeaveMeeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/)[NextRtkLivestreamPlayer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamplayer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkLivestreamIndicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

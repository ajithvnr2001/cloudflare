---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/
title: RtkLivestreamToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.280174+00:00
---

# RtkLivestreamToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkLivestreamToggle



# RtkLivestreamToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLivestreamToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkLivestreamToggle />;
    }

### With Properties
    
    
    import { RtkLivestreamToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkLivestreamToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkLivestreamPlayer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamplayer/)[NextRtkLogo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkLivestreamToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/
title: RtkCaptionToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:47.360357+00:00
---

# RtkCaptionToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkCaptionToggle



# RtkCaptionToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkCaptionToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkCaptionToggle />;
    }

### With Properties
    
    
    import { RtkCaptionToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkCaptionToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkCameraToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameratoggle/)[NextRtkChat](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkCaptionToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

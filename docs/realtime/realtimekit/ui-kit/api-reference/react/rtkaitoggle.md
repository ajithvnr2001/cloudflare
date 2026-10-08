---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/
title: RtkAiToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:12.498704+00:00
---

# RtkAiToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkAiToggle



# RtkAiToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkAiToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkAiToggle />;
    }

### With Properties
    
    
    import { RtkAiToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkAiToggle
          meeting={meeting}
          size="md"
          variant="button"
        />
      );
    }

[PreviousRtkAi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkai/)[NextRtkAiTranscriptions](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkAiToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

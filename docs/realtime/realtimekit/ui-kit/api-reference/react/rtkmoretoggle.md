---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmoretoggle/
title: RtkMoreToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:41.933189+00:00
---

# RtkMoreToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmoretoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMoreToggle



# RtkMoreToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles visibility of a more menu. When clicked it emits a `rtkStateUpdate` event with the data:
    
    
    { activeMoreMenu: boolean; }

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMoreToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMoreToggle />;
    }

### With Properties
    
    
    import { RtkMoreToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMoreToggle
          size="md"
        />
      );
    }

[PreviousRtkMixedGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmixedgrid/)[NextRtkMuteAllButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmuteallbutton/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMoreToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

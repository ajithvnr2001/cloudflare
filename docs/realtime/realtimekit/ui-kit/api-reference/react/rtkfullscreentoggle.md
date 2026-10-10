---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/
title: RtkFullscreenToggle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.243270+00:00
---

# RtkFullscreenToggle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfullscreentoggle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkFullscreenToggle



# RtkFullscreenToggle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button which toggles full screen mode for any existing `rtk-meeting` component in the DOM.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`targetElement` | `HTMLElement` | ✅ | - | Target Element to fullscreen  
`variant` | `ControlBarVariant` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkFullscreenToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkFullscreenToggle />;
    }

### With Properties
    
    
    import { RtkFullscreenToggle } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkFullscreenToggle
          size="md"
          targetElement={htmlelement}
          variant="button"
        />
      );
    }

[PreviousRtkFilePickerButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilepickerbutton/)[NextRtkGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkFullscreenToggle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

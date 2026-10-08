---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/
title: RtkPluginMain \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:25.978788+00:00
---

# RtkPluginMain · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkPluginMain



# RtkPluginMain

Last updated Jun 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which renders a plugin's UI.

The plugin's `component` (an HTMLElement) is placed into this element's light DOM and projected into the shadow DOM layout via a `<slot>`. This ensures external CSS from the consuming application continues to apply to the plugin content.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`plugin` | `RTKPlugin` | ✅ | - | Plugin  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPluginMain } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPluginMain />;
    }

### With Properties
    
    
    import { RtkPluginMain } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPluginMain
          meeting={meeting}
          plugin={rtkplugin}
        />
      );
    }

[PreviousRtkPipToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpiptoggle/)[NextRtkPlugins](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkplugins/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkPluginMain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

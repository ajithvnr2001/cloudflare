---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkplugins/
title: RtkPlugins \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:39.513535+00:00
---

# RtkPlugins · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkplugins/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkPlugins



# RtkPlugins

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lists all available plugins from their preset, and ability to enable or disable plugins.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPlugins } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPlugins />;
    }

### With Properties
    
    
    import { RtkPlugins } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPlugins
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkPluginMain](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/)[NextRtkPluginsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkPlugins.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

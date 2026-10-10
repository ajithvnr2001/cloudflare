---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/
title: RtkTabBar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:37.444026+00:00
---

# RtkTabBar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkTabBar



# RtkTabBar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`activeTab` | `Tab` | ✅ | - | Active tab  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack  
`layout` | `GridLayout1` | ✅ | - | Grid Layout  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`tabs` | `Tab[]` | ✅ | - | Tabs  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkTabBar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkTabBar />;
    }

### With Properties
    
    
    import { RtkTabBar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkTabBar
          activeTab={tab}
          layout={gridlayout1}
          meeting={meeting}
        />
      );
    }

[PreviousRtkSwitch](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/)[NextRtkTextComposerView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextcomposerview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkTabBar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

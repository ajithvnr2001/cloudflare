---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/
title: RtkSidebar \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:38.425862+00:00
---

# RtkSidebar · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSidebar



# RtkSidebar

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which handles the sidebar and you can customize which sections you want, and which section you want as the default.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`defaultSection` | `RtkSidebarSection` | ✅ | - | Default section  
`enabledSections` | `RtkSidebarTab[]` | ✅ | - | Enabled sections in sidebar  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`view` | `RtkSidebarView` | ✅ | - | View type  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSidebar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSidebar />;
    }

### With Properties
    
    
    import { RtkSidebar } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSidebar
          defaultSection={rtksidebarsection}
          enabledSections={[]}
          meeting={meeting}
        />
      );
    }

[PreviousRtkSetupScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/)[NextRtkSidebarUi](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksidebarui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSidebar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/
title: RtkSwitch \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:29.241509+00:00
---

# RtkSwitch · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSwitch



# RtkSwitch

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A switch component which follows RTK Design System.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`checked` | `boolean` | ✅ | - | Whether the switch is enabled/checked  
`disabled` | `boolean` | ✅ | - | Whether switch is readonly  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`readonly` | `boolean` | ✅ | - | Whether switch is readonly  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSwitch } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSwitch />;
    }

### With Properties
    
    
    import { RtkSwitch } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSwitch
          checked={true}
          disabled={true}
          readonly={true}
        />
      );
    }

[PreviousRtkStageToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstagetoggle/)[NextRtkTabBar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktabbar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSwitch.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

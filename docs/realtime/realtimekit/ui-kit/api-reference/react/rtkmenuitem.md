---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenuitem/
title: RtkMenuItem \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:42.467771+00:00
---

# RtkMenuItem · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenuitem/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMenuItem



# RtkMenuItem

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A menu item component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`menuVariant` | `'primary' | 'secondary'` | ✅ | - | Variant  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMenuItem } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMenuItem />;
    }

### With Properties
    
    
    import { RtkMenuItem } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMenuItem
          menuVariant={'primary' | 'secondary'}
          size="md"
        />
      );
    }

[PreviousRtkMenu](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenu/)[NextRtkMenuList](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMenuItem.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

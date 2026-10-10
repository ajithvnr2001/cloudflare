---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkheader/
title: RtkHeader \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.305650+00:00
---

# RtkHeader · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkheader/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkHeader



# RtkHeader

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component that houses all the header components.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config  
`disableRender` | `boolean` | ✅ | - | Whether to render the default UI  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `'solid' | 'boxed'` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkHeader } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkHeader />;
    }

### With Properties
    
    
    import { RtkHeader } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkHeader
          disableRender={true}
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkGridPagination](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/)[NextRtkIcon](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkHeader.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

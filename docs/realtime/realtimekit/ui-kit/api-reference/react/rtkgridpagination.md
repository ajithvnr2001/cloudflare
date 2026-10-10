---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/
title: RtkGridPagination \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.030946+00:00
---

# RtkGridPagination · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkGridPagination



# RtkGridPagination

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which allows you to change current page and view mode of active participants list. This is reflected in the `rtk-grid` component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size Prop  
`states` | `States` | ✅ | - | States  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
`variant` | `GridPaginationVariants` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkGridPagination } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkGridPagination />;
    }

### With Properties
    
    
    import { RtkGridPagination } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkGridPagination
          meeting={meeting}
          size="md"
          variant={gridpaginationvariants}
        />
      );
    }

[PreviousRtkGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/)[NextRtkHeader](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkheader/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkGridPagination.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/
title: RtkMenuList \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:42.340526+00:00
---

# RtkMenuList · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkMenuList



# RtkMenuList

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A menu list component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`menuVariant` | `'primary' | 'secondary'` | ✅ | - | Variant  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkMenuList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkMenuList />;
    }

### With Properties
    
    
    import { RtkMenuList } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkMenuList
          menuVariant={'primary' | 'secondary'}
        />
      );
    }

[PreviousRtkMenuItem](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenuitem/)[NextRtkMessageListView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkMenuList.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstage/
title: RtkStage \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:37.761152+00:00
---

# RtkStage · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkStage



# RtkStage

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component used as a stage that commonly houses the `grid` and `sidebar` components.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkStage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkStage />;
    }

### With Properties
    
    
    import { RtkStage } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkStage
          iconPack={defaultIconPack}
          t={rtki18n}
        />
      );
    }

[PreviousRtkSpotlightIndicator](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightindicator/)[NextRtkStageToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstagetoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkStage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

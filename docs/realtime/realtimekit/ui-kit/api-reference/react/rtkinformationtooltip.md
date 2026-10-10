---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/
title: RtkInformationTooltip \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:43.806966+00:00
---

# RtkInformationTooltip · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkInformationTooltip



# RtkInformationTooltip

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkInformationTooltip } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkInformationTooltip />;
    }

### With Properties
    
    
    import { RtkInformationTooltip } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkInformationTooltip
          iconPack={defaultIconPack}
        />
      );
    }

[PreviousRtkImageViewer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimageviewer/)[NextRtkJoinStage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkjoinstage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkInformationTooltip.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

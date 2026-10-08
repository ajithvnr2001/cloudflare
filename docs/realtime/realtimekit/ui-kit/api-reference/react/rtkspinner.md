---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/
title: RtkSpinner \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:28.567680+00:00
---

# RtkSpinner · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkSpinner



# RtkSpinner

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which shows an animating spinner.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`size` | `Size1` | ✅ | - | Size  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkSpinner } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkSpinner />;
    }

### With Properties
    
    
    import { RtkSpinner } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkSpinner
          size="md"
        />
      );
    }

[PreviousRtkSpeakerSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspeakerselector/)[NextRtkSpotlightGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightgrid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkSpinner.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/
title: RtkIcon \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:19.614793+00:00
---

# RtkIcon · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkIcon



# RtkIcon

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

An icon component which accepts an svg string and renders it.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`icon` | `string` | ✅ | - | Icon  
`size` | `Size1` | ✅ | - | Size  
`variant` | `IconVariant` | ✅ | - | Icon variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkIcon } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkIcon />;
    }

### With Properties
    
    
    import { RtkIcon } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkIcon
          icon="example"
          size="md"
          variant="primary"
        />
      );
    }

[PreviousRtkHeader](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkheader/)[NextRtkIdleScreen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkIcon.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

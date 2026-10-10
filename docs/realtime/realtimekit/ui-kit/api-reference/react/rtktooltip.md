---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/
title: RtkTooltip \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:37.024217+00:00
---

# RtkTooltip · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkTooltip



# RtkTooltip

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Tooltip component which follows RTK Design System.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`delay` | `number` | ✅ | - | Delay before showing the tooltip  
`disabled` | `boolean` | ✅ | - | Disabled  
`kind` | `TooltipKind` | ✅ | - | Tooltip kind  
`label` | `string` | ✅ | - | Tooltip label  
`open` | `boolean` | ✅ | - | Open  
`placement` | `Placement` | ✅ | - | Placement of menu  
`size` | `Size` | ✅ | - | Size  
`variant` | `TooltipVariant` | ✅ | - | Tooltip variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkTooltip } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkTooltip />;
    }

### With Properties
    
    
    import { RtkTooltip } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkTooltip
          delay={42}
          disabled={true}
          kind={tooltipkind}
        />
      );
    }

[PreviousRtkTextMessageView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktextmessageview/)[NextRtkTranscript](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkTooltip.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

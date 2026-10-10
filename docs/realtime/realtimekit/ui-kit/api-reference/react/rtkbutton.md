---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/
title: RtkButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:47.932664+00:00
---

# RtkButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkButton



# RtkButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A button that follows RTK Design System.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`disabled` | `boolean` | ✅ | - | Where the button is disabled or not  
`kind` | `ButtonKind` | ✅ | - | Button type  
`reverse` | `boolean` | ✅ | - | Whether to reverse order of children  
`size` | `Size` | ✅ | - | Size  
`type` | `HTMLButtonElement['type']` | ✅ | - | Button type  
`variant` | `ButtonVariant` | ✅ | - | Button variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkButton />;
    }

### With Properties
    
    
    import { RtkButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkButton
          disabled={true}
          kind={buttonkind}
          reverse={true}
        />
      );
    }

[PreviousRtkBroadcastMessageModal](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/)[NextRtkCameraSelector](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameraselector/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

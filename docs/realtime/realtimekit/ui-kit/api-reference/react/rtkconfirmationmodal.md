---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/
title: RtkConfirmationModal \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:16.202295+00:00
---

# RtkConfirmationModal · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkConfirmationModal



# RtkConfirmationModal

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A confirmation modal.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkConfirmationModal } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkConfirmationModal />;
    }

### With Properties
    
    
    import { RtkConfirmationModal } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkConfirmationModal
          meeting={meeting}
        />
      );
    }

[PreviousRtkClock](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/)[NextRtkControlbar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkConfirmationModal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

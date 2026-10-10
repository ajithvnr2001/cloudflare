---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/
title: RtkIdleScreen \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:44.426689+00:00
---

# RtkIdleScreen · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkIdleScreen



# RtkIdleScreen

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A screen that handles the idle state, i.e; when you are waiting for data about the meeting, specifically the `meeting` object.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkIdleScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkIdleScreen />;
    }

### With Properties
    
    
    import { RtkIdleScreen } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkIdleScreen
          meeting={meeting}
        />
      );
    }

[PreviousRtkIcon](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/)[NextRtkImageMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkimagemessage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkIdleScreen.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

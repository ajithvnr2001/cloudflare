---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpinnedmessageselector/
title: RtkPinnedMessageSelector \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:25.585411+00:00
---

# RtkPinnedMessageSelector · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpinnedmessageselector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkPinnedMessageSelector



# RtkPinnedMessageSelector

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpinnedmessageselector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPinnedMessageSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPinnedMessageSelector />;
    }

### With Properties
    
    
    import { RtkPinnedMessageSelector } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPinnedMessageSelector
          meeting={meeting}
        />
      );
    }

[PreviousRtkPermissionsMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpermissionsmessage/)[NextRtkPipToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpiptoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkPinnedMessageSelector.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

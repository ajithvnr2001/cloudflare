---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpolls/
title: RtkPolls \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:39.039302+00:00
---

# RtkPolls · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpolls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkPolls



# RtkPolls

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which lists all available plugins a user can access with the ability to enable or disable them as per their permissions.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size` | ✅ | - | Size  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPolls } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPolls />;
    }

### With Properties
    
    
    import { RtkPolls } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPolls
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkPollForm](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/)[NextRtkPollsToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollstoggle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkPolls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

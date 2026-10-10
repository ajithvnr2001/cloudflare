---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/
title: RtkLogo \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:42.948427+00:00
---

# RtkLogo · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklogo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkLogo



# RtkLogo

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component which loads the logo from your config, or via the `logo-url` attribute.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object  
`logoUrl` | `string` | ✅ | - | Logo URL  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLogo } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkLogo />;
    }

### With Properties
    
    
    import { RtkLogo } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkLogo
          logoUrl="example"
          meeting={meeting}
        />
      );
    }

[PreviousRtkLivestreamToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/)[NextRtkMarkdownView](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkLogo.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

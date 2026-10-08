---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggervideo/
title: RtkDebuggerVideo \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:17.844968+00:00
---

# RtkDebuggerVideo · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggervideo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkDebuggerVideo



# RtkDebuggerVideo

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggervideo/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`size` | `Size1` | ✅ | - | Size  
`states` | `States1` | ✅ | - | States object  
`t` | `RtkI18n1` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDebuggerVideo } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkDebuggerVideo />;
    }

### With Properties
    
    
    import { RtkDebuggerVideo } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkDebuggerVideo
          meeting={meeting}
          size="md"
        />
      );
    }

[PreviousRtkDebuggerToggle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggertoggle/)[NextRtkDialog](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkDebuggerVideo.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

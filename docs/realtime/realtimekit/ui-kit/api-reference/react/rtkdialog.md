---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialog/
title: RtkDialog \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:45.346984+00:00
---

# RtkDialog · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkDialog



# RtkDialog

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A dialog component.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config  
`disableEscapeKey` | `boolean` | ✅ | - | Whether Escape key can close the modal  
`hideCloseButton` | `boolean` | ✅ | - | Whether to show the close button  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`meeting` | `Meeting` | ✅ | - | Meeting object  
`open` | `boolean` | ✅ | - | Whether a dialog is open or not  
`size` | `Size` | ✅ | - | Size  
`states` | `States` | ✅ | - | States object  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDialog } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkDialog />;
    }

### With Properties
    
    
    import { RtkDialog } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkDialog
          disableEscapeKey={true}
          hideCloseButton={true}
          meeting={meeting}
        />
      );
    }

[PreviousRtkDebuggerVideo](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggervideo/)[NextRtkDialogManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialogmanager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkDialog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

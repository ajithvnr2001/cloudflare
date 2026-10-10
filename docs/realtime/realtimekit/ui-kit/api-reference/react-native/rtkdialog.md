---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialog/
title: RtkDialog \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:55.525130+00:00
---

# RtkDialog · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkDialog



# RtkDialog

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A modal dialog overlay component with optional close button.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`children` | `ReactNode` | ✅ | - | Dialog content  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`onRtkDialogClose` | `any` | ✅ | - | Callback when dialog is closed  
`config` | `UIConfig` | ❌ | `defaultConfig` | UI configuration object  
`hideCloseButton` | `boolean` | ❌ | `false` | Hide the close button  
`open` | `boolean` | ❌ | - | Whether the dialog is visible  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | - | Size variant  
`states` | `States` | ❌ | - | UI state object  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`t` | `RtkI18n` | ❌ | - | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkDialog } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkDialog meeting={meeting} onRtkDialogClose={() => setOpen(false)}>
    			<Text>Dialog content</Text>
    		</RtkDialog>
    	);
    }

### With Properties
    
    
    import { RtkDialog } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkDialog
    			meeting={meeting}
    			open={isOpen}
    			onRtkDialogClose={() => setOpen(false)}
    			hideCloseButton={false}
    			size="md"
    		>
    			<Text>Dialog content</Text>
    		</RtkDialog>
    	);
    }

[PreviousRtkControlbarButton](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkcontrolbarbutton/)[NextRtkDialogManager](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkdialogmanager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkDialog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpluginmain/
title: RtkPluginMain \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:08.649047+00:00
---

# RtkPluginMain · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpluginmain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkPluginMain



# RtkPluginMain

Last updated Jul 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpluginmain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Renders an active plugin by loading `plugin.component.src` in a `WebView`. Includes a header bar with the plugin name, a fullscreen toggle, and an optional close button (shown when `plugin.permissions.canDeactivate` is `true`). Pressing close calls `plugin.deactivate()`.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`plugin` | `RTKPlugin` | ✅ | - | The plugin to render  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPluginMain } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkPluginMain meeting={meeting} plugin={activePlugin} />;
    }

### With Properties
    
    
    import { RtkPluginMain } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkPluginMain
    			meeting={meeting}
    			plugin={activePlugin}
    			iconPack={customIconPack}
    		/>
    	);
    }

[PreviousRtkPermissionsMessage](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkpermissionsmessage/)[NextRtkPlugins](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkplugins/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkPluginMain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

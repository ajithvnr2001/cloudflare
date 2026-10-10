---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/
title: RTKPlugin \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:57.234216+00:00
---

# RTKPlugin · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKPlugin



# RTKPlugin

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview plugin.component plugin.activateForSelf() plugin.deactivateForSelf() plugin.activate() plugin.deactivate()

The RTKPlugin module represents a single plugin in the meeting. A plugin can be obtained from one of the plugin arrays in `meeting.plugins`. For example,
    
    
    const plugin1 = meeting.plugins.active.get(pluginId);
    const plugin2 = meeting.plugins.all.get(pluginId);

  * RTKPlugin
    * .component
    * .activateForSelf()
    * .deactivateForSelf()
    * .activate()
    * .deactivate()



### plugin.component

The component for this plugin, as provided in the plugin config.

**Kind** : instance property of `RTKPlugin`  


### plugin.activateForSelf()

**Kind** : instance method of `RTKPlugin`  


### plugin.deactivateForSelf()

**Kind** : instance method of `RTKPlugin`  


### plugin.activate()

Activate this plugin for all participants.

**Kind** : instance method of `RTKPlugin`  


### plugin.deactivate()

Deactivate this plugin for all participants.

**Kind** : instance method of `RTKPlugin`

[PreviousRTKPip](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/)[NextRTKPlugins](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKPlugin.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

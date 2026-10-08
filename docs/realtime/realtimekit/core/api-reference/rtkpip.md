---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/
title: RTKPip \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:55.921155+00:00
---

# RTKPip · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKPip



# RTKPip

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewModulesFunctions meeting.participants.pip.disable meeting.participants.pip.init([options]) meeting.participants.pip.disableSource(source) meeting.participants.pip.addSource(id, element, enabled, [displayText]) meeting.participants.pip.updateSource(id, source) meeting.participants.pip.removeSource(id) meeting.participants.pip.removePinnedSource(id) meeting.participants.pip.removeAllSources() meeting.participants.pip.enable()

## Modules

RTKPip
    

## Functions

getInitials()
    

Code from ui-kit. Same method used in the avatar component

  * RTKPip
    * .disable
    * .init([options])
    * .disableSource(source)
    * .addSource(id, element, enabled, [displayText])
    * .updateSource(id, source)
    * .removeSource(id)
    * .removePinnedSource(id)
    * .removeAllSources()
    * .enable()



### meeting.participants.pip.disable

Disable PiP

**Kind** : instance property of `RTKPip`  


### meeting.participants.pip.init([options])

Initialize PiP and prepare sources

**Kind** : instance method of `RTKPip`

Param | Type  
---|---  
[options] | `Object`  
[options.height] | `number`  
[options.width] | `number`  
  
### meeting.participants.pip.disableSource(source)

**Kind** : instance method of `RTKPip`

Param | Type  
---|---  
source | `string`  
  
### meeting.participants.pip.addSource(id, element, enabled, [displayText])

Add a video source from the participant grid

**Kind** : instance method of `RTKPip`

Param | Type | Description  
---|---|---  
id | `string` | id for the source (ex. participant id)  
element | `HTMLVideoElement` | HTMLVideoElement for the video source  
enabled | `boolean` | if source is enabled  
[displayText] | `string` | two character display text  
  
### meeting.participants.pip.updateSource(id, source)

Update a video source

**Kind** : instance method of `RTKPip`

Param | Type  
---|---  
id | `string`  
source | `any`  
  
### meeting.participants.pip.removeSource(id)

Remove the video source for the participant

**Kind** : instance method of `RTKPip`

Param | Description  
---|---  
id | id for the source (ex. participant id)  
  
### meeting.participants.pip.removePinnedSource(id)

Remove the pinned source

**Kind** : instance method of `RTKPip`

Param | Description  
---|---  
id | id for the source (ex. participant id)  
  
### meeting.participants.pip.removeAllSources()

Remove all sources

**Kind** : instance method of `RTKPip`  


### meeting.participants.pip.enable()

Enable PiP

**Kind** : instance method of `RTKPip`  


Code from ui-kit. Same method used in the avatar component

**Kind** : global function

[PreviousRTKPermissionsPreset](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpermissionspreset/)[NextRTKPlugin](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKPip.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

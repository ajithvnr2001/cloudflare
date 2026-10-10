---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/
title: RTKMeta \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:57.838434+00:00
---

# RTKMeta · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKMeta



# RTKMeta

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.meta.selfActiveTab meeting.meta.broadcastTabChanges meeting.meta.viewType meeting.meta.meetingStartedTimestamp meeting.meta.meetingTitle meeting.meta.sessionId meeting.meta.meetingId meeting.meta.setBroadcastTabChanges(broadcastTabChanges) meeting.meta.setSelfActiveTab(spotlightTab, tabChangeSource)

This consists of the metadata of the meeting, such as the room name and the title.

  * RTKMeta
    * .selfActiveTab
    * .broadcastTabChanges
    * .viewType
    * .meetingStartedTimestamp
    * .meetingTitle
    * .sessionId
    * .meetingId
    * .setBroadcastTabChanges(broadcastTabChanges)
    * .setSelfActiveTab(spotlightTab, tabChangeSource)



### meeting.meta.selfActiveTab

Represents the current active tab

**Kind** : instance property of `RTKMeta`  


### meeting.meta.broadcastTabChanges

Represents whether current user is spotlighted

**Kind** : instance property of `RTKMeta`  


### meeting.meta.viewType

The `viewType` tells the type of the meeting possible values are: GROUP_CALL| LIVESTREAM | CHAT | AUDIO_ROOM

**Kind** : instance property of `RTKMeta`  


### meeting.meta.meetingStartedTimestamp

The timestamp of the time when the meeting started.

**Kind** : instance property of `RTKMeta`  


### meeting.meta.meetingTitle

The title of the meeting.

**Kind** : instance property of `RTKMeta`  


### meeting.meta.sessionId

(Experimental) The sessionId this meeting object is part of.

**Kind** : instance property of `RTKMeta`  


### meeting.meta.meetingId

The room name of the meeting.

**Kind** : instance property of `RTKMeta`  


### meeting.meta.setBroadcastTabChanges(broadcastTabChanges)

Sets current user as broadcasting tab changes

**Kind** : instance method of `RTKMeta`

Param | Type  
---|---  
broadcastTabChanges | `boolean`  
  
### meeting.meta.setSelfActiveTab(spotlightTab, tabChangeSource)

Sets current active tab for user

**Kind** : instance method of `RTKMeta`

Param | Type  
---|---  
spotlightTab | `ActiveTab`  
tabChangeSource | `TabChangeSource`  
  
[PreviousRTKLivestream](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/)[NextRTKParticipant](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipant/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKMeta.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

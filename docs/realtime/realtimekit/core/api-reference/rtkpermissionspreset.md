---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpermissionspreset/
title: RTKPermissionsPreset \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:57.571045+00:00
---

# RTKPermissionsPreset · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpermissionspreset/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKPermissionsPreset



# RTKPermissionsPreset

Last updated Jul 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.self.permissions.stageEnabled meeting.self.permissions.stageAccess meeting.self.permissions.acceptWaitingRequests meeting.self.permissions.requestProduceVideo meeting.self.permissions.requestProduceAudio meeting.self.permissions.requestProduceScreenshare meeting.self.permissions.canAllowParticipantAudio meeting.self.permissions.canAllowParticipantScreensharing meeting.self.permissions.canAllowParticipantVideo meeting.self.permissions.canDisableParticipantAudio meeting.self.permissions.canDisableParticipantVideo meeting.self.permissions.kickParticipant meeting.self.permissions.pinParticipant meeting.self.permissions.canRecord meeting.self.permissions.waitingRoomBehaviour meeting.self.permissions.plugins meeting.self.permissions.polls meeting.self.permissions.canProduceVideo meeting.self.permissions.canProduceScreenshare meeting.self.permissions.canProduceAudio meeting.self.permissions.chatPublic meeting.self.permissions.chatPrivate meeting.self.permissions.hiddenParticipant meeting.self.permissions.showParticipantList meeting.self.permissions.canChangeParticipantPermissions meeting.self.permissions.canLivestream

The PermissionPreset class represents the meeting permissions for the current participant

  * PermissionPreset
    * .stageEnabled
    * .stageAccess
    * .acceptWaitingRequests
    * .requestProduceVideo
    * .requestProduceAudio
    * .requestProduceScreenshare
    * .canAllowParticipantAudio
    * .canAllowParticipantScreensharing
    * .canAllowParticipantVideo
    * .canDisableParticipantAudio
    * .canDisableParticipantVideo
    * .kickParticipant
    * .pinParticipant
    * .canRecord
    * .waitingRoomBehaviour
    * .plugins
    * .polls
    * .canProduceVideo
    * .canProduceScreenshare
    * .canProduceAudio
    * .chatPublic
    * .chatPrivate
    * .hiddenParticipant
    * .showParticipantList
    * .canChangeParticipantPermissions
    * .canLivestream



### meeting.self.permissions.stageEnabled

The `stageEnabled` property returns a boolean value. If `true`, stage management is available for the participant.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.stageAccess

The `stageAccess` property dictates how a user interacts with the stage. The possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`;

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.acceptWaitingRequests

The `acceptWaitingRequests` returns boolean value. If `true`, participant can accept the request of waiting participant.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.requestProduceVideo

The `requestProduceVideo` returns boolean value. If `true`, participant can send request to participants about producing video.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.requestProduceAudio

The `requestProduceAudio` returns boolean value. If `true`, participant can send request to participants about producing audio.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.requestProduceScreenshare

The `requestProduceScreenshare` returns boolean value. If `true`, participant can send request to participants about sharing screen.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canAllowParticipantAudio

The `canAllowParticipantAudio` returns boolean value. If `true`, participant can enable other participants` audio.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canAllowParticipantScreensharing

The `canAllowParticipantScreensharing` returns boolean value. If `true`, participant can enable other participants` screen share.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canAllowParticipantVideo

The `canAllowParticipantVideo` returns boolean value. If `true`, participant can enable other participants` video.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canDisableParticipantAudio

If `true`, a participant can disable other participants` audio.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canDisableParticipantVideo

If `true`, a participant can disable other participants` video.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.kickParticipant

The `kickParticipant` returns boolean value. If `true`, participant can remove other participants from the meeting.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.pinParticipant

The `pinParticipant` returns boolean value. If `true`, participant can pin a participant in the meeting.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canRecord

The `canRecord` returns boolean value. If `true`, participant can record the meeting.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.waitingRoomBehaviour

The `waitingRoomType` returns string value. type of waiting room behavior possible values are `SKIP`, `ON_PRIVILEGED_USER_ENTRY`, `SKIP_ON_ACCEPT`

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.plugins

The `plugins` tells if the participant can act on plugins there are 2 permissions with boolean values, `canStart` and `canClose`.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.polls

The `polls` tells if the participant can use polls. There are 3 permissions with boolean values, `canCreate`, `canVote`, `canViewResults`

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canProduceVideo

The `canProduceVideo` shows permissions for enabling video. There possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canProduceScreenshare

The `canProduceScreenshare` shows permissions for sharing screen. There possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canProduceAudio

The `canProduceAudio` shows permissions for enabling audio. There possible values are `ALLOWED`, `NOT_ALLOWED`, `CAN_REQUEST`

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.chatPublic

The `chatPublic` shows permissions for public chat there are 4 permissions `canSend` \- if true, the participant can send chat `text` \- if true, the participant can send text `files` \- if true, the participant can send files

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.chatPrivate

The `chatPrivate` shows permissions for public chat there are 4 permissions `canSend` \- if true, the participant can send private chat `text` \- if true, the participant can send text as private chat `files` \- if true, the participant can send files as private chat `canReceive` \- (optional) if true, the participant can receive private chat

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.hiddenParticipant

The `hiddenParticipant` returns boolean value. If `true`, participant is hidden.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.showParticipantList

The `showParticipantList` returns boolean value. If `true`, participant list can be shown to the participant.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canChangeParticipantPermissions

The `canChangeParticipantPermissions` returns boolean value. If `true`, allow changing the participants' permissions.

**Kind** : instance property of `PermissionPreset`  


### meeting.self.permissions.canLivestream

Livestream

**Kind** : instance property of `PermissionPreset`

[PreviousRTKParticipants](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipants/)[NextRTKPip](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkpip/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKPermissionsPreset.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

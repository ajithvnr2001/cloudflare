---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipant/
title: RTKParticipant \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:57.772567+00:00
---

# RTKParticipant · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipant/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKParticipant



# RTKParticipant

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview participant.id participant.userId participant.name participant.picture participant.customParticipantId participant.device participant.videoTrack participant.audioTrack participant.screenShareTracks participant.videoEnabled participant.audioEnabled participant.screenShareEnabled participant.producers participant.manualProducerConfig participant.supportsRemoteControl participant.presetName participant.stageStatus participant.isPinned participant.pin() participant.unpin() participant.disableAudio() participant.kick() participant.disableVideo() participant.registerVideoElement(videoElem) participant.deregisterVideoElement([videoElem])

This module represents a single participant in the meeting. The participant object can be accessed from one of the participant lists present in the `meeting.participants` object. For example,
    
    
    const participant1 = meeting.participants.active.get(participantId);
    const participant2 = meeting.participants.joined.get(participantId);
    const participant3 = meeting.participants.active.toArray()[0];
    const participantsNamedJohn = meeting.participants.active.toArray()
      .filter((p) => p.name === 'John');

  * RTKParticipant
    * .id
    * .userId
    * .name
    * .picture
    * .customParticipantId
    * .device
    * .videoTrack
    * .audioTrack
    * .screenShareTracks
    * .videoEnabled
    * .audioEnabled
    * .screenShareEnabled
    * .producers
    * .manualProducerConfig
    * .supportsRemoteControl
    * .presetName
    * .stageStatus
    * .isPinned
    * .pin()
    * .unpin()
    * .disableAudio()
    * .kick()
    * .disableVideo()
    * .registerVideoElement(videoElem)
    * .deregisterVideoElement([videoElem])



### participant.id

The peer ID of the participant. The participants are indexed by this ID in the participant map.

**Kind** : instance property of `RTKParticipant`  


### participant.userId

The user ID of the participant.

**Kind** : instance property of `RTKParticipant`  


### participant.name

The name of the participant.

**Kind** : instance property of `RTKParticipant`  


### participant.picture

The picture of the participant.

**Kind** : instance property of `RTKParticipant`  


### participant.customParticipantId

The custom id of the participant set during <https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant>[ ↗︎](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant) REST API

**Kind** : instance property of `RTKParticipant`  


### participant.device

The device configuration of the participant.

**Kind** : instance property of `RTKParticipant`  


### participant.videoTrack

The participant's video track.

**Kind** : instance property of `RTKParticipant`  


### participant.audioTrack

The participant's audio track.

**Kind** : instance property of `RTKParticipant`  


### participant.screenShareTracks

The participant's screenshare video and audio track.

**Kind** : instance property of `RTKParticipant`  


### participant.videoEnabled

This is true if the participant's video is enabled.

**Kind** : instance property of `RTKParticipant`  


### participant.audioEnabled

This is true if the participant's audio is enabled.

**Kind** : instance property of `RTKParticipant`  


### participant.screenShareEnabled

This is true if the participant is screensharing.

**Kind** : instance property of `RTKParticipant`  


### participant.producers

producers created by participant

**Kind** : instance property of `RTKParticipant`  


### participant.manualProducerConfig

producer config passed during manual subscription

**Kind** : instance property of `RTKParticipant`  


### participant.supportsRemoteControl

This is true if the participant supports remote control.

**Kind** : instance property of `RTKParticipant`  


### participant.presetName

The preset of the participant.

**Kind** : instance property of `RTKParticipant`  


### participant.stageStatus

Denotes the participants's current stage status.

**Kind** : instance property of `RTKParticipant`  


### participant.isPinned

Returns true if the participant is pinned.

**Kind** : instance property of `RTKParticipant`  


### participant.pin()

Returns `participant.id` if user has permission to pin participants.

**Kind** : instance method of `RTKParticipant`  


### participant.unpin()

Returns `participant.id` if user has permission to unpin participants.

**Kind** : instance method of `RTKParticipant`  


### participant.disableAudio()

Disables audio for this participant. Requires the permission to disable participant audio.

**Kind** : instance method of `RTKParticipant`  


### participant.kick()

Kicks this participant from the meeting. Requires the permission to kick a participant.

**Kind** : instance method of `RTKParticipant`  


### participant.disableVideo()

Disables video for this participant. Requires the permission to disable video for a participant.

**Kind** : instance method of `RTKParticipant`  


### participant.registerVideoElement(videoElem)

**Kind** : instance method of `RTKParticipant`

Param | Type  
---|---  
videoElem | `HTMLVideoElement`  
  
### participant.deregisterVideoElement([videoElem])

**Kind** : instance method of `RTKParticipant`

Param | Type  
---|---  
[videoElem] | `HTMLVideoElement`  
  
[PreviousRTKMeta](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/)[NextRTKParticipants](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkparticipants/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKParticipant.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

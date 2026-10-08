---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkselfmedia/
title: RTKSelfMedia \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:57.417713+00:00
---

# RTKSelfMedia · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkselfmedia/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKSelfMedia



# RTKSelfMedia

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkselfmedia/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview meeting.self.audioTrack meeting.self.rawAudioTrack meeting.self.mediaPermissions meeting.self.videoTrack meeting.self.rawVideoTrack meeting.self.screenShareTracks meeting.self.audioEnabled meeting.self.videoEnabled meeting.self.screenShareEnabled meeting.self.addAudioMiddleware(audioMiddleware) meeting.self.removeAudioMiddleware(audioMiddleware) meeting.self.removeAllAudioMiddlewares() meeting.self.addVideoMiddleware(videoMiddleware) meeting.self.setVideoMiddlewareGlobalConfig(config) meeting.self.removeVideoMiddleware(videoMiddleware) meeting.self.removeAllVideoMiddlewares() meeting.self.getCurrentDevices() meeting.self.getAudioDevices() meeting.self.getVideoDevices() meeting.self.getSpeakerDevices() meeting.self.getDeviceById(deviceId, kind) meeting.self.setDevice(device)

The RTKSelfMedia class provides methods to manage the local participant's media.

  * RTKSelfMedia
    * .audioTrack
    * .rawAudioTrack
    * .mediaPermissions
    * .videoTrack
    * .rawVideoTrack
    * .screenShareTracks
    * .audioEnabled
    * .videoEnabled
    * .screenShareEnabled
    * .addAudioMiddleware(audioMiddleware)
    * .removeAudioMiddleware(audioMiddleware)
    * .removeAllAudioMiddlewares()
    * .addVideoMiddleware(videoMiddleware)
    * .setVideoMiddlewareGlobalConfig(config)
    * .removeVideoMiddleware(videoMiddleware)
    * .removeAllVideoMiddlewares()
    * .getCurrentDevices()
    * .getAudioDevices()
    * .getVideoDevices()
    * .getSpeakerDevices()
    * .getDeviceById(deviceId, kind)
    * .setDevice(device)



### meeting.self.audioTrack

Returns the `audioTrack`.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.rawAudioTrack

Returns the `rawAudioTrack` having no middleware executed on it.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.mediaPermissions

Returns the current audio and video permissions given by the user. 'ACCEPTED' if the user has given permission to use the media. 'CANCELED' if the user has canceled the screenshare. 'DENIED' if the user has denied permission to use the media. 'SYS_DENIED' if the user's system has denied permission to use the media. 'UNAVAILABLE' if the media is not available (or being used by a different application).

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.videoTrack

Returns the `videoTrack`.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.rawVideoTrack

Returns the `videoTrack` having no middleware executed on it.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.screenShareTracks

Returns the screen share tracks.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.audioEnabled

Returns true if audio is enabled.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.videoEnabled

Returns true if video is enabled.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.screenShareEnabled

Returns true if screen share is enabled.

**Kind** : instance property of `RTKSelfMedia`  


### meeting.self.addAudioMiddleware(audioMiddleware)

Adds the audio middleware to be executed on the raw audio stream. If there are more than 1 audio middlewares, they will be executed in the sequence they were added in. If you want the sequence to be altered, please remove all previous middlewares and re-add.

**Kind** : instance method of `RTKSelfMedia`

Param | Type  
---|---  
audioMiddleware | `AudioMiddleware`  
  
### meeting.self.removeAudioMiddleware(audioMiddleware)

Removes the audio middleware, if it is there.

**Kind** : instance method of `RTKSelfMedia`

Param | Type  
---|---  
audioMiddleware | `AudioMiddleware`  
  
### meeting.self.removeAllAudioMiddlewares()

Removes all audio middlewares, if they are there.

**Kind** : instance method of `RTKSelfMedia`  


### meeting.self.addVideoMiddleware(videoMiddleware)

Adds the video middleware to be executed on the raw video stream. If there are more than 1 video middlewares, they will be executed in the sequence they were added in. If you want the sequence to be altered, please remove all previous middlewares and re-add.

**Kind** : instance method of `RTKSelfMedia`

Param | Type  
---|---  
videoMiddleware | `VideoMiddleware`  
  
### meeting.self.setVideoMiddlewareGlobalConfig(config)

Sets global config to be used by video middlewares.

**Kind** : instance method of `RTKSelfMedia`

Param | Type | Description  
---|---|---  
config | `VideoMiddlewareGlobalConfig` | config  
config.disablePerFrameCanvasRendering | `boolean` | If set to true, Instead of calling Middleware for every frame, Middleware will only be called once that too with empty canvas, it is the responsibility of the middleware author to keep updating this canvas. `meeting.self.rawVideoTrack` can be used to retrieve video track for the periodic updates.  
  
### meeting.self.removeVideoMiddleware(videoMiddleware)

Removes the video middleware, if it is there.

**Kind** : instance method of `RTKSelfMedia`

Param | Type  
---|---  
videoMiddleware | `VideoMiddleware`  
  
### meeting.self.removeAllVideoMiddlewares()

Removes all video middlewares, if they are there.

**Kind** : instance method of `RTKSelfMedia`  


### meeting.self.getCurrentDevices()

Returns the media devices currently being used.

**Kind** : instance method of `RTKSelfMedia`  


### meeting.self.getAudioDevices()

Returns the local participant's audio devices.

**Kind** : instance method of `RTKSelfMedia`  


### meeting.self.getVideoDevices()

Returns the local participant's video devices.

**Kind** : instance method of `RTKSelfMedia`  


### meeting.self.getSpeakerDevices()

Returns the local participant's speaker devices.

**Kind** : instance method of `RTKSelfMedia`  


### meeting.self.getDeviceById(deviceId, kind)

Returns the local participant's device, indexed by ID and kind.

**Kind** : instance method of `RTKSelfMedia`

Param | Type | Description  
---|---|---  
deviceId | `string` | The ID of the device.  
kind | `'audio'` | `'video'` | `'speaker'` | The kind of the device: audio, video, or speaker.  
  
### meeting.self.setDevice(device)

Change the current media device that is being used by the local participant.

**Kind** : instance method of `RTKSelfMedia`

Param | Type | Description  
---|---|---  
device | `MediaDeviceInfo` | The device that is to be used. A device of the same `kind` will be replaced. the primary stream.  
  
[PreviousRTKSelf](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkself/)[NextRTKStage](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKSelfMedia.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

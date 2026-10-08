---
url: https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/
title: Local Participant \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:59.733904+00:00
---

# Local Participant · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)
  5. /Local Participant



# Local Participant

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntroductionProperties Metadata Properties Audio control Get available devices Register video element Deregister video element Use UI Kit component Manage video element manually Get video view Manage lifecycle Complete Example Get video view Manage lifecycle Example Room joinedPin and Unpin Update Video Constraints Update Screenshare Constraints

Manage local user media devices, control audio, video, and screenshare, and handle events in RealtimeKit meetings.

Prerequisites

Initialize the SDK and understand the meeting object structure. Refer to [Initialize SDK](https://developers.cloudflare.com/realtime/realtimekit/core/) and [Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/).

## Introduction

The local user is accessible via `meeting.self` and contains all information and methods related to the current participant. This includes media controls, device management, participant metadata, and state information.

## Properties

WebMobile

ReactWeb ComponentsAngular

### Metadata Properties

Access participant identifiers and display information:
    
    
    // Participant identifiers
    meeting.self.id; // Peer ID (unique per session)
    meeting.self.userId; // User ID (persistent across sessions)
    meeting.self.customParticipantId; // Custom identifier set by developer
    meeting.self.name; // Display name
    meeting.self.picture; // Display picture URL
    
    
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react";
    
    // Participant identifiers
    const id = useRealtimeKitSelector((m) => m.self.id);
    const userId = useRealtimeKitSelector((m) => m.self.userId);
    const customParticipantId = useRealtimeKitSelector(
    	(m) => m.self.customParticipantId,
    );
    const name = useRealtimeKitSelector((m) => m.self.name);
    const picture = useRealtimeKitSelector((m) => m.self.picture);
    
    
    // Participant identifiers
    meeting.localUser.id // Peer ID (unique per session)
    meeting.localUser.userId // User ID (persistent across sessions)
    meeting.localUser.customParticipantId // Custom identifier set by developer
    meeting.localUser.name // Display name
    meeting.localUser.picture // Display picture URL
    
    
    // Participant identifiers
    meeting.localUser.id // Peer ID (unique per session)
    meeting.localUser.userId // User ID (persistent across sessions)
    meeting.localUser.customParticipantId // Custom identifier set by developer
    meeting.localUser.name // Display name
    meeting.localUser.picture // Display picture URL
    
    
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react-native";
    
    // Participant identifiers
    const id = useRealtimeKitSelector((m) => m.self.id);
    const userId = useRealtimeKitSelector((m) => m.self.userId);
    const customParticipantId = useRealtimeKitSelector(
    	(m) => m.self.customParticipantId,
    );
    const name = useRealtimeKitSelector((m) => m.self.name);
    const picture = useRealtimeKitSelector((m) => m.self.picture);

### Media Properties

Access the local user's media tracks and states:
    
    
    // Media state flags
    meeting.self.audioEnabled; // Boolean: Is audio enabled?
    meeting.self.videoEnabled; // Boolean: Is video enabled?
    meeting.self.screenShareEnabled; // Boolean: Is screen share active?
    
    // Media tracks (MediaStreamTrack objects)
    meeting.self.audioTrack; // Audio MediaStreamTrack (available when audioEnabled is true)
    meeting.self.videoTrack; // Video MediaStreamTrack (available when videoEnabled is true)
    meeting.self.screenShareTracks; // Object: { video: MediaStreamTrack, audio?: MediaStreamTrack }
    
    // Permissions granted by user
    meeting.self.mediaPermissions; // Current audio/video permissions
    
    
    // Media state flags
    const audioEnabled = useRealtimeKitSelector((m) => m.self.audioEnabled);
    const videoEnabled = useRealtimeKitSelector((m) => m.self.videoEnabled);
    const screenShareEnabled = useRealtimeKitSelector(
    	(m) => m.self.screenShareEnabled,
    );
    
    // Media tracks (MediaStreamTrack objects)
    const audioTrack = useRealtimeKitSelector((m) => m.self.audioTrack);
    const videoTrack = useRealtimeKitSelector((m) => m.self.videoTrack);
    const screenShareTracks = useRealtimeKitSelector(
    	(m) => m.self.screenShareTracks,
    );
    
    // Permissions granted by user
    const mediaPermissions = useRealtimeKitSelector((m) => m.self.mediaPermissions);
    
    
    // Media state flags
    meeting.localUser.audioEnabled // Boolean: Is audio enabled?
    meeting.localUser.videoEnabled // Boolean: Is video enabled?
    meeting.localUser.screenShareEnabled // Boolean: Is screen share active?
    
    // Permissions granted by user
    meeting.localUser.isCameraPermissionGranted // Camera permission status
    meeting.localUser.isMicrophonePermissionGranted // Microphone permission status
    
    
    // Media state flags
    meeting.localUser.audioEnabled // Boolean: Is audio enabled?
    meeting.localUser.videoEnabled // Boolean: Is video enabled?
    meeting.localUser.screenShareEnabled // Boolean: Is screen share active?
    
    // Permissions granted by user
    meeting.localUser.isCameraPermissionGranted // Camera permission status
    meeting.localUser.isMicrophonePermissionGranted // Microphone permission status
    
    
    // Media state flags
    const audioEnabled = useRealtimeKitSelector((m) => m.self.audioEnabled);
    const videoEnabled = useRealtimeKitSelector((m) => m.self.videoEnabled);
    const screenShareEnabled = useRealtimeKitSelector(
    	(m) => m.self.screenShareEnabled,
    );
    
    // Media tracks (MediaStreamTrack objects)
    const audioTrack = useRealtimeKitSelector((m) => m.self.audioTrack);
    const videoTrack = useRealtimeKitSelector((m) => m.self.videoTrack);
    const screenShareTracks = useRealtimeKitSelector(
    	(m) => m.self.screenShareTracks,
    );
    
    // Permissions granted by user
    const mediaPermissions = useRealtimeKitSelector((m) => m.self.mediaPermissions);

### State Properties

Access room state and participant status:
    
    
    // Room state
    meeting.self.roomJoined; // Boolean: Has joined the meeting?
    meeting.self.roomState; // Current room state (see possible values below)
    meeting.self.isPinned; // Boolean: Is the local user pinned?
    
    // Permissions and config
    meeting.self.permissions; // Capabilities defined by preset
    meeting.self.config; // Configuration for meeting appearance

**Room state values:**

  * `'init'` \- Initialized but not joined
  * `'joined'` \- Successfully joined the meeting
  * `'waitlisted'` \- Waiting in the waiting room
  * `'rejected'` \- Entry rejected
  * `'kicked'` \- Removed from meeting
  * `'left'` \- Left the meeting
  * `'ended'` \- Meeting has ended
  * `'disconnected'` \- Disconnected from meeting


    
    
    // Room state
    const roomJoined = useRealtimeKitSelector((m) => m.self.roomJoined);
    const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    const isPinned = useRealtimeKitSelector((m) => m.self.isPinned);
    
    // Permissions and config
    const permissions = useRealtimeKitSelector((m) => m.self.permissions);
    const config = useRealtimeKitSelector((m) => m.self.config);

**Example: Conditional rendering based on room state**
    
    
     const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    
    return (
    	<>
    		{roomState === "disconnected" && <div>You are disconnected</div>}
    		{roomState === "waitlisted" && <div>Waiting for host to admit you</div>}
    		{roomState === "joined" && <div>You are in the meeting</div>}
    	</>
    );

**Room state values:**

  * `'init'` \- Initialized but not joined
  * `'joined'` \- Successfully joined the meeting
  * `'waitlisted'` \- Waiting in the waiting room
  * `'rejected'` \- Entry rejected
  * `'kicked'` \- Removed from meeting
  * `'left'` \- Left the meeting
  * `'ended'` \- Meeting has ended
  * `'disconnected'` \- Disconnected from meeting


    
    
    // Room state
    meeting.localUser.roomJoined // Boolean: Has joined the meeting?
    meeting.localUser.waitListStatus // Waitlist status (None, Waiting, Accepted, Rejected)
    meeting.localUser.isPinned // Boolean: Is the local user pinned?
    
    // Permissions and config
    meeting.localUser.permissions // Capabilities defined by preset
    meeting.localUser.presetName // Name of preset for local user
    meeting.localUser.presetInfo // Typed object representing preset information
    
    
    // Room state
    meeting.localUser.roomJoined // Boolean: Has joined the meeting?
    meeting.localUser.waitListStatus // Waitlist status (None, Waiting, Accepted, Rejected)
    meeting.localUser.isPinned // Boolean: Is the local user pinned?
    
    // Permissions and config
    meeting.localUser.permissions // Capabilities defined by preset
    meeting.localUser.presetName // Name of preset for local user
    meeting.localUser.presetInfo // Typed object representing preset information
    
    
    // Room state
    const roomJoined = useRealtimeKitSelector((m) => m.self.roomJoined);
    const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    const isPinned = useRealtimeKitSelector((m) => m.self.isPinned);
    
    // Permissions and config
    const permissions = useRealtimeKitSelector((m) => m.self.permissions);
    const config = useRealtimeKitSelector((m) => m.self.config);

**Example: Conditional rendering based on room state**
    
    
     const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    
    return (
    	<>
    		{roomState === "disconnected" && <Text>You are disconnected</Text>}
    		{roomState === "waitlisted" && <Text>Waiting for host to admit you</Text>}
    		{roomState === "joined" && <Text>You are in the meeting</Text>}
    	</>
    );

**Room state values:**

  * `'init'` \- Initialized but not joined
  * `'joined'` \- Successfully joined the meeting
  * `'waitlisted'` \- Waiting in the waiting room
  * `'rejected'` \- Entry rejected
  * `'kicked'` \- Removed from meeting
  * `'left'` \- Left the meeting
  * `'ended'` \- Meeting has ended
  * `'disconnected'` \- Disconnected from meeting



## Media Controls

### Audio control

Mute and unmute the microphone:
    
    
    // Enable audio (unmute)
    await meeting.self.enableAudio();
    
    // Disable audio (mute)
    await meeting.self.disableAudio();
    
    // Check current status
    const isAudioEnabled = meeting.self.audioEnabled;
    
    
    import { useRealtimeKitClient } from "@cloudflare/realtimekit-react";
    
    function AudioControls() {
    	const [meeting] = useRealtimeKitClient();
    	const audioEnabled = useRealtimeKitSelector((m) => m.self.audioEnabled);
    
    	const toggleAudio = async () => {
    		if (audioEnabled) {
    			await meeting.self.disableAudio();
    		} else {
    			await meeting.self.enableAudio();
    		}
    	};
    
    	return (
    		<button onClick={toggleAudio}>{audioEnabled ? "Mute" : "Unmute"}</button>
    	);
    }
    
    
    // Enable audio (unmute)
    meeting.localUser.enableAudio { error: AudioError? -> }
    
    // Disable audio (mute)
    meeting.localUser.disableAudio { error: AudioError? -> }
    
    // Check current status
    val isAudioEnabled = meeting.localUser.audioEnabled
    
    
    // Enable audio (unmute)
    meeting.localUser.enableAudio { err in }
    
    // Disable audio (mute)
    meeting.localUser.disableAudio { err in }
    
    // Check current status
    let isAudioEnabled = meeting.localUser.audioEnabled
    
    
    import {
    	useRealtimeKitClient,
    	useRealtimeKitSelector,
    } from "@cloudflare/realtimekit-react-native";
    import { TouchableHighlight, Text } from "react-native";
    
    function AudioControls() {
    	const [meeting] = useRealtimeKitClient();
    	const audioEnabled = useRealtimeKitSelector((m) => m.self.audioEnabled);
    
    	const toggleAudio = async () => {
    		if (audioEnabled) {
    			await meeting.self.disableAudio();
    		} else {
    			await meeting.self.enableAudio();
    		}
    	};
    
    	return (
    		<TouchableHighlight onPress={toggleAudio}>
    			<Text>{audioEnabled ? "Mute" : "Unmute"}</Text>
    		</TouchableHighlight>
    	);
    }

### Video control

Enable and disable the camera:
    
    
    // Enable video
    await meeting.self.enableVideo();
    
    // Disable video
    await meeting.self.disableVideo();
    
    // Check current status
    const isVideoEnabled = meeting.self.videoEnabled;
    
    
    function VideoControls() {
    	const [meeting] = useRealtimeKitClient();
    	const videoEnabled = useRealtimeKitSelector((m) => m.self.videoEnabled);
    
    	const toggleVideo = async () => {
    		if (videoEnabled) {
    			await meeting.self.disableVideo();
    		} else {
    			await meeting.self.enableVideo();
    		}
    	};
    
    	return (
    		<button onClick={toggleVideo}>
    			{videoEnabled ? "Stop Video" : "Start Video"}
    		</button>
    	);
    }
    
    
    // Enable video
    meeting.localUser.enableVideo { error: VideoError? -> }
    
    // Disable video
    meeting.localUser.disableVideo { error: VideoError? -> }
    
    // Check current status
    val isVideoEnabled = meeting.localUser.videoEnabled
    
    
    // Enable video
    meeting.localUser.enableVideo { err in }
    
    // Disable video
    meeting.localUser.disableVideo { err in }
    
    // Check current status
    let isVideoEnabled = meeting.localUser.videoEnabled
    
    
    function VideoControls() {
    	const [meeting] = useRealtimeKitClient();
    	const videoEnabled = useRealtimeKitSelector((m) => m.self.videoEnabled);
    
    	const toggleVideo = async () => {
    		if (videoEnabled) {
    			await meeting.self.disableVideo();
    		} else {
    			await meeting.self.enableVideo();
    		}
    	};
    
    	return (
    		<TouchableHighlight onPress={toggleVideo}>
    			<Text>{videoEnabled ? "Stop Video" : "Start Video"}</Text>
    		</TouchableHighlight>
    	);
    }

### Screen share control

Start and stop screen sharing:
    
    
    // Enable screen share
    await meeting.self.enableScreenShare();
    
    // Disable screen share
    await meeting.self.disableScreenShare();
    
    // Check current status
    const isScreenShareEnabled = meeting.self.screenShareEnabled;
    
    
    function ScreenShareControls() {
    	const [meeting] = useRealtimeKitClient();
    	const screenShareEnabled = useRealtimeKitSelector(
    		(m) => m.self.screenShareEnabled,
    	);
    
    	const toggleScreenShare = async () => {
    		if (screenShareEnabled) {
    			await meeting.self.disableScreenShare();
    		} else {
    			await meeting.self.enableScreenShare();
    		}
    	};
    
    	return (
    		<button onClick={toggleScreenShare}>
    			{screenShareEnabled ? "Stop Sharing" : "Share Screen"}
    		</button>
    	);
    }
    
    
    // Enable screen share
    meeting.localUser.enableScreenShare()
    
    // Disable screen share
    meeting.localUser.disableScreenShare()
    
    // Check current status
    val isScreenShareEnabled = meeting.localUser.screenShareEnabled

Android API 14 and above

Declare the following permission in your app's AndroidManifest.xml to use screenshare on Android devices running Android API 14 and above:
    
    
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION" />

Adding this permission requires extra steps on Google Play Console. Refer to [Google's documentation ↗︎](https://support.google.com/googleplay/android-developer/answer/13392821?hl=en#declare) for more information.
    
    
    // Enable screen share
    let err: ScreenShareError? = meeting.localUser.enableScreenShare()
    
    // Disable screen share
    meeting.localUser.disableScreenShare()

Refer to [iOS screen sharing](https://developers.cloudflare.com/realtime/realtimekit/core/ios-screen-sharing/) for platform-specific configuration.
    
    
    function ScreenShareControls() {
    	const [meeting] = useRealtimeKitClient();
    	const screenShareEnabled = useRealtimeKitSelector(
    		(m) => m.self.screenShareEnabled,
    	);
    
    	const toggleScreenShare = async () => {
    		if (screenShareEnabled) {
    			await meeting.self.disableScreenShare();
    		} else {
    			await meeting.self.enableScreenShare();
    		}
    	};
    
    	return (
    		<TouchableHighlight onPress={toggleScreenShare}>
    			<Text>{screenShareEnabled ? "Stop Sharing" : "Share Screen"}</Text>
    		</TouchableHighlight>
    	);
    }

### Change display name

Update the display name before joining the meeting:
    
    
    await meeting.self.setName("New Name");

Note

Name changes only reflect across all participants if done before joining the meeting.
    
    
    await meeting.self.setName("New Name");

Note

Name changes only reflect across all participants if done before joining the meeting.
    
    
    meeting.localUser.setDisplayName("New Name")

Note

Name changes only reflect across all participants if done before joining the meeting.
    
    
    meeting.localUser.setDisplayName(name: "New Name")

Note

Name changes only reflect across all participants if done before joining the meeting.
    
    
    await meeting.self.setName("New Name");

Note

Name changes only reflect across all participants if done before joining the meeting.

## Manage media devices

### Get available devices
    
    
    // Get all media devices
    const devices = await meeting.self.getAllDevices();
    
    // Get all audio input devices (microphones)
    const audioDevices = await meeting.self.getAudioDevices();
    
    // Get all video input devices (cameras)
    const videoDevices = await meeting.self.getVideoDevices();
    
    // Get all audio output devices (speakers)
    const speakerDevices = await meeting.self.getSpeakerDevices();
    
    // Get device by ID
    const device = await meeting.self.getDeviceById("device-id", "audio");
    
    // Get current devices being used
    const currentDevices = meeting.self.getCurrentDevices();
    // Returns: { audio: MediaDeviceInfo, video: MediaDeviceInfo, speaker: MediaDeviceInfo }
    
    
    import { useRealtimeKitClient } from "@cloudflare/realtimekit-react";
    import { useState, useEffect } from "react";
    
    function DeviceSelector() {
    	const [meeting] = useRealtimeKitClient();
    	const [audioDevices, setAudioDevices] = useState([]);
    	const [videoDevices, setVideoDevices] = useState([]);
    
    	useEffect(() => {
    		if (!meeting) return;
    
    		const loadDevices = async () => {
    			const audio = await meeting.self.getAudioDevices();
    			const video = await meeting.self.getVideoDevices();
    			setAudioDevices(audio);
    			setVideoDevices(video);
    		};
    
    		loadDevices();
    	}, [meeting]);
    
    	const handleDeviceChange = async (device) => {
    		await meeting.self.setDevice(device);
    	};
    
    	return (
    		<div>
    			<select
    				onChange={(e) => {
    					const device = audioDevices.find(
    						(d) => d.deviceId === e.target.value,
    					);
    					handleDeviceChange(device);
    				}}
    			>
    				{audioDevices.map((device) => (
    					<option key={device.deviceId} value={device.deviceId}>
    						{device.label}
    					</option>
    				))}
    			</select>
    		</div>
    	);
    }

Get current devices being used:
    
    
    const currentDevices = meeting.self.getCurrentDevices();
    // Returns: { audio: MediaDeviceInfo, video: MediaDeviceInfo, speaker: MediaDeviceInfo }
    
    
    // Get all audio devices
    val audioDevices: List<AudioDevice> = meeting.localUser.getAudioDevices()
    
    // Get all video devices
    val videoDevices: List<VideoDevice> = meeting.localUser.getVideoDevices()
    
    // Get currently selected audio device
    val selectedAudioDevice: AudioDevice = meeting.localUser.getSelectedAudioDevice()
    
    // Get currently selected video device
    val selectedVideoDevice: VideoDevice = meeting.localUser.getSelectedVideoDevice()
    
    
    // Get all audio devices
    let audioDevices = meeting.localUser.getAudioDevices()
    
    // Get all video devices
    let videoDevices = meeting.localUser.getVideoDevices()
    
    // Get currently selected audio device
    let selectedAudioDevice = meeting.localUser.getSelectedAudioDevice()
    
    // Get currently selected video device
    let selectedVideoDevice = meeting.localUser.getSelectedVideoDevice()
    
    
    import { useRealtimeKitClient } from "@cloudflare/realtimekit-react-native";
    import { useState, useEffect } from "react";
    import { FlatList, TouchableHighlight, Text, View } from "react-native";
    
    function DeviceSelector() {
    	const [meeting] = useRealtimeKitClient();
    	const [audioDevices, setAudioDevices] = useState([]);
    	const [videoDevices, setVideoDevices] = useState([]);
    
    	useEffect(() => {
    		if (!meeting) return;
    
    		const loadDevices = async () => {
    			const audio = await meeting.self.getAudioDevices();
    			const video = await meeting.self.getVideoDevices();
    			setAudioDevices(audio);
    			setVideoDevices(video);
    		};
    
    		loadDevices();
    	}, [meeting]);
    
    	const handleDeviceChange = async (device) => {
    		await meeting.self.setDevice(device);
    	};
    
    	return (
    		<View>
    			<FlatList
    				data={audioDevices}
    				renderItem={({ item }) => (
    					<TouchableHighlight onPress={() => handleDeviceChange(item)}>
    						<Text>{item.label}</Text>
    					</TouchableHighlight>
    				)}
    				keyExtractor={(item) => item.deviceId}
    			/>
    		</View>
    	);
    }

Get current devices being used:
    
    
    const currentDevices = meeting.self.getCurrentDevices();
    // Returns: { audio: MediaDeviceInfo, video: MediaDeviceInfo, speaker: MediaDeviceInfo }

### Change device

Switch to a different media device:
    
    
    // Get all devices
    const devices = await meeting.self.getAllDevices();
    
    // Set a specific device (replaces device of the same kind)
    await meeting.self.setDevice(devices[0]);

Use the device selector example from the previous section. The `handleDeviceChange` function demonstrates how to switch devices.
    
    
    // Get all audio devices
    val audioDevices = meeting.localUser.getAudioDevices()
    
    // Set audio device
    meeting.localUser.setAudioDevice(audioDevices[0])
    
    // Get all video devices
    val videoDevices = meeting.localUser.getVideoDevices()
    
    // Set video device
    meeting.localUser.setVideoDevice(videoDevices[0])
    
    // Switch between front and back camera on devices with 2 cameras
    meeting.localUser.switchCamera()
    
    
    // Set audio device
    meeting.localUser.setAudioDevice(device)
    
    // Set video device
    meeting.localUser.setVideoDevice(videoDevice: device)
    
    // Switch between front and back camera
    meeting.localUser.switchCamera()

Use the device selector example from the previous section. The `handleDeviceChange` function demonstrates how to switch devices.
    
    
    const handleDeviceChange = async (device) => {
    	await meeting.self.setDevice(device);
    };

## Display local video

### Register video element

Attach the local video track to a `<video>` element:
    
    
    <video id="local-video" autoplay playsinline></video>
    
    
    const videoElement = document.getElementById("local-video");
    
    // Register the video element to display video
    meeting.self.registerVideoElement(videoElement);
    
    // For local preview (not sent to other users), pass true as second argument
    meeting.self.registerVideoElement(videoElement, true);

### Deregister video element

Remove the video element when no longer needed:
    
    
    meeting.self.deregisterVideoElement(videoElement);

### Use UI Kit component

Display local video with the UI Kit video tile component:
    
    
    import { RtkParticipantTile } from "@cloudflare/realtimekit-react-ui";
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react";
    
    function LocalVideo() {
    	const localUser = useRealtimeKitSelector((m) => m.self);
    
    	return <RtkParticipantTile participant={localUser} />;
    }

### Manage video element manually

Create custom video element implementations:
    
    
    import {
    	useRealtimeKitClient,
    	useRealtimeKitSelector,
    } from "@cloudflare/realtimekit-react";
    import { useEffect, useRef } from "react";
    
    function LocalVideoCustom() {
    	const [meeting] = useRealtimeKitClient();
    	const videoEnabled = useRealtimeKitSelector((m) => m.self.videoEnabled);
    	const videoTrack = useRealtimeKitSelector((m) => m.self.videoTrack);
    	const videoRef = useRef(null);
    
    	useEffect(() => {
    		if (!videoRef.current || !meeting) return;
    
    		// Register video element
    		meeting.self.registerVideoElement(videoRef.current);
    
    		return () => {
    			// Cleanup: deregister on unmount
    			meeting.self.deregisterVideoElement(videoRef.current);
    		};
    	}, [meeting]);
    
    	return (
    		<video
    			ref={videoRef}
    			autoPlay
    			playsInline
    			muted
    			style={{ display: videoEnabled ? "block" : "none" }}
    		/>
    	);
    }

### Get video view

Retrieve a self-preview video view that renders the local camera stream:
    
    
    // Get the self-preview video view
    val videoView = meeting.localUser.getSelfPreview()

For rendering other participants' video, use:
    
    
    // Get video view for camera stream
    val participantVideoView = participant.getVideoView()
    
    // Get video view for screenshare stream
    val screenshareView = participant.getScreenShareVideoView()

### Manage lifecycle

Control video rendering with lifecycle methods:
    
    
    // Start rendering video
    videoView.renderVideo()
    
    // Stop rendering video (but keep the view)
    videoView.stopVideoRender()
    
    // Release native resources when done
    videoView.release()

### Complete Example
    
    
    import android.os.Bundle
    import android.widget.FrameLayout
    import androidx.appcompat.app.AppCompatActivity
    import io.dyte.core.VideoView
    
    class MainActivity : AppCompatActivity() {
        private lateinit var videoView: VideoView
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
    
            // Get the self-preview video view
            videoView = meeting.localUser.getSelfPreview()
    
            // Add to your layout
            val container = findViewById<FrameLayout>(R.id.video_container)
            container.addView(videoView)
    
            // Start rendering
            videoView.renderVideo()
        }
    
        override fun onPause() {
            super.onPause()
            // Stop rendering when activity is paused
            videoView.stopVideoRender()
        }
    
        override fun onResume() {
            super.onResume()
            // Resume rendering when activity is resumed
            videoView.renderVideo()
        }
    
        override fun onDestroy() {
            super.onDestroy()
            // Clean up resources
            videoView.release()
        }
    }

### Get video view

Retrieve video views that render the participant's video streams:
    
    
    // Get video view for local camera stream
    let videoView = meeting.localUser.getVideoView()
    
    // Get video view for screenshare stream
    let screenshareView = meeting.localUser.getScreenShareVideoView()

### Manage lifecycle

The `UIView` handles its own lifecycle automatically and cleans up native resources when it exits the current window. No manual cleanup is required.

### Example
    
    
    import UIKit
    import RealtimeKit
    
    class VideoViewController: UIViewController {
        private var videoView: UIView?
    
        override func viewDidLoad() {
            super.viewDidLoad()
    
            // Get the video view for local camera
            videoView = meeting.localUser.getVideoView()
    
            // Add to your view hierarchy
            if let videoView = videoView {
                videoView.frame = view.bounds
                videoView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
                view.addSubview(videoView)
            }
        }
    }

For screenshare:
    
    
    // Get and display screenshare view
    let screenshareView = meeting.localUser.getScreenShareVideoView()
    if let screenshareView = screenshareView {
        screenshareView.frame = view.bounds
        screenshareView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(screenshareView)
    }
    
    
    import React from "react";
    import { useRealtimeKitSelector } from "@cloudflare/realtimekit-react-native";
    import { MediaStream, RTCView } from "@cloudflare/react-native-webrtc";
    
    export default function VideoView() {
    	const { videoTrack } = useRealtimeKitSelector(
    		(m) => m.participants.active,
    	).toArray()[0];
    	const stream = new MediaStream(undefined);
    	stream.addTrack(videoTrack);
    	return (
    		<RTCView
    			objectFit={"cover"}
    			style={{ flex: 1 }}
    			streamURL={stream.toURL()}
    			mirror={true}
    			zOrder={1}
    		/>
    	);
    }

## Events

### Room joined

Fires when the local user joins the meeting:
    
    
    meeting.self.on("roomJoined", () => {
    	console.log("Successfully joined the meeting");
    });
    
    
    const roomJoined = useRealtimeKitSelector((m) => m.self.roomJoined);
    
    useEffect(() => {
    	if (roomJoined) {
    		console.log("Successfully joined the meeting");
    	}
    }, [roomJoined]);

Or use event listener:
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleRoomJoined = () => {
    		console.log("Successfully joined the meeting");
    	};
    
    	meeting.self.on("roomJoined", handleRoomJoined);
    
    	return () => {
    		meeting.self.off("roomJoined", handleRoomJoined);
    	};
    }, [meeting]);

Android SDK uses a different event model. Monitor `roomJoined` property changes or use listeners for state changes.

iOS SDK uses a different event model. Monitor `roomJoined` property changes or use listeners for state changes.
    
    
    const roomJoined = useRealtimeKitSelector((m) => m.self.roomJoined);
    
    useEffect(() => {
    	if (roomJoined) {
    		console.log("Successfully joined the meeting");
    	}
    }, [roomJoined]);

Or use event listener:
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleRoomJoined = () => {
    		console.log("Successfully joined the meeting");
    	};
    
    	meeting.self.on("roomJoined", handleRoomJoined);
    
    	return () => {
    		meeting.self.off("roomJoined", handleRoomJoined);
    	};
    }, [meeting]);

### Room left

Fires when the local user leaves the meeting:
    
    
    meeting.self.on("roomLeft", ({ state }) => {
    	console.log("Left the meeting with state:", state);
    
    	// Handle different leave states
    	if (state === "left") {
    		console.log("User voluntarily left");
    	} else if (state === "kicked") {
    		console.log("User was kicked from the meeting");
    	} else if (state === "ended") {
    		console.log("Meeting has ended");
    	} else if (state === "disconnected") {
    		console.log("Lost connection to meeting");
    	}
    });

**Possible state values:** `'left'`, `'kicked'`, `'ended'`, `'rejected'`, `'disconnected'`, `'failed'`
    
    
    const roomJoined = useRealtimeKitSelector((m) => m.self.roomJoined);
    
    useEffect(() => {
    	if (!roomJoined) {
    		console.log("Left the meeting");
    	}
    }, [roomJoined]);

Or use event listener for detailed state:
    
    
    meeting.self.on("roomLeft", ({ state }) => {
    	if (state === "left") {
    		console.log("User voluntarily left");
    	} else if (state === "kicked") {
    		console.log("User was kicked");
    	}
    });

Use `RtkSelfEventListener` to monitor when the local user is removed from the meeting:
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
        override fun onRemovedFromMeeting() {
            // display alert that user is no longer in the meeting
        }
    })

iOS SDK uses a different event model. Monitor `roomJoined` property changes or use listeners for state changes.
    
    
    const roomJoined = useRealtimeKitSelector((m) => m.self.roomJoined);
    
    useEffect(() => {
    	if (!roomJoined) {
    		console.log("Left the meeting");
    	}
    }, [roomJoined]);

Or use event listener for detailed state:
    
    
    meeting.self.on("roomLeft", ({ state }) => {
    	if (state === "left") {
    		console.log("User voluntarily left");
    	} else if (state === "kicked") {
    		console.log("User was kicked");
    	}
    });

### Video update

Fires when video is enabled or disabled:
    
    
    meeting.self.on("videoUpdate", ({ videoEnabled, videoTrack }) => {
    	console.log("Video state:", videoEnabled);
    
    	if (videoEnabled) {
    		// Video track is available, can display it
    		const videoElement = document.getElementById("my-video");
    		const stream = new MediaStream();
    		stream.addTrack(videoTrack);
    		videoElement.srcObject = stream;
    		videoElement.play();
    	}
    });
    
    
    const videoEnabled = useRealtimeKitSelector((m) => m.self.videoEnabled);
    const videoTrack = useRealtimeKitSelector((m) => m.self.videoTrack);
    
    useEffect(() => {
    	if (videoEnabled && videoTrack) {
    		console.log("Video is enabled");
    		// Handle video track
    	}
    }, [videoEnabled, videoTrack]);
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
        override fun onVideoUpdate(isEnabled: Boolean) {
            if (isEnabled) {
                // video is enabled, other participants can see local user
            } else {
                // video is disabled, other participants cannot see local user
            }
        }
    })
    
    
    extension MeetingViewModel: RtkSelfEventListener {
        func onVideoUpdate(isEnabled: Bool) {
            if (isEnabled) {
                // video is enabled, other participants can see local user
            } else {
                // video is disabled, other participants cannot see local user
            }
        }
    }
    
    
    const videoEnabled = useRealtimeKitSelector((m) => m.self.videoEnabled);
    const videoTrack = useRealtimeKitSelector((m) => m.self.videoTrack);
    
    useEffect(() => {
    	if (videoEnabled && videoTrack) {
    		console.log("Video is enabled");
    		// Handle video track
    	}
    }, [videoEnabled, videoTrack]);

### Audio update

Fires when audio is enabled or disabled:
    
    
    meeting.self.on("audioUpdate", ({ audioEnabled, audioTrack }) => {
    	console.log("Audio state:", audioEnabled);
    
    	if (audioEnabled) {
    		// Audio track is available
    		console.log("Microphone is on");
    	}
    });
    
    
    const audioEnabled = useRealtimeKitSelector((m) => m.self.audioEnabled);
    const audioTrack = useRealtimeKitSelector((m) => m.self.audioTrack);
    
    useEffect(() => {
    	if (audioEnabled && audioTrack) {
    		console.log("Audio is enabled");
    		// Handle audio track
    	}
    }, [audioEnabled, audioTrack]);
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
        override fun onAudioUpdate(isEnabled: Boolean) {
            if (isEnabled) {
                // audio is enabled, other participants can hear local user
            } else {
                // audio is disabled, other participants cannot hear local user
            }
        }
    })
    
    
    extension MeetingViewModel: RtkSelfEventListener {
        func onAudioUpdate(isEnabled: Bool) {
            if (isEnabled) {
                // audio is enabled, other participants can hear local user
            } else {
                // audio is disabled, other participants cannot hear local user
            }
        }
    }
    
    
    const audioEnabled = useRealtimeKitSelector((m) => m.self.audioEnabled);
    const audioTrack = useRealtimeKitSelector((m) => m.self.audioTrack);
    
    useEffect(() => {
    	if (audioEnabled && audioTrack) {
    		console.log("Audio is enabled");
    		// Handle audio track
    	}
    }, [audioEnabled, audioTrack]);

### Screen share update

Fires when screen sharing starts or stops:
    
    
    meeting.self.on(
    	"screenShareUpdate",
    	({ screenShareEnabled, screenShareTracks }) => {
    		console.log("Screen share state:", screenShareEnabled);
    
    		if (screenShareEnabled) {
    			// Screen share tracks are available
    			const screenElement = document.getElementById("my-screen-share");
    			const stream = new MediaStream();
    			stream.addTrack(screenShareTracks.video);
    			if (screenShareTracks.audio) {
    				stream.addTrack(screenShareTracks.audio);
    			}
    			screenElement.srcObject = stream;
    			screenElement.play();
    		}
    	},
    );
    
    
    const screenShareEnabled = useRealtimeKitSelector(
    	(m) => m.self.screenShareEnabled,
    );
    const screenShareTracks = useRealtimeKitSelector(
    	(m) => m.self.screenShareTracks,
    );
    
    useEffect(() => {
    	if (screenShareEnabled && screenShareTracks) {
    		console.log("Screen sharing is active");
    		// Handle screen share tracks
    	}
    }, [screenShareEnabled, screenShareTracks]);
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
        override fun onScreenShareStartFailed(reason: String) {
            // screen share failed to start
        }
    
        override fun onScreenShareUpdate(isEnabled: Boolean) {
            if (isEnabled) {
                // screen share is enabled
            } else {
                // screen share is disabled
            }
        }
    })
    
    
    meeting.addSelfEventListener(self)
    
    extension MeetingViewModel: RtkSelfEventListener {
        func onRemovedFromMeeting() {
            // User was removed from the meeting (kicked or meeting ended)
            // Display alert or navigate to exit screen
        }
    
        func onMeetingRoomDisconnected() {
            // Lost connection to the meeting room
            // Display reconnection UI or error message
        }
    }

You can also monitor the `roomJoined` property for state changes:
    
    
    let isInMeeting = meeting.localUser.roomJoined
    
    
    const screenShareEnabled = useRealtimeKitSelector(
    	(m) => m.self.screenShareEnabled,
    );
    const screenShareTracks = useRealtimeKitSelector(
    	(m) => m.self.screenShareTracks,
    );
    
    useEffect(() => {
    	if (screenShareEnabled && screenShareTracks) {
    		console.log("Screen sharing is active");
    		// Handle screen share tracks
    	}
    }, [screenShareEnabled, screenShareTracks]);

### Device update

Fires when the active device changes:
    
    
    meeting.self.on("deviceUpdate", ({ device }) => {
    	// Handle device change
    	if (device.kind === "audioinput") {
    		console.log("Microphone changed:", device.label);
    	} else if (device.kind === "videoinput") {
    		console.log("Camera changed:", device.label);
    	} else if (device.kind === "audiooutput") {
    		console.log("Speaker changed:", device.label);
    	}
    });
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleDeviceUpdate = ({ device }) => {
    		if (device.kind === "audioinput") {
    			console.log("Microphone changed:", device.label);
    		} else if (device.kind === "videoinput") {
    			console.log("Camera changed:", device.label);
    		}
    	};
    
    	meeting.self.on("deviceUpdate", handleDeviceUpdate);
    
    	return () => {
    		meeting.self.off("deviceUpdate", handleDeviceUpdate);
    	};
    }, [meeting]);
    
    
    meeting.self.addSelfEventListener(object : RtkSelfEventListener() {
        override fun onAudioDeviceChanged(device: AudioDevice) {
            // Handle audio device change
            println("Audio device changed: ${device.label}")
        }
    
        override fun onVideoDeviceChanged(device: VideoDevice) {
            // Handle video device change
            println("Video device changed: ${device.label}")
        }
    })
    
    
    meeting.self.addSelfEventListener(self)
    
    // RtkSelfEventListener implementation
    func onAudioDeviceChanged(device: AudioDevice) {
        // Handle audio device change
        print("Audio device changed: \(device.label)")
    }
    
    func onVideoDeviceChanged(device: VideoDevice) {
        // Handle video device change
        print("Video device changed: \(device.label)")
    }
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleDeviceUpdate = ({ device }) => {
    		if (device.kind === "audioinput") {
    			console.log("Microphone changed:", device.label);
    		} else if (device.kind === "videoinput") {
    			console.log("Camera changed:", device.label);
    		}
    	};
    
    	meeting.self.on("deviceUpdate", handleDeviceUpdate);
    
    	return () => {
    		meeting.self.off("deviceUpdate", handleDeviceUpdate);
    	};
    }, [meeting]);

### Device List Update

Triggered when the list of available devices changes (device plugged in or out):
    
    
    meeting.self.on("deviceListUpdate", ({ added, removed, devices }) => {
    	console.log("Device list updated");
    	console.log("Added devices:", added);
    	console.log("Removed devices:", removed);
    	console.log("All devices:", devices);
    });
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleDeviceListUpdate = ({ added, removed, devices }) => {
    		console.log("Device list updated");
    		console.log("Added devices:", added);
    		console.log("Removed devices:", removed);
    		console.log("All devices:", devices);
    	};
    
    	meeting.self.on("deviceListUpdate", handleDeviceListUpdate);
    
    	return () => {
    		meeting.self.off("deviceListUpdate", handleDeviceListUpdate);
    	};
    }, [meeting]);
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
        // Triggered when audio devices are added or removed
        override fun onAudioDevicesUpdated() {
            val audioDevices = meeting.localUser.getAudioDevices()
            // Update UI with new audio device list
        }
    })
    
    
    meeting.addSelfEventListener(object: RtkSelfEventListener {
        // Triggered when audio devices are added or removed
        func onAudioDevicesUpdated() {
            let audioDevices = meeting.localUser.getAudioDevices()
            // Update UI with new audio device list
        }
    })
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleDeviceListUpdate = ({ added, removed, devices }) => {
    		console.log("Device list updated");
    		console.log("Added devices:", added);
    		console.log("Removed devices:", removed);
    		console.log("All devices:", devices);
    	};
    
    	meeting.self.on("deviceListUpdate", handleDeviceListUpdate);
    
    	return () => {
    		meeting.self.off("deviceListUpdate", handleDeviceListUpdate);
    	};
    }, [meeting]);

### Network Quality Score

Monitor your own network quality:
    
    
    meeting.self.on(
    	"mediaScoreUpdate",
    	({ kind, isScreenshare, score, scoreStats }) => {
    		if (kind === "video") {
    			console.log(
    				`Your ${isScreenshare ? "screenshare" : "video"} quality score is`,
    				score,
    			);
    		}
    
    		if (kind === "audio") {
    			console.log("Your audio quality score is", score);
    		}
    
    		if (score < 5) {
    			console.log("Your media quality is poor");
    		}
    	},
    );

The `scoreStats` object provides detailed statistics:
    
    
    // Audio Producer
    {
      "kind": "audio",
      "isScreenshare": false,
      "score": 10,
      "participantId": "meeting.self.id",
      "scoreStats": {
        "score": 10,
        "bitrate": 22452,
        "packetsLostPercentage": 0,
        "jitter": 0,
        "isScreenShare": false
      }
    }
    
    // Video Producer
    {
      "kind": "video",
      "isScreenshare": false,
      "score": 10,
      "participantId": "meeting.self.id",
      "scoreStats": {
        "score": 10,
        "frameWidth": 640,
        "frameHeight": 480,
        "framesPerSecond": 24,
        "jitter": 0,
        "isScreenShare": false,
        "packetsLostPercentage": 0,
        "bitrate": 576195,
        "cpuLimitations": false,
        "bandwidthLimitations": false
      }
    }
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleMediaScoreUpdate = ({
    		kind,
    		isScreenshare,
    		score,
    		scoreStats,
    	}) => {
    		if (kind === "video") {
    			console.log(
    				`Your ${isScreenshare ? "screenshare" : "video"} quality score is`,
    				score,
    			);
    		}
    
    		if (score < 5) {
    			console.log("Your media quality is poor");
    		}
    	};
    
    	meeting.self.on("mediaScoreUpdate", handleMediaScoreUpdate);
    
    	return () => {
    		meeting.self.off("mediaScoreUpdate", handleMediaScoreUpdate);
    	};
    }, [meeting]);

Android SDK does not currently expose network quality scores.

iOS SDK does not currently expose network quality scores.
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handleMediaScoreUpdate = ({
    		kind,
    		isScreenshare,
    		score,
    		scoreStats,
    	}) => {
    		if (kind === "video") {
    			console.log(
    				`Your ${isScreenshare ? "screenshare" : "video"} quality score is`,
    				score,
    			);
    		}
    
    		if (score < 5) {
    			console.log("Your media quality is poor");
    		}
    	};
    
    	meeting.self.on("mediaScoreUpdate", handleMediaScoreUpdate);
    
    	return () => {
    		meeting.self.off("mediaScoreUpdate", handleMediaScoreUpdate);
    	};
    }, [meeting]);

### Permission Updates

Triggered when permissions are updated dynamically:
    
    
    // Listen to specific permission updates
    meeting.self.permissions.on("chatUpdate", () => {
    	console.log("Chat permissions updated");
    	// Check meeting.self.permissions for updated permissions
    });
    
    meeting.self.permissions.on("pollsUpdate", () => {
    	console.log("Polls permissions updated");
    });
    
    meeting.self.permissions.on("pluginsUpdate", () => {
    	console.log("Plugins permissions updated");
    });
    
    // Listen to all permission updates
    meeting.self.permissions.on("*", () => {
    	console.log("Permissions updated");
    });

Monitor permissions using selectors:
    
    
    const permissions = useRealtimeKitSelector((m) => m.self.permissions);
    
    useEffect(() => {
    	console.log("Permissions updated:", permissions);
    }, [permissions]);

Android SDK uses a different permissions model. Refer to the Android-specific documentation.

iOS SDK uses a different permissions model. Refer to the iOS-specific documentation.

Monitor permissions using selectors:
    
    
    const permissions = useRealtimeKitSelector((m) => m.self.permissions);
    
    useEffect(() => {
    	console.log("Permissions updated:", permissions);
    }, [permissions]);

### Media Permission Errors

Triggered when media permissions are denied or media capture fails:
    
    
    meeting.self.on("mediaPermissionError", ({ message, kind }) => {
    	console.log(`Failed to capture ${kind}: ${message}`);
    
    	// Handle different error types
    	if (message === "DENIED") {
    		console.log("User denied permission");
    	} else if (message === "SYSTEM_DENIED") {
    		console.log("System denied permission");
    	} else if (message === "COULD_NOT_START") {
    		console.log("Failed to start media stream");
    	}
    });

**Possible values:**

  * `message`: `'DENIED'`, `'SYSTEM_DENIED'`, `'COULD_NOT_START'`
  * `kind`: `'audio'`, `'video'`, `'screenshare'`


    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handlePermissionError = ({ message, kind }) => {
    		console.log(`Failed to capture ${kind}: ${message}`);
    
    		if (message === "DENIED") {
    			// Show UI to guide user to grant permissions
    		}
    	};
    
    	meeting.self.on("mediaPermissionError", handlePermissionError);
    
    	return () => {
    		meeting.self.off("mediaPermissionError", handlePermissionError);
    	};
    }, [meeting]);
    
    
    meeting.addSelfEventListener(object : RtkSelfEventListener {
        override fun onMeetingRoomJoinedWithoutCameraPermission() {
            // meeting joined without camera permission
        }
    
        override fun onMeetingRoomJoinedWithoutMicPermission() {
            // meeting joined without microphone permission
        }
    })
    
    
    meeting.addSelfEventListener(self)
    
    extension MeetingViewModel: RtkSelfEventListener {
        func onMeetingRoomJoinedWithoutCameraPermission() {
            // meeting joined without camera permission
        }
    
        func onMeetingRoomJoinedWithoutMicPermission() {
            // meeting joined without microphone permission
        }
    }

You can also check permission status using properties:
    
    
    let hasCameraPermission = meeting.localUser.isCameraPermissionGranted
    let hasMicPermission = meeting.localUser.isMicrophonePermissionGranted
    
    
    useEffect(() => {
    	if (!meeting) return;
    
    	const handlePermissionError = ({ message, kind }) => {
    		console.log(`Failed to capture ${kind}: ${message}`);
    
    		if (message === "DENIED") {
    			// Show UI to guide user to grant permissions
    		}
    	};
    
    	meeting.self.on("mediaPermissionError", handlePermissionError);
    
    	return () => {
    		meeting.self.off("mediaPermissionError", handlePermissionError);
    	};
    }, [meeting]);

### Waitlist Status

For meetings with waiting room enabled:

Monitor the `roomState` property for waitlist status. The value `'waitlisted'` indicates the user is in the waiting room.
    
    
    const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    
    useEffect(() => {
    	if (roomState === "waitlisted") {
    		console.log("Waiting for host to admit you");
    	}
    }, [roomState]);
    
    
    // Get current waitlist status
    val waitListStatus = meeting.localUser.waitListStatus
    
    // Listen to waitlist status changes
    meeting.addSelfEventListener(object : RtkSelfEventListener {
        override fun onWaitListStatusUpdate(waitListStatus: WaitListStatus) {
            // handle waitlist status here
        }
    })
    
    
    // Get current waitlist status
    let waitListStatus = meeting.localUser.waitListStatus
    
    // Listen to waitlist status changes
    extension MeetingViewModel: RtkSelfEventListener {
        func onWaitlistedUpdate() {
            // handle waitlist update
        }
    }
    
    
    const roomState = useRealtimeKitSelector((m) => m.self.roomState);
    
    useEffect(() => {
    	if (roomState === "waitlisted") {
    		console.log("Waiting for host to admit you");
    	}
    }, [roomState]);

### iOS-Specific Events

The iOS SDK provides additional platform-specific events:

#### Proximity Sensor

Triggered when the proximity sensor detects a change (useful for earpiece detection):
    
    
    extension MeetingViewModel: RtkSelfEventListener {
        func onProximityChanged() {
            // Handle proximity sensor change
            // Useful for detecting when device is near user's ear
        }
    }

#### Webinar Events

For webinar-specific functionality:
    
    
    extension MeetingViewModel: RtkSelfEventListener {
        func onWebinarPresentRequestReceived() {
            // Handle request to present in webinar
        }
    
        func onStoppedPresenting() {
            // Handle stopped presenting in webinar
        }
    }

#### Room Messages

Listen to broadcast messages in the room:
    
    
    extension MeetingViewModel: RtkSelfEventListener {
        func onRoomMessage() {
            // Handle room broadcast message
        }
    }

## Pin and Unpin

Pin or unpin yourself in the meeting (requires appropriate permissions):

Web SDK does not currently support pinning the local participant.

Web SDK does not currently support pinning the local participant.

Android SDK does not currently support pinning the local participant.
    
    
    // Pin yourself
    meeting.localUser.pin()
    
    // Unpin yourself
    meeting.localUser.unpin()
    
    // Check if pinned
    let isPinned = meeting.localUser.isPinned
    
    
    // Pin yourself
    await meeting.self.pin();
    
    // Unpin yourself
    await meeting.self.unpin();
    
    // Check if pinned
    const isPinned = meeting.self.isPinned;

## Update Media Constraints

Update video or screenshare resolution at runtime:

Web SDK does not currently expose runtime constraint updates for local participant.

Web SDK does not currently expose runtime constraint updates for local participant.

Android SDK does not currently expose runtime constraint updates.

iOS SDK does not currently expose runtime constraint updates.

### Update Video Constraints

Update camera resolution while already streaming:
    
    
    meeting.self.updateVideoConstraints({
    	width: { ideal: 1920 },
    	height: { ideal: 1080 },
    });

### Update Screenshare Constraints

Update screenshare resolution while already streaming:
    
    
    meeting.self.updateScreenshareConstraints({
    	width: { ideal: 1920 },
    	height: { ideal: 1080 },
    });

[PreviousMeeting Metadata](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-metadata/)[NextiOS screen sharing](https://developers.cloudflare.com/realtime/realtimekit/core/ios-screen-sharing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/local-participant.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

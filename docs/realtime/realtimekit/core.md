---
url: https://developers.cloudflare.com/realtime/realtimekit/core/
title: Build using Core SDK \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:54.316838+00:00
---

# Build using Core SDK · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Build using Core SDK



# Build using Core SDK

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Initialize Core SDK Advanced Options

### Initialize Core SDK

To integrate the Core SDK, you will need to initialize it with a [participant's auth token](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/), and then use the provided SDK APIs to control the peer in the session.

Initialization might differ slightly based on your tech stack. Please choose your preferred tech stack below.

WebMobile

ReactWeb ComponentsAngular

Install the client SDK
    
    
    npm i @cloudflare/realtimekit-react

Use the `useRealtimeKitClient` hook to initialise the SDK.
    
    
    import { useEffect } from 'react';
    import { useRealtimeKitClient } from '@cloudflare/realtimekit-react';
    
    export default function App() {
    	const [meeting, initMeeting] = useRealtimeKitClient();
    
        useEffect(() => {
          const meetingDefaultOptions = {
            audio: true,
            video: true,
          };
    
        	initMeeting({
            authToken: "<auth-token>",
            defaults: meetingDefaultOptions, // optional
          });
        }, []);
    
        useEffect(() => {
        	// next - if (meeting) meeting.join();
        }, [meeting])
    
        return <div></div>;
    
    }

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.

Install the client SDK.
    
    
    npm i @cloudflare/realtimekit

Alternatively, you can also use the CDN.
    
    
    <script src="https://cdn.jsdelivr.net/npm/@cloudflare/realtimekit@latest/dist/browser.js"></script>

You can initialise the SDK using `RealtimeKitClient.init`.
    
    
    	const authToken = <auth-token>;
    
      const meetingDefaultOptions = {
        audio: true,
        video: true,
      };
    
    	RealtimeKitClient.init({
    	  authToken,
    	  defaults: meetingDefaultOptions, // optional
    	}).then((meeting) => {
    		// next - meeting.join();
    	});

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.

Install the client SDK.
    
    
    npm i @cloudflare/realtimekit-angular

You can initialise the SDK using `RealtimeKitClient.init`.
    
    
    class AppComponent {
    	title = "MyProject";
    	@ViewChild("myid") meetingComponent: RtkMeeting;
    	rtkMeeting: RealtimeKitClient;
    
    	async ngAfterViewInit() {
    		const meetingDefaultOptions = {
    			audio: true,
    			video: true,
    		};
    		const meeting = await RealtimeKitClient.init({
    			authToken: "<auth-token>",
    			defaults: meetingDefaultOptions, // optional
    		});
    		// next - meeting.join();
    	}
    }

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.

Initialize the RealtimeKit SDK by obtaining an instance of `RealtimeKitClient` using the `RealtimeKitMeetingBuilder` helper.
    
    
    val meeting = RealtimeKitMeetingBuilder.build(activity)

Configure the meeting properties in the `RtkMeetingInfo` class with a valid participant `authToken` from the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/).
    
    
    val meetingInfo =
      RtkMeetingInfo(
        authToken = authToken,
        enableAudio = true,
        enableVideo = true,
      )

Initialize the meeting by calling the `init()` method. This establishes a connection with the RealtimeKit meeting server.
    
    
    meeting.init(
      meetingInfo,
      onInitCompleted = { ... },
      onInitFailed = { ... },
    )

Initialize the RealtimeKit SDK by creating an instance of `RealtimeKitClient`.
    
    
    let meeting = RealtimeKitiOSClientBuilder().build()

Add the required listeners to receive callbacks for meeting events.
    
    
    meeting.addMeetingRoomEventListener(meetingRoomEventListener: self)
    meeting.addParticipantsEventListener(participantsEventListener: self)
    meeting.addSelfEventListener(selfEventListener: self)

Configure the meeting properties in the `RtkMeetingInfo` class with a valid participant `authToken` from the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/).
    
    
    let meetingInfo = RtkMeetingInfo(authToken: authToken,
                                      enableAudio: true,
                                      enableVideo: true)

Initialize the meeting by calling the `doInit()` method. This establishes a connection with the RealtimeKit meeting server.
    
    
    meeting.doInit(meetingInfo: meetingInfo, onSuccess: {}, onFailure: {_ in})

Initialize the RealtimeKit SDK using the `useRealtimeKitClient` hook.
    
    
    import React from 'react';
    import { View, Text } from 'react-native';
    import { useRealtimeKitClient, RealtimeKitProvider } from '@cloudflare/realtimekit-react-native';
    
    export default function App() {
      const [meeting, initMeeting] = useRealtimeKitClient();
      React.useEffect(() => {
        const init = async () => {
          const meetingOptions = {
            audio: true,
            video: true,
          };
          await initMeeting({
            authToken: 'YourAuthToken',
            defaults: meetingOptions,
          });
        };
        init();
        // next - if (meeting) meeting.joinRoom();
      }, []);
    
      if (meeting) {
        return (
          <RealtimeKitProvider value={meeting}>
            {/* Render your components here */}
          </RealtimeKitProvider>
        );
      } else {
        return (
          <View>
            <Text>Loading...</Text>
          <View>
        )
      }
    }

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.

### Advanced Options

You can **optionally** configure meeting defaults, media quality, screen share preferences, simulcast settings, ice connection behavior, logging, and error handling while initializing the SDK.
    
    
    init({
    	authToken: "<auth_token>",
    	defaults: {
    		video: true,
    		audio: true,
    		mediaConfiguration: {
    			// Configure custom video quality (e.g., 1080p). Disable simulcast using `simulcastConfig` override for single-layer streaming.
    			video: {
    				width: { ideal: 1920 },
    				height: { ideal: 1080 },
    				frameRate: { ideal: 15 },
    			},
    			screenshare: {
    				frameRate: { ideal: 15, max: 30 }, // Default 5
    				displaySurface: "monitor", // Given surface is suggested to the end user
    			},
    		},
    	},
    	overrides: {
    		simulcastConfig: {
    			// If you want to disable simulcast
    			disable: false,
    			// If you want to pass custom simulcast encodings
    			encodings: [
    				{
    					rid: "f", // full / highest quality
    					scaleResolutionDownBy: 1.0,
    					maxBitrate: 2500000, // ~2.5 Mbps
    				},
    				{
    					rid: "h", // half
    					scaleResolutionDownBy: 2.0,
    					maxBitrate: 900000, // ~0.9 Mbps
    				},
    				{
    					rid: "q", // quarter
    					scaleResolutionDownBy: 4.0,
    					maxBitrate: 250000, // ~0.25 Mbps
    				},
    			],
    		},
    		forceRelay: false, // forceRelay, if true, TURN will be preferred over STUN
    	},
    	modules: {
    		devTools: {
    			logs: true, // Prints SDK logs to console, Useful in initial integration phase
    		},
    	},
    	onError: (error) => {
    		console.error(error); // SDK errors, Useful in detecting common issues
    	},
    });

Tip

`onError` callback is used to handle SDK errors. These errors could be due to invalid auth token, network issues, media permissions, etc. Each error is thrown with a unique error code. Learn more about SDK [error codes](https://developers.cloudflare.com/realtime/realtimekit/core/error-codes/).

You can pass the following options as `defaults` to alter default behavior.

Option | Description | Type | Required  
---|---|---|---  
**video** | Should video be enabled by default | `boolean` | false  
**audio** | Should audio be enabled by default | `boolean` | false  
**mediaConfiguration** | Allows you to pass custom media quality constraints | `MediaConfiguration` | false  
**autoSwitchAudioDevice** | Automatically switch to a newly plugged microphone or speaker | `boolean` | false  
**isNonPreferredDevice** | Allows you to set specific devices as "not preferred" | `(device: MediaDeviceInfo) => boolean` | false  
**recording** | Allows you to configure recording settings | RecordingConfig | false  
  
Note

By default, audio and video are auto enabled, as per preset permissions. SDK uses 640x480 quality as default for group calls, which can be overridden with `mediaConfiguration`. By default, the SDK automatically switches to the best available device and marks virtual devices as not preferred.

Reference for the types:
    
    
    interface AudioQualityConstraints {
    	echoCancellation?: boolean;
    	noiseSuppression?: boolean;
    	autoGainControl?: boolean;
    	enableStereo?: boolean;
    	enableHighBitrate?: boolean;
    }
    
    interface VideoQualityConstraints {
    	width: { ideal: number };
    	height: { ideal: number };
    	frameRate?: { ideal: number };
    }
    
    interface ScreenshareQualityConstraints {
    	width?: { max: number };
    	height?: { max: number };
    	frameRate?: {
    		ideal: number;
    		max: number;
    	};
    	displaySurface?: "window" | "monitor" | "browser";
    	selfBrowserSurface?: "include" | "exclude";
    }
    
    interface MediaConfiguration {
    	video?: VideoQualityConstraints;
    	audio?: AudioQualityConstraints;
    	screenshare?: ScreenshareQualityConstraints;
    }
    
    interface RecordingConfig {
    	fileNamePrefix?: string;
    	videoConfig?: {
    		height?: number;
    		width?: number;
    		codec?: string;
    	};
    }
    
    interface DefaultOptions {
    	video?: boolean;
    	audio?: boolean;
    	mediaConfiguration?: MediaConfiguration;
    	isNonPreferredDevice?: (device: MediaDeviceInfo) => boolean;
    	autoSwitchAudioDevice?: boolean;
    	recording?: RecordingConfig;
    }
    
    interface Overrides {
    	simulcastConfig?: {
    		disable?: boolean;
    		encodings?: RTCRtpEncodingParameters[];
    	};
    	forceRelay?: boolean;
    }

You can configure meeting defaults using `enableAudio` and `enableVideo` parameters.

[Previousrtk-waiting-screen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-waiting-screen/)[NextMeeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

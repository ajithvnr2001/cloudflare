---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/
title: Build using UI Kit \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:09.593114+00:00
---

# Build using UI Kit · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Build using UI Kit



# Build using UI Kit

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitialize the SDKCreate a meeting componentDisplay the meetingImport the SDKDisplay the meetingInitialize the SDKLoad the moduleDisplay the meetingInitialize the SDKInitialize and display the meetingInitialize and display the meetingInitialize the SDKDisplay the meetingNext steps Build a custom meeting experience

The default RealtimeKit Meeting UI component gives you a complete meeting experience out of the box, with all the essential features built in. Drop it into your app and you are ready to go.

Select a framework based on the platform you are building for.

WebMobile

ReactWeb ComponentsAngular

Please install the following dependencies into your project repository:
    
    
    npm i @cloudflare/realtimekit-react @cloudflare/realtimekit-react-ui

 _Optional:_ You can also build on top of our ready-made template:
    
    
    git clone https://github.com/cloudflare/realtimekit-web-examples.git
    cd realtimekit-web-examples/react-examples/examples/default-meeting-ui

Please install the following dependencies into your project repository:
    
    
    npm i @cloudflare/realtimekit-web @cloudflare/realtimekit-ui

 _Optional:_ You can also build on top of our ready-made template:
    
    
    git clone https://github.com/cloudflare/realtimekit-web-examples.git
    cd realtimekit-web-examples/html-examples/examples/default-meeting-ui

Please install the following dependencies into your project repository:
    
    
    npm i @cloudflare/realtimekit-angular @cloudflare/realtimekit-angular-ui

 _Optional:_ You can also build on top of our ready-made template:
    
    
    git clone https://github.com/cloudflare/realtimekit-web-examples.git
    cd realtimekit-web-examples/angular-examples/examples/default-meeting-ui

Add the following dependency to your `build.gradle` file:
    
    
    dependencies {
      implementation 'com.cloudflare.realtimekit:ui-android:0.3.0'
    }

Install the RealtimeKit UI Kit using Swift Package Manager:

  1. In Xcode, go to **File > Add Package Dependencies**.
  2. Enter the package URL: `https://github.com/dyte-in/RealtimeKitUI`.
  3. Select the version and add the package to your project.



Add the following entries to the `Info.plist` file. This gives your app permissions to access the camera and microphone, access photos, and install the required fonts and icons.
    
    
    <key>NSBluetoothPeripheralUsageDescription</key>
    <string>Access Bluetooth to connect to headphones and audio devices during calls.</string>
    <key>NSBluetoothAlwaysUsageDescription</key>
    <string>Access Bluetooth to connect to headphones and audio devices during calls.</string>
    <key>NSCameraUsageDescription</key>
    <string>Access camera to enable video during meetings.</string>
    <key>NSMicrophoneUsageDescription</key>
    <string>Access microphone to enable audio during meetings.</string>
    <key>NSPhotoLibraryUsageDescription</key>
    <string>Access photos to share images during meetings.</string>
    <key>UIBackgroundModes</key>
    <array>
      <string>audio</string>
      <string>voip</string>
      <string>fetch</string>
      <string>remote-notification</string>
    </array>

The `UIBackgroundModes` key is used in the `Info.plist` file of an iOS app to declare the app's supported background execution modes. This key is an array of strings that specifies the types of background tasks that the app supports. By declaring the background modes, the app can continue to run in the background and perform specific tasks even when it is not in the foreground.

Note

The use of background modes should be justified and comply with Apple's App Store Review Guidelines. Apps that misuse background modes or unnecessarily run in the background may be rejected during the app review process.

Source: [Apple Developer Documentation: Declaring Your App's Supported Background Tasks ↗︎](https://developer.apple.com/documentation/xcode/configuring-background-execution-modes)

**Minimum requirements:** React Native 0.84 or above, React 19 or above.

Install the dependencies:
    
    
    npm install @cloudflare/realtimekit-react-native @cloudflare/react-native-webrtc @cloudflare/realtimekit-react-native-ui @react-native-documents/picker react-native-file-viewer react-native-fs react-native-sound-player react-native-webview react-native-svg@^15.13.0 react-native-safe-area-context@^5.0.0

**Minimum Expo version:** 56 or above.

Install the dependencies:
    
    
    npx expo install @cloudflare/realtimekit-react-native-ui @cloudflare/realtimekit-react-native @cloudflare/react-native-webrtc @react-native-documents/picker react-native-file-viewer react-native-fs react-native-sound-player react-native-webview react-native-svg@^15.13.0 react-native-safe-area-context@^5.0.0

Install Expo config plugins:
    
    
    npx expo install @expo/config-plugins

Add the plugins to your `app.json`:
    
    
    {
    	"expo": {
    		"plugins": [
    			"@cloudflare/realtimekit-react-native",
    			"@cloudflare/react-native-webrtc"
    		]
    	}
    }

Run `prebuild` to set up native modules:
    
    
    npx expo prebuild

The following instructions are for release builds. Debug builds should work without additional steps.

Edit your `android/gradle.properties` and add the following lines:
    
    
    android.useFullClasspathForDexingTransform=true

Add a required `blob_provider_authority` string resource in the `strings.xml` file:
    
    
    <resources>
      ...
      <string name="blob_provider_authority">YOUR_APP_RESOURCE_NAME</string>
      ...
    </resources>

Create or append to the file `android/app/proguard-rules.pro`:
    
    
    -keep class realtimekit.org.webrtc.** { *; }
    -dontwarn org.chromium.build.BuildHooksAndroid

In your `android/app/build.gradle`, edit the release configuration and add the following line importing the ProGuard configuration:
    
    
    buildTypes {
      release {
        ...
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
      }
    }

#### Background audio and video (Android)

The SDK includes an Android foreground service that keeps audio and video running when the app moves to the background. The service starts automatically when a participant joins a meeting and stops when they leave.

By default the service is enabled with generic notification text. To customize the notification or disable the service, pass `keepAliveService` to the `useRealtimeKitClient` hook before calling `initMeeting`:
    
    
    const [meeting, initMeeting] = useRealtimeKitClient({
      keepAliveService: {
        enabled: true,                        // set to false to disable entirely
        title: "Team call",                   // notification title
        text: "Tap to return to your meeting", // notification body
      },
    });

On Android 13 and above, the SDK automatically requests the `POST_NOTIFICATIONS` permission so the notification appears in the shade. No additional setup is required.

**Minimum supported iOS version: 15.1.**

Open your `Podfile` and set the platform to iOS 15.1:
    
    
    platform :ios, '15.1'

Add the following permission entries to your `Info.plist` file:
    
    
    <key>NSCameraUsageDescription</key>
    <string>Access camera to enable video during meetings.</string>
    <key>NSMicrophoneUsageDescription</key>
    <string>Access microphone to enable audio during meetings.</string>
    <key>NSPhotoLibraryUsageDescription</key>
    <string>Access photos to share images during meetings.</string>
    <key>UIViewControllerBasedStatusBarAppearance</key>
    <false/>

#### Screen sharing (iOS)

iOS screen sharing requires a Broadcast Upload Extension and additional native setup. Refer to the [iOS screen sharing](https://developers.cloudflare.com/realtime/realtimekit/core/ios-screen-sharing/) guide for full instructions.

Once native setup is complete, pass `iOSScreenshareEnabled={true}` to `RtkMeeting` to enable the screen share button in the UI:
    
    
    <RtkMeeting meeting={meeting} iOSScreenshareEnabled={true} />

## Initialize the SDK

Add the following code to your React application:

App.tsxts
    
    
    import { useEffect } from 'react';
    import { useRealtimeKitClient } from '@cloudflare/realtimekit-react';
    
    export default function App() {
      const [meeting, initMeeting] = useRealtimeKitClient();
      useEffect(() => {
        initMeeting({ authToken: '<auth-token>' });
      }, []);
    
      return <div></div>;
    }

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.

## Create a meeting component

Use the `RtkMeeting` component and the `useRealtimeKitMeeting` hook. This hook provides access to the meeting object that contains all the meeting state and methods.

MyMeetingUI.tsxts
    
    
    import { useRealtimeKitMeeting } from '@cloudflare/realtimekit-react';
    import { RtkMeeting } from '@cloudflare/realtimekit-react-ui';
    
    export default function MyMeetingUI() {
      const { meeting } = useRealtimeKitMeeting();
      return (
        <RtkMeeting mode="fill" meeting={meeting} showSetupScreen={true} />
      );
    }

## Display the meeting

Wrap your meeting component in `RealtimeKitProvider`:

App.tsxts
    
    
    import { useEffect } from 'react';
    import { useRealtimeKitClient, RealtimeKitProvider } from '@cloudflare/realtimekit-react';
    import MyMeetingUI from './MyMeetingUI.tsx'
    
    export default function App() {
      const [meeting, initMeeting] = useRealtimeKitClient();
    
      useEffect(() => {
        initMeeting({ authToken: '<auth-token>' });
      }, []);
    
      return (
        <RealtimeKitProvider value={meeting}>
          <MyMeetingUI />
        </RealtimeKitProvider>
      );
    }

## Import the SDK

Add the following imports to your HTML file:

index.htmlhtml
    
    
    <!DOCTYPE html>
    <html lang="en">
    	<head>
    		<!-- Import helper to load UI Kit components -->
    		<script type="module">
    			import { defineCustomElements } from "https://cdn.jsdelivr.net/npm/@cloudflare/realtimekit-ui@latest/loader/index.es2017.js";
    			defineCustomElements();
    		</script>
    		<!-- Import RealtimeKit Core via CDN -->
    		<script src="https://cdn.jsdelivr.net/npm/@cloudflare/realtimekit@latest/dist/browser.js"></script>
    	</head>
    </html>

## Display the meeting

Use the `rtk-meeting` component to render the meeting UI:
    
    
    <body>
    	<rtk-meeting id="my-meeting" show-setup-screen="true" />
    </body>

## Initialize the SDK

Pass the `authToken` and connect the meeting object to the UI component:

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.
    
    
    <script>
    	const authToken = "<auth-token>";
    	// Initialize the SDK
    	RealtimeKitClient.init({
    		authToken,
    	}).then((meeting) => {
    		document.getElementById("my-meeting").meeting = meeting;
    	});
    </script>

## Load the module

Load `RTKComponentsModule` into your app module. This is typically the `app.module.ts` file and allows you to use the UI components in your component HTML files.
    
    
    import { NgModule } from "@angular/core";
    import { BrowserModule } from "@angular/platform-browser";
    import { RTKComponentsModule } from "@cloudflare/realtimekit-angular";
    import { AppComponent } from "./app.component";
    
    @NgModule({
    	declarations: [AppComponent],
    	imports: [BrowserModule, RTKComponentsModule],
    	providers: [],
    	bootstrap: [AppComponent],
    })
    export class AppModule {}

_Optional:_ If you are using TypeScript, set `allowSyntheticDefaultImports` as `true` in your `tsconfig.json`.
    
    
    {
    	"compilerOptions": {
    		"allowSyntheticDefaultImports": true
    	}
    }

## Display the meeting

Load the `RtkMeeting` component in your template file (`component.html`):
    
    
    <rtk-meeting #myid></rtk-meeting>

## Initialize the SDK
    
    
    class AppComponent {
    	title = "MyProject";
    	@ViewChild("myid") meetingComponent: RtkMeeting;
    	rtkMeeting: RealtimeKitClient;
    
    	async ngAfterViewInit() {
    		const meeting = await RealtimeKitClient.init({
    			authToken: "<auth-token>",
    		});
    		meeting.join();
    		this.rtkMeeting = meeting;
    		if (this.meetingComponent) this.meetingComponent.meeting = meeting;
    	}
    }

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.

## Initialize and display the meeting

Create a `RealtimeKitUI` instance with your auth token, then call `startMeeting(completion:)` to get a view controller. Present it to display the full meeting UI.

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.
    
    
    import RealtimeKit
    import RealtimeKitUI
    
    let rtkUI = RealtimeKitUI(
        meetingInfo: RtkMeetingInfo(
            authToken: "<auth-token>",
            enableAudio: true,
            enableVideo: true
        )
    )
    
    let controller = rtkUI.startMeeting {
        // Called when the meeting ends or the user leaves
        self.dismiss(animated: true)
    }
    controller.modalPresentationStyle = .fullScreen
    present(controller, animated: true)

## Initialize and display the meeting

Create an `RtkMeetingInfo` with your auth token, wrap it in `RealtimeKitUIInfo`, build the UI Kit, and call `startMeeting()`.

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.
    
    
    import com.cloudflare.realtimekit.models.RtkMeetingInfo
    import com.cloudflare.realtimekit.ui.RealtimeKitUIBuilder
    import com.cloudflare.realtimekit.ui.RealtimeKitUIInfo
    
    val meetingInfo = RtkMeetingInfo(authToken = "<auth-token>")
    val uiKitInfo = RealtimeKitUIInfo(
        activity = this,
        rtkMeetingInfo = meetingInfo,
    )
    val rtkUIKit = RealtimeKitUIBuilder.build(uiKitInfo)
    rtkUIKit.startMeeting()

## Initialize the SDK

Use the `useRealtimeKitClient` hook from the core React Native package to create a meeting instance: Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.
    
    
    import {
    	useRealtimeKitClient,
    	RealtimeKitProvider,
    } from "@cloudflare/realtimekit-react-native";
    import {
    	RtkMeeting,
    	RtkUIProvider,
    } from "@cloudflare/realtimekit-react-native-ui";
    import React, { useEffect } from "react";
    import { Text } from "react-native";

## Display the meeting

Wrap your app in `RtkUIProvider`, initialize the client, and render `RtkMeeting`:
    
    
    function App() {
      return (
        <RtkUIProvider>
          <Meeting authToken="<auth-token>" />
        </RtkUIProvider>
      );
    }
    
    function Meeting({ authToken }: { authToken: string }) {
      const [meet, initMeeting] = useRealtimeKitClient();
    
      useEffect(() => {
        initMeeting({
          authToken,
          defaults: { audio: true, video: true },
        });
      }, [authToken]);
    
      if (!meet) return <Text>Loading...</Text>;
    
      return (
        <RealtimeKitProvider value={meet}>
          <RtkMeeting meeting={meet} showSetupScreen={true} />
        </RealtimeKitProvider>
      );
    }

## Next steps

You have integrated RealtimeKit with the default meeting UI. Participants can now see and hear each other in sessions.

### Build a custom meeting experience

While the default UI provides a complete meeting experience, you may want to build a custom interface using individual UI Kit components. This approach gives you full control over the layout, design, and user experience.

To build your own custom meeting UI, follow these guides in order:

  1. **[UI Kit Components Library](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/component-library/)** \- Browse available components and their visual representations
  2. **[UI Kit Meeting Lifecycle](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/state-management/)** \- Lifecycle of a meeting and how components communicate and synchronize with each other
  3. **[Session Lifecycle](https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/)** \- Understand different peer states and transitions
  4. **[Meeting Object Explained](https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/)** \- Access meeting data and participant information using the Core SDK
  5. **[Build Your Own UI](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/build-your-own-ui/)** \- Put everything together to create a custom meeting interface



[PreviousSelect SDK(s)](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/)[NextState Management](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/state-management/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

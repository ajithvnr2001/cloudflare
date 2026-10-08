---
url: https://developers.cloudflare.com/realtime/sfu/examples/embedded-devices/
title: Embedded devices and remote control \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:35.250597+00:00
---

# Embedded devices and remote control · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/examples/embedded-devices/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

  4. /[Examples](https://developers.cloudflare.com/realtime/sfu/examples/)
  5. /Embedded devices



# Embedded devices and remote control

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/examples/embedded-devices/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksFollow the firmware integrationRun Pocket RadioReconnect and clean upAdapt to other devices Adapt the pattern to roboticsInspect the implementationTry another example

Use Realtime SFU to connect embedded hardware to browser listeners. Pocket Radio shows how firmware connects over WebRTC, publishes audio and telemetry, and receives authorized control commands from a browser.

Pocket Radio runs on an ESP32-S3. It reads a playlist from flash, publishes Opus audio, and sends spectrum data and device state to browsers. One listener can control playback and the board's LED.

The example is experimental and targets the documented board and toolchain. It does not implement microphone capture, device speaker output, a camera, or a complete robotics stack.

![Pocket Radio with browser playback, spectrum, device telemetry, and controller controls.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2720,height=2724,format=webp/_astro/pocket-radio.DMfiRY4v.png)[Open the example](https://github.com/cloudflare/realtime-examples/tree/main/esp32-radio) [Follow the firmware walkthrough](https://github.com/cloudflare/realtime-examples/blob/main/esp32-radio/firmware/docs/sfu.md)

## How it works

The firmware and each browser maintain a separate WebRTC peer. A Worker holds the SFU credentials and handles signaling. A Durable Object tracks the device, listeners, controller lease, and cleanup.

Embedded WebRTC with Realtime SFU

**Device firmware** ESP32-S3 + Rust / str0mOne peer and UDP socketOpus source + application channels

Opus audio  
robot + spectrum

Commands

Cloudflare**Realtime SFU** One session per endpointAudio and DataChannels

Audio + data

robot replies  
controller only

**Browser listeners** One peer per tabPlay audio, show dataOne authorized controller

HTTPS signaling  
offer, answer, IDs, liveness

SFU HTTPS API  
sessions, tracks, channels

HTTPS signaling  
join, SDP, control lease

Trusted application backend (this example)

**Worker** Device / viewer authenticationSFU credentials

RPC

**RobotRoom Durable Object** Session state + discoveryController lease + cleanup

Device firmwareOpus audio, robot + spectrum →Realtime SFU

Realtime SFUCommands →Device firmware

Realtime SFUAudio + data →Browser listeners

Browser listenersrobot replies, controller only →Realtime SFU

Device firmwareHTTPS signaling ↔Worker

Browser listenersHTTPS signaling ↔Worker

WorkerRPC →RobotRoom Durable Object

RobotRoom Durable ObjectSFU HTTPS API →Realtime SFU

The example uses these paths:

Path | Purpose  
---|---  
Device audio track to browser listeners | Publish pre-encoded Opus audio for playback  
Reliable, ordered `robot` DataChannel | Send telemetry, metadata, commands, and command acknowledgments  
Unordered `spectrum` DataChannel with zero retransmissions | Send replaceable spectrum samples  
Controller replies on `robot` | Return authorized browser commands to the device using `canReply`  
Device and browser signaling to the backend | Authenticate, allocate SFU resources, exchange Session Description Protocol (SDP) offers and answers, and manage application state  
  
SFU App Secrets stay on the Worker. The firmware receives its device credential, Wi-Fi configuration, and signaling origin. This example uses a Worker as its backend. Other application servers can use the same SFU interfaces.

## Follow the firmware integration

The [firmware/SFU walkthrough ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/esp32-radio/firmware/docs/sfu.md) explains the protocol sequence and identifies the code responsible for each step:

  1. Create and configure the firmware's WebRTC peer.
  2. Exchange a session description through the application backend.
  3. Publish the audio track and establish negotiated DataChannels.
  4. Connect a browser listener and acknowledge DataChannel readiness.
  5. Grant the controller reply access and handle device commands.
  6. Retain resource identifiers for teardown and retries.



Keep one owner for the WebRTC peer and its SDP state. Adapt hardware I/O and media timing for your device. You can replace HTTPS device-to-backend signaling with another application protocol, such as Constrained Application Protocol (CoAP). The backend must still call the SFU over HTTPS.

## Run Pocket Radio

The example targets the ESP32-S3-DevKitC-1 N32R16V, with 32 MiB flash, 16 MiB PSRAM, and the documented LED pin. To build it, you need a Linux x86_64 toolchain, Node.js 24, Python, Rust, and ESP-IDF. The board requires outbound IPv4 UDP and HTTPS. Refer to the [complete prerequisites ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/esp32-radio#set-up) for exact tool versions and hardware requirements.

  1. **Prepare the checkout.** Run:
         
         git clone https://github.com/cloudflare/realtime-examples.git
         cd realtime-examples/esp32-radio
         make setup
         cp .credential.env.example .credential.env

  2. **Configure and deploy the backend.** [Create an SFU app](https://developers.cloudflare.com/realtime/sfu/get-started/#create-your-first-app). Follow the example's [setup procedure ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/esp32-radio#set-up) to provision credentials, configure your hostname and account, and deploy the Worker. Keep `.credential.env` private.

  3. **Prepare the device.** Follow [Back up and flash ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/esp32-radio#back-up-and-flash). Use audio you have permission to distribute. Back up the board before replacing its software. Flashing resets the device.

  4. **Listen and control.** Open the Worker URL, sign in with the configured viewer password, and select **Start listening**. Open another listener tab. Both tabs should receive audio, spectrum, and telemetry.

In one tab, select **Take control** , then change the LED or pause playback. The other tab keeps listening. Select **Release control** before transferring control to another listener.




## Reconnect and clean up

Browsers rejoin manually after a board restart or terminal connection failure. When the board is online, select **Start listening** again. The example uses a shared viewer password for application authentication. For a deployment that serves distinct users, per-user identity and abuse controls remain part of the integration.

The example allows eight listeners per board and one controller. The application sets the eight-listener cap. It does not define the SFU subscriber limit.

To stop, release control and disconnect listeners, then power off the board. Keep the backend available for as long as required cleanup remains pending. The example's [operations guide ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/esp32-radio/PRODUCTION.md#stop-and-clean-up) explains publisher replacement, state expiry, and resource cleanup before removing the Worker or SFU app.

## Adapt to other devices

For a shared camera or microscope monitor, keep the observer and controller model, then add camera capture, [supported video encoding](https://developers.cloudflare.com/realtime/sfu/platform/limits/#supported-codecs), and browser video playback. Use hardware or a gateway capable of supplying that video.

For a sensor dashboard, replace spectrum samples with your measurements. Add sensor capture, units, timestamps, and behavior for stale readings.

### Adapt the pattern to robotics

Apply the observer/operator model to a robot gateway using these substitutions:

Radio component | Robotics adaptation  
---|---  
Playlist audio source | Camera, microphone, or other supported media source  
Device telemetry and spectrum samples | Sensor state, diagnostics, and replaceable measurements  
Playback and LED commands | Validated commands to a robot's local control interface  
Listener membership and controller lease | Observer and operator roles for the selected robot  
Firmware platform layer | The robot's hardware or Robot Operating System (ROS) integration  
  
Implement camera capture, ROS integration, and actuator behavior separately. Include command expiry, stale-command rejection, and local watchdog or stopping behavior in that integration. Emergency stopping and actuator limits belong on the device or its local controller.

For a related implementation with a native video publisher, the [cloud-gaming example](https://developers.cloudflare.com/realtime/sfu/examples/cloud-gaming/) uses separate channels for reliable and transient input.

## Inspect the implementation

Inspect the [architecture guide ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/esp32-radio/ARCHITECTURE.md) for authentication, controller ownership, and reconnect behavior.

## Try another example

For a smaller browser-only exercise, run the [DataChannel example](https://developers.cloudflare.com/realtime/sfu/features/datachannels/#learn-with-an-example).

[PreviousOverview](https://developers.cloudflare.com/realtime/sfu/examples/)[NextCloud gaming](https://developers.cloudflare.com/realtime/sfu/examples/cloud-gaming/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/examples/embedded-devices.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

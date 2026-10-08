---
url: https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/
title: AI audio pipelines \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:35.017648+00:00
---

# AI audio pipelines · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

  4. /[Examples](https://developers.cloudflare.com/realtime/sfu/examples/)
  5. /AI audio pipelines



# AI audio pipelines

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFollow the audioRequirementsRun the exampleStop and clean upAdapt the exampleInspect the implementationTroubleshootingTry another example

Use the `ai-tts-stt` example to connect speech-to-text and text-to-speech services to WebRTC audio. A publisher can generate speech for browser listeners and send microphone audio for transcription.

The application uses Workers AI, a Worker, Durable Objects, and Realtime SFU's WebSocket adapters. The browser uses WebRTC for audio and an application WebSocket for transcription results.

[Open the example](https://github.com/cloudflare/realtime-examples/tree/main/ai-tts-stt)

The example is experimental. It keeps SFU and AI credentials on the server, but its publisher and cleanup operations are unauthenticated. Add application authentication, authorization, and resource controls before sharing a deployment publicly.

## Follow the audio

The application uses separate adapters for the two audio directions:

**Publisher text**

**TTS Durable Object**

PCM over WebSocket

Cloudflare**Realtime SFU**

WebRTC audio

**Browser listeners**

**Workers AI speech generation**

**Browser microphone**

WebRTC audio

Cloudflare**Realtime SFU**

PCM over WebSocket

**STT Durable Object**

Transcript WebSocket

**Browser transcript**

**Workers AI transcription**

Publisher text→TTS Durable Object

TTS Durable Object↔Workers AI speech generation

TTS Durable ObjectPCM over WebSocket →Realtime SFU

Realtime SFUWebRTC audio →Browser listeners

Browser microphoneWebRTC audio →Realtime SFU

Realtime SFUPCM over WebSocket →STT Durable Object

STT Durable Object↔Workers AI transcription

STT Durable ObjectTranscript WebSocket →Browser transcript

`TTSAdapter` and `STTAdapter` are application Durable Objects. They call Workers AI, manage application state, and convert audio to or from the SFU adapter's 48 kHz stereo PCM format.

The SFU uses separate WebSocket ingest and egress adapters for the two audio directions. Transcripts use a separate application WebSocket. Refer to [WebSocket media formats](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#media-formats).

## Requirements

Use a Cloudflare account with Workers, Durable Objects, Workers AI access, and a [Realtime SFU app](https://developers.cloudflare.com/realtime/sfu/get-started/#create-your-first-app). The example also needs Node.js and a [Workers AI API token](https://developers.cloudflare.com/workers-ai/get-started/rest-api/#1-get-api-token-and-account-id) for that account. Use the Workers AI token template, or grant `Workers AI - Read` and `Workers AI - Edit` permissions.

Deploy the Worker for end-to-end audio. The SFU needs a publicly reachable WebSocket endpoint; localhost development is useful for browser UI changes.

## Run the example

  1. **Prepare the checkout.** Run:
         
         git clone https://github.com/cloudflare/realtime-examples.git
         cd realtime-examples/ai-tts-stt

npmyarnpnpmbun
         
         npm install
         
         yarn install
         
         pnpm install
         
         bun install

  2. **Configure the application.** In the checked-in Wrangler configuration, set `CF_ACCOUNT` and `REALTIME_SFU_APP_ID` to your account and SFU app identifiers. Follow the [configuration guide ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/ai-tts-stt#configuration) for the model and audio-processing configuration.

Add the backend secrets through Wrangler's interactive prompts:

npmyarnpnpm
         
         npx wrangler secret put CF_API_TOKEN
         
         yarn wrangler secret put CF_API_TOKEN
         
         pnpm wrangler secret put CF_API_TOKEN

npmyarnpnpm
         
         npx wrangler secret put REALTIME_SFU_BEARER_TOKEN
         
         yarn wrangler secret put REALTIME_SFU_BEARER_TOKEN
         
         pnpm wrangler secret put REALTIME_SFU_BEARER_TOKEN

  3. **Build and deploy.** Build the browser assets, then deploy the Worker:

npmyarnpnpm
         
         npm run build:web
         
         yarn run build:web
         
         pnpm run build:web

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  4. **Connect a publisher and listener.** Choose an application session name, such as `audio-demo`. This is a name you choose, separate from an SFU-generated session ID.

Open `https://<WORKER_HOSTNAME>/audio-demo/publisher` and select **Publish Session**. In another tab, open `https://<WORKER_HOSTNAME>/audio-demo/player`. Select **Connect** and wait for the connection. Use the same application name in both URLs.

  5. **Generate speech.** In the publisher tab, enter text and select **Generate Speech**. Confirm that the listener plays the generated audio.

  6. **Transcribe speech.** In the publisher tab, select the **STT** tab, then **Start Mic** , and allow microphone access. Wait for the WebRTC connection to become connected, then select **Start Forwarding**. Speak and observe the returned transcript.




The example's [deployment and use guide ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/ai-tts-stt#deploy-and-use) describes the controls and URL patterns in detail.

## Stop and clean up

To stop the example's flows, select **Stop Forwarding** , **Stop Mic** , and **Unpublish** as applicable. Review the example's [Stop the Session and Debug Cleanup instructions ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/ai-tts-stt#deploy-and-use) before deleting the backend or exposing administrative operations. Resource ownership and failure recovery need validation for your integration.

## Adapt the example

For a spoken tutor, connect finalized transcripts to your dialogue logic and send its responses to TTS. Add turn-taking, interruption handling, conversation state, and authorization for those actions. Keep SFU and AI credentials on the Worker as you adapt the application.

## Inspect the implementation

Follow the [TTS implementation guide ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/ai-tts-stt/TTSAdapter.md) for speech generation, conversion, and publication. The [STT implementation guide ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/ai-tts-stt/STTAdapter.md) covers microphone forwarding and transcript delivery.

## Troubleshooting

Use [adapter troubleshooting](https://developers.cloudflare.com/realtime/sfu/features/media-transport-adapters/websocket-adapter/#troubleshooting) to diagnose endpoint and media-format failures.

## Try another example

For video processing, the [WebRTC-to-JPEG example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg) demonstrates an SFU video track delivered as JPEG frames to a Worker.

[PreviousCloud gaming](https://developers.cloudflare.com/realtime/sfu/examples/cloud-gaming/)[NextCustom video room](https://developers.cloudflare.com/realtime/sfu/examples/video-room/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/examples/ai-audio.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

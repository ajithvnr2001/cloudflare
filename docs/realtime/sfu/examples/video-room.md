---
url: https://developers.cloudflare.com/realtime/sfu/examples/video-room/
title: Custom video room \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:35.452311+00:00
---

# Custom video room · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/examples/video-room/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

  4. /[Examples](https://developers.cloudflare.com/realtime/sfu/examples/)
  5. /Custom video room



# Custom video room

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/sfu/examples/video-room/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksPublication and discoveryIdentity and room permissionsDeploy the roomReconnect and cleanup Remove a deploymentAdapt the roomInspect the implementationTroubleshooting

Build a browser room where participants publish camera and microphone tracks and receive each other's media. The example exposes the SFU operations and the application state that connects them.

[Run the quickstart](https://developers.cloudflare.com/realtime/sfu/get-started/) [Open the source](https://github.com/cloudflare/realtime-examples/tree/main/video-room)

The example is experimental. It includes backend authentication and authorization, reconnect, and cleanup. Its [production guide ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/video-room/PRODUCTION.md) identifies the policies and controls to integrate for your application.

## How it works

Each browser owns separate publishing and receiving PeerConnections. Each connection corresponds to an SFU session. This makes the two negotiation lifecycles independent.

Trusted application boundary

Realtime SFU

**Browser participant**

**Worker**

**Room Durable Object**

**Producer session**

**Consumer session**

Access identity + member capability · HTTP owns snapshots, SDP, and mutations

Authenticated HTTP request

Typed RPC

Tagged result

Authorized JSON + SDP

Separate producer and consumer PeerConnections · Separate per-session SDP queues

SFU API with server credential

Publish audio + video

SFU API with server credential

Remote audio + video

WebSocket upgrade + single-use ticket

fetch() for upgrade only

room-changed revision

Notification triggers an authorized HTTP snapshot

The components have these responsibilities:

Component | Responsibility  
---|---  
Browser | Capture media, apply SDP, receive tracks, and display room and connection state  
Worker | Authenticate requests and route authorized application operations  
Durable Object | Own room membership, track discovery, room permissions, reconnect state, and cleanup  
Realtime SFU | Receive published audio/video and forward the tracks requested by each receiving session  
  
A hibernating WebSocket notifies browsers that a room revision changed. Browsers fetch the authoritative snapshot over HTTP. A periodic safety poll also checks for changes. Closing the notification socket does not by itself remove a participant.

## Publication and discovery

The publisher sends an SDP offer through the backend to `tracks/new`. After publication succeeds, the Durable Object stores the track names and media kinds in the room's discovery state.

Other participants request the publications they want. The backend translates those requests into remote track subscriptions using publisher session IDs and track names. Any required SFU offer/answer exchange completes before another mutation starts on that session.

Refer to [sessions and tracks](https://developers.cloudflare.com/realtime/sfu/concepts/sessions-tracks/) and [negotiation](https://developers.cloudflare.com/realtime/sfu/concepts/negotiation/) for the shared model.

## Identity and room permissions

A deployed room uses Cloudflare Access identity. A browser also receives application membership that owns its subsequent room operations. Room names, participant IDs, track names, and SFU session IDs are locators, not credentials.

The first successful participant becomes the room creator and can terminate the room. Other participants can leave their own membership. The example keeps provider secrets on the Worker and validates operations before calling the SFU.

## Deploy the room

Complete the [local quickstart](https://developers.cloudflare.com/realtime/sfu/get-started/) to prepare the checkout and `.dev.vars` file. A deployed room uses Workers, Durable Objects, and a Cloudflare Access application protecting the Worker hostname.

  1. Complete the [Access application setup](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) for your Worker hostname. Keep the Access team domain and application audience for deployment.

  2. From `realtime-examples/video-room`, run the deployment script:

npmyarnpnpm
         
         npm run deploy -- --secrets-file .dev.vars --var "CF_ACCESS_TEAM_DOMAIN:<TEAM_NAME>.cloudflareaccess.com" --var "CF_ACCESS_AUD:<ACCESS_APPLICATION_AUDIENCE>"
         
         yarn run deploy -- --secrets-file .dev.vars --var "CF_ACCESS_TEAM_DOMAIN:<TEAM_NAME>.cloudflareaccess.com" --var "CF_ACCESS_AUD:<ACCESS_APPLICATION_AUDIENCE>"
         
         pnpm run deploy -- --secrets-file .dev.vars --var "CF_ACCESS_TEAM_DOMAIN:<TEAM_NAME>.cloudflareaccess.com" --var "CF_ACCESS_AUD:<ACCESS_APPLICATION_AUDIENCE>"

Replace both Access placeholders. The script uploads the SFU values as Worker secrets. The Worker verifies the matching Access identity before allowing room operations.

  3. On the protected hostname, open `/rooms/two-browser-check`. Sign in and repeat the quickstart's two-participant verification before sharing the deployment.




## Reconnect and cleanup

The application defines these transitions:

Action | Behavior  
---|---  
Join | Create membership plus publishing and receiving sessions  
Refresh or replace a failed connection | Retain application identity, replace SFU sessions, republish, and rebuild subscriptions  
Leave | Close known resources and confirm cleanup before clearing membership in the browser  
Terminate room | The creator ends the room and starts cleanup for its participants  
Abandoned tab | Heartbeat expiry schedules cleanup, with retries when resource closure fails  
  
A missing heartbeat can leave an abandoned participant visible for up to 45 seconds before it becomes eligible for cleanup. Backend errors can delay completion. Repeated reconnect setup failures can require a page reload.

### Remove a deployment

End active rooms and wait for cleanup confirmation before removing the backend. From the example directory, delete the Worker:

npmyarnpnpm
    
    
    npx wrangler delete
    
    
    yarn wrangler delete
    
    
    pnpm wrangler delete

Remove the associated Access application separately. Delete `.dev.vars` when you no longer need the credentials. Delete a dedicated SFU app only after all applications using it have stopped.

## Adapt the room

Keep authentication, resource ownership, and the per-session negotiation queues when adapting the example. Replace display and presence behavior through the browser/backend contract rather than trusting browser-supplied SFU identifiers.

The example does not implement screen sharing, chat, recording, simulcast controls, or advanced layouts. Rate limiting, room quotas, and Access policy provisioning remain application responsibilities.

## Inspect the implementation

Trace the example's [signaling and state flow ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/video-room/ARCHITECTURE.md#signaling-and-state-flow) and [SDP serialization ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/video-room/ARCHITECTURE.md#sdp-serialization).

## Troubleshooting

Use the [troubleshooting guide ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/video-room/TROUBLESHOOTING.md) for media, authentication, and lifecycle symptoms.

[PreviousAI audio pipelines](https://developers.cloudflare.com/realtime/sfu/examples/ai-audio/)[NextConnection API](https://developers.cloudflare.com/realtime/sfu/api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/examples/video-room.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

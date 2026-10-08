---
url: https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/
title: Session Lifecycle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:54.062532+00:00
---

# Session Lifecycle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Concepts](https://developers.cloudflare.com/realtime/realtimekit/concepts/)
  5. /Session Lifecycle



# Session Lifecycle

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Lifecycle of a Peer in a Session

The [Session Guide](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#session) explains what a session is and how to initialize one. In this guide we will talk about what happens to a peer as they move through a session, when do they go to the setup screen, waitlist screen, ended screen or any other screen, and how you can hook into these events to perform custom actions.

### Lifecycle of a Peer in a Session

![Peer Lifecycle In a Session](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=545,height=326,format=svg/_astro/peer-lifecycle.ChUtQdVP.svg)

Here’s how the peer lifecycle works:

  1. **Initialization state** : When the SDK is initialized, the peer first sees a Setup Screen, where they can preview their audio and video before joining.
  2. **Join intent** : When the peer decides to join, one of two things happens: 
     * If waitlisting is enabled, they are moved to a Waitlist and see a Waitlist screen.
     * If not waitlisted, they join the session and see the main Meeting screen (Stage), where they can interact with others.
  3. **During the session** : The peer can see and interact with others in the main Meeting screen (Stage).
  4. **Session transitions** : 
     * If the peer is rejected from the waitlist, they see a dedicated Rejected screen.
     * If the peer is kicked out, they see an Ended screen and the session ends for them.
     * If the peer leaves voluntarily, or if the meeting ends, they see an Ended screen, and the session ends for them.



Each of these screens is built with UI Kit components, which you can fully customize to match your app’s design and requirements.

The UI Kit SDKs automatically handle which notifications or screens to show at each state, so you don’t have to manage these transitions manually.

In upcoming pages, we will see how to hook into these events to perform custom actions and to build your own custom meeting experience.

[PreviousParticipant](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/)[NextSelect SDK(s)](https://developers.cloudflare.com/realtime/realtimekit/sdk-selection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/concepts/session-lifecycle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

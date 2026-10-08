---
url: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/pip/
title: Picture in Picture \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:02.408891+00:00
---

# Picture in Picture · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/pip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /[Remote Participants](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/)
  5. /Picture in Picture



# Picture in Picture

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/pip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCheck supportEnable Picture-in-PictureDisable Picture-in-PictureCheck supportEnable Picture-in-PictureDisable Picture-in-Picture

Picture-in-Picture API allows you to render `meeting.participants.active` participant's video as a floating tile outside of the current webpage's context.

Note

Supported in Chrome, Edge, and Chromium-based browsers only.

WebMobile

ReactWeb ComponentsAngular

Picture-in-Picture is not available on this platform.

## Check support

Picture-in-Picture API might not be supported in your browser. Always check for support before using the API.
    
    
    const isSupported = meeting.participants.pip.isSupported();

## Enable Picture-in-Picture
    
    
    await meeting.participants.pip.enable();

## Disable Picture-in-Picture
    
    
    await meeting.participants.pip.disable();

## Check support

Picture-in-Picture API might not be supported in your browser. Always check for support before using the API.
    
    
    const isSupported = meeting.participants.pip.isSupported();

## Enable Picture-in-Picture
    
    
    await meeting.participants.pip.enable();

## Disable Picture-in-Picture
    
    
    await meeting.participants.pip.disable();

[PreviousEvents](https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/events/)[NextDisplay active speakers](https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/remote-participants/pip.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/
title: Rewind, Replay, Resume: Introducing DVR for Stream Live \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.833439+00:00
---

# Rewind, Replay, Resume: Introducing DVR for Stream Live · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-14-introducing-dvr-for-stream-live/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 14, 2025

## Rewind, Replay, Resume: Introducing DVR for Stream Live

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Previously, all viewers watched "the live edge," or the latest content of the broadcast, synchronously. If a viewer paused for more than a few seconds, the player would automatically "catch up" when playback started again. Seeking through the broadcast was only available once the recording was available after it concluded.

Starting today, customers can make a small adjustment to the player embed or manifest URL to enable the DVR experience for their viewers. By offering this feature as an opt-in adjustment, our customers are empowered to pick the best experiences for their applications.

When building a player embed code or manifest URL, just add `dvrEnabled=true` as a query parameter. There are some things to be aware of when using this option. For more information, refer to [DVR for Live](https://developers.cloudflare.com/stream/stream-live/dvr-for-live/).

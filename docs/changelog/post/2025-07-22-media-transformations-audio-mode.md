---
url: https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/
title: Audio mode for Media Transformations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.698825+00:00
---

# Audio mode for Media Transformations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-22-media-transformations-audio-mode/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 22, 2025

## Audio mode for Media Transformations

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We now support `audio` mode! Use this feature to extract audio from a source video, outputting an M4A file to use in downstream workflows like [AI inference](https://developers.cloudflare.com/workers-ai/), content moderation, or transcription.

For example,

Example URLtext
    
    
    https://example.com/cdn-cgi/media/<OPTIONS>/<SOURCE-VIDEO>
    https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/<input video with diction>

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

---
url: https://developers.cloudflare.com/stream/examples/shaka-player/
title: Shaka Player \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:47.028347+00:00
---

# Shaka Player · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/examples/shaka-player/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Examples](https://developers.cloudflare.com/stream/examples/)
  4. /Shaka Player



# Shaka Player

Example of video playback with Cloudflare Stream and Shaka Player

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/examples/shaka-player/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

First, create a video element, using the poster attribute to set a preview thumbnail image. Refer to [Display thumbnails](https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/) for instructions on how to generate a thumbnail image using Cloudflare Stream.
    
    
    <video
    	id="video"
    	width="640"
    	poster="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg"
    	controls
    	autoplay
    ></video>

Then listen for `DOMContentLoaded` event, create a new instance of Shaka Player, and load the manifest URI.
    
    
    // Replace the manifest URI with an HLS or DASH manifest from Cloudflare Stream
    const manifestUri =
    	'https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd';
    
    document.addEventListener('DOMContentLoaded', () => {
    	const video = document.getElementById('video');
      const player = new shaka.Player(video);
    	await player.load(manifestUri);
    });

Refer to the [Shaka Player documentation ↗︎](https://github.com/shaka-project/shaka-player) for more information.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/examples/shaka-player.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

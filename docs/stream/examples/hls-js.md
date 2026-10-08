---
url: https://developers.cloudflare.com/stream/examples/hls-js/
title: hls.js \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:46.731279+00:00
---

# hls.js · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/examples/hls-js/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Examples](https://developers.cloudflare.com/stream/examples/)
  4. /Hls Js



# hls.js

Example of video playback with Cloudflare Stream and the HLS reference player (hls.js)

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/examples/hls-js/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    <html>
    	<head>
    		<script src="//cdn.jsdelivr.net/npm/hls.js@latest"></script>
    	</head>
    	<body>
    		<video id="video"></video>
    		<script>
    			if (Hls.isSupported()) {
    				const video = document.getElementById('video');
    				const hls = new Hls();
    				hls.attachMedia(video);
    				hls.on(Hls.Events.MEDIA_ATTACHED, () => {
    					hls.loadSource(
    						'https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8'
    					);
    				});
    			}
    
    			video.play();
    		</script>
    	</body>
    </html>

Refer to the [hls.js documentation ↗︎](https://github.com/video-dev/hls.js/blob/master/docs/API.md) for more information.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/examples/hls-js.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

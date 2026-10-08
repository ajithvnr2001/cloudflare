---
url: https://developers.cloudflare.com/stream/examples/video-js/
title: Video.js \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:47.287604+00:00
---

# Video.js · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/examples/video-js/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Examples](https://developers.cloudflare.com/stream/examples/)
  4. /Video Js



# Video.js

Example of video playback with Cloudflare Stream and Video.js

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/examples/video-js/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    <html>
    	<head>
    		<link
    			href="https://cdnjs.cloudflare.com/ajax/libs/video.js/7.10.2/video-js.min.css"
    			rel="stylesheet"
    		/>
    		<script src="https://cdnjs.cloudflare.com/ajax/libs/video.js/7.10.2/video.min.js"></script>
    	</head>
    	<body>
    		<video-js id="vid1" controls preload="auto">
    			<source
    				src="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8"
    				type="application/x-mpegURL"
    			/>
    		</video-js>
    
    		<script>
    			const vid = document.getElementById('vid1');
    			const player = videojs(vid);
    		</script>
    	</body>
    </html>

Refer to the [Video.js documentation ↗︎](https://docs.videojs.com/) for more information.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/examples/video-js.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

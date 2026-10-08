---
url: https://developers.cloudflare.com/stream/examples/dash-js/
title: dash.js \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:46.898037+00:00
---

# dash.js · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/examples/dash-js/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Examples](https://developers.cloudflare.com/stream/examples/)
  4. /Dash Js



# dash.js

Example of video playback with Cloudflare Stream and the DASH reference player (dash.js)

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/examples/dash-js/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    <html>
    	<head>
    		<script src="https://cdn.dashjs.org/latest/dash.all.min.js"></script>
    	</head>
    	<body>
    		<div>
    			<div class="code">
    				<video
    					data-dashjs-player=""
    					autoplay=""
    					src="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd"
    					controls="true"
    				></video>
    			</div>
    		</div>
    	</body>
    </html>

Refer to the [dash.js documentation ↗︎](https://github.com/Dash-Industry-Forum/dash.js/) for more information.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/examples/dash-js.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

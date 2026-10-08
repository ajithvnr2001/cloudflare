---
url: https://developers.cloudflare.com/stream/uploading-videos/upload-via-link/
title: Upload with a link \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:50.205514+00:00
---

# Upload with a link · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/uploading-videos/upload-via-link/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Upload videos](https://developers.cloudflare.com/stream/uploading-videos/)
  4. /Upload with a link



# Upload with a link

Last updated Jun 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/uploading-videos/upload-via-link/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCheck video status

If you have videos stored in a cloud storage bucket (R2, S3, GCS) or hosted by a service that exposes a download link, you can pass its URL. Stream will fetch the file on your behalf.

Note

Google Drive share links are _not_ recommended for this purpose. They are prone to rate limiting and access restrictions imposed by Google that may prevent Stream from downloading the file.

Make a `POST` request to the Stream API using the link to your video.
    
    
    		curl \
    		--data '{"url":"https://pub-2da57dbfcf5f4369863991d59747d686.r2.dev/acadia.mp4","meta":{"name":"My First Stream Video"}}' \
    		--header "Authorization: Bearer <API_TOKEN>" \
    		https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/copy
    
    
    const client = new Cloudflare({
    	apiEmail: process.env['CLOUDFLARE_EMAIL'], // This is the default and can be omitted
    	apiKey: process.env['CLOUDFLARE_API_KEY'], // This is the default and can be omitted
    });
    
    const video = await client.stream.copy.create({
    	account_id: '<ACCOUNT_ID>',
    	url: 'https://pub-2da57dbfcf5f4369863991d59747d686.r2.dev/acadia.mp4',
    });

See the full Stream [REST API and SDK reference](https://developers.cloudflare.com/api/resources/stream/) for details on using REST API from external applications, with pre-generated SDK's for external TypeScript, Python, or Go applications.
    
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		// upload a video with a link
    		const videoDetails = await env.STREAM.upload(
    			"https://pub-2da57dbfcf5f4369863991d59747d686.r2.dev/acadia.mp4",
    			// (optional) attach metadata
    			{ meta: { name: "My First Stream Video" } }
    		);
    
    		// return a Workers response
    		return new Response(
    			JSON.stringify(videoDetails),
    		);
    	},
    
    } satisfies ExportedHandler<{ STREAM: StreamBinding }>;
    
    
    {
    	"$schema": "node_modules/wrangler/config-schema.json",
    	"name": "<ENTER_WORKER_NAME>",
    	"main": "src/index.ts",
    	"compatibility_date": "2026-04-14",
    	"observability": {
    		"enabled": true
    	},
    	"stream": {
    		"binding": "STREAM"
    	}
    }

See the full [Workers Stream binding API reference](https://developers.cloudflare.com/stream/manage-video-library/bindings/).

If you have videos stored in a cloud storage bucket, you can pass a HTTP link for the file, and Stream will fetch the file on your behalf.

## Check video status

Stream must download and encode the video, which can take a few seconds to a few minutes depending on the length of your video.

When the `readyToStream` value returns `true`, your video is ready for streaming.

You can optionally use [webhooks](https://developers.cloudflare.com/stream/manage-video-library/using-webhooks/) which will notify you when the video is ready to stream or if an error occurs.
    
    
    {
      "result": {
        "uid": "6b9e68b07dfee8cc2d116e4c51d6a957",
        "thumbnail": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg",
        "thumbnailTimestampPct": 0,
        "readyToStream": false,
        "status": {
          "state": "downloading"
        },
        "meta": {
          "downloaded-from": "https://pub-2da57dbfcf5f4369863991d59747d686.r2.dev/acadia.mp4",
          "name": "My First Stream Video"
        },
        "created": "2020-10-16T20:20:17.872170843Z",
        "modified": "2020-10-16T20:20:17.872170843Z",
        "size": 9032701,
        "preview": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/watch",
        "allowedOrigins": [],
        "requireSignedURLs": false,
        "uploaded": "2020-10-16T20:20:17.872170843Z",
        "uploadExpiry": null,
        "maxSizeBytes": 0,
        "maxDurationSeconds": 0,
        "duration": -1,
        "input": {
          "width": -1,
          "height": -1
        },
        "playback": {
          "hls": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8",
          "dash": "https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd"
        },
        "watermark": null
      },
      "success": true,
      "errors": [],
      "messages": []
    }

After the video is uploaded, you can use the video `uid` shown in the example response above to play the video using the [Stream video player](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/).

If you are using your own player or rendering the video in a mobile app, refer to [using your own player](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/using-the-player-api/).

[PreviousResumable and large files (tus)](https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/)[NextDirect creator uploads](https://developers.cloudflare.com/stream/uploading-videos/direct-creator-uploads/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/uploading-videos/upload-via-link.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/
title: Basic video uploads \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:50.270090+00:00
---

# Basic video uploads · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Upload videos](https://developers.cloudflare.com/stream/uploading-videos/)
  4. /Basic video uploads



# Basic video uploads

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/uploading-videos/upload-video-file/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic UploadsUpload through the Cloudflare dashboardUpload with the Stream API

## Basic Uploads

For files smaller than 200 MB, you can use simple form-based uploads.

## Upload through the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to the **Stream** page.

[ Go to **Videos** ↗ ](https://dash.cloudflare.com/?to=/:account/stream/videos)
  2. Drag and drop your video into the **Quick upload** area. You can also click to browse for the file on your machine.




After the video finishes uploading, the video appears in the list.

## Upload with the Stream API

Make a `POST` request with the `content-type` header set to `multipart/form-data` and include the media as an input with the name set to `file`.

Upload video POST requestbash
    
    
    curl --request POST \
    --header "Authorization: Bearer <API_TOKEN>" \
    --form file=@/Users/user_name/Desktop/my-video.mp4 \
    https://api.cloudflare.com/client/v4/accounts/{account_id}/stream

Note

Note that cURL's `--form` flag automatically configures the `content-type` header and maps `my-video.mp4` to a form input called `file`.

[PreviousOverview](https://developers.cloudflare.com/stream/uploading-videos/)[NextResumable and large files (tus)](https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/uploading-videos/upload-video-file.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/stream/manage-video-library/searching/
title: Search for videos \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:48.506871+00:00
---

# Search for videos · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/manage-video-library/searching/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /Manage videos
  4. /Search for videos



# Search for videos

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/manage-video-library/searching/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat you will needcURL example

You can search for videos by name through the Stream API by adding a `search` query parameter to the [list media files](https://developers.cloudflare.com/api/resources/stream/methods/list/) endpoint.

## What you will need

To make API requests you will need a [Cloudflare API token ↗︎](https://www.cloudflare.com/a/account/my-account) and your Cloudflare [account ID ↗︎](https://www.cloudflare.com/a/overview/).

## cURL example

This example lists media where the name matches `puppy.mp4`.
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/stream?search=puppy" \
         -H "Authorization: Bearer <API_TOKEN>" \
         -H "Content-Type: application/json"

[PreviousManage creators](https://developers.cloudflare.com/stream/manage-video-library/creator-id/)[NextOverview](https://developers.cloudflare.com/stream/getting-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/manage-video-library/searching.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

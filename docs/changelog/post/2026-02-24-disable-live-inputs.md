---
url: https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/
title: Stream live inputs can now be disabled and enabled \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.257407+00:00
---

# Stream live inputs can now be disabled and enabled · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-24-disable-live-inputs/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 24, 2026

## Stream live inputs can now be disabled and enabled

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now disable a live input to reject incoming RTMPS and SRT connections. When a live input is disabled, any broadcast attempts will fail to connect.

This gives you more control over your live inputs:

  * Temporarily pause an input without deleting it
  * Programmatically end creator broadcasts
  * Prevent new broadcasts from starting on a specific input



To disable a live input via the API, set the `enabled` property to `false`:
    
    
    curl --request PUT \
    https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \
    --header "Authorization: Bearer <API_TOKEN>" \
    --data '{"enabled": false}'

You can also disable or enable a live input from the **Live inputs** list page or the live input detail page in the Dashboard.

All existing live inputs remain enabled by default. For more information, refer to [Start a live stream](https://developers.cloudflare.com/stream/stream-live/start-stream-live/).

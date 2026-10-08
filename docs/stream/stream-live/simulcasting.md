---
url: https://developers.cloudflare.com/stream/stream-live/simulcasting/
title: Simulcast (restream) videos \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:49.039915+00:00
---

# Simulcast (restream) videos · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/stream-live/simulcasting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Stream live video](https://developers.cloudflare.com/stream/stream-live/)
  4. /Simulcast (restream) videos



# Simulcast (restream) videos

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/stream-live/simulcasting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd an Output using the APIControl when you start and stop simulcasting Enable outputs from the dashboard:Manage outputs

Simulcasting lets you forward your live stream to third-party platforms such as Twitch, YouTube, Facebook, Twitter, and more. You can simulcast to up to 50 concurrent destinations from each live input. To begin simulcasting, select an input and add one or more Outputs.

## Add an Output using the API

Add an Output to start retransmitting live video. You can add or remove Outputs at any time during a broadcast to start and stop retransmitting.

Requestbash
    
    
    curl -X POST \
    --data '{"url": "rtmp://a.rtmp.youtube.com/live2","streamKey": "<redacted>"}' \
    -H "Authorization: Bearer <API_TOKEN>" \
    https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/stream/live_inputs/<INPUT_UID>/outputs

Responsejson
    
    
    {
      "result": {
        "uid": "6f8339ed45fe87daa8e7f0fe4e4ef776",
        "url": "rtmp://a.rtmp.youtube.com/live2",
        "streamKey": "<redacted>"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

## Control when you start and stop simulcasting

You can enable and disable individual live outputs with either:

  * The **Live inputs** page of the Cloudflare dashboard.

[ Go to **Live inputs** ↗ ](https://dash.cloudflare.com/?to=/:account/stream/inputs)
  * [The API](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/update/)




This allows you to:

  * Start a live stream, but wait to start simulcasting to YouTube and Twitch until right before the content begins.
  * Stop simulcasting before the live stream ends, to encourage viewers to transition from a third-party service like YouTube or Twitch to a direct live stream.
  * Give your own users manual control over when they go live to specific simulcasting destinations.



When a live output is disabled, video is not simulcast to the live output, even when actively streaming to the corresponding live input.

By default, all live outputs are enabled.

### Enable outputs from the dashboard:

  1. In the Cloudflare dashboard, go to the **Live inputs** page.

[ Go to **Live inputs** ↗ ](https://dash.cloudflare.com/?to=/:account/stream/inputs)
  2. Select an input from the list.

  3. Under **Outputs** > **Enabled** , set the toggle to enabled or disabled.




## Manage outputs

Command | Method | Endpoint  
---|---|---  
[List outputs](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/list/) | `GET` | `accounts/:account_identifier/stream/live_inputs`  
[Delete outputs](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/delete/) | `DELETE` | `accounts/:account_identifier/stream/live_inputs/:live_input_identifier`  
[List All Outputs Associated With A Specified Live Input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/list/) | `GET` | `/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs`  
[Delete An Output](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/delete/) | `DELETE` | `/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}`  
  
If the associated live input is already retransmitting to this output when you make the `DELETE` request, that output will be disconnected within 30 seconds.

[PreviousRecord and replay live streams](https://developers.cloudflare.com/stream/stream-live/replay-recordings/)[NextReceive Live Webhooks](https://developers.cloudflare.com/stream/stream-live/webhooks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/stream-live/simulcasting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

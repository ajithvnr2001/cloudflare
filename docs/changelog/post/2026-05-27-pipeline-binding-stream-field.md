---
url: https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/
title: Pipeline binding configuration field renamed to stream \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:54.779966+00:00
---

# Pipeline binding configuration field renamed to stream · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 4, 2026

## Pipeline binding configuration field renamed to stream

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-27-pipeline-binding-stream-field/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `pipeline` field inside the `pipelines` binding configuration in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) has been renamed to `stream`. The old field is deprecated but still accepted.

Update your configuration to use `stream` to avoid the deprecation warning.

**Before (deprecated):**
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "pipelines": [
        {
          "binding": "MY_PIPELINE",
          "pipeline": "<STREAM_ID>"
        }
      ]
    }
    
    
    [[pipelines]]
    binding = "MY_PIPELINE"
    pipeline = "<STREAM_ID>"

**After:**
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "pipelines": [
        {
          "binding": "MY_PIPELINE",
          "stream": "<STREAM_ID>"
        }
      ]
    }
    
    
    [[pipelines]]
    binding = "MY_PIPELINE"
    stream = "<STREAM_ID>"

No other changes are required. The binding name, TypeScript types, and runtime API (`env.MY_PIPELINE.send(...)`) remain the same.

For more information on configuring pipeline bindings, refer to [Writing to streams](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/#configure-pipeline-binding).

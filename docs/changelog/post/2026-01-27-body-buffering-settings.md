---
url: https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/
title: Control request and response body buffering in Configuration Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:34.886819+00:00
---

# Control request and response body buffering in Configuration Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 27, 2026

## Control request and response body buffering in Configuration Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-27-body-buffering-settings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now control how Cloudflare buffers HTTP request and response bodies using two new settings in [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/).

#### Request body buffering

Controls how Cloudflare buffers HTTP request bodies before forwarding them to your origin server:

Mode | Behavior  
---|---  
**Standard** (default) | Cloudflare can inspect a prefix of the request body for enabled functionality such as WAF and Bot Management.  
**Full** | Buffers the entire request body before sending to origin.  
**None** | No buffering — the request body streams directly to origin without inspection.  
  
#### Response body buffering

Controls how Cloudflare buffers HTTP response bodies before forwarding them to the client:

Mode | Behavior  
---|---  
**Standard** (default) | Cloudflare can inspect a prefix of the response body for enabled functionality.  
**None** | No buffering — the response body streams directly to the client without inspection.  
  
Caution

Setting body buffering to **None** may break security functionality that requires body inspection, including the Web Application Firewall (WAF) and Bot Management. Ensure that any paths where you disable buffering do not require security inspection.

#### API example
    
    
    {
      "action": "set_config",
      "action_parameters": {
        "request_body_buffering": "standard",
        "response_body_buffering": "none"
      }
    }

For more information, refer to [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/).

---
url: https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/
title: Metro code field now available in Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:33.171856+00:00
---

# Metro code field now available in Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 12, 2026

## Metro code field now available in Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `ip.src.metro_code` field in the Ruleset Engine is now populated with DMA (Designated Market Area) data.

You can use this field to build rules that target traffic based on geographic market areas, enabling more granular location-based policies for your applications.

#### Field details

Field | Type | Description  
---|---|---  
`ip.src.metro_code` | String | null | The metro code (DMA) of the incoming request's IP address. Returns the designated market area code for the client's location.  
  
Example filter expression:
    
    
    ip.src.metro_code eq "501"

For more information, refer to the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/).

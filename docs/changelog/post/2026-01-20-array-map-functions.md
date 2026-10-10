---
url: https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/
title: New functions for array and map operations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.912233+00:00
---

# New functions for array and map operations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-20-array-map-functions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 20, 2026

## New functions for array and map operations

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

#### New functions for array and map operations

Cloudflare Rulesets now include new functions that enable advanced expression logic for evaluating arrays and maps. These functions allow you to build rules that match against lists of values in request or response headers, enabling use cases like country-based blocking using custom headers.

* * *

#### New functions

Function | Description  
---|---  
`split(source, delimiter)` | Splits a string into an array of strings using the specified delimiter.  
`join(array, delimiter)` | Joins an array of strings into a single string using the specified delimiter.  
`has_key(map, key)` | Returns `true` if the specified key exists in the map.  
`has_value(map, value)` | Returns `true` if the specified value exists in the map.  
  
* * *

#### Example use cases

**Check if a country code exists in a header list:**
    
    
    has_value(split(http.response.headers["x-allow-country"][0], ","), ip.src.country)

**Check if a specific header key exists:**
    
    
    has_key(http.request.headers, "x-custom-header")

**Join array values for logging or comparison:**
    
    
    join(http.request.headers.names, ", ")

For more information, refer to the [Functions reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/).

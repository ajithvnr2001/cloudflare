---
url: https://developers.cloudflare.com/changelog/post/2026-07-16-cache-rules-bot-fields-asn/
title: Bot management fields and ASN support in Cache Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.303879+00:00
---

# Bot management fields and ASN support in Cache Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-16-cache-rules-bot-fields-asn/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 16, 2026

## Bot management fields and ASN support in Cache Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-16-cache-rules-bot-fields-asn/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Bot management fields and ASN support in Cache Rules

Cache Rules now supports bot management fields and the `ip.src.asnum` field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).

This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.

#### New fields

The following fields are now available in Cache Rules expressions:

Field | Type | Description  
---|---|---  
`cf.bot_management.score` | Number | Bot score from `1` to `99`, where a lower value indicates a higher likelihood that the request originates from a bot.  
`cf.bot_management.ja3_hash` | String | JA3 fingerprint of the request, which helps identify the client making the connection.  
`cf.bot_management.ja4` | String | JA4 fingerprint of the request, which provides a more detailed client identification than JA3.  
`cf.bot_management.verified_bot` | Boolean | Whether the request originates from a verified bot, such as a search engine crawler.  
`cf.bot_management.static_resource` | Boolean | Whether the request is for a static resource and therefore exempt from bot detection.  
`cf.bot_management.js_detection.passed` | Boolean | Whether the browser passed JavaScript detection when the feature is enabled.  
`cf.bot_management.detection_ids` | Array<Number> | List of IDs that correspond to Bot Management heuristic detections made on the request.  
`cf.bot_management.tags` | Array<String> | List of tags associated with the bot traffic, such as `API`, `GOOGLE`, or `BING`. Match a tag with an expression such as `any(cf.bot_management.tags[*] eq "API")`.  
`cf.bot_management.signed_agent` | Boolean | Whether the request originates from a known agent that identifies itself with Web Bot Auth.  
`cf.bot_management.corporate_proxy` | Boolean | Whether the request originates from a known corporate proxy.  
`ip.src.asnum` | Number | The autonomous system number (ASN) of the incoming request's IP address.  
  
Note

Bot management fields require a Bot Management subscription. `ip.src.asnum` is available on all plans.

#### Example

Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:
    
    
    (http.request.uri.path contains "/api/" and cf.bot_management.score lt 30)
    or
    (http.request.uri.path contains "/api/" and not ip.src.asnum in {12345 67890})

To learn more, refer to the [Cache Rules documentation](https://developers.cloudflare.com/cache/how-to/cache-rules/) and the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/).

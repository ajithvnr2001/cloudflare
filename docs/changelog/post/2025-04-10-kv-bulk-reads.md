---
url: https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/
title: Read multiple keys from Workers KV with bulk reads \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.986812+00:00
---

# Read multiple keys from Workers KV with bulk reads · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 17, 2025

## Read multiple keys from Workers KV with bulk reads

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.

This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by [Workers simultaneous connection limits](https://developers.cloudflare.com/workers/platform/limits/#simultaneous-open-connections).
    
    
    // Read single key
    const key = "key-a";
    const value = await env.NAMESPACE.get(key);
    
    // Read multiple keys
    const keys = ["key-a", "key-b", "key-c", ...] // up to 100 keys
    const values : Map<string, string?> = await env.NAMESPACE.get(keys);
    
    // Print the value of "key-a" to the console.
    console.log(`The first key is ${values.get("key-a")}.`)

Consult the [Workers KV Read key-value pairs API](https://developers.cloudflare.com/kv/api/read-key-value-pairs/) for full details on Workers KV's new bulk reads support.

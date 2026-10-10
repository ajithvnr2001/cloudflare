---
url: https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/
title: New cryptographic functions \u2014 encode_base64() and sha256() \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.965318+00:00
---

# New cryptographic functions — encode_base64() and sha256() · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-22-sha256-base64-encode-functions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 22, 2026

## New cryptographic functions — encode_base64() and sha256()

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Rulesets now includes `encode_base64()` and `sha256()` functions, enabling you to generate signed request headers directly in rule expressions. These functions support common patterns like constructing a canonical string from request attributes, computing a SHA256 digest, and Base64-encoding the result.

* * *

#### New functions

Function | Description | Availability  
---|---|---  
`encode_base64(input, flags)` | Encodes a string to Base64 format. Optional `flags` parameter: `u` for URL-safe encoding, `p` for padding (adds `=` characters to make the output length a multiple of 4, as required by some systems). By default, output is standard Base64 without padding. | All plans (in header transform rules)  
`sha256(input)` | Computes a SHA256 hash of the input string. | Requires enablement  
  
Note

The `sha256()` function is available as an Enterprise add-on and requires a specific entitlement. Contact your account team to enable it.

* * *

#### Examples

**Encode a string to Base64 format:**
    
    
    encode_base64("hello world")

Returns: `aGVsbG8gd29ybGQ`

**Encode a string to Base64 format with padding:**
    
    
    encode_base64("hello world", "p")

Returns: `aGVsbG8gd29ybGQ=`

**Perform a URL-safe Base64 encoding of a string:**
    
    
    encode_base64("hello world", "u")

Returns: `aGVsbG8gd29ybGQ`

**Compute the SHA256 hash of a secret token:**
    
    
    sha256("my-token")

Returns a hash that your origin can validate to authenticate requests.

**Compute the SHA256 hash of a string and encode the result to Base64 format:**
    
    
    encode_base64(sha256("my-token"))

Combines hashing and encoding for systems that expect Base64-encoded signatures.

For more information, refer to the [Functions reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/).

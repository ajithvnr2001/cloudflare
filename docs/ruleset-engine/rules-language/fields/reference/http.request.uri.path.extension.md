---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/
title: http.request.uri.path.extension \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:12.392835+00:00
---

# http.request.uri.path.extension · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Uri.Path.Extension



# http.request.uri.path.extension

`http.request.uri.path.extension``String`

The lowercased file extension in the URI path without the dot (`.`) character.

This corresponds to the string after the last dot in the URI path, excluding the query string.

If the first character of the last path segment is a dot and the segment does not contain other dot characters, the field value will be an empty string (`""`). Having a dot as the first character does not represent a file extension and is commonly used in UNIX-like systems to denote a hidden file or directory.

Example values:

  * If the URI path is `/articles/index.html`, the field value will be `"html"`.
  * If the URI path is `/articles/index.`, the field value will be an empty string (`""`).



Example values:

URI path | Field value  
---|---  
`/foo` | `""`  
`/foo.mp3` | `"mp3"`  
`/.mp3` | `""`  
`/.foo.mp3` | `"mp3"`  
`/foo.tar.bz2` | `"bz2"`  
`/foo.` | `""`  
`/foo.MP3` | `"mp3"`  
  
Categories: 

  * Request
  * URI



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

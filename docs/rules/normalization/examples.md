---
url: https://developers.cloudflare.com/rules/normalization/examples/
title: URL normalization examples \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:49.235344+00:00
---

# URL normalization examples · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/normalization/examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[URL normalization](https://developers.cloudflare.com/rules/normalization/)
  4. /Examples



# URL normalization examples

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/normalization/examples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following table shows how different [URL normalization settings](https://developers.cloudflare.com/rules/normalization/settings/) affect request URLs before they pass to other Cloudflare features and to the origin server:

Incoming URL | Normalization type | Normalize incoming URLs | Normalize URLs to origin | URL at Cloudflare's network | URL passed to origin server  
---|---|---|---|---|---  
`www.example.com/hello` | (any) | _Off_ | _Off_ | `www.example.com/hello` | `www.example.com/hello`  
`www.example.com/hello` | (any) | _On_ | _Off_ | `www.example.com/hello` | `www.example.com/hello`  
`www.example.com/hello` | (any) | _On_ | _On_ | `www.example.com/hello` | `www.example.com/hello`  
`example.com/%68ello` | (any) | _Off_ | _Off_ | `example.com/%68ello` | `example.com/%68ello`  
`example.com/%68ello` | (any) | _On_ | _Off_ | `example.com/hello` | `example.com/%68ello`  
`example.com/%68ello` | (any) | _On_ | _On_ | `example.com/hello` | `example.com/hello`  
`example.com/%68ello//pa\th` | _RFC-3986_ | _Off_ | _Off_ | `example.com/%68ello//pa\th` | `example.com/%68ello//pa\th`  
`example.com/%68ello//pa\th` | _RFC-3986_ | _On_ | _Off_ | `example.com/hello//pa%5Cth` | `example.com/%68ello//pa\th`  
`example.com/%68ello//pa\th` | _RFC-3986_ | _On_ | _On_ | `example.com/hello//pa%5Cth` | `example.com/hello//pa%5Cth`  
`example.com/%68ello//pa\th` | _Cloudflare_ | _Off_ | _Off_ | `example.com/%68ello//pa\th` | `example.com/%68ello//pa\th`  
`example.com/%68ello//pa\th` | _Cloudflare_ | _On_ | _Off_ | `example.com/hello/pa/th` | `example.com/%68ello//pa\th`  
`example.com/%68ello//pa\th` | _Cloudflare_ | _On_ | _On_ | `example.com/hello/pa/th` | `example.com/hello/pa/th`  
`example.com/hello//../path` | _RFC-3986_ | _On_ | _On_ | `example.com/hello/path` | `example.com/hello/path`  
`example.com/hello//../path` | _Cloudflare_ | _On_ | _On_ | `example.com/path` | `example.com/path`  
`example.com/hello/\../path` | _RFC-3986_ | _On_ | _On_ | `example.com/hello/%5C../path` | `example.com/hello/%5C../path`  
`example.com/hello/\../path` | _Cloudflare_ | _On_ | _On_ | `example.com/path` | `example.com/path`  
  
[PreviousSettings](https://developers.cloudflare.com/rules/normalization/settings/)[NextOverview](https://developers.cloudflare.com/rules/trace-request/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/normalization/examples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

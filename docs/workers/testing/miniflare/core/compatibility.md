---
url: https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/
title: Compatibility Dates \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:54.202667+00:00
---

# Compatibility Dates · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Core
  5. /Compatibility Dates



# Compatibility Dates

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/compatibility/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCompatibility DatesCompatibility Flags

  * [Compatibility Dates Reference](https://developers.cloudflare.com/workers/configuration/compatibility-dates)



## Compatibility Dates

Miniflare uses compatibility dates to opt-into backwards-incompatible changes from a specific date. If one isn't set, it will default to some time far in the past.
    
    
    const mf = new Miniflare({
    	compatibilityDate: "2021-11-12",
    });

## Compatibility Flags

Miniflare also lets you opt-in/out of specific changes using compatibility flags:
    
    
    const mf = new Miniflare({
    	compatibilityFlags: [
    		"formdata_parser_supports_files",
    		"durable_object_fetch_allows_relative_url",
    	],
    });

[PreviousWriting tests](https://developers.cloudflare.com/workers/testing/miniflare/writing-tests/)[NextFetch Events](https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/core/compatibility.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

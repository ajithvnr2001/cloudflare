---
url: https://developers.cloudflare.com/rules/normalization/how-it-works/
title: How URL normalization works \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:49.311199+00:00
---

# How URL normalization works · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/normalization/how-it-works/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[URL normalization](https://developers.cloudflare.com/rules/normalization/)
  4. /How it works



# How URL normalization works

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/normalization/how-it-works/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRFC 3986 normalizationCloudflare normalization

URL normalization modifies separators, encoded elements, and literal bytes in incoming URLs so that they conform to a consistent formatting standard.

For example, consider a WAF custom rule that blocks requests whose URLs match `www.example.com/hello`. The rule would not block a request containing an encoded element — `www.example.com/%68ello`. Normalizing incoming URLs on the Cloudflare global network helps simplify rules expressions containing URLs.

The two available types of URL normalization are:

  * RFC 3986 normalization
  * Cloudflare normalization



The location where URL normalization will occur depends on the [configured settings](https://developers.cloudflare.com/rules/normalization/settings/).

For examples of the different settings and their impact on request URLs, refer to the [URL normalization examples](https://developers.cloudflare.com/rules/normalization/examples/).

## RFC 3986 normalization

The URL normalization performed according to [RFC 3986 ↗︎](https://www.ietf.org/rfc/rfc3986.txt) is as follows:

  * The following unreserved characters are [percent decoded ↗︎](https://tools.ietf.org/html/rfc3986#section-2.1) (converted from their `%XX` encoded form back to the original character): 
    * Alphabetical characters: `a`-`z`, `A`-`Z` (decoded from `%41`-`%5A` and `%61`-`%7A`)
    * Digit characters: `0`-`9` (decoded from `%30`-`%39`)
    * hyphen `-` (`%2D`), period `.` (`%2E`), underscore `_` (`%5F`), and tilde `~` (`%7E`)
  * These reserved characters are not encoded or decoded: `: / ? # [ ] @ ! $ & ' ( ) * + , ; =`
  * Other characters, for example literal byte values, are percent encoded.
  * Percent encoded representations are converted to upper case.
  * URL paths are normalized according to the [Remove Dot Segments ↗︎](https://tools.ietf.org/html/rfc3986#section-5.2.4) protocol.



## Cloudflare normalization

When using the Cloudflare URL normalization, some extra normalization techniques will be applied to URLs of incoming requests, in the following order:

  1. Normalize back slashes (`\`) into forward slashes (`/`).
  2. Merge successive forward slashes (for example, `//` will be normalized to `/`).
  3. Perform RFC 3986 normalization of the resulting URL.



[PreviousOverview](https://developers.cloudflare.com/rules/normalization/)[NextConfigure in the dashboard](https://developers.cloudflare.com/rules/normalization/manage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/normalization/how-it-works.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

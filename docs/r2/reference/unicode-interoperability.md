---
url: https://developers.cloudflare.com/r2/reference/unicode-interoperability/
title: Unicode interoperability \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:49.198121+00:00
---

# Unicode interoperability · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/reference/unicode-interoperability/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /Reference
  4. /Unicode interoperability



# Unicode interoperability

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/reference/unicode-interoperability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 is built on top of Workers and supports Unicode natively. One nuance of Unicode that is often overlooked is the issue of [filename interoperability ↗︎](https://en.wikipedia.org/wiki/Filename#Encoding_indication_interoperability) due to [Unicode equivalence ↗︎](https://en.wikipedia.org/wiki/Unicode_equivalence).

Based on feedback from our users, we have chosen to NFC-normalize key names before storing by default. This means that `Héllo` and `Héllo`, for example, are the same object in R2 but different objects in other storage providers. Although `Héllo` and `Héllo` may be different character byte sequences, they are rendered the same.

R2 preserves the encoding for display though. When you list the objects, you will get back the last encoding you uploaded with.

There are still some platform-specific differences to consider:

  * Windows and macOS filenames are case-insensitive while R2 and Linux are not.
  * Windows console support for Unicode can be error-prone. Make sure to run `chcp 65001` before using command-line tools or use Cygwin if your object names appear to be incorrect.
  * Linux allows distinct files that are unicode-equivalent because filenames are byte streams. Unicode-equivalent filenames on Linux will point to the same R2 object.



If it is important for you to be able to bypass the unicode equivalence and use byte-oriented key names, contact your Cloudflare account team.

[PreviousDurability](https://developers.cloudflare.com/r2/reference/durability/)[NextWrangler commands](https://developers.cloudflare.com/r2/reference/wrangler-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/reference/unicode-interoperability.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

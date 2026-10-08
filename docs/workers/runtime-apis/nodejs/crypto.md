---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/
title: crypto \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:45.510439+00:00
---

# crypto · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /crypto



# crypto

Last updated Aug 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`node:crypto` ↗︎](https://nodejs.org/docs/latest/api/crypto.html) module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

All `node:crypto` APIs are fully supported in Workers with the following exceptions:

  * The functions [generateKeyPair ↗︎](https://nodejs.org/api/crypto.html#cryptogeneratekeypairtype-options-callback) and [generateKeyPairSync ↗︎](https://nodejs.org/api/crypto.html#cryptogeneratekeypairsynctype-options) do not support DSA or DH key pairs.
  * `argon2` and `argon2Sync` are not supported.
  * `ed448` and `x448` curves are not supported.
  * It is not possible to manually enable or disable [FIPS mode ↗︎](https://nodejs.org/docs/latest/api/crypto.html#fips-mode).



The full `node:crypto` API is documented in the [Node.js documentation for `node:crypto` ↗︎](https://nodejs.org/api/crypto.html).

The [WebCrypto API](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/) is also available within Cloudflare Workers. This does not require the `nodejs_compat` compatibility flag.

[PreviousBuffer](https://developers.cloudflare.com/workers/runtime-apis/nodejs/buffer/)[NextDiagnostics Channel](https://developers.cloudflare.com/workers/runtime-apis/nodejs/diagnostics-channel/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/crypto.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

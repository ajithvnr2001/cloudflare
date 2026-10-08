---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/
title: dns \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:45.590560+00:00
---

# dns · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /dns



# dns

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

You can use [`node:dns` ↗︎](https://nodejs.org/api/dns.html) for name resolution via [DNS over HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/) using [Cloudflare DNS ↗︎](https://www.cloudflare.com/application-services/products/dns/) at 1.1.1.1.

index.jsjs
    
    
    import dns from "node:dns";
    
    let response = await dns.promises.resolve4("cloudflare.com", "NS");

index.tsts
    
    
    import dns from 'node:dns';
    
    let response = await dns.promises.resolve4('cloudflare.com', 'NS');

All `node:dns` functions are available, except `lookup`, `lookupService`, and `resolve` which throw "Not implemented" errors when called.

Note

DNS requests will execute a subrequest, counts for your [Worker's subrequest limit](https://developers.cloudflare.com/workers/platform/limits/#subrequests).

The full `node:dns` API is documented in the [Node.js documentation for `node:dns` ↗︎](https://nodejs.org/api/dns.html).


[PreviousDiagnostics Channel](https://developers.cloudflare.com/workers/runtime-apis/nodejs/diagnostics-channel/)[NextEventEmitter](https://developers.cloudflare.com/workers/runtime-apis/nodejs/eventemitter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/dns.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/url/
title: url \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:47.107711+00:00
---

# url · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/url/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /url



# url

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/url/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewdomainToASCIIdomainToUnicode

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

## domainToASCII

Returns the Punycode ASCII serialization of the domain. If domain is an invalid domain, the empty string is returned.
    
    
    import { domainToASCII } from "node:url";
    
    console.log(domainToASCII("español.com"));
    // Prints xn--espaol-zwa.com
    console.log(domainToASCII("中文.com"));
    // Prints xn--fiq228c.com
    console.log(domainToASCII("xn--iñvalid.com"));
    // Prints an empty string

## domainToUnicode

Returns the Unicode serialization of the domain. If domain is an invalid domain, the empty string is returned.

It performs the inverse operation to `domainToASCII()`.
    
    
    import { domainToUnicode } from "node:url";
    
    console.log(domainToUnicode("xn--espaol-zwa.com"));
    // Prints español.com
    console.log(domainToUnicode("xn--fiq228c.com"));
    // Prints 中文.com
    console.log(domainToUnicode("xn--iñvalid.com"));
    // Prints an empty string

[Previoustls](https://developers.cloudflare.com/workers/runtime-apis/nodejs/tls/)[Nextutil](https://developers.cloudflare.com/workers/runtime-apis/nodejs/util/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/url.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

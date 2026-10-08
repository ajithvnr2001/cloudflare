---
url: https://developers.cloudflare.com/workers/runtime-apis/nodejs/path/
title: path \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:48.720520+00:00
---

# path · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/nodejs/path/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
  5. /path



# path

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/nodejs/path/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).

The [`node:path` ↗︎](https://nodejs.org/api/path.html) module provides utilities for working with file and directory paths. The `node:path` module can be accessed using:
    
    
    import path from "node:path";
    path.join("/foo", "bar", "baz/asdf", "quux", "..");
    // Returns: '/foo/bar/baz/asdf'

Refer to the [Node.js documentation for `path` ↗︎](https://nodejs.org/api/path.html) for more information.

[Previousnet](https://developers.cloudflare.com/workers/runtime-apis/nodejs/net/)[Nextprocess](https://developers.cloudflare.com/workers/runtime-apis/nodejs/process/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/nodejs/path.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

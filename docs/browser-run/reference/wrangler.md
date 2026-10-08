---
url: https://developers.cloudflare.com/browser-run/reference/wrangler/
title: Wrangler \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.358708+00:00
---

# Wrangler · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/reference/wrangler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Reference
  4. /Wrangler



# Wrangler

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/reference/wrangler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallBindings Headful mode (experimental)

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) is a command-line tool for building with Cloudflare developer products.

Use Wrangler to deploy projects that use the Workers Browser Run API.

## Install

To install Wrangler, refer to [Install and Update Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/).

## Bindings

[Bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) allow your Workers to interact with resources on the Cloudflare developer platform. A browser binding will provide your Worker with an authenticated endpoint to interact with a dedicated Chromium browser instance.

To deploy a Browser Run Worker, you must declare a [browser binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/) in your Worker's Wrangler configuration file.

Note

For compatibility dates of `2026-08-04` or later, Workers enables both `nodejs_compat` and `nodejs_compat_v2` by default. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date. For earlier dates, add `nodejs_compat` to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to opt in. For instructions to turn off Node.js compatibility, refer to the [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	// Top-level configuration
    	"name": "browser-rendering",
    	"main": "src/index.ts",
    	"workers_dev": true,
    	"compatibility_flags": ["nodejs_compat_v2"],
    	"browser": {
    		"binding": "MYBROWSER",
    	},
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "browser-rendering"
    main = "src/index.ts"
    workers_dev = true
    compatibility_flags = [ "nodejs_compat_v2" ]
    
    [browser]
    binding = "MYBROWSER"

After the binding is declared, access the DevTools endpoint using `env.MYBROWSER` in your Worker code:
    
    
    const browser = await puppeteer.launch(env.MYBROWSER);

Browser bindings also provide typed methods for [session management, outbound Worker routing, and DevTools operations](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/).

Quick Actions compatibility

The browser binding's `.quickAction()` method requires a compatibility date of `2026-03-24` or later. Ensure your `wrangler.json` includes:
    
    
    {
      "compatibility_date": "2026-03-24"
    }

Quick Actions require remote mode for local development

The `.quickAction()` method is not yet supported in local development mode. When using `wrangler dev`, you must run with `--remote` or set `"remote": true` in your browser binding configuration:
    
    
    {
      "browser": {
        "binding": "MYBROWSER",
        "remote": true
      }
    }

Without remote mode, calls to `.quickAction()` will fail with: `The RPC receiver does not implement the method "quickAction"`.

For Puppeteer, Playwright, or CDP-based Workers, run `npx wrangler dev` to test locally. For Quick Actions via `.quickAction()`, use `npx wrangler dev --remote` as noted above.

### Headful mode (experimental)

By default, local development runs Chrome in headless mode. To launch Chrome in visible (headful) mode for debugging, set the `X_BROWSER_HEADFUL` environment variable:
    
    
    X_BROWSER_HEADFUL=true npx wrangler dev

This opens a browser window on screen so you can watch navigations, interactions, and rendering in real time. Headful mode is for local development only and does not affect deployed Workers. This feature is experimental and may change without notice.

Note

When using [`@cloudflare/playwright`](https://developers.cloudflare.com/browser-run/playwright/), two Chrome windows may appear. This is expected behavior due to how Playwright handles browser contexts via CDP.

Use real headless browser during local development

To interact with a real headless browser during local development, set `"remote" : true` in the Browser binding configuration. Learn more in our [remote bindings documentation](https://developers.cloudflare.com/workers/local-development/#remote-bindings).

[PreviousBrowser close reasons](https://developers.cloudflare.com/browser-run/reference/browser-close-reasons/)[NextWrangler commands](https://developers.cloudflare.com/browser-run/reference/wrangler-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/reference/wrangler.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

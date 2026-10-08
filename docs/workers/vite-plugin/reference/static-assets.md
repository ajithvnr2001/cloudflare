---
url: https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/
title: Static Assets \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:05.402415+00:00
---

# Static Assets · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/)

  4. /Reference
  5. /Static Assets



# Static Assets

Last updated Aug 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/vite-plugin/reference/static-assets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigurationFeaturesHeaders and redirects

This guide focuses on the areas of working with static assets that are unique to the Vite plugin. For more general documentation, see [Static Assets](https://developers.cloudflare.com/workers/static-assets/).

## Configuration

The Vite plugin does not require that you provide the `assets` field in order to enable assets and instead determines whether assets should be included based on whether the `client` environment has been built. By default, the `client` environment is built if any of the following conditions are met:

  * There is an `index.html` file in the root of your project
  * `build.rollupOptions.input` or `environments.client.build.rollupOptions.input` is specified in your Vite config
  * You have a non-empty [`public` directory ↗︎](https://vite.dev/guide/assets#the-public-directory)
  * Your Worker [imports assets as URLs ↗︎](https://vite.dev/guide/assets#importing-asset-as-url)



On running `vite build`, an output `wrangler.json` configuration file is generated as part of the build output. The `assets.directory` field in this file is automatically populated with the path to your `client` build output. It is therefore not necessary to provide the `assets.directory` field in your input Worker configuration.

Cloudflare Access context

The Vite plugin can add Static Assets to the generated deployment configuration even when the input Wrangler configuration does not include `assets`. Workers with Static Assets do not receive `ctx.access` in the user Worker.

This behavior affects frameworks that use the Cloudflare Vite plugin, including TanStack Start. For more information, refer to [`ctx.access` limitations](https://developers.cloudflare.com/workers/configuration/cloudflare-access/#ctxaccess-limitations).

The `assets` configuration should be used, however, if you wish to set [routing configuration](https://developers.cloudflare.com/workers/static-assets/routing/) or enable the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/#binding). The following example configures the `not_found_handling` for a single-page application so that the fallback will always be the root `index.html` file.
    
    
    {
    	"assets": {
    		"not_found_handling": "single-page-application"
    	}
    }
    
    
    [assets]
    not_found_handling = "single-page-application"

## Features

The Vite plugin ensures that all of Vite's [static asset handling ↗︎](https://vite.dev/guide/assets) features are supported in your Worker as well as in your frontend. These include importing assets as URLs, importing as strings and importing from the `public` directory as well as inlining assets.

Assets [imported as URLs ↗︎](https://vite.dev/guide/assets#importing-asset-as-url) can be fetched via the [assets binding](https://developers.cloudflare.com/workers/static-assets/binding/#binding). As the binding's `fetch` method requires a full URL, we recommend using the request URL as the `base`. This is demonstrated in the following example:
    
    
    import myImage from "./my-image.png";
    
    export default {
    	fetch(request, env) {
    		return env.ASSETS.fetch(new URL(myImage, request.url));
    	},
    };

Assets imported as URLs in your Worker will automatically be moved to the client build output. When running `vite build` the paths of any moved assets will be displayed in the console.

Note

If you are developing a multi-Worker application, assets can only be accessed on the client and in your entry Worker.

## Headers and redirects

Custom [headers](https://developers.cloudflare.com/workers/static-assets/headers/) and [redirects](https://developers.cloudflare.com/workers/static-assets/redirects/) are supported at build, preview and deploy time by adding `_headers` and `_redirects` files to your [`public` directory ↗︎](https://vite.dev/guide/assets#the-public-directory). The paths in these files should reflect the structure of your client build output. For example, generated assets are typically located in an [assets subdirectory ↗︎](https://vite.dev/config/build-options#build-assetsdir).

[PreviousAPI](https://developers.cloudflare.com/workers/vite-plugin/reference/api/)[NextDebugging](https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/vite-plugin/reference/static-assets.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

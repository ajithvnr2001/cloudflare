---
url: https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/eject-webpack/
title: 1. Migrate webpack projects \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:12.295497+00:00
---

# 1. Migrate webpack projects · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/eject-webpack/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Wrangler](https://developers.cloudflare.com/workers/wrangler/)Migrations

  4. /Migrate from Wrangler v1 to v2
  5. /1\. Migrate webpack projects



# 1\. Migrate webpack projects

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/eject-webpack/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview I use [build] to run webpack (or another bundler) external to Wrangler. I use type = webpack, but do not provide my own configuration and let Wrangler take care of it. I use type = webpack and webpack_config = <path/to/webpack.config.js> to handle JSX, TypeScript, WebAssembly, HTML files, and other non-standard filetypes. I use type = webpack and webpack_config = <path/to/webpack.config.js> to perform code-transforms and/or other code-modifying functionality.

This guide describes the steps to migrate a webpack project from Wrangler v1 to Wrangler v2. After completing this guide, [update your Wrangler version](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/).

Previous versions of Wrangler offered rudimentary support for [webpack ↗︎](https://webpack.js.org/) with the `type` and `webpack_config` keys in the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). Starting with Wrangler v2, Wrangler no longer supports the `type` and `webpack_config` keys, but you can still use webpack with your Workers.

As a developer using webpack with Workers, you may be in one of four categories:

  1. I use `[build]` to run webpack (or another bundler) external to `wrangler`..

  2. I use `type = webpack`, but do not provide my own configuration and let Wrangler take care of it..

  3. I use `type = webpack` and `webpack_config = <path/to/webpack.config.js>` to handle JSX, TypeScript, WebAssembly, HTML files, and other non-standard filetypes..

  4. I use `type = webpack` and `webpack_config = <path/to/webpack.config.js>` to perform code-transforms and/or other code-modifying functionality..




If you do not see yourself represented, [file an issue ↗︎](https://github.com/cloudflare/workers-sdk/issues/new/choose) and we can assist you with your specific situation and improve this guide for future readers.

### I use `[build]` to run webpack (or another bundler) external to Wrangler.

Wrangler v2 supports the `[build]` key, so your Workers will continue to build using your own setup.

### I use `type = webpack`, but do not provide my own configuration and let Wrangler take care of it.

Wrangler will continue to take care of it. Remove `type = webpack` from your Wrangler file.

### I use `type = webpack` and `webpack_config = <path/to/webpack.config.js>` to handle JSX, TypeScript, WebAssembly, HTML files, and other non-standard filetypes.

As of Wrangler v2, Wrangler has built-in support for this use case. Refer to [Bundling](https://developers.cloudflare.com/workers/wrangler/bundling/) for more details.

The Workers runtime handles JSX and TypeScript. You can `import` any modules you need into your code and the Workers runtime includes them in the built Worker automatically.

You should remove the `type` and `webpack_config` keys from your Wrangler file.

### I use `type = webpack` and `webpack_config = <path/to/webpack.config.js>` to perform code-transforms and/or other code-modifying functionality.

Wrangler v2 drops support for project types, including `type = webpack` and configuration via the `webpack_config` key. If your webpack configuration performs operations beyond adding loaders (for example, for TypeScript) you will need to maintain your custom webpack configuration. In the long term, you should [migrate to an external `[build]` process](https://developers.cloudflare.com/workers/wrangler/custom-builds/). In the short term, it is still possible to reproduce Wrangler v1's build steps in newer versions of Wrangler by following the instructions below.

  1. Add [wranglerjs-compat-webpack-plugin ↗︎](https://www.npmjs.com/package/wranglerjs-compat-webpack-plugin) as a `devDependency`.



[wrangler-js ↗︎](https://www.npmjs.com/package/wrangler-js), shipped as a separate library from [Wrangler v1 ↗︎](https://www.npmjs.com/package/@cloudflare/wrangler/v/1.19.11), is a Node script that configures and executes [webpack 4 ↗︎](https://unpkg.com/browse/wrangler-js@0.1.11/package.json) for you. When you set `type = webpack`, Wrangler v1 would execute this script for you. We have ported the functionality over to a new package, [wranglerjs-compat-webpack-plugin ↗︎](https://www.npmjs.com/package/wranglerjs-compat-webpack-plugin), which you can use as a [webpack plugin ↗︎](https://v4.webpack.js.org/configuration/plugins/).

To do that, you will need to add it as a dependency:

npmyarnpnpmbun
    
    
    npm i -D webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin
    
    
    yarn add -D webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin
    
    
    pnpm add -D webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin
    
    
    bun add -d webpack@^4.46.0 webpack-cli wranglerjs-compat-webpack-plugin

You should see this reflected in your `package.json` file:
    
    
    {
    	"name": "my-worker",
    	"version": "x.y.z",
    	// ...
    	"devDependencies": {
    		// ...
    		"wranglerjs-compat-webpack-plugin": "^x.y.z",
    		"webpack": "^4.46.0",
    		"webpack-cli": "^x.y.z"
    	}
    }

  2. Add `wranglerjs-compat-webpack-plugin` to `webpack.config.js`.



Modify your `webpack.config.js` file to include the plugin you just installed.
    
    
    const {
    	WranglerJsCompatWebpackPlugin,
    } = require("wranglerjs-compat-webpack-plugin");
    
    module.exports = {
    	// ...
    	plugins: [new WranglerJsCompatWebpackPlugin()],
    };

  3. Add a build script your `package.json`.


    
    
    {
    	"name": "my-worker",
    	"version": "2.0.0",
    	// ...
    	"scripts": {
    		"build": "webpack" // <-- Add this line!
    		// ...
    	}
    }

  4. Remove unsupported entries from your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).



Remove the `type` and `webpack_config` keys from your Wrangler file, as they are not supported anymore.
    
    
    {
    	// Remove these!
    	"type": "webpack",
    	"webpack_config": "webpack.config.js"
    }
    
    
    type = "webpack"
    webpack_config = "webpack.config.js"

  5. Tell Wrangler how to bundle your Worker.



Wrangler no longer has any knowledge of how to build your Worker. You will need to tell it how to call webpack and where to look for webpack's output. This translates into two fields:
    
    
    {
    	"main": "./worker/script.js", // by default, or whatever file webpack outputs
    	"build": {
    		"command": "npm run build" // or "yarn build"
    	}
    }
    
    
    main = "./worker/script.js"
    
    [build]
    command = "npm run build"

  6. Test your project.



Try running `npx wrangler deploy` to test that your configuration works as expected.

[PreviousWebpack](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/webpack/)[Next2\. Update to Wrangler v2](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/migration/v1-to-v2/eject-webpack.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

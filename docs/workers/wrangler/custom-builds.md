---
url: https://developers.cloudflare.com/workers/wrangler/custom-builds/
title: Custom builds \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:10.723365+00:00
---

# Custom builds · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/custom-builds/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Wrangler](https://developers.cloudflare.com/workers/wrangler/)
  4. /Custom builds



# Custom builds

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/custom-builds/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure custom buildsWRANGLER_COMMAND environment variable

Custom builds are a way for you to customize how your code is compiled, before being processed by Wrangler.

Note

Wrangler runs [esbuild ↗︎](https://esbuild.github.io/) by default as part of the `dev` and `deploy` commands, and bundles your Worker project into a single Worker script. Refer to [Bundling](https://developers.cloudflare.com/workers/wrangler/bundling/).

## Configure custom builds

Custom builds are configured by adding a `[build]` section in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/), and using the following options for configuring your custom build.

  * `command` `string` optional

    * The command used to build your Worker. On Linux and macOS, the command is executed in the `sh` shell and the `cmd` shell for Windows. The `&&` and `||` shell operators may be used. This command will be run as part of `wrangler dev` and `npx wrangler deploy`.
  * `cwd` `string` optional

    * The directory in which the command is executed.
  * `watch_dir` `string | string\[]` optional

    * The directory to watch for changes while using `wrangler dev`. Defaults to the current working directory.



Example:
    
    
    {
    	"build": {
    		"command": "npm run build",
    		"cwd": "build_cwd",
    		"watch_dir": "build_watch_dir"
    	}
    }
    
    
    [build]
    command = "npm run build"
    cwd = "build_cwd"
    watch_dir = "build_watch_dir"

## `WRANGLER_COMMAND` environment variable

When Wrangler runs your custom build command, it sets the `WRANGLER_COMMAND` environment variable so your build script can detect which Wrangler command triggered the build. This allows you to customize the build process based on the deployment context.

The possible values are:

Value | Wrangler command triggered  
---|---  
`dev` | `wrangler dev`  
`deploy` | `wrangler deploy`  
`versions upload` | `wrangler versions upload`  
`types` | `wrangler types`  
  
For example, you can use this to apply different build settings for development and production:
    
    
    #!/bin/bash
    if [ "$WRANGLER_COMMAND" = "dev" ]; then
      echo "Building for development..."
      # run a development build
    else
      echo "Building for production..."
      # run a production build
    fi

[PreviousConfiguration](https://developers.cloudflare.com/workers/wrangler/configuration/)[NextDeprecations](https://developers.cloudflare.com/workers/wrangler/deprecations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/custom-builds.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/
title: Attaching a Debugger \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:55.511824+00:00
---

# Attaching a Debugger · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Developing
  5. /Attaching a Debugger



# Attaching a Debugger

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewVisual Studio Code Create configurationWebStormDevTools

Caution

This documentation describes breakpoint debugging when using Miniflare directly, which is only relevant for advanced use cases. Instead, most users should refer to the [Workers Observability documentation for how to set this up when using Wrangler](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/).

You can use regular Node.js tools to debug your Workers. Setting breakpoints, watching values and inspecting the call stack are all examples of things you can do with a debugger.

## Visual Studio Code

### Create configuration

The easiest way to debug a Worker in VSCode is to create a new configuration.

Open the **Run and Debug** menu in the VSCode activity bar and create a `.vscode/launch.json` file that contains the following:
    
    
    ---
    filename: .vscode/launch.json
    ---
    {
      "configurations": [
        {
          "name": "Miniflare",
          "type": "node",
          "request": "attach",
          "port": 9229,
          "cwd": "/",
          "resolveSourceMapLocations": null,
          "attachExistingChildren": false,
          "autoAttachChildProcesses": false,
        }
      ]
    }

From the **Run and Debug** menu in the activity bar, select the `Miniflare` configuration, and click the green play button to start debugging.

## WebStorm

Create a new configuration, by clicking **Add Configuration** in the top right.

![WebStorm add configuration button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=177,height=28,format=webp/_astro/debugger-webstorm-node-add.1Aka_l-1.png)

Click the **plus** button in the top left of the popup and create a new **Node.js/Chrome** configuration. Set the **Host** field to `localhost` and the **Port** field to `9229`. Then click **OK**.

![WebStorm Node.js debug configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=705,height=531,format=webp/_astro/debugger-webstorm-settings.CxmegMYm.png)

With the new configuration selected, click the green debug button to start debugging.

![WebStorm configuration debug button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=303,height=68,format=webp/_astro/debugger-webstorm-node-run.BodpA57u.png)

## DevTools

Breakpoints can also be added via the Workers DevTools. For more information, [read the guide](https://developers.cloudflare.com/workers/observability/dev-tools) in the Cloudflare Workers docs.

[PreviousWebSockets](https://developers.cloudflare.com/workers/testing/miniflare/core/web-sockets/)[NextLive Reload](https://developers.cloudflare.com/workers/testing/miniflare/developing/live-reload/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/developing/debugger.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

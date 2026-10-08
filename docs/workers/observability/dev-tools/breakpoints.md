---
url: https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/
title: Breakpoints \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:34.474470+00:00
---

# Breakpoints · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Observability](https://developers.cloudflare.com/workers/observability/)

  4. /[DevTools](https://developers.cloudflare.com/workers/observability/dev-tools/)
  5. /Breakpoints



# Breakpoints

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDebug via breakpoints VSCode debug terminals Setup VS Code to use breakpoints with launch.json filesRelated resources

## Debug via breakpoints

When developing a Worker locally using Wrangler or Vite, you can debug via breakpoints in your Worker. Breakpoints provide the ability to review what is happening at a given point in the execution of your Worker. Breakpoint functionality exists in both DevTools and VS Code.

For more information on breakpoint debugging via Chrome's DevTools, refer to [Chrome's article on breakpoints ↗︎](https://developer.chrome.com/docs/devtools/javascript/breakpoints/).

### VSCode debug terminals

Using VSCode's built-in [JavaScript Debug Terminals ↗︎](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal), all you have to do is open a JS debug terminal (`Cmd + Shift + P` and then type `javascript debug`) and run `wrangler dev` (or `vite dev`) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.

### Setup VS Code to use breakpoints with `launch.json` files

To setup VS Code for breakpoint debugging in your Worker project:

  1. Create a `.vscode` folder in your project's root folder if one does not exist.
  2. Within that folder, create a `launch.json` file with the following content:


    
    
    {
    	"configurations": [
    		{
    			"name": "Listen Wrangler",
    			"type": "node",
    			"request": "attach",
    			"port": 9229,
    			"cwd": "/",
    			"resolveSourceMapLocations": null,
    			"attachExistingChildren": false,
    			"autoAttachChildProcesses": false,
    			"sourceMaps": true // works with or without this line
    		},
    		{
    			"name": "Launch Wrangler",
    			"command": "npm run dev",
    			"type": "node-terminal",
    			"request": "launch",
    			"console": "integratedTerminal",
    			"sourceMaps": true
    		}
    	]
    }

  3. Open your project in VS Code, open a new terminal window from VS Code, and run `npx wrangler dev` to start the local dev server.

  4. At the top of the **Run & Debug** panel, you should see an option to select a configuration. Choose **Wrangler** , and select the play icon. **Wrangler: Remote Process [0]** should show up in the Call Stack panel on the left.

  5. Go back to a `.js` or `.ts` file in your project and add at least one breakpoint.

  6. Open your browser and go to the Worker's local URL (default `http://127.0.0.1:8787`). The breakpoint should be hit, and you should be able to review details about your code at the specified line.




Caution

Breakpoint debugging in `wrangler dev` using `--remote` could extend Worker CPU time and incur additional costs since you are testing against actual resources that count against usage limits. It is recommended to use `wrangler dev` without the `--remote` option. This ensures you are developing locally.

If you are debugging using `--remote`, you cannot use code minification as the debugger will be unable to find vars when stopped at a breakpoint. Do not set minify to `true` in your Wrangler configuration file.

Note

The `.vscode/launch.json` file only applies to a single workspace. If you prefer, you can add the above launch configuration to your User Settings (per the [official VS Code documentation ↗︎](https://code.visualstudio.com/docs/editor/debugging#_global-launch-configuration)) to have it available for all your workspaces.

## Related resources

  * [Local Development](https://developers.cloudflare.com/workers/local-development/) \- Develop your Workers and connected resources locally via Wrangler and [`workerd` ↗︎](https://github.com/cloudflare/workerd), for a fast, accurate feedback loop.



[PreviousOverview](https://developers.cloudflare.com/workers/observability/dev-tools/)[NextProfiling CPU usage](https://developers.cloudflare.com/workers/observability/dev-tools/cpu-usage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/observability/dev-tools/breakpoints.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

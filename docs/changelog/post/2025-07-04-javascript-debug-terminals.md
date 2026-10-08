---
url: https://developers.cloudflare.com/changelog/post/2025-07-04-javascript-debug-terminals/
title: Workers now supports JavaScript debug terminals in VSCode, Cursor and Windsurf IDEs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:16.256969+00:00
---

# Workers now supports JavaScript debug terminals in VSCode, Cursor and Windsurf IDEs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-04-javascript-debug-terminals/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 4, 2025

## Workers now supports JavaScript debug terminals in VSCode, Cursor and Windsurf IDEs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-04-javascript-debug-terminals/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers now support breakpoint debugging using VSCode's built-in [JavaScript Debug Terminals ↗︎](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal). All you have to do is open a JS debug terminal (`Cmd + Shift + P` and then type `javascript debug`) and run `wrangler dev` (or `vite dev`) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.

In 2023 we announced [breakpoint debugging support ↗︎](https://blog.cloudflare.com/debugging-cloudflare-workers/) for Workers, which meant that you could easily debug your Worker code in Wrangler's built-in devtools (accessible via the `[d]` hotkey) as well as multiple other devtools clients, [including VSCode ↗︎](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/). For most developers, breakpoint debugging via VSCode is the most natural flow, but until now it's required [manually configuring a `launch.json` file ↗︎](https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/#setup-vs-code-to-use-breakpoints), running `wrangler dev`, and connecting via VSCode's built-in debugger. Now it's much more seamless!

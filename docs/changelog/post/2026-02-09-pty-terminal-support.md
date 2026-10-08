---
url: https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/
title: Interactive browser terminals in Sandboxes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:36.089163+00:00
---

# Interactive browser terminals in Sandboxes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 9, 2026

## Interactive browser terminals in Sandboxes

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Sandbox SDK ↗︎](https://github.com/cloudflare/sandbox-sdk) now supports PTY (pseudo-terminal) passthrough, enabling browser-based terminal UIs to connect to sandbox shells via WebSocket.

#### `sandbox.terminal(request)`

The new `terminal()` method proxies a WebSocket upgrade to the container's PTY endpoint, with output buffering for replay on reconnect.
    
    
    // Worker: proxy WebSocket to container terminal
    return sandbox.terminal(request, { cols: 80, rows: 24 });
    
    
    // Worker: proxy WebSocket to container terminal
    return sandbox.terminal(request, { cols: 80, rows: 24 });

#### Multiple terminals per sandbox

Each session can have its own terminal with an isolated working directory and environment, so users can run separate shells side-by-side in the same container.
    
    
    // Multiple isolated terminals in the same sandbox
    const dev = await sandbox.getSession("dev");
    return dev.terminal(request);
    
    
    // Multiple isolated terminals in the same sandbox
    const dev = await sandbox.getSession("dev");
    return dev.terminal(request);

#### xterm.js addon

The new `@cloudflare/sandbox/xterm` export provides a `SandboxAddon` for [xterm.js ↗︎](https://xtermjs.org/) with automatic reconnection (exponential backoff + jitter), buffered output replay, and resize forwarding.
    
    
    import { SandboxAddon } from "@cloudflare/sandbox/xterm";
    
    const addon = new SandboxAddon({
    	getWebSocketUrl: ({ sandboxId, origin }) =>
    		`${origin}/ws/terminal?id=${sandboxId}`,
    	onStateChange: (state, error) => updateUI(state),
    });
    terminal.loadAddon(addon);
    addon.connect({ sandboxId: "my-sandbox" });
    
    
    import { SandboxAddon } from "@cloudflare/sandbox/xterm";
    
    const addon = new SandboxAddon({
    	getWebSocketUrl: ({ sandboxId, origin }) =>
    		`${origin}/ws/terminal?id=${sandboxId}`,
    	onStateChange: (state, error) => updateUI(state),
    });
    terminal.loadAddon(addon);
    addon.connect({ sandboxId: "my-sandbox" });

#### Upgrade

To update to the latest version:
    
    
    npm i @cloudflare/sandbox@latest
